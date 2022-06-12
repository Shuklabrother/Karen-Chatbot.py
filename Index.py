import datetime
import pyfiglet
import pyjokes

joke= pyjokes.get_joke()
word = pyfiglet.figlet_format("Karen")
Bot = "Bot: "
year= datetime.datetime.now().year
month= datetime.datetime.now().month
date= datetime.datetime.now().day
hour= datetime.datetime.now().hour
minute= datetime.datetime.now().minute
second= datetime.datetime.now().second

print(word)
while True:
    write =  input("You: ")
    if write =="hello":
              print(Bot, "Hi Sir")
    elif write=="what is time now":
              print(Bot, hour, ":", minute, ":", second)
    elif write=="what is your name":
              print(Bot, "My name is KAREN")
    elif write=="what is today date":
             print(Bot, date, "/", month, "/", year)
    elif write=="tell me a joke":
             print(Bot, joke, "Ha-Ha-Ha...")
    elif write=="who is your creator":
             print(Bot, "Ayush Shukla")
    elif write=="how are you":
             print(Bot, "I am fine")
    elif write=="say Jai shree ram":
             print (Bot, "Jai shree Ram")
    elif write=="Piyush":
             print(Bot, "My second creator")
    elif write=="Ayush":
             print(Bot, "My creator")     
    else:
             print(Bot, "I am Not understand?")