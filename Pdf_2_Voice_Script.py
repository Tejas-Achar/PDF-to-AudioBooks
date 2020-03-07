#Importing Libraries
#Importing Google Text to Speech library
from gtts import gTTS

#Importing PDF reader PyPDF2
import PyPDF2

#Open file Path
pdf_File = open('Path To The PDF file', 'rb') 

#Create PDF Reader Object
pdf_Reader = PyPDF2.PdfFileReader(pdf_File)
count = pdf_Reader.numPages # counts number of pages in pdf
TextList = []

#Extracting text data from each page of the pdf file
for i in range(count):
   try:
    page = pdf_Reader.getPage(i)
    print(page.extractText())
    TextList.append(page.extractText())
   except:
       pass

#Converting multiline text to single line text
TextString = " ".join(TextList)

#Set language to english (en)
language = 'en'

#Call GTTS
myobj = gTTS(text=TextString, lang=language, slow=False)

#Save as mp3 file
myobj.save("AudioBook.mp3")



