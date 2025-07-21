import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_keywords(text):
    words = re.findall(r'\b\w+\b', text.lower())
    common_keywords = [word for word in words if len(word) > 3]
    return list(set(common_keywords))

def match_keywords(user_skills, jd_keywords):
    user_keywords = [s.strip().lower() for s in user_skills.split(',')]
    matched = [skill for skill in user_keywords if skill in jd_keywords]
    return ', '.join(matched)
