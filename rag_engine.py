from PyPDF2 import PdfReader
import random

def extract_text_from_pdf(file):
    pdf = PdfReader(file)
    text = ""
    for page in pdf.pages:
        text += page.extract_text()
    return text

def get_learning_card(file, topic):
    content = extract_text_from_pdf(file)
    # Dummy simulation of retrieval
    return f"**Topic:** {topic}\n\nKey Concepts:\n- {topic} basics\n- Practice this daily\n- Example: {random.choice(content.split('.')[:5])}"
