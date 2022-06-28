#importing required modules
import PyPDF2
import os

#for loop to walk through each PDF in the specified location
for foldername, subfolder, files in os.walk(r"D:\PDF_Extract\PDF Files"):
    for file in files:
 
# open the pdf file
        pdfFileObj = PyPDF2.PdfFileReader(os.path.join(foldername,file))
 
# creating a page object
        pageObj = pdfFileObj.getPage(0)

#parsing out the text from the page object
        text=(pageObj.extractText())
        text=text.split(",")
        text
 
# creating a list of keywords to search for in the pdf file
        search_keywords=['Memo', 'Memorandum']

# to search for the keywords in the extracted text and then locate sentences with keywords
        for sentence in text:
            lst = []
            for word in search_keywords:
                if word in sentence: 
                    lst.append(word)
            print('{0} key word(s) in sentence: {1}'.format(len(lst), ', '.join(lst)))
            print(sentence + "\n")

