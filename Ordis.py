from plyer import notification                              # ➥da installare su cmd con pip install -U plyer
from pyttsx3 import init                                    # ➥da installare su cmd con pip install -U pyttsx3
from speech_recognition import Recognizer, Microphone       # ➥da installare su cmd con pip install -U recognizer
from datetime import datetime                               # ♠per segnare il tempo
from random import *                                        # ♠per scelte randomiche
from tkinter import *                                       # ♠per calcolatrice
import mss                                                  # ➥da installare su cmd con pip install -U mss
import mss.tools                                            # ➥|
import webbrowser                                           # ♠per funzioni web
import os                                                   # ♠per funzioni sul computer
import time                                                 # ♠per segnare il tempo
import pyautogui                                            # ♠fa in automatico

#----------- Funzione ----------------
def contatore():
    contatore = random(0,100)
    return contatore

#----------- Variabili ---------------
flag1 = True                                                # ☘variabile per il ciclo del programma
flag2 = True                                                # ☘variabile per far cambiare frase
flag3 = True                                                # ☘variabile per il ciclo del promemoria
#
root = Tk()                                                 # ☘invocazione del metodo
monitor_height = root.winfo_screenheight()                  # ☘variabile che prende altezza ripresa dal pc
monitor_width = root.winfo_screenwidth()                    # ☘variabile che prendelunghezza ripresa dal pc
#root.configure(background="dark")                           # ☘colore di sfondo
#root.title("Ordis")                                         # ☘nome visualizzabile mentre l'app è in esecuzione
#root.geometry("270x150")                                    # ☘risoluzione dello schermo
#root.mainloop()                                             # ☘per avviare lo schermo
#
#x,y = pyautogui.locateAll('testo.png')                      # ☘per prendere tutti gli oggetti su desktop
#pyautogui.moveTo(x,y,0.5)                                   # ☘per inserire il file a quelle coordinate
#pyautogui.mouseDown()                                       # ☘per tenere
#pyautogui.mouseUp()                                         # ☘per rilasciare
#pyautogui.leftClick()                                       # ☘per cliccare con tasto sinistro
#pyautogui.rightClick()                                      # ☘per cliccare con tasto destro

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
        #------------ avvisi di promemoria ------------------------
        if any(parola in testo for parola in ["attiva promemoria", "attiva", "ricerca", "ricercami", "trova", "trovami"]):
            while flag3:
                notification.notify(
                    title = "Attenzione!!!",
                    message = "Prenditi una pausa! Sei online da un'ora!",
                    timeout = 10
                )
            time.sleep(3600)
        elif any(parola in testo for parola in ["spegni notifiche", "chiudi notifiche", "spegni avvisi", "chiudi avvisi", "spegni avviso", "chiudi avviso"]):
            flag3 = False

        #------------ cerca online ---------------------------
        elif any(parola in testo for parola in ["cerca", "cercami", "ricerca", "ricercami", "trova", "trovami", "cerca su google", "cercami su google", "ricerca su google", "ricercami su google", "trova su google", "trovamisu google"]):
            risposta = "sto cercando " + testo
            webbrowser.open("https://www.google.it/search?q=" + testo)
            risposta = "questo è quello che ho trovato"

        #------------ apre youtube ---------------------------
        elif any(parola in testo for parola in ["apri youtube", "aprimi youtube"]):
            webbrowser.open("https://www.youtube.com/")
            risposta = "apertura youtube in corso..."

        #------------ apre gmail -----------------------------
        elif any(parola in testo for parola in ["apri gmail", "aprimi gmail", "apri email", "aprimi email", "apri gimeil", "aprimi gimeil", "apri imeil", "aprimi imeil"]):
            webbrowser.open("https://mail.google.com/")
            risposta = "apertura gmail in corso..."

        #------------ apre spotify ---------------------------
#        elif "apri spotify" in testo:
#            os.popen("/Applications/Spotify.app")
#            risposta = "apertura di Spotify in corso..."
        
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

        #------------ dice l'ora -----------------------------
        elif any(parola in testo for parola in ["ore", "ora", "orario"]):
            risposta = f"sono le ore {datetime.now().strftime('%H e %M')}"
        
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