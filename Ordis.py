#from plyer import notification                              # ➥da installare su cmd con pip install -U plyer
from pyttsx3 import init                                    # ➥da installare su cmd con pip install -U pyttsx3
from speech_recognition import Recognizer, Microphone       # ➥da installare su cmd con pip install -U recognizer
from datetime import datetime                               # ♠per segnare il tempo
from random import *                                        # ♠per scelte randomiche
from tkinter import *                                       # ♠per calcolatrice
from tqdm import tqdm                                       # ➥da installare su cmd con pip install -U mss | fa animazioni
import mss                                                  # ➥da installare su cmd con pip install -U mss
import mss.tools                                            # ➥|
import webbrowser                                           # ♠per funzioni web
import platform                                             # ♠per funzioni di piattaforma
import time                                                 # ♠per segnare il tempo
import subprocess                                           # ♠per funzioni di sottoprocessi
import pyperclip                                            # ♠per copiare ed incollare

#----------- Funzione ----------------
#estrattore da 0 a 100
def contatore():
    contatore = random(0,100)
    return contatore

def loading():
    # definire la lunghezza della barra di caricamento
    progress_bar = tqdm(total=100)

    # ciclo per simulare il caricamento
    for i in range(100):
        time.sleep(0.1) # attendere per simulare il tempo di caricamento
        progress_bar.update(1) # aggiornare la barra di progresso

    progress_bar.close() # chiudere la barra di progresso
    print("Caricamento completato!")
#----------- Variabili ---------------
flag1 = True                                                # ☘variabile per il ciclo del programma
flag2 = True                                               # ☘variabile per far cambiare frase
#
root = Tk()                                                 # ☘invocazione del metodo
monitor_height = root.winfo_screenheight()                  # ☘variabile che prende altezza ripresa dal pc
monitor_width = root.winfo_screenwidth()                    # ☘variabile che prendelunghezza ripresa dal pc
#----------- Ciclo -------------------
while flag1:

    #----------- Parla ---------------
    engine = init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    if flag2 == True:
        engine.say("Ciao sono Ordis! Cosa desìderi?")
        flag2 = False
    else:
        engine.say("cos'altro desìderi?")
    engine.runAndWait()
    r = Recognizer()

    #----------- Capisce --------------
    with Microphone() as source:
        print("in ascolto...")
        audio = r.listen(source)
        testo = r.recognize_google(audio, language = "it-IT").lower()

    #----------- quando riconosce queste parole fa ----------------
        #------------ cerca online ---------------------------
        if any(parola in testo for parola in ["cerca","cercami","ricerca","ricercami","trova","trovami","cerca su google", "cercami su google", "ricerca su google", "ricercami su google", "trova su google", "trovami su google"]):
            risposta = "sto cercando " + testo
            webbrowser.open("https://www.google.it/search?q=" + testo)
            risposta = "questo è quello che ho trovato"

        #------------ apre youtube ---------------------------
        elif any(parola in testo for parola in ["apri youtube e cerca", "aprimi youtube e cerca", "cerca su youtube","cercami su youtube"]):    
            risposta = "sto cercando " + testo
            webbrowser.open("https://www.youtube.com/"+ testo)
            risposta = "apertura youtube in corso..."

        #------------ apre gmail -----------------------------
        elif any(parola in testo for parola in ["apri gmail", "aprimi gmail", "apri email", "aprimi email", "apri gimeil", "aprimi gimeil", "apri imeil", "aprimi imeil"]):
            webbrowser.open("https://mail.google.com/")
            risposta = "apertura gmail in corso..."

        #------------ apre spotify ---------------------------
        elif "apri spotify" in testo:
            subprocess.run(["spotify"])
            risposta = "apertura di Spotify in corso..."
        
        #------------ apre le password -----------------------
        elif any(parola in testo for parola in ["ore", "ora", "orario"]):
            psw = {
                'Facebook': 'password',
                'Instagram': 'password',
                'Tik Tok': 'password',
                'Youtube': 'password',
                'GMAIL': 'password',
            }
            risposta = ("Quale password ti interessa?")
            for sito in psw:
                print(" -"+sito)
        # Facebook
        elif "Facebook" in testo:
            try:
                password_scelta = psw[testo]
                pyperclip.copy(password_scelta)
                risposta = ("password ottenuta! sei pronto ad incollarla")
            except:
                risposta = ("ricomincia perchè non ho capito!")
        # Instagram
        elif "Instagram" in testo:
            try:
                password_scelta = psw[testo]
                pyperclip.copy(password_scelta)
                risposta = ("password ottenuta! sei pronto ad incollarla")
            except:
                risposta = ("ricomincia perchè non ho capito!")
        # Tik Tok
        elif "Tik Tok" in testo:
            try:
                password_scelta = psw[testo]
                pyperclip.copy(password_scelta)
                risposta = ("password ottenuta! sei pronto ad incollarla")
            except:
                risposta = ("ricomincia perchè non ho capito!")
        # Youtube
        elif "Youtube" in testo:
            try:
                password_scelta = psw[testo]
                pyperclip.copy(password_scelta)
                risposta = ("password ottenuta! sei pronto ad incollarla")
            except:
                risposta = ("ricomincia perchè non ho capito!")
        # GMAIL
        elif "GMAIL" in testo:
            try:
                password_scelta = psw[testo]
                pyperclip.copy(password_scelta)
                risposta = ("password ottenuta! sei pronto ad incollarla")
            except:
                risposta = ("ricomincia perchè non ho capito!")


        #------------ screenshot -----------------------------
        elif any(parola in testo for parola in ["fai uno screen", "fammi uno screen", "fai uno screenshot", "fammi uno screenshot", "screenshotta", "screenshotta lo schermo", "salva lo schermo"]):
            with mss.mss() as sct:
                #la parte di screen catturata 
                monitor = {"top": 0, "left": 0, "width": monitor_width, "height": monitor_height}
                output = "screenshot(" + contatore + ").png".format(**monitor)
                sct_img = sct.grab(monitor)
                # Salvataggio
                mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
                print(output)
            risposta = "screen eseguito con successo"

        #------------- dice l'ora ------------------------------
        elif any(parola in testo for parola in ["ore", "ora", "orario"]):
            risposta = f"sono le ore {datetime.now().strftime('%H e %M')}"

        #------------ caratteristiche del dispositivo ----------
        elif any(parola in testo for parola in ["dimmi le caratteristiche del mio dispositivo", "dimmi le info del mio dispositivo", "dimmi le informazioni del mio dispositivo"]):
            risposta = "Il Sistema attualmente in uso è: " + platform.system() + platform.release()

        #------------ fa una battuta --------------------------
        elif any(parola in testo for parola in["fammi una battuta", "dimmi una battuta"]):
            risposta = choice(["scusi, per andare all ospedale? alla prima curva, dritto!", "hanno rubato un tir pieno di lampadine. la polizia brancola nel buio.", "il deserto del sahara è in africa. su questo non ci piove.", "Bomba esplode al cimitero. Tutti morti.", "Ogni mattina mi alzo e dico 20 volte ciao. Dicono che sia salutare.", "Che vitaccia, ci vorrebbe un cacciavite più grosso.", "Chiude una fabbrica di carta igienica: andava a rotoli.", "Non è bello ciò che è bello. Figuriamoci ciò che è brutto.", "Una mela al giorno leva il medico di torno. Una cipolla al giorno leva tutti di torno.", "Arrestato er Caccola: si pensa ad una soffiata!", "Arrestato er Caccola: si pensa ad una soffiata!"])

        #------------ imprecazioni ----------------------------
        elif any(parola in testo for parola in["cazzo", "pirla", "mignotta", "cornuta", "terrone", "vucumprà", "baldracca", "vaffanculo", "stronza", "stronzo", "dio", "madonna", "gesù", "cristo", "coglione", "troia", "puttana", "zoccola", "sta merda", "figa", "fica", "buttana", "rincoglionita", "ritardata"]):
            risposta = "cavolo tieni proprio ragione"

#----------- conclusione ciclo ----------------------
        elif any(parola in testo for parola in["chiuditi", "spegniti","chiudi programma",  "chiuditi ordis", "spegniti ordis", "spegni ordis", "chiudi ordis", "chiudi assistente"]):
            risposta = "spegnimento in corso..."
            flag1 = False

        #----------- parla ----------------------------------
        engine.say(risposta)
        engine.runAndWait()
        loading()
