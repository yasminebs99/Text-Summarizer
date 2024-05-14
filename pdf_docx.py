#import openai
import PyPDF2
from docx import Document
from transformers import pipeline
def read_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ''
        for page_num in range(reader.numPages):
            text += reader.getPage(page_num).extractText()
        return text
def read_text_from_docx(docx_path):
    doc = Document(docx_path)
    text = ''
    for paragraph in doc.paragraphs:
        text += paragraph.text + '\n'
    return text
def read_text_from_text_file(txt_path):
    with open(txt_path, 'r') as file:
        return file.read()
def read_file(file_path):
    # Read text from the input file
    if file_path.endswith('.pdf'):
        input_text = read_text_from_pdf(file_path)
    elif file_path.endswith('.docx'):
        input_text = read_text_from_docx(file_path)
    elif file_path.endswith('.txt'):
        input_text = read_text_from_text_file(file_path)
    else:
        raise ValueError("Unsupported file format. Please provide a PDF, DOCX, or TXT file.")
    return input_text
def Summuraize(file_path):
    # Set your API key
    #openai.api_key = '.'
    #response = openai.completions.create(
     #   model="gpt-3.5-turbo-instruct",  # Use the Davinci Codex model for text summarization
      #  prompt=read_file(file_path),
       # max_tokens=150,  # Adjust the max number of tokens for the summary
    #    temperature=0.5,  # Adjust the randomness of the output
     #   top_p=1.0,
      #  frequency_penalty=0.0,
       # presence_penalty=0.0
    #)
    # Get the summary from the API response
    #summary = response.choices[0].text.strip()
    #return summary



    summarization_pipeline = pipeline("summarization")
    summary = summarization_pipeline(read_file(file_path), max_length=150, min_length=30, do_sample=False)
    return summary[0]['summary_text']
