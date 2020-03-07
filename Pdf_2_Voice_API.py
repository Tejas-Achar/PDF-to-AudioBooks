#Importing Libraries
#Importing Flask library
from flask import send_file, send_from_directory, safe_join, abort
import flask
from flask import send_file

#Importing Google Text to Speech library
from gtts import gTTS

#Importing PDF reader PyPDF2
import PyPDF2

#Initializing
app = flask.Flask(__name__)
app.config["DEBUG"] = True
@app.route('/')

#Main method which takes the path of the pdf file as a parameter
def convFile(FilePath):

 #Open file Path
 pdf_File = open(FilePath, 'rb')
 
 #Create PDF Reader Object
 pdf_Reader = PyPDF2.PdfFileReader(pdf_File)
 
 count = pdf_Reader.numPages# counts number of pages in pdf
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

 myobj.save("welcome.mp3")
 filename = "welcome.mp3"
 
 #Return the mp3 file
 return send_file(
     filename,
     mimetype="audio/mp3",
     as_attachment=True,
     attachment_filename="test.mp3")
app.run()
