from fpdf import FPDF, XPos, YPos

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_margins(15, 15, 15)  # Balanced margins for better readability
    
    def header(self):
        # Header with improved proportional sizes
        self.set_font("Helvetica", "B", 16)  # Reduced size but still prominent
        self.cell(0, 10, "EVER LOZA RUIZ", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
        self.set_font("Helvetica", "B", 12)  # Reduced size to save space
        self.cell(0, 8, " Software & AI Developer  | Advanced Technician in Data Science and AI", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")

        # Contact information (centered with better spacing)
        self.set_font("Helvetica", "", 10)  # Reduced size to save space
        self.cell(0, 7, "Rio Grande, Tierra del Fuego | everlozaruiz@gmail.com | +54 2964 452631", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
        self.cell(0, 7, "Linkedin: www.linkedin.com/in/never130 | Github: www.github.com/never130 | Portfolio: https://everloza-porfolio.netlify.app", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
        # Separated to avoid overly long line
        self.ln(5)  # Very reduced space to maximize space

    def section_title(self, title):
        # More prominent section titles
        self.set_font("Helvetica", "B", 13)  # Reduced size for sections
        # Underline for better visual ATS structure
        self.cell(0, 8, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.line(15, self.get_y(), 195, self.get_y())
        self.ln(2)

    def footer(self):
        self.set_y(-18)
        self.set_font("Helvetica", "I", 10)  # Increased to 10 for better readability
        self.cell(0, 6, f"{self.page_no()}", border=0, align="C")

# Initialize PDF
pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=18)
pdf.add_page()

# Optimized font sizes for 2 pages
normal_text = 10  # Reduced to save space
small_text = 9    # Reduced to save space
title_size = 13   # Reduced but maintaining visual hierarchy

# Professional Profile
pdf.section_title("PROFESSIONAL PROFILE")
pdf.set_font("Helvetica", "", normal_text)
pdf.multi_cell(0, 7,
    "Software & AI Developer with a technical background in Data Science and Artificial Intelligence. Experience building end-to-end web and mobile applications, integrating backend, frontend, and modern databases. Proficient in JavaScript/TypeScript and Python (Node.js, Express, React, FastAPI), API integrations, and data pipelines. Strong ability to deliver product-oriented features, improve performance, and ship solutions to production."
    ,
    new_x=XPos.LMARGIN,
    new_y=YPos.NEXT,
)
pdf.ln(5)

# Work Experience - Optimized for ATS with highlighted keywords
pdf.section_title("WORK EXPERIENCE")

experiences = [
    {
        "title": "FULL STACK DEVELOPER",
        "company": "Agencia de Innovacion TDF (Government of Tierra del Fuego)",
        "period": "Nov 2025 - Present",
        "technologies": "Python, Django/FastAPI, TypeScript, REST APIs, Integrations, Git",
        "bullets": [
            "Developed and maintained backend and frontend features for institutional platforms.",
            "Integrated external services and improved performance and production stability.",
            "Collaborated with internal teams on requirements analysis, incremental deliveries, and incident fixes."
        ]
    },
    {
        "title": "SOFTWARE DEVELOPER - Full Stack E-commerce",
        "company": "PachaMates (Handcrafted e-commerce)",
        "period": "Oct 2025 - Dec 2025",
        "technologies": "React, TypeScript, Node.js, Express, MongoDB, JWT, MercadoPago (Checkout Pro), Webhooks",
        "bullets": [
            "Built a full-stack e-commerce: catalog, search, categories, persistent cart, and complete checkout.",
            "Integrated MercadoPago (Checkout Pro) with return URLs and backend webhook validation in real time.",
            "Implemented shipping management with rate calculation and tracking, plus order history and address management.",
            "Delivered an admin panel for products, orders, reports, and users; SPA + API architecture ready for deployment."
        ]
    },
    {
        "title": "SOFTWARE DEVELOPMENT - Restaurant System",
        "company": "Isidro Libre & Gourmet (Gastronomy)",
        "period": "Apr 2025 - Jun 2025",
        "technologies": "Node.js, PostgreSQL, Express, TypeScript, TypeORM, JWT, Tailwind CSS",
        "bullets": [
            "Developed an order management system with stock control and automatic daily closing.",
            "Automated raw material deduction upon sales registration, optimizing inventory management.",
            "Reduced manual entry errors through backend validations and UI improvements."
        ]
    },
    {
        "title": "AI DEVELOPMENT - Computer Vision",
        "company": "El Dorado",
        "period": "Apr 2025 - Jun 2025",
        "technologies": "Python, FastAPI, MongoDB, React, YOLOv8, OpenCV, WebSockets, Tailwind CSS",
        "bullets": [
            "Built a computer vision system to detect numbers on carts using trained YOLOv8 models.",
            "Designed a FastAPI + MongoDB backend for persistence, a REST API, and real-time WebSockets notifications.",
            "Implemented image and video processing with manual uploads and automated capture from configurable cameras."
        ]
    },
    {
        "title": "FULL STACK DEVELOPMENT - E-commerce",
        "company": "Tienda del Fuego Accesorios",
        "period": "Apr 2024 - Dec 2024",
        "technologies": "React, Node.js, MongoDB, Express, JavaScript/TypeScript, REST API, MercadoPago",
        "bullets": [
            "Built an e-commerce platform with product, user, order, and shipping management.",
            "Integrated MercadoPago payments and improved the purchase flow.",
            "Developed an admin dashboard with sales metrics and inventory management."
        ]
    }
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
# pdf.add_page()

# pdf.add_page()
# # Technical Skills - Format for better ATS detection
# pdf.section_title("TECHNICAL SKILLS")
# skills = [
#     ("Programming Languages:", "Python, JavaScript, TypeScript, SQL, Java"),
#     ("Frontend Development:", "React, HTML5, CSS3, Bootstrap, Redux, Responsive Design"),
#     ("Backend Development:", "Node.js, Express, FastAPI, Django, REST APIs, Microservices"),
#     ("Data Science & AI:", "Pandas, NumPy, Scikit-learn, Power BI, Tableau, Machine Learning"),
#     ("Databases:", "MongoDB, PostgreSQL, MySQL, Redis, Schema Design"),
#     ("Cloud & DevOps:", "AWS (EC2, S3), Google Cloud Platform, Docker, CI/CD, Git")
# ]

# for skill, details in skills:
#     pdf.set_font("Helvetica", "B", normal_text)
#     pdf.cell(55, 6, skill, ln=0)  # Reduced to save space
#     pdf.set_font("Helvetica", "", normal_text)
#     pdf.multi_cell(0, 6, details)
# pdf.ln(5)

# Second Page

# Education
pdf.section_title("EDUCATION")
pdf.set_font("Helvetica", "B", normal_text)
pdf.cell(0, 7, "Advanced Technician in Data Science and Artificial Intelligence", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_font("Helvetica", "", small_text)
pdf.cell(0, 6, "Centro Politécnico Superior Malvinas Argentinas | 2023-2025", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.ln(4)

# Certifications - Improved format for ATS
pdf.section_title("CERTIFICATIONS")
certs = [
    {"title": "SQL/NodeJS", "issuer": "Alkemy", "hours": "160h"},
    {"title": "Full Stack Web Development", "issuer": "Ministerio de Educacion BA", "hours": "200h"},
    {"title": "Google Cloud Computing Fundamentals", "issuer": "Google", "hours": "40h"},
    {"title": "JavaScript Algorithms and Data Structures", "issuer": "FreeCodeCamp", "hours": "300h"},
    {"title": "Backend Development and APIs", "issuer": "FreeCodeCamp", "hours": "300h"},
]

pdf.set_font("Helvetica", "", normal_text)
for cert in certs:
    x_left = pdf.l_margin
    pdf.set_x(x_left)
    pdf.cell(4, 6, "-", new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.set_x(x_left + 8)
    pdf.multi_cell(0, 6, f"{cert['title']} - {cert['issuer']} ({cert['hours']})", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.ln(2)

# Featured Projects - Optimized for ATS
pdf.section_title("FEATURED PROJECTS")
projects = [
    {
        "title": "Wind Energy Prediction with Machine Learning",
        "tech": "Python, Scikit-learn, Pandas",
        "bullets": [
            "Developed a predictive model based on Random Forest with 92% accuracy for wind energy forecasting",
            "Processed and cleaned datasets with over 20,000 historical records using Pandas and NumPy",
        ]
    },
    {
  "title": "Expert System for Respiratory Disease Diagnosis",
  "tech": "Python, Flask, DecisionTree, JSON, Next.js, Tailwind CSS",
  "bullets": [
    "Developed a hybrid expert system for respiratory disease diagnosis using IF-THEN rules and ML with explainability.",
    "Implemented a decoupled inference engine backend with Flask to evaluate customizable rules.",
    "Built a Next.js + Tailwind CSS frontend for symptom input, results visualization, and rule management."
  ]
}

]

for project in projects:
    pdf.set_font("Helvetica", "B", normal_text)
    pdf.cell(0, 7, project["title"], new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Helvetica", "I", small_text)
    pdf.cell(0, 6, f"Technologies: {project['tech']}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)  # Explicit technologies for ATS
    pdf.set_font("Helvetica", "", normal_text)
    for bullet in project["bullets"]:
        x_left = pdf.l_margin
        pdf.set_x(x_left)
        pdf.cell(4, 6, "-", new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.set_x(x_left + 8)
        pdf.multi_cell(0, 6, bullet, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(3)
# Languages - Additional ATS section

# Languages - Additional ATS section
pdf.section_title("LANGUAGES")
pdf.set_font("Helvetica", "", normal_text)
pdf.cell(40, 6, "Spanish:", new_x=XPos.RIGHT, new_y=YPos.TOP)
pdf.cell(40, 6, "Native", new_x=XPos.RIGHT, new_y=YPos.TOP)
pdf.cell(40, 6, "English:", new_x=XPos.RIGHT, new_y=YPos.TOP)
pdf.cell(0, 6, "Professional (B2)", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.ln(3)

# Save PDF
pdf.output("CV_EverLoza_dev.pdf")
