# Solución: reemplazar viñetas Unicode por un guion estándar antes de generar el PDF

from fpdf import FPDF

def sanitize_text(text):
    return text.replace("•", "-")

# Crear la clase PDF personalizada
class PDF(FPDF):
    def header(self):
        from fpdf.enums import XPos, YPos
        self.set_font("Helvetica", "B", 14)
        self.set_text_color(33, 37, 41)
        self.cell(0, 10, "EVER LOZA RUIZ", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
        self.set_font("Helvetica", "", 11)
        self.cell(0, 10, "Software & AI Developer | Estudiante en Ciencia de Datos e IA", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
        self.set_font("Helvetica", "", 10)
        self.cell(0, 8, "Rio Grande, Tierra del Fuego | never130@hotmail.com | +54 2964 452631", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
        self.cell(0, 6, "Linkedin: never130 | Github: never130 | Portfolio: everloza-porfolio.netlify.app", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
        self.ln(5)

    def chapter_title(self, title):
        from fpdf.enums import XPos, YPos
        self.set_fill_color(230, 230, 230)
        self.set_text_color(0)
        self.set_font("Helvetica", "B", 12)
        self.cell(0, 8, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT, fill=True)
        self.ln(2)

    def chapter_body(self, body):
        self.set_font("Helvetica", "", 10)
        self.multi_cell(0, 6, sanitize_text(body))
        self.ln()

pdf = PDF()
pdf.add_page()

# Datos para agregar al PDF
sections = {
    "PERFIL PROFESIONAL": """Software & AI Developer con formación técnica en curso en Ciencia de Datos e Inteligencia Artificial. Combinado con la implementación de soluciones inteligentes basadas en datos. Certificado en Cloud Computing (Google Cloud) y metodologías ágiles. Capacidad comprobada para integrar análisis predictivo, visión computacional, sistemas expertos y visualización de datos en productos funcionales, escalables y explicables.""",

    "EXPERIENCIA LABORAL": """DESARROLLO MÓVIL - App de Identificación de Llamadas | Macrobow (Jul 2025 - Actualidad)
• Desarrollo de aplicación móvil para identificación de llamadas dirigida a agentes inmobiliarios.
• Backend con Express y Firebase para sincronización en tiempo real.
• Interfaz móvil intuitiva con Flutter.

DESARROLLO DE INTELIGENCIA ARTIFICIAL - Sistema de Visión Computacional | El Dorado (May 2025 - Jul 2025)
• Modelo YOLOv8 personalizado para detección numérica en vagonetas.
• API RESTful con FastAPI, almacenamiento MongoDB.
• Notificaciones en tiempo real con WebSockets.

DESARROLLO DE SOFTWARE - Sistema de Restaurantes | Isidro Libre & Gourmet (Abr 2025 - Jun 2025)
• Sistema de comandas en tiempo real, Next.js y PostgreSQL.
• Automatización de stock y validaciones de backend.

DESARROLLO FULL STACK | Tienda del Fuego Accesorios (Abr 2024 - Actualidad)
• Plataforma e-commerce completa, incremento del 25% en ventas.
• Integración con MercadoPago, autenticación segura con JWT.

ANALISTA DE DATOS | Aeropuerto Internacional Trejo Noel (Mar 2024 - Oct 2024)
• Dashboards de KPIs en Power BI.
• Análisis de datos de tráfico aéreo para optimización.""" ,

    "HABILIDADES TÉCNICAS": """Frontend: React, HTML5, CSS3, Bootstrap, Redux, Responsive Design, Next.js
Backend: Node.js, Express, FastAPI, Django, REST APIs, Microservicios
Móvil: Flutter, Dart
IA y Datos: Pandas, NumPy, Scikit-learn, Power BI, Tableau, Machine Learning
Bases de Datos: MongoDB, PostgreSQL, MySQL, Redis, Firebase
Cloud/DevOps: AWS, Google Cloud, Docker, CI/CD, Git""",

    "FORMACIÓN ACADÉMICA": "Técnico Superior en Ciencias de Datos e Inteligencia Artificial, Centro Politécnico Superior Malvinas Argentinas (2023-2025)",

    "CERTIFICACIONES": """- SQL/NodeJS - Alkemy (160h)
- Desarrollo Web Full Stack - Ministerio de Educación BA (200h)
- Google Cloud Computing Fundamentals - Google (40h)
- JavaScript Algorithms & Data Structures - FreeCodeCamp (300h)
- Backend Development & APIs - FreeCodeCamp (300h)""",

    "PROYECTOS DESTACADOS": """Predicción de Energía Eólica con Machine Learning
- Modelo Random Forest con 92% precisión, procesamiento de +20.000 registros.

Sistema Experto para Diagnóstico de Enfermedades Respiratorias
- Motor de inferencia con reglas JSON + árbol de decisión.
- Interfaz web moderna editable sin tocar el código.""",

    "IDIOMAS": "Español: Nativo | Inglés: Profesional"
}

# Agregar secciones
for title, body in sections.items():
    pdf.chapter_title(title)
    pdf.chapter_body(body)

# Guardar PDF en el escritorio de Windows
output_path = r"C:\Users\Ever\Desktop\CV_EverLoza_2025.pdf"
pdf.output(output_path)
output_path