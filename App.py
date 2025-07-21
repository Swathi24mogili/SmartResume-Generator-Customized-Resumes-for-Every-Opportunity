import streamlit as st
from resume_generator import generate_resume

st.set_page_config(page_title="SmartResume Generator", layout="centered")
st.title("📄 SmartResume Generator")

st.markdown("Customize your resume based on job descriptions using AI!")

jd_input = st.text_area("Paste the Job Description:", height=250)

skills = st.text_input("Your Skills (comma separated):")
experience = st.text_area("Your Experience Summary:")
education = st.text_area("Your Education Details:")
name = st.text_input("Your Name:")
email = st.text_input("Your Email:")

if st.button("Generate Resume"):
    if jd_input and skills and experience and education and name and email:
        resume = generate_resume(jd_input, skills, experience, education, name, email)
        st.download_button("📥 Download Resume", resume, file_name="SmartResume.txt")
        st.text_area("Generated Resume", resume, height=500)
    else:
        st.warning("Please fill in all fields to generate your resume.")
