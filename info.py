
"""Editable content blocks for the single-page Streamlit portfolio."""

# Core identity and contact
name = "Raghavan Madabushi"
major = "Electrical Engineering"
school = "Georgia Institute of Technology"
hometown = "Birmingham, Alabama"

my_linkedin_url = "https://www.linkedin.com/in/raghavan-madabushi-0aaa0533b/"
my_github_url = "https://github.com/RaghavanMadabushi14/autismtrackerv2"
my_email_address = "raghavanmadabushi10@gmail.com"

contact_links = {
    "LinkedIn": my_linkedin_url,
    "GitHub": my_github_url,
    "Email": f"mailto:{my_email_address}",
}

# Media assets
profile_picture = "Images/profile.jpeg"
resume_pdf_path = "Images/resume.pdf"

# Rubric-oriented visual checklist (5 required visuals)
visual_assets = {
    "Profile Picture": "Images/profile.jpeg",
    "Observa Graphic": "Images/cook.jpg",
    "Tennis or Activity Image": "Images/puff2.jpg",
    "Resume Screenshot": "Images/cleaner.jpg",
    "GT or Campus Graphic": "Images/puff.jpg",
}

welcome_statement = (
    "Welcome to my ECE 1100 ePortfolio. This site is my personal hub, where I combine "
    "my story, technical work, leadership involvement, and roadmap for becoming another "
    "great Georgia Tech engineer. I designed this portfolio to demonstrate my coursework "
    "and projects as I grow through Georgia Tech."
)

summary_introduction = """
This ePortfolio is designed as both a professional tool and a personal roadmap. For a
recruiter, professor, or collaborator, it provides a clear roadmap of what roles I am
interested in and why I am a good fit for those roles. For me, it functions as a reflection
system where I can document growth over time and identify gaps in my preparation. Rather than
just focusing on outcomes, this site also focuses on ongoing projects to showcase what I am
truly working on.

I approach engineering as a method of solving problems conveniently. When I see a challenge,
I do not only think about a solution; I think about one that can scale well and be used by a
large number of people. This perspective is visible in my discovery project, research interests,
and service work. My long-term goal is to become a systems engineer who can bridge the gap
between software and hardware technology.
"""

about_me = """
My name is Raghavan Madabushi, and I am an Electrical Engineering student at Georgia Tech.
Originally from Birmingham, Alabama, I saw that there was a lack of access to high-tech
medical resources. I made it a goal to engineer for impact: the most advanced tools should
be transformed into solutions that are affordable and accessible to everyone.

My journey to Georgia Tech was fueled by the desire to be at a world-class research institute.
This institution is always at the cutting edge of technology, and it was the perfect place for me.
While my academics are centered on physics, circuits, and coding, I also enjoy working out,
playing tennis, and serving my community. I currently support the Kidzz2Leaders philanthropy
through my fraternity. These experiences have taught me that technical skill is only half the
battle; the other half is understanding people and having a desire to make a lasting connection
and impact.
"""

career_goals = {
    "Year 1 (Current)": (
        "Master the fundamentals of Electrical Engineering while participating "
        "in the Create-X Startup Launch."
    ),
    "Year 2 (2026-2027)": (
        "Specialize in the Signal Processing and Robotics threads. Present Observa "
        "research findings at the American Psychiatric Association Conference."
    ),
    "Year 3 (2027-2028)": (
        "Secure a specialized internship at a robotics firm (like Intuitive Surgical "
        "or a med-tech startup) to learn hardware integration."
    ),
    "Year 4 (2028-2029)": (
        "Complete my Senior Design project focusing on low-cost sensor arrays and prepare "
        "for a career as a Systems Engineer in the Electrical Engineering space."
    ),
}

discovery_project_overview = """
Project Observa: Building an Eye Tracking Model using Arducam

Problem:
The grander scheme of this project was fueled by the desire to build an accessible, low-cost
screening tool for autism. The current screening tool is a questionnaire given to parents. It
is often not completed properly, resulting in diagnostic delays. For many families, this screening
is not even conducted. I wanted to build a bridge between high-level signal processing and pediatric
care. That is where Observa jumps in.

Technical Architecture:
Observa uses a Python-based machine learning pipeline to analyze gaze biomarkers. It tracks
fixation duration, saccades, and gaze preference when a child is presented with various stimuli.
On the hardware side, through the duration of the discovery project, I have been trying to build
the eye-tracking module. Using a basic Arduino camera, I was able to use a high-speed camera to
map gaze patterns in adults. This required a deep dive into computer vision libraries like OpenCV.
I had to learn how to filter noise in real time. I also had to think about practical tradeoffs
such as lighting, camera placement, and calibration.

Future Objectives:
The progress I have made includes being accepted to the Create-X Summer Launch program. I am
hoping to receive IRB approval and then start real clinical trials to take the screening tool
toward FDA approval. While these are long-term goals, I am satisfied with the progress I have
made through the creation of the eye-tracking module for my discovery project.
"""

technical_growth_reflection = ""

education_data = {
    "Degree": "Bachelor of Science in Electrical Engineering",
    "Institution": "Georgia Institute of Technology",
    "Location": "Atlanta, GA",
    "Graduation Date": "2029",
    "GPA": "3.50",
}

experience_data = {
    "Intern at RRPA": (
        [
            "Secured the role of intake coordinator where I developed practical skills in clinical operations and data management.",
            "Managed communication logistics for more than 500 patients while maintaining data accuracy and privacy.",
            "Worked within HIPAA-aligned workflows to process sensitive records and support timely patient onboarding.",
            "Improved tracking procedures for patient progress, helping reduce administrative bottlenecks.",
        ],
        "Images/cleaner.jpg",
    ),
    "Cardiovascular Research": (
        [
            "Researched cardiovascular disease trends affecting children and adolescents with a prevention-first mindset.",
            "Analyzed health datasets to surface early warning signals often missed in standard screenings.",
            "Explored how wearable systems can support real-time monitoring in low-resource contexts.",
            "Presented findings centered on early intervention and data-driven care pathways.",
        ],
        "Images/jelly.jpg",
    ),
}

projects_data = {
    "Ghost QA (EMR Testing Concept)": [
        "Built Playwright-based QA flows targeting EMR reliability and billing integrity.",
        "Designed automated test cases to detect data persistence defects in patient charts.",
        "Documented failure scenarios involving unusual input and edge-case workflows.",
        "Concluded with a strong prototype foundation and clear technical next steps.",
    ],
    "Observa Founder Work": [
        "Designed an early autism screening concept based on gaze markers and gaze analytics.",
        "Developed initial end-to-end prototypes combining Python, computer vision, and low-cost hardware.",
        "Established pilot conversations with clinics in the Southeastern United States.",
        "Prepared to present findings at the 2026 American Psychiatric Association conference cycle.",
    ],
}

leadership_data = {
    "GT Energy Hack": (
        [
            "Served as a technical executive, coordinating project planning and deliverable quality.",
            "Supported team collaboration workflows and event submission readiness.",
        ],
        "Images/puff.jpg",
    ),
}

activity_data = {
    "Beta Theta Pi Service Work": (
        [
            "Contributed to Beta Lei, a philanthropy initiative supporting children with incarcerated parents in Atlanta.",
            "Helped organize logistics, outreach, and fundraising operations across student teams.",
            "Balanced engineering coursework with sustained community engagement and leadership.",
        ],
        "Images/puff2.jpg",
    ),
}

programming_data = {
    "Python": 90,
    "Java": 65,
    "C/C++": 55,
}

programming_icons = {
    "Python": "🐍",
    "Java": "☕",
    "C/C++": "⚙️",
}

spoken_data = {
    "English": "Fluent",
}

spoken_icons = {
    "English": "🇬🇧",
}
