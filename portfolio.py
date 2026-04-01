import re
from pathlib import Path

import streamlit as st

import info


st.set_page_config(page_title="Raghavan Madabushi | ePortfolio", layout="wide")

st.markdown(
    """
<style>
.main .block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}
.contact-pill {
    display: inline-block;
    border: 1px solid #91c9e8;
    border-radius: 999px;
    padding: 0.3rem 0.8rem;
    margin-right: 0.4rem;
    margin-bottom: 0.5rem;
    background-color: #f5fbff;
    text-decoration: none;
    color: #0b3f59 !important;
    font-weight: 600;
}
.hero-tech-card {
    position: relative;
    border: 1px solid #b7d9ee;
    border-radius: 14px;
    padding: 0.9rem;
    margin-top: 0.2rem;
    background: linear-gradient(145deg, #f6fbff 0%, #e7f5ff 100%);
    overflow: hidden;
}
.ee-animated-title {
    font-size: 1rem;
    font-weight: 800;
    letter-spacing: 0.5px;
    margin-bottom: 0.4rem;
    background: linear-gradient(90deg, #0b3f59, #2f8bbf, #0b3f59);
    background-size: 220% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: pulseGradient 3s linear infinite;
}
.circuit-grid {
    position: relative;
    height: 66px;
    border-radius: 10px;
    background:
        linear-gradient(90deg, rgba(47, 139, 191, 0.18) 1px, transparent 1px),
        linear-gradient(rgba(47, 139, 191, 0.18) 1px, transparent 1px);
    background-size: 14px 14px;
    margin-top: 0.5rem;
}
.signal-dot {
    position: absolute;
    width: 10px;
    height: 10px;
    background: #0b3f59;
    border-radius: 50%;
    top: 28px;
    left: 4px;
    animation: signalTravel 3.6s ease-in-out infinite;
    box-shadow: 0 0 12px rgba(11, 63, 89, 0.6);
}
.robot-row {
    margin-top: 0.45rem;
    font-size: 1.2rem;
    display: flex;
    gap: 0.4rem;
    align-items: center;
}
.robot {
    display: inline-block;
    animation: robotFloat 2.4s ease-in-out infinite;
}
.robot:nth-child(2) {
    animation-delay: 0.35s;
}
.robot:nth-child(3) {
    animation-delay: 0.7s;
}
@keyframes pulseGradient {
    0% { background-position: 0% center; }
    100% { background-position: 220% center; }
}
@keyframes signalTravel {
    0% { transform: translateX(0); opacity: 0.6; }
    50% { transform: translateX(118px); opacity: 1; }
    100% { transform: translateX(236px); opacity: 0.6; }
}
@keyframes robotFloat {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-5px); }
}
</style>
""",
    unsafe_allow_html=True,
)


def image_exists(path: str) -> bool:
    return Path(path).exists()


def safe_image(
    path: str,
    caption: str,
    width: int = 360,
    fit_container: bool = False,
) -> None:
    if image_exists(path):
        if fit_container:
            st.image(path, caption=caption, use_container_width=True)
        else:
            st.image(path, caption=caption, width=width)
    else:
        st.warning(f"Missing image: `{path}`")


def text_word_count(text: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", text))


st.title(f"{info.name} - ECE 1100 ePortfolio")
st.subheader(f"{info.major}, {info.school}")
st.write(info.welcome_statement)
st.write(info.summary_introduction)

st.markdown("### Contact")
contact_badges = []
for label, url in info.contact_links.items():
    contact_badges.append(f'<a class="contact-pill" href="{url}" target="_blank">{label}</a>')
st.markdown("".join(contact_badges), unsafe_allow_html=True)

left_col, mid_col, right_col = st.columns([1, 1, 2])
with left_col:
    safe_image(info.profile_picture, "Profile", fit_container=True)
with mid_col:
    screening_path = "Images/screening.jpg"
    fallback_path = info.visual_assets["Observa Graphic"]
    image_path = screening_path if image_exists(screening_path) else fallback_path
    safe_image(image_path, "Screening Visual", fit_container=True)
    st.markdown(
        """
        <div class="hero-tech-card">
          <div class="ee-animated-title">Electrical Engineering in Motion</div>
          <div>Signal Processing • Circuits • Robotics</div>
          <div class="circuit-grid"><span class="signal-dot"></span></div>
          <div class="robot-row">
            <span class="robot">🤖</span>
            <span class="robot">⚙️</span>
            <span class="robot">🔌</span>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with right_col:
    st.markdown("### About Me")
    st.write(info.about_me)

st.markdown("### Education")
st.markdown(
    f"""
- **Degree:** {info.education_data['Degree']}
- **Institution:** {info.education_data['Institution']}
- **Location:** {info.education_data['Location']}
- **Graduation Date:** {info.education_data['Graduation Date']}
- **GPA:** {info.education_data['GPA']}
"""
)

st.markdown("### Resume")
resume_path = Path(info.resume_pdf_path)
if resume_path.exists():
    with open(resume_path, "rb") as resume_file:
        st.download_button(
            label="Download Resume PDF",
            data=resume_file.read(),
            file_name=resume_path.name,
            mime="application/pdf",
        )
else:
    st.error(f"Resume file not found: `{info.resume_pdf_path}`")

st.markdown("### Career Goals Roadmap")
for year, goal in info.career_goals.items():
    st.markdown(f"- **{year}:** {goal}")

st.markdown("### Discovery Project (Observa)")
safe_image(info.visual_assets["Observa Graphic"], "Project Observa", width=700)
st.write(info.discovery_project_overview)

st.markdown("### Additional Experience")
for role, (bullets, image_path) in info.experience_data.items():
    with st.expander(role):
        safe_image(image_path, role, width=300)
        for bullet in bullets:
            st.markdown(f"- {bullet}")

st.markdown("### Technical Projects")
for project, bullets in info.projects_data.items():
    with st.expander(project):
        for bullet in bullets:
            st.markdown(f"- {bullet}")

st.markdown("### Leadership and Service")
for title, (bullets, image_path) in info.leadership_data.items():
    with st.expander(title):
        safe_image(image_path, title, width=300)
        for bullet in bullets:
            st.markdown(f"- {bullet}")

for title, (bullets, image_path) in info.activity_data.items():
    with st.expander(title):
        safe_image(image_path, title, width=300)
        for bullet in bullets:
            st.markdown(f"- {bullet}")

st.markdown("### Skills")
skill_col_1, skill_col_2 = st.columns(2)
with skill_col_1:
    st.markdown("**Programming**")
    for skill, score in info.programming_data.items():
        st.write(f"{info.programming_icons.get(skill, '')} {skill}")
        st.progress(score)
with skill_col_2:
    st.markdown("**Languages**")
    for spoken, level in info.spoken_data.items():
        st.write(f"{info.spoken_icons.get(spoken, '')} {spoken}: {level}")

