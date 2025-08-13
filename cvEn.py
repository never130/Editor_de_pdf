from fpdf import FPDF

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_margins(15, 15, 15)  # Balanced margins for better readability
    
    def header(self):
        # Header with improved proportional sizes
        self.set_font("Helvetica", "B", 16)  # Reduced size but still prominent
        self.cell(0, 10, "EVER LOZA RUIZ", ln=True, align="C")
        self.set_font("Helvetica", "B", 12)  # Reduced size to save space
        self.cell(0, 8, " Software & AI Developer  | Advanced Technician in Data Science and AI", ln=True, align="C")

        # Contact information (centered with better spacing)
        self.set_font("Helvetica", "", 10)  # Reduced size to save space
        self.cell(0, 7, "Rio Grande, Tierra del Fuego | everlozaruiz@gmail.com | +54 2964 452631", ln=True, align="C")
        self.cell(0, 7, "Linkedin: www.linkedin.com/in/never130 | Github: www.github.com/never130 | Portfolio: https://everloza-porfolio.netlify.app", ln=True, align="C")
        # Separated to avoid overly long line
        self.ln(5)  # Very reduced space to maximize space

    def section_title(self, title):
        # More prominent section titles
        self.set_font("Helvetica", "B", 13)  # Reduced size for sections
        # Underline for better visual ATS structure
        self.cell(0, 8, title, ln=True)
        self.line(15, self.get_y(), 195, self.get_y())
        self.ln(2)

    def footer(self):
        self.set_y(-18)
        self.set_font("Helvetica", "I", 10)  # Increased to 10 for better readability
        self.cell(0, 6, f"{self.page_no()}", 0, 0, 'C')

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
    "Software & AI Developer with a technical background in Data Science and Artificial Intelligence. Proven experience in end-to-end development of web and mobile applications, integrating backend, frontend, and modern database solutions. Proficient in multiple technology stacks (JavaScript/TypeScript, Python, Node.js, React, Flutter, FastAPI, MongoDB) and in implementing data-driven solutions. Skilled in integrating advanced analytics, computer vision, and predictive models into production systems."
)
pdf.ln(5)

# Work Experience - Optimized for ATS with highlighted keywords
pdf.section_title("WORK EXPERIENCE")

experiences = [
    {
        "title": "MOBILE DEVELOPMENT - Call Identification App",
        "company": "Macrobow",
        "period": "Jul 2025 - Aug 2025",
        "technologies": "Flutter, Express.js, Firebase, Node.js, Firebase Authentication, Dart",
        "bullets": [
            "Development of a mobile call identification app tailored for real estate agents to verify client exclusivity",
            "Backend design using Express.js and Firebase for real-time data synchronization and user authentication via SMS",
            "Creation of a smooth and intuitive mobile interface with Flutter, adapted to the specific needs of the real estate sector"
        ]
    },
    {
        "title": "SOFTWARE DEVELOPMENT - Restaurant System",
        "company": "Isidro Libre & Gourmet - Gastronomy",
        "period": "Apr 2025 - Jun 2025",
        "technologies": "Node.js, PostgreSQL, Express, Typescript, TypeORM, JWT, Tailwind CSS",
        "bullets": [
            "Built a real-time order management system with stock control and automatic daily closing using Next.js and PostgreSQL.",
            "Automated raw material deduction upon sales registration, optimizing inventory efficiency.",
            "Reduced manual input errors by 30% through a simplified user interface and backend validation."
        ]
    },
    {
        "title": "AI SOFTWARE DEVELOPMENT - Vision System for Industrial Carts",
        "company": "El Dorado",
        "period": "Apr 2025 - Jun 2025",
        "technologies": "React, Node.js, Postgresql, Express, Typescript",  # Keywords for ATS
        "bullets": [
            "Designed and trained a custom YOLOv8 model for automatic detection of numeric identifiers on industrial carts.",
            "Implemented a robust RESTful API with FastAPI and NoSQL storage with MongoDB for managing historical records.",
            "Developed real-time notifications using WebSockets to enhance logistical movement traceability.",
        ]
    },
    {
        "title": "FULL STACK DEVELOPMENT",
        "company": "Tienda del Fuego Accesorios",
        "period": "Feb 2024 - May 2024",
        "technologies": "React, Node.js, MongoDB, Express, JavaScript, REST API",
        "bullets": [
            "Developed and deployed a complete e-commerce platform, increasing sales by 25% in the first 3 months.",
            "Integrated payment gateway with MercadoPago and security logic based on JWT for secure authentication.",
            "Designed an admin dashboard with metrics and product CRUD using React + Redux."
        ]
    },
    {
        "title": "DATA ANALYST",
        "company": "Aeropuerto Internacional Trejo Noel",
        "period": "Mar 2024 - Aug 2024",
        "technologies": "Python, Power BI, ETL, Pandas, NumPy",
        "bullets": [
            "Designed interactive dashboards to visualize operational KPIs using Power BI.",
            "Analyzed large volumes of air traffic data to identify bottlenecks and improvement opportunities."
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
        pdf.cell(8, 6, "-", ln=0)  # Dash as bullet point compatible with latin1
        pdf.cell(4, 6, "", ln=0)   # Space after bullet
        pdf.multi_cell(0, 5.5, bullet)
    pdf.ln(2)

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
pdf.cell(0, 7, "Advanced Technician in Data Science and Artificial Intelligence", ln=True)
pdf.set_font("Helvetica", "", small_text)
pdf.cell(0, 6, "Centro Politécnico Superior Malvinas Argentinas | 2023-2025", ln=True)
pdf.ln(4)

# Certifications - Improved format for ATS
pdf.section_title("CERTIFICATIONS")
certs = [
    {"title": "SQL/NodeJS", "issuer": "Alkemy", "hours": "160h"},
    {"title": "Full Stack Web Development", "issuer": "Ministry of Education BA", "hours": "200h"},
    {"title": "Google Cloud Computing Fundamentals", "issuer": "Google", "hours": "40h"},
    {"title": "JavaScript Algorithms and Data Structures", "issuer": "FreeCodeCamp", "hours": "300h"},
    {"title": "Backend Development and APIs", "issuer": "FreeCodeCamp", "hours": "300h"},
]

pdf.set_font("Helvetica", "", normal_text)
for cert in certs:
    pdf.cell(8, 7, "-", ln=0)  # Dash as bullet point
    pdf.cell(4, 7, "", ln=0)   # Space
    pdf.multi_cell(0, 6, f"{cert['title']} - {cert['issuer']} ({cert['hours']})")
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
    "Development of a hybrid expert system for diagnosing respiratory diseases using medical IF-THEN rules and Machine Learning models",
    "Implementation of a decoupled inference engine backend with Flask, capable of evaluating customizable rules and backed by Decision Tree models",
    "Design of a modern frontend using Next.js and Tailwind CSS, with an intuitive interface for symptom input, results visualization, and rule management"
  ]
}

]

for project in projects:
    pdf.set_font("Helvetica", "B", normal_text)
    pdf.cell(0, 7, project["title"], ln=True)
    pdf.set_font("Helvetica", "I", small_text)
    pdf.cell(0, 6, f"Technologies: {project['tech']}", ln=True)  # Explicit technologies for ATS
    pdf.set_font("Helvetica", "", normal_text)
    for bullet in project["bullets"]:
        pdf.cell(8, 6, "-", ln=0)  # Dash as bullet point
        pdf.cell(4, 6, "", ln=0)   # Space
        pdf.multi_cell(0, 6, bullet)
    pdf.ln(3)

# Languages - Additional ATS section
pdf.section_title("LANGUAGES")
pdf.set_font("Helvetica", "", normal_text)
pdf.cell(40, 6, "Spanish:", ln=0)
pdf.cell(40, 6, "Native", ln=0)
pdf.cell(40, 6, "English:", ln=0)
pdf.cell(0, 6, "Professional (B2)", ln=True)
pdf.ln(3)

# Save PDF
pdf.output("CV_EverLoza_dev.pdf")
