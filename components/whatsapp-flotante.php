<?php
/**
 * ============================================================
 * BOTÓN FLOTANTE DE WHATSAPP — Snippet para "Fragmentos de código"
 * (plugin Code Snippets) en WordPress + Divi.
 *
 * Uso: Fragmentos > Añadir nuevo > tipo "PHP" > pegar este código
 *      (sin la línea "<?php" si el plugin ya la incluye) >
 *      "Ejecutar en todas partes" o "Solo en el front-end" > Guardar y activar.
 * ============================================================
 */

add_action( 'wp_footer', function () {

	// No mostrar en el constructor visual de Divi ni en el admin.
	if ( is_admin() || isset( $_GET['et_fb'] ) ) {
		return;
	}

	// ---------- CONFIGURACIÓN ----------
	$telefono = '34600000000';                                   // Prefijo de país + número, sin "+" ni espacios.
	$mensaje  = 'Hola, vengo de la web y me gustaría más información.';
	$texto    = '¿Hablamos?';                                    // Texto de la etiqueta. Déjalo vacío ('') para ocultarla.
	$posicion = 'right';                                         // 'right' o 'left'.
	// -----------------------------------

	$url = 'https://wa.me/' . preg_replace( '/\D/', '', $telefono ) . '?text=' . rawurlencode( $mensaje );
	?>
	<a href="<?php echo esc_url( $url ); ?>"
	   class="rm-wa rm-wa--<?php echo esc_attr( $posicion ); ?>"
	   target="_blank" rel="noopener noreferrer"
	   aria-label="Escríbenos por WhatsApp">
		<?php if ( $texto ) : ?>
			<span class="rm-wa__label"><?php echo esc_html( $texto ); ?></span>
		<?php endif; ?>
		<span class="rm-wa__icon" aria-hidden="true">
			<svg viewBox="0 0 32 32" width="30" height="30" fill="currentColor">
				<path d="M16.04 3C8.86 3 3.03 8.82 3.03 16c0 2.29.6 4.53 1.74 6.5L3 29l6.68-1.75A12.95 12.95 0 0 0 16.04 29C23.2 29 29 23.18 29 16S23.2 3 16.04 3zm0 23.8c-1.98 0-3.92-.53-5.62-1.54l-.4-.24-3.96 1.04 1.06-3.86-.26-.4A10.76 10.76 0 0 1 5.2 16c0-5.97 4.86-10.83 10.84-10.83A10.8 10.8 0 0 1 26.83 16c0 5.97-4.84 10.8-10.8 10.8zm5.93-8.1c-.33-.16-1.93-.95-2.23-1.06-.3-.11-.52-.16-.73.17-.22.32-.84 1.05-1.03 1.27-.19.22-.38.24-.7.08-.33-.16-1.38-.51-2.62-1.62-.97-.86-1.62-1.93-1.81-2.26-.19-.32-.02-.5.14-.66.15-.15.33-.38.49-.57.16-.19.22-.32.33-.54.11-.22.05-.4-.03-.57-.08-.16-.73-1.76-1-2.41-.26-.63-.53-.55-.73-.56h-.62c-.22 0-.57.08-.87.4-.3.33-1.14 1.12-1.14 2.72s1.17 3.16 1.33 3.38c.16.22 2.3 3.5 5.56 4.91.78.34 1.39.54 1.86.69.78.25 1.49.21 2.05.13.63-.09 1.93-.79 2.2-1.55.27-.76.27-1.42.19-1.55-.08-.14-.3-.22-.62-.38z"/>
			</svg>
		</span>
	</a>

	<style>
		.rm-wa {
			position: fixed;
			bottom: 24px;
			z-index: 99999;
			display: flex;
			align-items: center;
			gap: 10px;
			text-decoration: none !important;
		}
		.rm-wa--right { right: 24px; }
		.rm-wa--left  { left: 24px; flex-direction: row-reverse; }

		.rm-wa__icon {
			position: relative;
			display: flex;
			align-items: center;
			justify-content: center;
			width: 60px;
			height: 60px;
			border-radius: 50%;
			background: #25d366;
			color: #fff;
			box-shadow: 0 6px 20px rgba(0, 0, 0, .25);
			transition: transform .25s ease, box-shadow .25s ease;
		}
		/* Halo pulsante */
		.rm-wa__icon::before {
			content: "";
			position: absolute;
			inset: 0;
			border-radius: 50%;
			background: #25d366;
			z-index: -1;
			animation: rm-wa-pulse 2.2s ease-out infinite;
		}
		.rm-wa:hover .rm-wa__icon,
		.rm-wa:focus-visible .rm-wa__icon {
			transform: scale(1.08);
			box-shadow: 0 10px 28px rgba(0, 0, 0, .3);
		}
		.rm-wa:focus-visible { outline: none; }
		.rm-wa:focus-visible .rm-wa__icon { outline: 3px solid #128c7e; outline-offset: 3px; }

		.rm-wa__label {
			background: #fff;
			color: #1a1a2e;
			font-size: 14px;
			font-weight: 600;
			line-height: 1;
			padding: 10px 14px;
			border-radius: 20px;
			box-shadow: 0 4px 14px rgba(0, 0, 0, .15);
			white-space: nowrap;
			opacity: 0;
			transform: translateX(8px);
			transition: opacity .25s ease, transform .25s ease;
			pointer-events: none;
		}
		.rm-wa--left .rm-wa__label { transform: translateX(-8px); }
		.rm-wa:hover .rm-wa__label,
		.rm-wa:focus-visible .rm-wa__label {
			opacity: 1;
			transform: translateX(0);
		}

		@keyframes rm-wa-pulse {
			0%   { transform: scale(1);   opacity: .6; }
			100% { transform: scale(1.6); opacity: 0; }
		}

		/* Móvil: un poco más pequeño y sin etiqueta */
		@media (max-width: 767px) {
			.rm-wa { bottom: 16px; }
			.rm-wa--right { right: 16px; }
			.rm-wa--left  { left: 16px; }
			.rm-wa__icon { width: 54px; height: 54px; }
			.rm-wa__label { display: none; }
		}

		/* Respeta a quien prefiere menos movimiento */
		@media (prefers-reduced-motion: reduce) {
			.rm-wa__icon::before { animation: none; }
			.rm-wa__icon, .rm-wa__label { transition: none; }
		}

		/* Evita que tape el botón "volver arriba" de Divi */
		.et_pb_scroll_top.et-pb-icon { bottom: 100px !important; }
	</style>
	<?php
} );
