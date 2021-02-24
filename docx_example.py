import docx

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs: #for every paragraph, take its text and add it to the list
        fullText.append(para.text)
    return '\n'.join(fullText)

print(getText('demo.docx'))


