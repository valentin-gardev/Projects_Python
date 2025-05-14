from docx import Document
import random


def extract_category_items(file_path, category):
    document = Document(file_path)
    items = []
    collecting = False
    for para in document.paragraphs:
        is_bold = any(run.bold for run in para.runs if run.text.strip())
        text = para.text.strip()
        if is_bold:
            if text.lower().startswith(category.lower()):
                collecting = True

                if ':' in text:
                    content = text.split(':', 1)[1]
                    list_of_sentences = content.split('; ')
                    items.extend([sentence.strip() for sentence in list_of_sentences if sentence.strip()])

            elif collecting:
                break

        elif collecting:
            items.extend([sentence.strip() for sentence in text.split('; ') if sentence.strip()])

    random_encouragement = random.choice(items)

    return random_encouragement





