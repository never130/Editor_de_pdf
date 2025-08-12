from fpdf import FPDF

class ProposalPDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 14)
        self.cell(0, 10, "Propuesta de Desarrollo de Aplicación Móvil", ln=True, align="C")
        self.ln(5)

    def chapter_title(self, title):
        self.set_font("Helvetica", "B", 12)
        self.cell(0, 10, title, ln=True)
        self.ln(2)

    def chapter_body(self, text):
        self.set_font("Helvetica", "", 11)
        self.multi_cell(0, 8, text)
        self.ln()

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 9)
        self.cell(0, 10, f"Página {self.page_no()}", align="C")

# Crear PDF
pdf = ProposalPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Título
pdf.set_title("Propuesta de Desarrollo")
pdf.set_author("Ever Loza")

# Secciones
pdf.chapter_title("Proyecto: Plataforma de Verificación de Exclusividad para Agentes Inmobiliarios")

pdf.chapter_title("Introducción")
pdf.chapter_body("""En el ámbito inmobiliario es común que un mismo cliente se contacte con múltiples agentes o inmobiliarias al mismo tiempo, generando competencia interna, pérdida de oportunidades y un uso ineficiente del tiempo de los profesionales. Esta propuesta busca resolver ese problema con una solución moderna y automatizada que mejora la gestión de contactos, protege la exclusividad y aporta transparencia al proceso comercial entre los agentes y sus clientes.""")

pdf.chapter_title("Objetivo de la aplicación")
pdf.chapter_body("""El objetivo principal de esta aplicación es ayudar a los agentes inmobiliarios a identificar, en tiempo real, si un cliente ya está siendo atendido por otro colega, utilizando el número de teléfono como identificador. De este modo, se reduce la duplicación de esfuerzos, se protege el trabajo previo realizado por los agentes y se mejora la gestión de relaciones comerciales.""")

pdf.chapter_title("Funcionalidad del sistema")
pdf.chapter_body("""Registro de agentes:
El sistema estará disponible exclusivamente para agentes inmobiliarios. Cada agente podrá registrarse con su número de teléfono y quedará identificado como usuario autorizado para acceder a la plataforma.

Registro y gestión de contactos:
Cada agente podrá cargar los datos de sus clientes (nombre, número de teléfono y comentarios opcionales) en su espacio personal. Esta información no será visible para otros usuarios, pero servirá como base de verificación ante futuras interacciones.

Detección automática de llamadas:
Cuando un cliente llama al número del agente, la aplicación detecta la llamada y automáticamente verifica si ese número ya está registrado por otro profesional dentro del sistema. En caso de coincidencia, se mostrará una notificación informando al agente que el cliente podría estar trabajando con otra inmobiliaria.

Alertas inteligentes:
El sistema no bloqueará las llamadas, pero brindará información clara y directa para que el agente pueda decidir cómo proceder: continuar, esperar o verificar con el cliente.

Acceso controlado y seguro:
Solo usuarios registrados podrán acceder a la aplicación. Se garantizará un entorno seguro, privado y adecuado al manejo de datos sensibles como números de teléfono y relaciones comerciales.

Sistema de suscripción:
El uso de la plataforma estará basado en un sistema de suscripción mensual. Cada agente podrá suscribirse fácilmente con tarjeta de crédito, y el acceso al servicio se mantendrá activo mientras la suscripción esté vigente. El cobro se realizará de forma automática para garantizar continuidad.

Pruebas y entrega:
La aplicación podrá ser probada tanto en teléfonos Android como en iPhone. En Android, se entregará una versión de instalación directa para pruebas inmediatas. En el caso de iPhone, se facilitará una prueba interna a través de un sistema oficial de evaluación temporal (sin necesidad de pagar membresía de Apple en esta etapa).""")

pdf.chapter_title("Presupuesto")
pdf.chapter_body("""Valor total del desarrollo: USD 325

Este precio incluye:
- Diseño, desarrollo e implementación del sistema completo.
- Soporte para pruebas internas tanto en Android como en iPhone.
- Asesoramiento para publicación oficial si se desea en una siguiente etapa.
- Inclusión del costo único para publicar en Google Play.

Forma de pago:
- 50% al iniciar el proyecto: USD 162.50
- 50% al finalizar y entregar la versión funcional: USD 162.50
- Medio de cobro: A convenir (transferencia bancaria, PayPal u otro medio acordado).""")

pdf.chapter_title("Plazos de entrega")
pdf.chapter_body("""Duración estimada del desarrollo: 3 a 4 semanas desde la confirmación del proyecto.
Comunicación continua para revisión y ajustes durante el desarrollo.""")

pdf.chapter_title("Aclaración sobre iPhone")
pdf.chapter_body("""Para la fase de prueba, la app podrá instalarse en iPhone mediante un sistema de pruebas internas válido por 90 días. Si el cliente desea publicar oficialmente la aplicación en la tienda de Apple en el futuro, deberá contar con una cuenta de desarrollador que tiene un costo anual de 99 USD (opcional en esta etapa).La aplicación podrá probarse en Android directamente. Para su uso en iPhone, Apple exige contar con una cuenta de desarrollador con un costo anual de 99 USD. En una etapa posterior, si el cliente lo desea, podrá gestionarse la publicación en App Store o pruebas internas mediante TestFlight.""")

pdf.chapter_title("Cierre")
pdf.chapter_body("""Esta solución está diseñada específicamente para resolver una necesidad real y frecuente en el sector inmobiliario. Apunta a fortalecer la gestión profesional de los contactos, mejorar el respeto entre colegas, y optimizar el uso de recursos a través de una herramienta intuitiva, eficaz y adaptada al flujo diario de trabajo.

Estoy a disposición para responder cualquier consulta y avanzar con el desarrollo.""")

pdf.chapter_title("Contacto")
pdf.chapter_body("""Ever Loza
Desarrollador de Software e Inteligencia Artificial
Correo: everlozaruiz@gmail.com
WhatsApp: +54 2964 452631""")

# Guardar PDF
pdf.output("Propuesta_EverLoza_Final.pdf")
