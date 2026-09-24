<?php
/**
 * RM — Comprobador real de disponibilidad de dominios (RDAP + WHOIS)
 *
 * Endpoint AJAX que usa el hero de la página de dominio
 * (components/rm-hero-domain.html) para comprobar disponibilidad SIN
 * mandar al visitante fuera de la web y SIN exponer ninguna clave —
 * todo corre en el servidor, donde no hay restricción CORS.
 *
 * Cómo instalarlo:
 * 1. Pega este archivo entero al final de functions.php de tu child
 *    theme (o súbelo como plugin de un solo archivo — cualquiera de
 *    las dos formas vale, es autocontenido).
 * 2. No hace falta configurar nada más: en cuanto está activo, el
 *    hero ya llama a /wp-admin/admin-ajax.php?action=rm_domain_check.
 *
 * Cómo comprueba cada dominio:
 * - gTLD (.com, .net, .org, .eu, .info, .io...): RDAP, el protocolo
 *   oficial que exige ICANN a estos registros. Sin autenticación, sin
 *   coste, y con una respuesta estructurada fiable: 404 = libre,
 *   200 = ya registrado.
 * - .es: RDAP no está garantizado para las extensiones nacionales
 *   (ccTLD) — Red.es, el registro de .es, no lo tenía como servicio
 *   público la última vez que se comprobó. Por eso aquí se usa WHOIS
 *   directamente (whois.nic.es, puerto 43) y se busca el texto que
 *   Red.es devuelve cuando un dominio NO está registrado.
 *   IMPORTANTE: no he podido probar esta consulta en vivo (esta
 *   sesión no tiene salida a internet para verificarlo). Antes de
 *   darlo por bueno, comprueba con un par de dominios .es reales
 *   (uno que sepas libre y otro que sepas ocupado) que
 *   $es_available_markers seguye detectando bien el caso "libre" —
 *   si Red.es ha cambiado el texto de su respuesta, ajusta ese array.
 *
 * Devuelve JSON: {"state": "available"} | {"state": "taken"} |
 * {"state": "error"}
 */

add_action( 'wp_ajax_rm_domain_check', 'rm_domain_check_handler' );
add_action( 'wp_ajax_nopriv_rm_domain_check', 'rm_domain_check_handler' );

function rm_domain_check_handler() {
	$raw = isset( $_GET['domain'] ) ? sanitize_text_field( wp_unslash( $_GET['domain'] ) ) : '';
	$domain = rm_domain_check_normalize( $raw );

	if ( ! $domain ) {
		wp_send_json( array( 'state' => 'error' ) );
	}

	$dot = strrpos( $domain, '.' );
	$tld = substr( $domain, $dot + 1 );

	if ( 'es' === $tld ) {
		$state = rm_domain_check_whois_es( $domain );
	} else {
		$state = rm_domain_check_rdap( $domain, $tld );
	}

	wp_send_json( array( 'state' => $state ) );
}

function rm_domain_check_normalize( $raw ) {
	$v = strtolower( trim( $raw ) );
	$v = preg_replace( '#^https?://#', '', $v );
	$v = preg_replace( '#^www\.#', '', $v );
	$v = preg_replace( '#/.*$#', '', $v );
	// Solo letras, números, guiones y puntos — nada más pasa a la consulta.
	if ( ! preg_match( '/^[a-z0-9-]+(\.[a-z0-9-]+)+$/', $v ) ) {
		return '';
	}
	return $v;
}

/**
 * RDAP para gTLDs (mandatado por ICANN, sin autenticación).
 * Mapa reducido a las extensiones que ofrece esta página — amplíalo
 * si añades más. Para cualquier TLD no listado aquí, se usa el
 * bootstrap oficial de IANA como último recurso.
 */
function rm_domain_check_rdap( $domain, $tld ) {
	$known = array(
		'com'  => 'https://rdap.verisign.com/com/v1/domain/',
		'net'  => 'https://rdap.verisign.com/net/v1/domain/',
		'org'  => 'https://rdap.publicinterestregistry.org/rdap/domain/',
		'info' => 'https://rdap.identitydigital.services/rdap/domain/',
		'io'   => 'https://rdap.nic.io/domain/',
		'eu'   => 'https://rdap.eu.org/domain/', // verifica el endpoint real de EURid antes de publicar
	);

	$base = isset( $known[ $tld ] ) ? $known[ $tld ] : rm_domain_check_rdap_bootstrap( $tld );
	if ( ! $base ) {
		return 'error';
	}

	$response = wp_remote_get(
		$base . rawurlencode( $domain ),
		array(
			'timeout'   => 6,
			'headers'   => array( 'Accept' => 'application/rdap+json' ),
			'sslverify' => true,
		)
	);

	if ( is_wp_error( $response ) ) {
		return 'error';
	}

	$code = wp_remote_retrieve_response_code( $response );
	if ( 404 === $code ) {
		return 'available';
	}
	if ( 200 === $code ) {
		return 'taken';
	}
	return 'error';
}

/**
 * Último recurso para un TLD que no está en el mapa fijo: consulta el
 * bootstrap oficial de IANA (data.iana.org/rdap/dns.json) para saber
 * qué servidor RDAP lo atiende, con una caché de 24h vía transient
 * para no golpear ese archivo en cada búsqueda.
 */
function rm_domain_check_rdap_bootstrap( $tld ) {
	$cache_key = 'rm_rdap_base_' . $tld;
	$cached    = get_transient( $cache_key );
	if ( false !== $cached ) {
		return $cached ?: false;
	}

	$response = wp_remote_get( 'https://data.iana.org/rdap/dns.json', array( 'timeout' => 6 ) );
	if ( is_wp_error( $response ) ) {
		return false;
	}

	$data = json_decode( wp_remote_retrieve_body( $response ), true );
	$base = false;

	if ( ! empty( $data['services'] ) ) {
		foreach ( $data['services'] as $service ) {
			if ( in_array( $tld, $service[0], true ) && ! empty( $service[1][0] ) ) {
				$base = rtrim( $service[1][0], '/' ) . '/domain/';
				break;
			}
		}
	}

	set_transient( $cache_key, $base, DAY_IN_SECONDS );
	return $base;
}

/**
 * WHOIS para .es (whois.nic.es, puerto 43) — Red.es no expone RDAP
 * público. Sin verificar en vivo: revisa $es_available_markers contra
 * una consulta real antes de publicar (ver nota arriba).
 */
function rm_domain_check_whois_es( $domain ) {
	$fp = @fsockopen( 'whois.nic.es', 43, $errno, $errstr, 6 );
	if ( ! $fp ) {
		return 'error';
	}

	stream_set_timeout( $fp, 6 );
	fwrite( $fp, $domain . "\r\n" );

	$body = '';
	while ( ! feof( $fp ) ) {
		$body .= fgets( $fp, 512 );
	}
	fclose( $fp );

	if ( '' === trim( $body ) ) {
		return 'error';
	}

	// Red.es devuelve un texto de "no encontrado" cuando el dominio
	// está libre; para el resto de casos, el whois trae los datos del
	// registro (fechas, nameservers...), señal de que está ocupado.
	$es_available_markers = array(
		'no existe',
		'not exist',
		'no ha sido registrado',
		'not been registered',
	);

	$body_lc = mb_strtolower( $body );
	foreach ( $es_available_markers as $marker ) {
		if ( false !== strpos( $body_lc, $marker ) ) {
			return 'available';
		}
	}

	return 'taken';
}
