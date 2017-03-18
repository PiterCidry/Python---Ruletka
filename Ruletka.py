import random 
import time
import linecache
import datetime

def ruletka():
       czerwone = (1,3,5,7,9,12,14,16,18,21,23,25,27,30,32,34,36) #listy numerów przyporządkowanych odpowiednim grupom
       czarne = (2,4,6,8,10,11,13,15,17,19,20,22,24,26,28,29,31,33,35)
       zielone = (0,)
       wysokie = (19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36)
       niskie = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18)
       atuzin = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
       btuzin = (13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24)
       ctuzin = (25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36)
       op = 't' #zmienna sterująca pętlą

       print("R")
       time.sleep(0.1)
       print("U")
       time.sleep(0.1)
       print("L")
       time.sleep(0.1)
       print("E")
       time.sleep(0.1)
       print("T")
       time.sleep(0.1)
       print("K")
       time.sleep(0.1)
       print("A")
       time.sleep(0.1)
       print(" ")
       time.sleep(0.1)
       print("W")
       time.sleep(0.1)
       print(" ")
       time.sleep(0.1)
       print("P")
       time.sleep(0.1)
       print("Y")
       time.sleep(0.1)
       print("T")
       time.sleep(0.1)
       print("H")
       time.sleep(0.1)
       print("O")
       time.sleep(0.1)
       print("N")
       time.sleep(0.1)
       print("I")
       time.sleep(0.1)
       print("E\n\n")
       time.sleep(1)
       print("Projekt zaliczeniowy stworzony przez: Piotr Gretszel, Marcin Buda, Rafal Kedzior\n\n")
       time.sleep(2)
        
       while op == "t": #główna pętla, działa dopóki użytkownik będzie chciał grać
           print("+=+=+=+=+=+=+=+=+=+=+=+")
           print("Ostatni zapisany wynik: "+linecache.getline("wyniki.txt", 2)) #wypisywanie ostatniego wyniku
           print("Zdobyty: "+linecache.getline("wyniki.txt", 4)) #wypisywanie daty zdobycia ostatniego wyniku
           print("Przez: "+linecache.getline("wyniki.txt", 6)) #wypisywaniie nicku
           print("+=+=+=+=+=+=+=+=+=+=+=+")
           print("\n")
           op2 = input("Czy chcesz wczytac ostatni wynik? (t/n)") #zmienna sterujaca wczytywaniem
           print("\n")
           kredyty = 50
           while op2 == "t": #pętla do wczytywania wyniku z pliku
               try:  
                   kasa = linecache.getline("wyniki.txt", 2) #pobranie ilości zapisanych kredytów
                   kredyty = int(kasa)
                   print("Wczytano ostatni wynik")
                   print("\n")
                   time.sleep(1)
                   nick = linecache.getline("wyniki.txt", 6) #pobranie nicku
                   break
               except: #jeżeli plik nie istnieje albo wystepuja inne problemy
                   print("Nie mozna wczytac ostatniego wyniku z pliku\n")
                   time.sleep(0.5)                    
                   kredyty = 50
                   break

           while kredyty > 0: #główna pętla
                    if op2 != "t":
                        print("-----------------------")
                        nick = input("Podaj swoj nick: ")
                        print("-----------------------")
                        op2 = "t"
                    else:
                        print("\n")
                        print ("-=-=-=-=-=-=-=-=-=-=-=-")
                        print ("Obcenie masz ", kredyty, "kredytow")
                        print ("Wybierz z poniższych, co obstawiasz:")
                        print ("1.Liczbe")
                        print ("2.Grupe")
                        print ("3.Wysokie/Niskie")
                        print ("4.Tuziny")
                        wybor= int(input("Wybieram: ",)) #wybór tego co chcemy obstawiać
                        print ("-=-=-=-=-=-=-=-=-=-=-=-\n")
                        wylosowana = random.randint(0, 36) #program już wie co będzie porównywał z naszą deklaracją

                        if wybor == 1: #w tych miejscach rozpoczynamy działanie podpętli do różnych możliwości obstawiania
                            print("Podaj swoja stawke: ")
                            stawka= int(input("Moja stawka to: ")) #wpisujemy co obstawiamy
                            if stawka < 1 or stawka > kredyty: #zabezpieczenie przed obstawianiem ujemnych wartości i pieniędzy "na dług"
                                print("Obstaw co najmniej jeden kredyt i nie wiecej niz ich posiadasz!")
                                print("+++++++++++++++++++++\n\n")
                                time.sleep(1.5) #sztucznie opóźnia wykonanie części programu aby budować napięcie
                            else: #jeżeli stawka jest prawidłowa
                                kredyty -= stawka #odejmujemy od naszej podstawowej kwoty tyle ile zadeklarowaliśmy
                                print("+++++++++++++++++++++\n")
                                print("Podaj swoja liczbe (0-36):")
                                wybor_liczba = int(input("Moja liczba to: ")) #Wprowadzanie obstawianej liczby calkowitej za pomocą inputa

                                if wybor_liczba < 0 or wybor_liczba > 36: #kolejne zabezpieczenie przed wyborem nieprawidłowej liczby
                                        print("Podales bledna liczbe, zacznijmy jeszcze raz")
                                        print("+++++++++++++++++++++\n\n")
                                        time.sleep(1)
                                        kredyty +=stawka #powrót do starej liczby kredytów
                                else:  #jeżeli wszystko jest jak należy
                                        print("+++++++++++++++++++++\n")
                                        print("Trwa losowanie liczby ")                                
                                        time.sleep(1) #budowa napięcia
                                        print(".")
                                        time.sleep(1) 
                                        print(".")
                                        time.sleep(1) 
                                        print(".")
                                        print("Wylosowano liczbe", wylosowana)
                                        if wybor_liczba == wylosowana: #porównianie wylosowanej liczby z zadeklarowaną
                                                kredyty=kredyty + (stawka*35) #wygrana dodaje się do liczby kredytów z mnożnikiem 35
                                                time.sleep(0.5) 
                                                print("+++++++++++++++++++++\n")
                                                print("\nBrawo, wygrales!!!\n\n")
                                                time.sleep(2) 
                                                print("Grasz dalej czy odchodzisz z wygrana?", "Masz", kredyty, "kredytow")
                                                print("t - Gram")
                                                print("n - Odchodze")
                                                xxx = input("Postanawiam, ze ") #decydyjemy czy chcemy grać dalej czy nie
                                                if xxx == "n": #jeżeli użytkownik odchodzi to przerywa się działanie pętli
                                                       #nick = input("Podaj swoj nick: ")
                                                       print("\n")
                                                       print("\n")                                                   
                                                       if kredyty > 0:
                                                           try: #zapis do pliku (analogicznie w każdej dalszej sytuacji)
                                                               lista = [kredyty]
                                                               plik = open("wyniki.txt", "w")
                                                               plik.write("Ostatni wynik to:\n" + str(lista[0]))
                                                               #czas = time.localtime()
                                                               plik.write("\nZdobyty: \n%s" % datetime.datetime.now()) 
                                                               plik.write("\nPrzez:\n")
                                                               plik.write(nick)
                                                           except:
                                                               print("Nie mozna zapisac do pliku\n")
                                                           finally:
                                                               plik.close()
                                                               break
                                                print("\n")

                                        else: #jeżeli wylosowana liczba nie jest równa obstawionej
                                                time.sleep(0.5)
                                                print("+++++++++++++++++++++\n")
                                                print("\nNiestety, nie udalo Ci sie :(\n\n")
                                                time.sleep(2) 
                                                print("Grasz dalej czy odchodzisz z wygrana?", "Masz", kredyty, "kredytow")
                                                print("t - Gram")
                                                print("n - Odchodze")         
                                                xxx = input("Postanawiam, ze ") #j/w
                                                if xxx == "n": #j/w
                                                       #nick = input("Podaj swoj nick: ")
                                                       print("\n")
                                                       print("\n")
                                                       if kredyty > 0:
                                                           try: #zapis do pliku (analogicznie w każdej dalszej sytuacji)
                                                               lista = [kredyty]
                                                               plik = open("wyniki.txt", "w")
                                                               plik.write("Ostatni wynik to:\n" + str(lista[0]))
                                                               #czas = time.localtime()
                                                               plik.write("\nZdobyty: \n%s" % datetime.datetime.now()) 
                                                               plik.write("\nPrzez:\n")
                                                               plik.write(nick)
                                                           except:
                                                               print("Nie mozna zapisac do pliku\n")
                                                           finally:
                                                               plik.close()
                                                               break
                                                print("\n")                       

                        if wybor == 2: #jeżeli wybralismy obstawianie grup
                            print("Podaj swoja stawke: ")
                            stawka= int(input("Moja stawka to: "))
                            if stawka < 1 or stawka > kredyty: #zapezpieczenie
                                print("Obstaw co najmniej jeden kredyt i nie wiecej niz ich posiadasz!")
                                print("+++++++++++++++++++++\n\n")
                                time.sleep(1.5)
                            else: #jeżeli jest poprawny wybór
                                kredyty -= stawka
                                print("+++++++++++++++++++++\n")
                                print("Na jaka grupe chcesz obstawic?\n 1. Czerwone\n 2. Czarne\n 3. Zielone")
                                wybor_grupy= int(input("Wybieram grupe nr ")) #deklaracja grupy którą obstawiamy

                                if wybor_grupy == 1 and czerwone.count(wylosowana) == 1: #pętla dla wygranej grupy czerwonych
                                        print("+++++++++++++++++++++\n")
                                        print("Trwa losowanie grupy")
                                        time.sleep(1)
                                        print(".")
                                        time.sleep(1)
                                        print(".")
                                        time.sleep(1)
                                        print(".")
                                        if wylosowana == 1 or wylosowana == 3 or wylosowana == 5 or wylosowana == 7 or wylosowana == 9 or wylosowana == 12 or wylosowana == 14 or wylosowana == 16 or wylosowana == 18 or wylosowana == 21 or wylosowana == 25 or wylosowana == 23 or wylosowana == 27 or wylosowana == 30 or wylosowana == 32 or wylosowana == 36 or wylosowana == 34: #liczby odpowiadające grupiie czerwonych
                                            print("Wylosowano grupe: czerwone")
                                        elif wylosowana == 0: #dla zielonych
                                            print("Wylosowano grupe: zielone")
                                        else: #dla całej reszty czyli dla czarnych
                                            print("Wylosowano grupe: czarne")
                                        kredyty= kredyty + (stawka*2) #mnożnik dla czerwonych
                                        time.sleep(0.5)
                                        print("+++++++++++++++++++++\n")
                                        print("Brawo, wygrales!\n\n")
                                        time.sleep(2) 
                                        print("Grasz dalej czy odchodzisz z wygrana?", "Masz", kredyty, "kredytow")
                                        print("t - Gram")
                                        print("n - Odchodze")
                                        xxx = input("Postanawiam, ze ")
                                        if xxx == "n": #jeżeli nie chcemy dalej grać
                                                #nick = input("Podaj swoj nick: ")
                                                print("\n")
                                                print("\n")
                                                if kredyty > 0:
                                                    try: #zapis do pliku (analogicznie w każdej dalszej sytuacji)
                                                        lista = [kredyty]
                                                        plik = open("wyniki.txt", "w")
                                                        plik.write("Ostatni wynik to:\n" + str(lista[0]))
                                                        #czas = time.localtime()
                                                        plik.write("\nZdobyty: \n%s" % datetime.datetime.now()) 
                                                        plik.write("\nPrzez:\n")
                                                        plik.write(nick)
                                                    except:
                                                        print("Nie mozna zapisac do pliku\n")
                                                    finally:
                                                        plik.close()
                                                        break
                                        print("\n")

                                elif wybor_grupy == 2 and czarne.count(wylosowana) == 1: #pętla dla wygranej czarnych (reszta j/w)
                                        print("+++++++++++++++++++++\n")
                                        print("Trwa losowanie grupy")
                                        time.sleep(1)
                                        print(".")
                                        time.sleep(1)
                                        print(".")
                                        time.sleep(1)
                                        print(".")
                                        if wylosowana == 1 or wylosowana == 3 or wylosowana == 5 or wylosowana == 7 or wylosowana == 9 or wylosowana == 12 or wylosowana == 14 or wylosowana == 16 or wylosowana == 18 or wylosowana == 21 or wylosowana == 25 or wylosowana == 23 or wylosowana == 27 or wylosowana == 30 or wylosowana == 32 or wylosowana == 36 or wylosowana == 34: #liczby odpowiadające grupiie czerwonych
                                            print("Wylosowano grupe: czerwone")
                                        elif wylosowana == 0: #jeżeli wylosowano zielone
                                            print("Wylosowano grupe: zielone")
                                        else: #jeżeli wylosowano czarne
                                            print("Wylosowano grupe: czarne")
                                        kredyty= kredyty + (stawka*2) #mnożkik dla wygranej czarnych
                                        time.sleep(0.5) 
                                        print("+++++++++++++++++++++\n")
                                        print("Brawo, wygrales!\n\n")
                                        time.sleep(2)
                                        print("Grasz dalej czy odchodzisz z wygrana?", "Masz", kredyty, "kredytow")
                                        print("t - Gram")
                                        print("n - Odchodze")
                                        xxx = input("Postanawiam, ze ")
                                        if xxx == "n":
                                                #nick = input("Podaj swoj nick: ")
                                                print("\n")
                                                print("\n")
                                                if kredyty > 0:
                                                    try: #zapis do pliku (analogicznie w każdej dalszej sytuacji)
                                                        lista = [kredyty]
                                                        plik = open("wyniki.txt", "w")
                                                        plik.write("Ostatni wynik to:\n" + str(lista[0]))
                                                        #czas = time.localtime()
                                                        plik.write("\nZdobyty: \n%s" % datetime.datetime.now()) 
                                                        plik.write("\nPrzez:\n")
                                                        plik.write(nick)
                                                    except:
                                                        print("Nie mozna zapisac do pliku\n")
                                                    finally:
                                                        plik.close()
                                                        break
                                        print("\n")
                                
                                elif wybor_grupy == 3 and zielone.count(wylosowana) == 1: #pętla dla wygranej zielonych (reszta j/w)
                                        print("+++++++++++++++++++++\n")
                                        print("Trwa losowanie grupy")
                                        time.sleep(1)
                                        print(".")
                                        time.sleep(1)
                                        print(".")
                                        time.sleep(1)
                                        print(".")
                                        if wylosowana == 1 or wylosowana == 3 or wylosowana == 5 or wylosowana == 7 or wylosowana == 9 or wylosowana == 12 or wylosowana == 14 or wylosowana == 16 or wylosowana == 18 or wylosowana == 21 or wylosowana == 25 or wylosowana == 23 or wylosowana == 27 or wylosowana == 30 or wylosowana == 32 or wylosowana == 36 or wylosowana == 34: #liczby odpowiadające grupiie czerwonych
                                            print("Wylosowano grupe: czerwone")
                                        elif wylosowana == 0:
                                            print("Wylosowano grupe: zielone")
                                        else:
                                            print("Wylosowano grupe: czarne")
                                        kredyty = kredyty + (stawka*35)
                                        time.sleep(0.5) 
                                        print("+++++++++++++++++++++\n")
                                        print("Brawo, wygrales!\n\n")
                                        time.sleep(2)
                                        print("Grasz dalej czy odchodzisz z wygrana?", "Masz", kredyty, "kredytow")
                                        print("t - Gram")
                                        print("n - Odchodze")
                                        xxx = input("Postanawiam, ze ")
                                        if xxx == "n":
                                                #nick = input("Podaj swoj nick: ")
                                                print("\n")
                                                print("\n")
                                                if kredyty > 0:
                                                    try: #zapis do pliku (analogicznie w każdej dalszej sytuacji)
                                                        lista = [kredyty]
                                                        plik = open("wyniki.txt", "w")
                                                        plik.write("Ostatni wynik to:\n" + str(lista[0]))
                                                        #czas = time.localtime()
                                                        plik.write("\nZdobyty: \n%s" % datetime.datetime.now()) 
                                                        plik.write("\nPrzez:\n")
                                                        plik.write(nick)
                                                    except:
                                                        print("Nie mozna zapisac do pliku\n")
                                                    finally:
                                                        plik.close()
                                                        break
                                        print("\n")

                                elif wybor_grupy != 1 and wybor_grupy != 2 and wybor_grupy !=3: #zabezpieczenie przed nieprawdiłowym numerem grupy
                                        print("+++++++++++++++++++++")                                        
                                        print("Wpisales zly numer, sprobujmy jeszcze raz\n\n")
                                        kredyty += stawka
                                        time.sleep(1)

                                else: #jeżeli wylosowana grupa nie równa się obstawionej a wszystko poprawnie wpisaliśmy (reszta j/w)
                                        print("+++++++++++++++++++++\n")
                                        print("Trwa losowanie grupy")
                                        time.sleep(1)
                                        print(".")
                                        time.sleep(1)
                                        print(".")
                                        time.sleep(1)
                                        print(".")
                                        if wylosowana == 1 or wylosowana == 3 or wylosowana == 5 or wylosowana == 7 or wylosowana == 9 or wylosowana == 12 or wylosowana == 14 or wylosowana == 16 or wylosowana == 18 or wylosowana == 21 or wylosowana == 25 or wylosowana == 23 or wylosowana == 27 or wylosowana == 30 or wylosowana == 32 or wylosowana == 36 or wylosowana == 34:
                                            print("Wylosowano grupe: czerwone")
                                        elif wylosowana == 0: 
                                            print("Wylosowano grupe: zielone")
                                        else:
                                            print("Wylosowano grupe: czarne")
                                        time.sleep(0.5) 
                                        print("+++++++++++++++++++++\n")
                                        print ("Niestety, nie udalo Ci sie :(\n\n")
                                        time.sleep(2)
                                        print("Grasz dalej czy odchodzisz z wygrana?", "Masz", kredyty, "kredytow")
                                        print("t - Gram")
                                        print("n - Odchodze")
                                        xxx = input("Postanawiam, ze ")
                                        if xxx == "n":
                                                #nick = input("Podaj swoj nick: ")
                                                print("\n")
                                                print("\n")
                                                if kredyty > 0:
                                                    try: #zapis do pliku (analogicznie w każdej dalszej sytuacji)
                                                        lista = [kredyty]
                                                        plik = open("wyniki.txt", "w")
                                                        plik.write("Ostatni wynik to:\n" + str(lista[0]))
                                                        #czas = time.localtime()
                                                        plik.write("\nZdobyty: \n%s" % datetime.datetime.now()) 
                                                        plik.write("\nPrzez:\n")
                                                        plik.write(nick)
                                                    except:
                                                        print("Nie mozna zapisac do pliku\n")
                                                    finally:
                                                        plik.close()
                                                        break
                                        print("\n")

                        if wybor == 3: #jeżeli wybraliśmy obstawianie wysokich/niskich numerów
                            print("Podaj swoja stawke: ")
                            stawka= int(input("Moja stawka to: "))
                            if stawka < 1 or stawka > kredyty: #zabezpieczenie
                                print("Obstaw co najmniej jeden kredyt i nie wiecej niz ich posiadasz!")
                                print("+++++++++++++++++++++\n\n")
                                time.sleep(1.5)
                            else: #jak jest OK
                                kredyty -= stawka
                                print("+++++++++++++++++++++\n")
                                print("Na jaka grupe liczb chcesz obstawic?\n 1. Wysokie (19-36)\n 2. Niskie(1-18)")
                                wybor_wys = int(input("Wybieram liczby ")) #wprowadzamy jaką grupę liczb obstawiamy
                                
                                if wybor_wys == 1 and wysokie.count(wylosowana) == 1: #wysokie i wygrana
                                        print("+++++++++++++++++++++\n")
                                        print("Trwa losowanie liczby")
                                        time.sleep(1)
                                        print(".")
                                        time.sleep(1)
                                        print(".")
                                        time.sleep(1)
                                        print(".")
                                        if wylosowana > 18:
                                            print("Wylosowano grupe: wysokie")
                                        else:
                                            print("Wylosowano grupe: niskie")
                                        kredyty= kredyty + (stawka*2)
                                        time.sleep(0.5)
                                        print("+++++++++++++++++++++\n")
                                        print("Brawo, wygrales!\n\n")
                                        time.sleep(2) 
                                        print("Grasz dalej czy odchodzisz z wygrana?", "Masz", kredyty, "kredytow")
                                        print("t - Gram")
                                        print("n - Odchodze")
                                        xxx = input("Postanawiam, ze ")
                                        if xxx == "n":
                                                #nick = input("Podaj swoj nick: ")
                                                print("\n")
                                                print("\n")
                                                if kredyty > 0:
                                                    try: #zapis do pliku (analogicznie w każdej dalszej sytuacji)
                                                        lista = [kredyty]
                                                        plik = open("wyniki.txt", "w")
                                                        plik.write("Ostatni wynik to:\n" + str(lista[0]))
                                                        #czas = time.localtime()
                                                        plik.write("\nZdobyty: \n%s" % datetime.datetime.now()) 
                                                        plik.write("\nPrzez:\n")
                                                        plik.write(nick)
                                                    except:
                                                        print("Nie mozna zapisac do pliku\n")
                                                    finally:
                                                        plik.close()
                                                        break
                                        print("\n")

                                elif wybor_wys == 2 and niskie.count(wylosowana) == 1: #niskie i wygrana
                                        print("+++++++++++++++++++++\n")
                                        print("Trwa losowanie liczby")
                                        time.sleep(1)
                                        print(".")
                                        time.sleep(1)
                                        print(".")
                                        time.sleep(1)
                                        print(".")
                                        if wylosowana < 19:
                                            print("Wylosowano grupe: niskie")
                                        else:
                                            print("Wylosowano grupe: wysokie")
                                        kredyty= kredyty + (stawka*2)
                                        time.sleep(0.5) 
                                        print("+++++++++++++++++++++\n")
                                        print("Brawo, wygrales!\n\n")
                                        time.sleep(2)
                                        print("Grasz dalej czy odchodzisz z wygrana?", "Masz", kredyty, "kredytow")
                                        print("t - Gram")
                                        print("n - Odchodze")
                                        xxx = input("Postanawiam, ze ")
                                        if xxx == "n":
                                                #nick = input("Podaj swoj nick: ")
                                                print("\n")
                                                print("\n")
                                                if kredyty > 0:
                                                    try: #zapis do pliku (analogicznie w każdej dalszej sytuacji)
                                                        lista = [kredyty]
                                                        plik = open("wyniki.txt", "w")
                                                        plik.write("Ostatni wynik to:\n" + str(lista[0]))
                                                        #czas = time.localtime()
                                                        plik.write("\nZdobyty: \n%s" % datetime.datetime.now()) 
                                                        plik.write("\nPrzez:\n")
                                                        plik.write(nick)
                                                    except:
                                                        print("Nie mozna zapisac do pliku\n")
                                                    finally:
                                                        plik.close()
                                                        break
                                        print("\n")

                                elif wybor_wys != 1 and wybor_wys != 2: #zabezpieczenie
                                        print("+++++++++++++++++++++")                                        
                                        print("Wpisales zly numer, sprobujmy jeszcze raz\n\n")
                                        kredyty += stawka
                                        time.sleep(1)

                                else: #przegrana
                                        print("+++++++++++++++++++++\n")
                                        print("Trwa losowanie grupy")
                                        time.sleep(1)
                                        print(".")
                                        time.sleep(1)
                                        print(".")
                                        time.sleep(1)
                                        print(".")
                                        if wylosowana > 18:
                                            print("Wylosowano grupe: wysokie")
                                        else:
                                            print("Wylosowano grupe: niskie")
                                        time.sleep(0.5) 
                                        print("+++++++++++++++++++++\n")
                                        print ("Niestety, nie udalo Ci sie :(\n\n")
                                        time.sleep(2)
                                        print("Grasz dalej czy odchodzisz z wygrana?", "Masz", kredyty, "kredytow")
                                        print("t - Gram")
                                        print("n - Odchodze")
                                        xxx = input("Postanawiam, ze ")
                                        if xxx == "n":
                                                #nick = input("Podaj swoj nick: ")
                                                print("\n")
                                                print("\n")
                                                if kredyty > 0:
                                                    try: #zapis do pliku (analogicznie w każdej dalszej sytuacji)
                                                        lista = [kredyty]
                                                        plik = open("wyniki.txt", "w")
                                                        plik.write("Ostatni wynik to:\n" + str(lista[0]))
                                                        #czas = time.localtime()
                                                        plik.write("\nZdobyty: \n%s" % datetime.datetime.now()) 
                                                        plik.write("\nPrzez:\n")
                                                        plik.write(nick)
                                                    except:
                                                        print("Nie mozna zapisac do pliku\n")
                                                    finally:
                                                        plik.close()
                                                        break
                                        print("\n")

                        if wybor == 4: #jeżeli wybraliśmy obstawianie tuzionów liczb
                            print("Podaj swoja stawke: ")
                            stawka = int(input("Moja stawka to: "))
                            if stawka < 1 or stawka > kredyty: #zabezpieczenie
                                print("Obstaw co najmniej jeden kredyt i nie wiecej niz ich posiadasz!")
                                print("+++++++++++++++++++++\n\n")
                                time.sleep(1.5)
                            else: #jak jest OK
                                kredyty -= stawka
                                print("+++++++++++++++++++++\n")
                                print("Na jaki tuzin liczb chcesz obstawic?\n 1. Pierwszy (1-12)\n 2. Drugi(13-24)\n 3. Trzeci(25-36)")
                                wybor_tuz = int(input("Wybieram tuzin "))
                                
                                if wybor_tuz == 1 and atuzin.count(wylosowana) == 1: #tuzin pierwszy
                                        print("+++++++++++++++++++++\n")
                                        print("Trwa losowanie tuzinu")
                                        time.sleep(1)
                                        print(".")
                                        time.sleep(1)
                                        print(".")
                                        time.sleep(1)
                                        print(".")
                                        if wylosowana < 13:
                                            print("Wylosowano tuzin: 1")
                                        elif wylosowana >= 13 and wylosowana < 25:
                                            print("Wylosowano tuzin: 2")
                                        else:
                                            print("wylosowano tuzin: 3")
                                        kredyty= kredyty + (stawka*3)
                                        time.sleep(0.5)
                                        print("+++++++++++++++++++++\n")
                                        print("Brawo, wygrales!\n\n")
                                        time.sleep(2) 
                                        print("Grasz dalej czy odchodzisz z wygrana?", "Masz", kredyty, "kredytow")
                                        print("t - Gram")
                                        print("n - Odchodze")
                                        xxx = input("Postanawiam, ze ")
                                        if xxx == "n":
                                                #nick = input("Podaj swoj nick: ")
                                                print("\n")
                                                print("\n")
                                                if kredyty > 0:
                                                    try: #zapis do pliku (analogicznie w każdej dalszej sytuacji)
                                                        lista = [kredyty]
                                                        plik = open("wyniki.txt", "w")
                                                        plik.write("Ostatni wynik to:\n" + str(lista[0]))
                                                        #czas = time.localtime()
                                                        plik.write("\nZdobyty: \n%s" % datetime.datetime.now()) 
                                                        plik.write("\nPrzez:\n")
                                                        plik.write(nick)
                                                    except:
                                                        print("Nie mozna zapisac do pliku\n")
                                                    finally:
                                                        plik.close()
                                                        break
                                        print("\n")

                                elif wybor_tuz == 2 and btuzin.count(wylosowana) == 1: #tuzin2
                                        print("+++++++++++++++++++++\n")
                                        print("Trwa losowanie tuzinu")
                                        time.sleep(1)
                                        print(".")
                                        time.sleep(1)
                                        print(".")
                                        time.sleep(1)
                                        print(".")
                                        if wylosowana < 13:
                                            print("Wylosowano tuzin: 1")
                                        elif wylosowana >= 13 and wylosowana < 25:
                                            print("Wylosowano tuzin: 2")
                                        else:
                                            print("wylosowano tuzin: 3")
                                        kredyty= kredyty + (stawka*3) #mnożnik dla tuzinów
                                        time.sleep(0.5)
                                        print("+++++++++++++++++++++\n")
                                        print("Brawo, wygrales!\n\n")
                                        time.sleep(2) 
                                        print("Grasz dalej czy odchodzisz z wygrana?", "Masz", kredyty, "kredytow")
                                        print("t - Gram")
                                        print("n - Odchodze")
                                        xxx = input("Postanawiam, ze ")
                                        if xxx == "n":
                                                #nick = input("Podaj swoj nick: ")
                                                print("\n")
                                                print("\n")
                                                if kredyty > 0:
                                                    try: #zapis do pliku (analogicznie w każdej dalszej sytuacji)
                                                        lista = [kredyty]
                                                        plik = open("wyniki.txt", "w")
                                                        plik.write("Ostatni wynik to:\n" + str(lista[0]))
                                                        #czas = time.localtime()
                                                        plik.write("\nZdobyty: \n%s" % datetime.datetime.now()) 
                                                        plik.write("\nPrzez:\n")
                                                        plik.write(nick)
                                                    except:
                                                        print("Nie mozna zapisac do pliku\n")
                                                    finally:
                                                        plik.close()
                                                        break
                                        print("\n")

                                elif wybor_tuz == 3 and ctuzin.count(wylosowana) ==1: #tuzin3
                                        print("+++++++++++++++++++++\n")
                                        print("Trwa losowanie tuzinu")
                                        time.sleep(1)
                                        print(".")
                                        time.sleep(1)
                                        print(".")
                                        time.sleep(1)
                                        print(".")
                                        if wylosowana < 13:
                                            print("Wylosowano tuzin: 1")
                                        elif wylosowana >= 13 and wylosowana < 25:
                                            print("Wylosowano tuzin: 2")
                                        else:
                                            print("wylosowano tuzin: 3")
                                        kredyty= kredyty + (stawka*3) #mnożnik dla tuzinów
                                        time.sleep(0.5)
                                        print("+++++++++++++++++++++\n")
                                        print("Brawo, wygrales!\n\n")
                                        time.sleep(2) 
                                        print("Grasz dalej czy odchodzisz z wygrana?", "Masz", kredyty, "kredytow")
                                        print("t - Gram")
                                        print("n - Odchodze")
                                        xxx = input("Postanawiam, ze ")
                                        if xxx == "n":
                                                #nick = input("Podaj swoj nick: ")
                                                print("\n")
                                                print("\n")
                                                if kredyty > 0:
                                                    try: #zapis do pliku (analogicznie w każdej dalszej sytuacji)
                                                        lista = [kredyty]
                                                        plik = open("wyniki.txt", "w")
                                                        plik.write("Ostatni wynik to:\n" + str(lista[0]))
                                                        #czas = time.localtime()
                                                        plik.write("\nZdobyty: \n%s" % datetime.datetime.now()) 
                                                        plik.write("\nPrzez:\n")
                                                        plik.write(nick)
                                                    except:
                                                        print("Nie mozna zapisac do pliku\n")
                                                    finally:
                                                        plik.close()
                                                        break
                                        print("\n")

                                elif wybor_tuz != 1 and wybor_tuz != 2 and wybor_tuz !=3: #zabezpieczenie przed wybraniem niewłaściwego numeru
                                        print("+++++++++++++++++++++")                                        
                                        print("Wpisales zly numer, sprobujmy jeszcze raz\n\n")
                                        kredyty += stawka #zwrot kredytów wcześniej odjętych
                                        time.sleep(1)

                                else:
                                        print("+++++++++++++++++++++\n")
                                        print("Trwa losowanie tuzinu")
                                        time.sleep(1)
                                        print(".")
                                        time.sleep(1)
                                        print(".")
                                        time.sleep(1)
                                        print(".")
                                        if wylosowana < 13:
                                            print("Wylosowano tuzin: 1")
                                        elif wylosowana >= 13 and wylosowana < 25:
                                            print("Wylosowano tuzin: 2")
                                        else:
                                            print("wylosowano tuzin: 3")
                                        time.sleep(0.5)
                                        print("+++++++++++++++++++++\n")
                                        print ("Niestety, nie udalo Ci sie :(\n\n")
                                        time.sleep(2) 
                                        print("Grasz dalej czy odchodzisz z wygrana?", "Masz", kredyty, "kredytow")
                                        print("t - Gram")
                                        print("n - Odchodze")
                                        xxx = input("Postanawiam, ze ")
                                        if xxx == "n":
                                                #nick = input("Podaj swoj nick: ")
                                                print("\n")
                                                print("\n")
                                                if kredyty > 0:
                                                    try: #zapis do pliku (analogicznie w każdej dalszej sytuacji)
                                                        lista = [kredyty]
                                                        plik = open("wyniki.txt", "w")
                                                        plik.write("Ostatni wynik to:\n" + str(lista[0]))
                                                        #czas = time.localtime()
                                                        plik.write("\nZdobyty: \n%s" % datetime.datetime.now()) 
                                                        plik.write("\nPrzez:\n")
                                                        plik.write(nick)
                                                    except:
                                                        print("Nie mozna zapisac do pliku\n")
                                                    finally:
                                                        plik.close()
                                                        break
                                        print("\n")
           kredyty2 = 50
           print("\n")
           print(" ****************************************")
           print(" *Zakonczyles gre z portfelem o wartosci*", kredyty, "kredytow") #ostateczna informacja jak nam poszło
           print(" ****************************************")
           print("\n")
           wygrana = kredyty - kredyty2 
           time.sleep(1)
           if wygrana > 0:
               print("Brawo", nick ,"! udalo ci sie wygrac", wygrana, "kredytow") #informacja o tym ile udało nam się ugrać
           elif wygrana == 0:
               print("Przynajmniej wyszedles na 0 :)") #jeżeli zakończyliśmy grę z 50 kredytami
           else:
               print(nick, "przegrales", wygrana, "kredytow. Zdarza sie nawet najlepszym\n\n") #jeżeli zakończyliśmy z mniejszą ilością kredytów niż na początku
           time.sleep(1)
           print("\n")
           op = input("Czy chcesz zagrac jeszcze raz? (t/n)") #zmienna op sterująca główną pętlą while
           print("\n")

ruletka() #wywołanie programu ruletki