from fpdf import FPDF

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_margins(15, 15, 15)  # Márgenes balanceados para mejor legibilidad
    
    def header(self):
        # Encabezado con tamaños proporcionales mejorados
        self.set_font("Helvetica", "B", 16)  # Tamaño reducido pero aún destacado
        self.cell(0, 10, "EVER LOZA RUIZ", ln=True, align="C")
        self.set_font("Helvetica", "B", 12)  # Tamaño reducido para ahorrar espacio
        self.cell(0, 8, "Software & AI Developer | Técnico Superior en Ciencia de Datos e IA", ln=True, align="C")
        
        # Información de contacto (centrada y con mejor espaciado)
        self.set_font("Helvetica", "", 10)  # Tamaño reducido para ahorrar espacio
        self.cell(0, 7, "Rio Grande, Tierra del Fuego | never130@hotmail.com | +54 2964 452631", ln=True, align="C")
        self.cell(0, 7, "Linkedin: never130 | Github: never130 | Portfolio: everloza-porfolio.netlify.app", ln=True, align="C")
          # Separado para evitar línea demasiado larga
        self.ln(5)  # Espacio muy reducido para maximizar espacio

    def section_title(self, title):
        # Títulos de sección más destacados
        self.set_font("Helvetica", "B", 13)  # Tamaño reducido para secciones
        # Línea subrayada para mejorar la estructura visual para ATS
        self.cell(0, 8, title, ln=True)
        self.line(15, self.get_y(), 195, self.get_y())
        self.ln(2)

    def footer(self):
        self.set_y(-18)
        self.set_font("Helvetica", "I", 10)  # Aumentado a 10 para mejor legibilidad
        self.cell(0, 6, f"{self.page_no()}", 0, 0, 'C')

# Inicializar PDF
pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=18)
pdf.add_page()

# Tamaños de fuente optimizados para 2 páginas
normal_text = 10  # Reducido para ahorrar espacio
small_text = 9    # Reducido para ahorrar espacio
title_size = 13   # Reducido pero manteniendo jerarquía visual

# Perfil Profesional
pdf.section_title("PERFIL PROFESIONAL")
pdf.set_font("Helvetica", "", normal_text)
pdf.multi_cell(0, 7,
    "Software & AI Developer con formación técnica en Ciencia de Datos e Inteligencia Artificial. "
    "Combinado con la implementación de soluciones inteligentes basadas en datos. Certificado en Cloud Computing (Google Cloud) y metodologías ágiles. "
    "Capacidad comprobada para integrar análisis predictivo, visión computacional, sistemas expertos y visualización de datos en productos funcionales, escalables y explicables."
)
pdf.ln(5)

# Experiencia Laboral - Optimizado para ATS con palabras clave destacadas
pdf.section_title("EXPERIENCIA LABORAL")

experiences = [
    {
        "title": "DESARROLLO DE INTELIGENCIA ARTIFICAL - Sistema de Visión Computacional",
        "company": "El Dorado",
        "period": "May 2025 - Jul 2025",
        "technologies": "FastAPI, MongoDB, React, YOLOv8, OpenCV, WebSockets, Tailwind CSS, Axios, JavaScript, Python",
        "bullets": [
            "Diseñé y entrené un modelo YOLOv8 personalizado para la detección automática de identificadores numéricos en vagonetas industriales.",
            "Implementé una API RESTful robusta con FastAPI y almacenamiento NoSQL con MongoDB para gestión de registros históricos.",
            "Desarrollé notificaciones en tiempo real utilizando WebSockets para mejorar la trazabilidad de los movimientos logísticos.",
        ]
    },   
    {
        "title": "DESARROLLO DE SOFTWARE - Sistema de Restaurantes",
        "company": "Isidro Libre & Gourmet",
        "period": "Abr 2025 - Jun 2025", 
        "technologies": "NextJS, Node.js, PostgreSQL, Express, Typescript, TypeORM, JWT, Tailwind CSS",
        "bullets": [
            "Construí un sistema de comandas en tiempo real con gestión de stock y cierre automático diario utilizando Next.js y PostgreSQL.",
            "Automaticé la deducción de materias primas al registrar ventas, optimizando la eficiencia del inventario.",
            "Reduje los errores de carga manual en un 30% mediante interfaz de usuario simplificada y validación por backend."
        ]
    },
    {
        "title": "DESARROLLO FULL STACK",
        "company": "Tienda del Fuego Accesorios",
        "period": "Abr 2024 - Actualidad", 
        "technologies": "React, Node.js, MongoDB, Express, JavaScript, REST API",
        "bullets": [
            "Desarrollé e implementé una plataforma e-commerce completa, aumentando un 25% las ventas en los primeros 3 meses.",
            "Integré pasarela de pagos con MercadoPago y lógica de seguridad basada en JWT para autenticación segura.",
            "Diseñé un dashboard de administración con métricas y CRUD de productos usando React + Redux."
        ]
    },
    {
        "title": "ANALISTA DE DATOS",
        "company": "Aeropuerto Internacional Trejo Noel",
        "period": "Mar 2024 - Oct 2024",
        "technologies": "Python, Power BI, ETL, DAX",
        "bullets": [
            "Diseñé dashboards interactivos para visualizar KPIs operativos utilizando Power BI.",
            "Analicé grandes volúmenes de datos de tráfico aéreo para identificar cuellos de botella y oportunidades de mejora."
        ]
    }
]

for exp in experiences:
    pdf.set_font("Helvetica", "B", normal_text)
    pdf.cell(0, 7, f"{exp['title']} | {exp['company']}", ln=True)
    pdf.set_font("Helvetica", "I", small_text)
    pdf.cell(0, 6, f"{exp['period']} | {exp['technologies']}", ln=True)
    pdf.set_font("Helvetica", "", normal_text)
    for bullet in exp["bullets"]:
        pdf.cell(8, 6, "-", ln=0)  # Guion como bullet point compatible con latin1
        pdf.cell(4, 6, "", ln=0)   # Espacio después del bullet
        pdf.multi_cell(0, 5.5, bullet)
    pdf.ln(2)

pdf.add_page()
# Habilidades Técnicas - Formato para mejor detección ATS
pdf.section_title("HABILIDADES TÉCNICAS")
skills = [
    ("Desarrollo Frontend:", "React, HTML5, CSS3, Bootstrap, Redux, Responsive Design, Next.js"),
    ("Desarrollo Backend:", "Node.js, Express, FastAPI, Django, REST APIs, Microservicios"),
    ("Ciencia de Datos e IA:", "Pandas, NumPy, Scikit-learn, Power BI, Tableau, Machine Learning"),
    ("Bases de Datos:", "MongoDB, PostgreSQL, MySQL, Redis, Diseño de esquemas"),
    ("Cloud & DevOps:", "AWS (EC2, S3), Google Cloud Platform, Docker, CI/CD, Git")
]

for skill, details in skills:
    pdf.set_font("Helvetica", "B", normal_text)
    pdf.cell(55, 6, skill, ln=0)  # Reducido para ahorrar espacio
    pdf.set_font("Helvetica", "", normal_text)
    pdf.multi_cell(0, 6, details)
pdf.ln(5)

# Segunda Página

# Formación Académica
pdf.section_title("FORMACIÓN ACADÉMICA")
pdf.set_font("Helvetica", "B", normal_text)
pdf.cell(0, 7, "Técnico Superior en Ciencias de Datos e Inteligencia Artificial", ln=True)
pdf.set_font("Helvetica", "", small_text)
pdf.cell(0, 6, "Centro Politécnico Superior Malvinas Argentinas | 2023-2025", ln=True)
pdf.ln(4)

# Certificaciones - Formato mejorado para ATS
pdf.section_title("CERTIFICACIONES")
certs = [
    {"title": "SQL/NodeJS", "issuer": "Alkemy", "hours": "160h"},
    {"title": "Desarrollo Web Full Stack", "issuer": "Ministerio de Educación BA", "hours": "200h"},
    {"title": "Google Cloud Computing Fundamentals", "issuer": "Google", "hours": "40h"},
    {"title": "Algoritmos de JavaScript y Estructuras de Datos", "issuer": "FreeCodeCamp", "hours": "300h"},
    {"title": "Desarrollo Back End y APIs", "issuer": "FreeCodeCamp", "hours": "300h"},
]

pdf.set_font("Helvetica", "", normal_text)
for cert in certs:
    pdf.cell(8, 7, "-", ln=0)  # Guion como bullet point
    pdf.cell(4, 7, "", ln=0)   # Espacio
    pdf.multi_cell(0, 6, f"{cert['title']} - {cert['issuer']} ({cert['hours']})")
pdf.ln(2)

# Proyectos Destacados - Optimizados para ATS
pdf.section_title("PROYECTOS DESTACADOS")
projects = [
    {
        "title": "Predicción de Energía Eólica con Machine Learning",
        "tech": "Python, Scikit-learn, Pandas",
        "bullets": [
            "Desarrollo de modelo predictivo basado en Random Forest con 92% de precisión para pronóstico de generación eólica",
            "Procesamiento y limpieza de datasets con más de 20,000 registros históricos utilizando Pandas y NumPy",
        ]
    },
    {
    "title": "Sistema Experto para Diagnóstico de Enfermedades Respiratorias",
    "tech": "Python, Flask, Sklearn, JSON Rules, Next.js, Tailwind CSS",
    "bullets": [
        "Desarrollo de un sistema experto híbrido con motor de inferencia desacoplado que aplica reglas SI-ENTONCES en formato JSON para el diagnóstico de enfermedades respiratorias comunes",
        "Integración de un modelo supervisado (Árbol de Decisión) como respaldo predictivo cuando no se cumplen reglas, garantizando cobertura de casos y explicabilidad completa",
        "Diseño de una interfaz web moderna con Next.js para ingreso de síntomas, visualización del diagnóstico y edición dinámica de reglas sin intervención del código fuente"
    ]
}
]

for project in projects:
    pdf.set_font("Helvetica", "B", normal_text)
    pdf.cell(0, 7, project["title"], ln=True)
    pdf.set_font("Helvetica", "I", small_text)
    pdf.cell(0, 6, f"Tecnologías: {project['tech']}", ln=True)  # Tecnologías explícitas para ATS
    pdf.set_font("Helvetica", "", normal_text)
    for bullet in project["bullets"]:
        pdf.cell(8, 6, "-", ln=0)  # Guion como bullet point
        pdf.cell(4, 6, "", ln=0)   # Espacio
        pdf.multi_cell(0, 6, bullet)
    pdf.ln(3)

# Idiomas - Sección adicional para ATS
pdf.section_title("IDIOMAS")
pdf.set_font("Helvetica", "", normal_text)
pdf.cell(40, 6, "Español:", ln=0)
pdf.cell(40, 6, "Nativo", ln=0)
pdf.cell(40, 6, "Inglés:", ln=0)
pdf.cell(0, 6, "Profesional (B2)", ln=True)
pdf.ln(3)

# Guardar PDF
pdf.output("CV_EverLoza_FullStack_DataScience_ATS.pdf")