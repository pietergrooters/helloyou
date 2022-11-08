#from __future__ import annotations
import time


answera = ("A, a")
answerb = ("B, b")
answerc = ("C, c")
answerd = ("D, d")


gebruik = ("kies alleen A, B, C of D")


def begin():
    print("Der is oorlog uit gebroken in bosnie tussen de bosniers en de serven je wilt iets doen, wat ga je doen?")
    print("A, je doet niks")
    print("B, je vecht")
    print("C, je vlucht")
    time.sleep(1)
    keuze = input("..")
    if keuze in answera:
        option_niks()
    elif keuze in answerb:
        option_vechten()
    elif keuze in answerc:
        option_vluchten()
    else:
        print(gebruik)
        begin()


def option_niks():
    print("je ziet dat de mensen om je heen tegen de serven vechten je wilt iets doen wat doe je?")
    print("A, je vecht mee")
    print("B, je gaat vluchten")
    time.sleep(1)
    keuze = input("..")
    if keuze in answera:
        print("je gaat mee vechten tegen de serven je groep word in een val gelokt en jullie worden allemaal dood geschoten")
        quit()
    elif keuze in answerb:
        option_vluchten()
    else:
        print(gebruik)
        option_niks()


def option_vechten():
    print("je hebt besloten om mee te vechten jij en je groep komen een veel grotere groep serven tegen wat doe je?")
    print("A, je geeft je over")
    print("B, je vlucht")
    time.sleep(1)
    keuze = input("..")
    if keuze in answera:
        print("je geeft je zelf over aan de groep serven je bent mee genomen voor een paar dagen gemarteld en uitgehongerd naar een paar dagen wordt jij met een hoop andere neer geschoten")
        quit()
    elif keuze in answerb:
        option_vluchten()
    else:
        print(gebruik)
        option_vechten


def option_mening():
    print("door dat je wilt vluchten wordt je nu gezocht door de serven ze willen je dood hebben wat ga je doen?")
    print("A, je gaat vluchten.")
    print("B, je geeft je over.")
    time.sleep(1)
    keuze = input("..")
    if keuze in answera:
        print("")
        option_vluchten()
    if keuze in answerb:
        print(" je bent door de serven dood geschoten")
        quit()
    else:
        print(gebruik)
        option_mening()


def option_vluchten():
    print("je hebt gekozen om te vluchten je hebt een aantal opties hoe je vlucht.")
    print("A, je gaat met de boot naar italie.")
    print("B, je gaat met de auto naar kroatie.")
    print("C, je gaat met de auto naar oostenrijk.")
    time.sleep(1)
    keuze = input("..")
    if keuze in answera:
        option_paspoortitalie()
    elif keuze in answerb:
        option_paspoortkroatie()
    elif keuze in answerc:
        option_paspoortoostenrijk()
    else:
        print(gebruik)
        option_vluchten


def option_paspoortitalie():
    print("Om met de boot naar Italie te kunnen heb je je paspoort nodig. Heb je die meegenomen?")
    print("A, nee")
    print("B, ja")
    time.sleep(1)
    keuze = input("..")
    if keuze in answera:
        print("Je hebt je paspoort niet mee dus kan je de boot niet meenemen de boot is al vertrokken jij wordt gepakt door de serven die nemen je mee en je gaat naar een paar dagen dood.")
        quit()
    elif keuze in answerb:
        option_paspoortmeeitalie()
    else:
        print(gebruik)
        option_paspoortitalie()


def option_paspoortmeeitalie():
    print("je hebt je paspoort meegenomen je bent nu veilig aangekomen in Italie. Je gaat met de vliegtuig naar nederland.")
    time.sleep(1)
    print("Je bent in Nederland aangekomen bij de douane wordt je tegen gehouden omdat je verdacht lijkt je wordt mee genomen en uiteindelijk haalt de poitie je op na onderzoek wordt je beschuldigt van illegaal het land in komen hier door moet je 5 jaar de gevangenis in.")
    time.sleep(5)
    print("Je bent na 5 jaar uit de gevanenis gekomen je hebt de kans gekregen op een verblijf vergunning maar daarvoor ga je eerst een vraag moeten beantwoorden.")
    time.sleep(1)
    print("De vraag die je beantwoorden moet is. Wat is de hoofdstad van Nederland?")
    print("A, Amsterdam.")
    print("B, Denhaag.")
    print("C, Rotterdam.")
    time.sleep(1)
    keuze = input("..")
    if keuze in answera:
        print("Goed beantwoord je krijgt nu een verblijfsvergunning.")

    elif keuze in answerb:
        print("Helaas heb je het fout je krijgt nu geen verblijfs vergunning maar je kan wel een basis kenis imigranten toets doen zo kan je ook een verblijfvergunning krijgen.")
        quit()    
    elif keuze in answerc:
        print("Helaas heb je het fout je krijgt nu geen verblijfs vergunning maar je kan wel een basis kenis imigranten toets doen zo kan je ook een verblijfvergunning krijgen.")
        quit()
    else:
        print(gebruik)
        time.sleep(1)
       
    print("Je hebt je verblijfs vergunning gekregen. NU moet je een baan zoeken voor je toekomst in Nederland wat kies je?")
    print("A, Docent.")
    print("B, Militair.")
    print("C, Architect. ")
    print("D, ingenieur.")
    time.sleep(1)
    keuze = input("..")
    if keuze in answera:
        print("Gefeliciteerd je bent docent geworden.")
        time.sleep(1)
        print("Je gaat wonen in een huisje en leeft lang en gelukkig.")
        quit()
    elif keuze in answerb:
        print("Gefeliciteerd je bent aangesloten bij het leger en bent een militair geowrden.")
        time.sleep(1)
        print("Je wordt uitgezonde naar het buiteand daar krijg je een mislukte inval als missie jij en je team omen te overlijden.")
        quit()
    elif keuze in answerc:
        print("Gefeliciteerd je bent een architect geworden.")
        time.sleep(1)
        print("Je gaat wonen in een hele mooie huis en je leeft nog lang en gelukkig.")
        quit()
    elif keuze in answerd:
        print("Gefeliciteerd je bent een ingenieur geworden.")
        time.sleep(1)
        print("Je gaat wonen in een hele mooie huis en je leeft nog lang en gelukkig.")
        quit()
    else:
            print(gebruik)
            option_paspoortmeeitalie


def option_paspoortkroatie():
    print("Om met de auto naar Kroatie te kunnen heb je je paspoort nodig. Heb je die meegenomen?")
    print("A, nee")
    print("B, ja")
    time.sleep(1)
    keuze = input("..")
    if keuze in answera:
        print("Je hebt je paspoort niet mee in kroatie wordt je onderzocht en omdat je je paspoort niet bij je hebt wordt je terug gestuurd naar bosnie hier ga je dood.")
        quit()
    elif keuze in answerb:
        option_paspoortmeekroatie()
    else:
        print(gebruik)
        option_paspoortkroatie()


def option_paspoortmeekroatie():
     print("je hebt je paspoort meegenomen je bent nu veilig aangekomen in Kroatie. Je gaat met de vliegtuig naar nederland.")
     time.sleep(1)
     print("Je bent in Nederland aangekomen bij de douane wordt je tegen gehouden omdat je verdacht lijkt je wordt mee genomen en uiteindelijk haalt de poitie je op na onderzoek wordt je beschuldigt van illegaal het land in komen hier door moet je 5 jaar de gevangenis in.")
     time.sleep(5)
     print("Je bent na 5 jaar uit de gevanenis gekomen je ebt de kans gekregen op een verblijf vergunning maar daarvoor ga je eerst een vraag moeten beantwoorden.")
     time.sleep(1)
     print("De vraag die je beantwoorden moet is. Wat is de hoofdstad van Nederland?")
     print("A, Amsterdam.")
     print("B, Denhaag.")
     print("C, Rotterdam.")
     time.sleep(1)
     keuze = input("..")
     if keuze in answera:
        print("Goed beantwoord je krijgt nu een verblijfsvergunning.")
     elif keuze in answerb:
         print("Helaas heb je het fout je krijgt nu geen verblijfs vergunning maar je kan wel een basis kenis imigranten toets doen zo kan je ook een verblijfvergunning krijgen.")
         quit()    
     elif keuze in answerc:
         print("Helaas heb je het fout je krijgt nu geen verblijfs vergunning maar je kan wel een basis kenis imigranten toets doen zo kan je ook een verblijfvergunning krijgen.")
         quit()
     else:
         print(gebruik)
         time.sleep(1)

     print("Je hebt je verblijfs vergunning gekregen. NU moet je een baan zoeken voor je toekomst in Nederland wat kies je?")
     print("A, Docent.")
     print("B, Militair.")
     print("C, Architect. ")
     print("D, ingenieur.")
     time.sleep(1)
     keuze = input("..")
     if keuze in answera:
        print("Gefeliciteerd je bent docent geworden.")
        time.sleep(1)
        print("Je gaat wonen in een huisje en leeft lang en gelukkig.")
        quit()
     elif keuze in answerb:
        print("Gefeliciteerd je bent aangesloten bij het leger en bent een militair geowrden.")
        time.sleep(1)
        print("Je wordt uitgezonde naar het buiteand daar krijg je een mislukte inval als missie jij en je team omen te overlijden.")
        quit()
     elif keuze in answerc:
         print("Gefeliciteerd je bent een architect geworden.")
         time.sleep(1)
         print("Je gaat wonen in een hele mooie huis en je leeft nog lang en gelukkig.")
         quit()
     elif keuze in answerd:
        print("Gefeliciteerd je bent een ingenieur geworden.")
        time.sleep(1)
        print("Je gaat wonen in een hele mooie huis en je leeft nog lang en gelukkig.")
        quit()
     else:
        print(gebruik)
        option_paspoortmeekroatie()


def option_paspoortoostenrijk():
    print("Om met de auto naar Oostenrijk te kunnen heb je je paspoort nodig. Heb je die meegenomen?")
    print("A, nee")
    print("B, ja")
    time.sleep(1)
    keuze = input("..")
    if keuze in answera:
        print("Je hebt je paspoort niet mee in Oostenrijk wordt je onderzocht en omdat je je paspoort niet bij je hebt wordt je terug gestuurd naar bosnie hier ga je dood.")
        quit()
    elif keuze in answerb:
        option_paspoortmeeoostenrijk()
    else:
        print(gebruik)
        option_paspoortoostenrijk()


def option_paspoortmeeoostenrijk():
     print("je hebt je paspoort meegenomen je bent nu veilig aangekomen in Oostenrijk. Je gaat met de vliegtuig naar nederland.")
     time.sleep(1)
     print("Je bent in Nederland aangekomen bij de douane wordt je tegen gehouden omdat je verdacht lijkt je wordt mee genomen en uiteindelijk haalt de poitie je op na onderzoek wordt je beschuldigt van illegaal het land in komen hier door moet je 5 jaar de gevangenis in.")
     time.sleep(5)
     print("Je bent na 5 jaar uit de gevanenis gekomen je ebt de kans gekregen op een verblijf vergunning maar daarvoor ga je eerst een vraag moeten beantwoorden.")
     time.sleep(1)
     print("De vraag die je beantwoorden moet is. Wat is de hoofdstad van Nederland?")
     print("A, Amsterdam.")
     print("B, Denhaag.")
     print("C, Rotterdam.")
     time.sleep(1)
     keuze = input("..")
     if keuze in answera:
        print("Goed beantwoord je krijgt nu een verblijfsvergunning.")
     elif keuze in answerb:
         print("Helaas heb je het fout je krijgt nu geen verblijfs vergunning maar je kan wel een basis kenis imigranten toets doen zo kan je ook een verblijfvergunning krijgen.")
         quit()    
     elif keuze in answerc:
         print("Helaas heb je het fout je krijgt nu geen verblijfs vergunning maar je kan wel een basis kenis imigranten toets doen zo kan je ook een verblijfvergunning krijgen.")
         quit()
     else:
         print(gebruik)
         time.sleep(1)

     print("Je hebt je verblijfs vergunning gekregen. NU moet je een baan zoeken voor je toekomst in Nederland wat kies je?")
     print("A, Docent.")
     print("B, Militair.")
     print("C, Architect. ")
     print("D, ingenieur.")
     time.sleep(1)
     keuze = input("..")
     if keuze in answera:
        print("Gefeliciteerd je bent docent geworden.")
        time.sleep(1)
        print("Je gaat wonen in een huisje en leeft lang en gelukkig.")
        quit()
     elif keuze in answerb:
        print("Gefeliciteerd je bent aangesloten bij het leger en bent een militair geowrden.")
        time.sleep(1)
        print("Je wordt uitgezonde naar het buiteand daar krijg je een mislukte inval als missie jij en je team omen te overlijden.")
        quit()
     elif keuze in answerc:
         print("Gefeliciteerd je bent een architect geworden.")
         time.sleep(1)
         print("Je gaat wonen in een hele mooie huis en je leeft nog lang en gelukkig.")
         quit()
     elif keuze in answerd:
          print("Gefeliciteerd je bent een ingenieur geworden.")
          time.sleep(1)
          print("Je gaat wonen in een hele mooie huis en je leeft nog lang en gelukkig.")
          quit()
     else:
         print(gebruik)
         option_paspoortmeeoostenrijk()



begin()