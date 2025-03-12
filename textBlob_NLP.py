# import textblob
from textblob import *

def tashkhise_ehsasat(text):
    pardazesh_ehsas = TextBlob(text)
    tabdil = pardazesh_ehsas.sentiment.polarity   

    if tabdil > 0:
        print(f"😊 mosbat | {tabdil}")
    
    elif tabdil < 0:
        print(f"😡 manfi | {tabdil}")

    else:
        print(f"😐 khonsa | {tabdil}")

ssentence = input("Enter ur text: ")
tashkhise_ehsasat(ssentence)