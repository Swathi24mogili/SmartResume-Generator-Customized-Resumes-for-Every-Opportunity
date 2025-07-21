from utils import extract_keywords, match_keywords

def generate_resume(jd, skills, experience, education, name, email):
    jd_keywords = extract_keywords(jd)
    matched_skills = match_keywords(skills, jd_keywords)

    resume_template = f"""
    Name: {name}
    Email: {email}

    Professional Summary:
    {experience}

    Key Skills:
    {matched_skills}

    Education:
    {education}

    Matched Keywords from Job Description:
    {", ".join(jd_keywords)}

    Resume tailored using SmartResume AI Generator.
    """
    return resume_template
