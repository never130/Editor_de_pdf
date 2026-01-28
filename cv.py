from fpdf import FPDF, XPos, YPos

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_margins(15, 15, 15)

    def header(self):
        self.set_font("Helvetica", "B", 16)
        self.cell(0, 10, "EVER LOZA RUIZ", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
        self.set_font("Helvetica", "B", 12)
        self.cell(0, 8, "Software & AI Developer | Tecnico Superior en Ciencia de Datos e IA", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")

        self.set_font("Helvetica", "", 10)
        self.cell(0, 7, "Rio Grande, Tierra del Fuego | everlozaruiz@gmail.com | +54 2964 452631", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
        self.cell(0, 7, "LinkedIn: www.linkedin.com/in/never130 | GitHub: www.github.com/never130 | Portfolio: everloza-porfolio.netlify.app", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
        self.ln(5)

    def section_title(self, title):
        self.set_font("Helvetica", "B", 13)
        self.cell(0, 8, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.line(15, self.get_y(), 195, self.get_y())
        self.ln(2)

    def footer(self):
        self.set_y(-18)
        self.set_font("Helvetica", "I", 10)
        self.cell(0, 6, f"{self.page_no()}", border=0, align="C")


pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=18)
pdf.add_page()

normal_text = 10
small_text = 9

# PERFIL
pdf.section_title("PERFIL PROFESIONAL")
pdf.set_font("Helvetica", "", normal_text)
pdf.multi_cell(
    0, 7,
    "Software & AI Developer con formacion tecnica en Ciencia de Datos e Inteligencia Artificial. "
    "Experiencia en desarrollo de aplicaciones web y moviles end-to-end, integrando backend, frontend "
    "y bases de datos modernas. Competente en JavaScript/TypeScript y Python (Node.js, Express, React, "
    "FastAPI), integraciones con APIs y pipelines de datos. Capacidad para implementar funcionalidades "
    "orientadas a producto, mejorar performance y llevar soluciones a produccion."
    ,
    new_x=XPos.LMARGIN,
    new_y=YPos.NEXT,
)
pdf.ln(5)

# EXPERIENCIA
pdf.section_title("EXPERIENCIA LABORAL")

experiences = [
    # NUEVO: Agencia de Innovacion TDF
    {
        "title": "DESARROLLADOR FULL STACK",
        "company": "Agencia de Innovacion TDF (Gobierno de Tierra del Fuego)",
        "period": "Nov 2025 - Actualidad",
        "technologies": "Python, Django/FastAPI, TypeScript, REST APIs, Integraciones, Git",
        "bullets": [
            "Desarrollo y mantenimiento de funcionalidades backend y frontend en plataformas institucionales.",
            "Implementacion de integraciones con servicios externos y mejoras de performance y estabilidad en produccion.",
            "Colaboracion con equipos internos para analisis de requerimientos, entregas incrementales y correccion de incidencias."
        ]
    },

    # NUEVO: PachaMates
    {
        "title": "SOFTWARE DEVELOPER - E-commerce Full Stack",
        "company": "PachaMates (E-commerce artesanal)",
        "period": "Oct 2025 - Dic 2025",
        "technologies": "React, TypeScript, Node.js, Express, MongoDB, JWT, MercadoPago (Checkout Pro), Webhooks",
        "bullets": [
            "Desarrollo full stack de e-commerce: catalogo, busqueda, categorias, carrito persistente y checkout completo.",
            "Integracion de pagos con MercadoPago (Checkout Pro) con return URLs y webhook backend para validacion en tiempo real.",
            "Implementacion de gestion de envios con calculo de tarifas y seguimiento; historial de ordenes y gestion de direcciones.",
            "Panel administrador para productos, pedidos, reportes y usuarios; arquitectura SPA + API lista para despliegue."
        ]
    },

    # # Macrobow
    # {
    #     "title": "DESARROLLO MOVIL - App de Identificacion de Llamadas",
    #     "company": "Macrobow",
    #     "period": "Jul 2025 - Ago 2025",
    #     "technologies": "Flutter, Express.js, Firebase, Node.js, Firebase Authentication, Dart",
    #     "bullets": [
    #         "Desarrollo de aplicacion movil de identificacion de llamadas enfocada en agentes inmobiliarios para verificacion de exclusividad de clientes.",
    #         "Diseno de backend con Express.js y Firebase para sincronizacion de datos en tiempo real y autenticacion mediante SMS.",
    #         "Construccion de una interfaz movil fluida e intuitiva con Flutter, adaptada al flujo de trabajo del sector inmobiliario."
    #     ]
    # },

    # Isidro Libre & Gourmet
    {
        "title": "DESARROLLO DE SOFTWARE - Sistema para Restaurantes",
        "company": "Isidro Libre & Gourmet (Gastronomia)",
        "period": "Abr 2025 - Jun 2025",
        "technologies": "Node.js, PostgreSQL, Express, TypeScript, TypeORM, JWT, Tailwind CSS",
        "bullets": [
            "Desarrollo de sistema de gestion de pedidos con control de stock y cierre automatico diario.",
            "Automatizacion de deduccion de materias primas al registrar ventas, optimizando la gestion de inventario.",
            "Reduccion de errores de carga manual mediante validaciones en backend y mejoras de interfaz."
        ]
    },

    # El Dorado
    {
        "title": "DESARROLLO DE IA - Vision Computacional",
        "company": "El Dorado",
        "period": "Abr 2025 - Jun 2025",
        "technologies": "Python, FastAPI, MongoDB, React, YOLOv8, OpenCV, WebSockets, Tailwind CSS",
        "bullets": [
            "Desarrollo de sistema de vision computacional para deteccion de numeros en vagonetas mediante modelos YOLOv8 entrenados.",
            "Diseno de backend con FastAPI y MongoDB para almacenamiento persistente, API REST y notificaciones en tiempo real via WebSockets.",
            "Implementacion de procesamiento de imagenes y video, con carga manual y captura automatica desde camaras configurables."
        ]
    },

    # Tienda del Fuego (corregido a Actualidad)
    {
        "title": "DESARROLLO FULL STACK - E-commerce",
        "company": "Tienda del Fuego Accesorios",
        "period": "Abr 2024 - Dec 2024",
        "technologies": "React, Node.js, MongoDB, Express, JavaScript/TypeScript, REST API, MercadoPago",
        "bullets": [
            "Desarrollo de plataforma e-commerce con gestion de productos, usuarios, pedidos y envios.",
            "Implementacion de pagos integrados con MercadoPago y mejoras en el flujo de compra.",
            "Desarrollo de dashboard administrativo con metricas de ventas y gestion de inventario."
        ]
    },

    # Aeropuerto
    # {
    #     "title": "ANALISTA DE DATOS",
    #     "company": "Aeropuerto Internacional Trejo Noel",
    #     "period": "Mar 2024 - Ago 2024",
    #     "technologies": "Python, Power BI, ETL, SQL, Pandas, NumPy",
    #     "bullets": [
    #         "Creacion de dashboards interactivos para visualizacion de KPIs operacionales utilizando Power BI.",
    #         "Analisis de grandes volumenes de datos para identificar patrones y oportunidades de optimizacion."
    #     ]
    # }
]

for exp in experiences:
    pdf.set_font("Helvetica", "B", normal_text)
    pdf.cell(0, 7, f"{exp['title']} | {exp['company']}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.set_font("Helvetica", "I", small_text)
    pdf.cell(0, 6, f"{exp['period']} | {exp['technologies']}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.set_font("Helvetica", "", normal_text)
    for bullet in exp["bullets"]:
        x_left = pdf.l_margin
        pdf.set_x(x_left)
        pdf.cell(4, 5.5, "-", new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.set_x(x_left + 8)
        pdf.multi_cell(0, 5.5, bullet, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(2)

# FORMACION
pdf.section_title("FORMACION ACADEMICA")
pdf.set_font("Helvetica", "B", normal_text)
pdf.cell(0, 7, "Tecnico Superior en Ciencias de Datos e Inteligencia Artificial", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_font("Helvetica", "", small_text)
pdf.cell(0, 6, "Centro Politecnico Superior Malvinas Argentinas | 2023 - 2025", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.ln(4)

# CERTIFICACIONES
pdf.section_title("CERTIFICACIONES RELEVANTES")
certs = [
    {"title": "SQL/NodeJS", "issuer": "Alkemy", "hours": "160h"},
    {"title": "Desarrollo Web Full Stack", "issuer": "Ministerio de Educacion BA", "hours": "200h"},
    {"title": "Google Cloud Computing Fundamentals", "issuer": "Google", "hours": "40h"},
    {"title": "Algoritmos de JavaScript y Estructuras de Datos", "issuer": "FreeCodeCamp", "hours": "300h"},
    {"title": "Desarrollo Back End y APIs", "issuer": "FreeCodeCamp", "hours": "300h"},
]

pdf.set_font("Helvetica", "", normal_text)
for cert in certs:
    x_left = pdf.l_margin
    pdf.set_x(x_left)
    pdf.cell(4, 6, "-", new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.set_x(x_left + 8)
    pdf.multi_cell(0, 6, f"{cert['title']} - {cert['issuer']} ({cert['hours']})", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.ln(2)

# PROYECTOS
pdf.section_title("PROYECTOS DESTACADOS")
projects = [
    {
        "title": "Prediccion de Energia Eolica con Machine Learning",
        "tech": "Python, Scikit-learn, Pandas",
        "bullets": [
            "Desarrollo de modelo predictivo basado en Random Forest con 92% de precision para pronostico de generacion eolica.",
            "Procesamiento y limpieza de datasets con mas de 20.000 registros historicos con Pandas y NumPy."
        ]
    },
    {
        "title": "Sistema Experto para Diagnostico de Enfermedades Respiratorias",
        "tech": "Python, Flask, DecisionTree, JSON, Next.js, Tailwind CSS",
        "bullets": [
            "Sistema experto hibrido con reglas SI-ENTONCES y modelo ML con explicabilidad para apoyo diagnostico.",
            "Backend con Flask y motor de inferencia desacoplado para evaluar reglas personalizables.",
            "Frontend con Next.js y Tailwind CSS para ingreso de sintomas, resultados y gestion de reglas."
        ]
    }
]

for project in projects:
    pdf.set_font("Helvetica", "B", normal_text)
    pdf.cell(0, 7, project["title"], new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.set_font("Helvetica", "I", small_text)
    pdf.cell(0, 6, f"Tecnologias: {project['tech']}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.set_font("Helvetica", "", normal_text)
    for bullet in project["bullets"]:
        x_left = pdf.l_margin
        pdf.set_x(x_left)
        pdf.cell(4, 6, "-", new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.set_x(x_left + 8)
        pdf.multi_cell(0, 6, bullet, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(3)

# IDIOMAS
pdf.section_title("IDIOMAS")
pdf.set_font("Helvetica", "", normal_text)
pdf.cell(40, 6, "Espanol:", new_x=XPos.RIGHT, new_y=YPos.TOP)
pdf.cell(40, 6, "Nativo", new_x=XPos.RIGHT, new_y=YPos.TOP)
pdf.cell(40, 6, "Ingles:", new_x=XPos.RIGHT, new_y=YPos.TOP)
pdf.cell(0, 6, "Profesional (B2)", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.ln(3)

pdf.output("CV_EverLoza_des.pdf")
print("OK - CV_EverLoza_des.pdf generado")
