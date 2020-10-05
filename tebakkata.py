import time, sys, os

#color
HEADER = '\033[95m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
CYAN = '\033[96m'
RESET = '\033[0m'




#tebakan EASY
level1 = "kasih mudah ni, pemain bola yang berat nya 3kg siapa?"
jawaban1 = "bambang tabung gas"

level2 = "penyanyi luar negri yang suka bersepeda?"
jawaban2 = "selena goes"

level3 = "Penyanyi yang rambutnya gak lurus?"
jawaban3 = "ayu kriting"

level4 = "Guru, guru apa yang gk gemukan?"
jawaban4 = "gurusan"

level5 = "Sayur, sayur apa yang bersinar?"
jawaban5 = "terong"

level6 = "Ayam, ayam apa yang gak bisa di pegang?"
jawaban6 = "ayam hilang"

level7 = "Buah, buah apa yang kerja keras?"
jawaban7 = "buahpak"

level8 = "Kenapa zombie kalo nyerang rame rame?"
jawaban8 = "karena kalau sendiri zomblo"

level9 = "Presiden / Wakil Presiden yang sering nonton streaming?"
jawaban9 = "muhammad youtube kalla"

level10 = "Kue apa yang paling kaya?"
jawaban10 = "sri kaya"


#Tebakan HARD
lvl1 = "Apa nama sebuah benda yang kalau ditutup berubah jadi tongkat, tapi ketika dibuka malah jadi tenda?"
jwb1 = "payung"

lvl2 = "Jika perlu waktu merebus 20 menit agar sebutir telur bisa matang, berapa lama waktu merebus yang dibutuhkan agar 10 butir telur bisa matang?"
jwb2 = "tetap 20 menit"
ulasan2 = "Tinggal rebus aja semua ngapain satu satu :D"

lvl3 = "Seorang pria terjebak di dalam gua, ia kebingungan karena gua tersebut gelap. Di tangannya ada lilin dan obor. Apa yang harus ia nyalakan terlebih dahulu?"
jwb3 = "korek api"

lvl4 = "Jika ada 10 pejuang Indonesia yang berperang lalu ada satu orang yang gugur, ada berapa orang yang akan kembali ke markas?"
jwb4 = "1009"
ulasan4 = "Karena pepatah pernah berkata\nGugur satu tumbuh seribu\nMati 1 = 1000 sisa 9\n1000+9 = 1009 :D"

lvl5 = "Kalau sedang sendiri, kakinya ada empat, kalau berdua, kakinya jadi ada delapan. Siapakah aku?"
jwb5 = "kursi"

lvl6 = "Apa yang ada di ujung langit?"
jwb6 = "huruf t"

lvl7 = "Aku selalu ada di atas presiden dan menteri, tapi aku tidak punya jabatan apapun dalam pemerintahan. Siapakah aku?"
jwb7 = "peci"

lvl8 = "Kalau singa jadi ayam, lalu jerapah jadi ayam, dan sapi jadi ayam, terus ayam jadi apa?"
jwb8 = "jadi banyak"

lvl9 = "Apa nama hewan yang keahliannya sangat banyak?"
jwb9 = "kukang"

lvl10 = "Sandal apa yang rasanya enak dan bikin ketagihan?"
jwb10 = "sandal terasi"


#menu utama
menu = True
while menu:
    os.system('clear')
    time.sleep(2)
    print(RED+"================================\n".center(55))
    print(GREEN+"+-----Welcome to Brain out-----+\n".center(55))
    print("+--------By: Mr.G2M8N05--------+\n".center(55))
    print(RED+"================================\n".center(55))
    time.sleep(2)
    print(HEADER+"PILIH TANTANGAN ATAU MODE YANG ANDA MAMPU")
    time.sleep(1)
    print("1.Easy")
    time.sleep(1)
    print("2.Hard")
    time.sleep(1)
    print("3.Keluar (ENTER)")
    time.sleep(2)
    menu=input("PILIH MODE > ")

#buat fungsi
    if menu == '1':
        os.system('clear')
        time.sleep(2)
        print(RED+"==============================".center(55))
        print(CYAN+"|+++++++Are You ready?+++++++|".center(55))
        print(RED+"==============================".center(55))
        print(CYAN+"•> EASY <•".center(55))
        print(GREEN+"++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
        print(HEADER+"1.SIAP\n")
        print("2.Belum Siap\n")
        jwb=input("|•> ")
        #tugas ready
        #lvl 1
        os.system('clear')
        if jwb == '1':
            time.sleep(2)
            print(HEADER+"=====================".center(55))
            print(CYAN+"|••••••LEVEL 1••••••|".center(55))
            print(HEADER+"=====================".center(55))
            time.sleep(2)
            print(RED+"Pertanyaan:\n",CYAN+ level1)
            time.sleep(2)
            while (True):
                jb1=input(YELLOW+"Jawaban: ")
                if jawaban1 == jb1:
                    time.sleep(2)
                    print(RED+"Anjay Pinter Dong")
                    time.sleep(2)
                    print("Ayo Semangat Next -->")
                    break
                else:
                    print("SALAH CUK")
        #lvl 2
            time.sleep(2)
            os.system('clear')
            print(HEADER+"=====================".center(55))
            print(CYAN+"|••••••LEVEL 2••••••|".center(55))
            print(HEADER+"=====================".center(55))
            time.sleep(2)
            print(RED+"Pertanyaan:\n",CYAN+ level2)
            time.sleep(2)
            while (True):
                jb2=input(YELLOW+"Jawaban: ")
                if jawaban2 == jb2:
                    time.sleep(2)
                    print(RED+"Kerja Bagus")
                    time.sleep(2)
                    print("NEXT -->")
                    break
                else:
                    print("SALAH CUK")
                    
        #lvl 3
            time.sleep(2)
            os.system('clear')
            print(HEADER+"=====================".center(55))
            print(CYAN+"|••••••LEVEL 3••••••|".center(55))
            print(HEADER+"=====================".center(55))
            time.sleep(2)
            print(RED+"Pertanyaan:\n",CYAN+ level3)
            time.sleep(2)
            while (True):
                jb3=input(YELLOW+"Jawaban: ")
                if jawaban3 == jb3:
                    time.sleep(2)
                    print(RED+"GOOD BOY")
                    time.sleep(2)
                    print("NEXT -->")
                    break
                else:
                    print("SALAH CUK")
                    print("SALAH CUK")
                    
        #lvl 4
            time.sleep(2)
            os.system('clear')
            print(HEADER+"=====================".center(55))
            print(CYAN+"|••••••LEVEL 4••••••|".center(55))
            print(HEADER+"=====================".center(55))
            time.sleep(2)
            print(RED+"Pertanyaan:\n",CYAN+ level4)
            time.sleep(2)
            while (True):
                jb4=input(YELLOW+"Jawaban: ")
                if jawaban4 == jb4:
                    time.sleep(2)
                    print(RED+"GOOD BOY")
                    time.sleep(2)
                    print("NEXT -->")
                    break
                else:
                    print("SALAH CUK")
                    
        # lvl 5
            time.sleep(2)
            os.system('clear')
            print(HEADER+"=====================".center(55))
            print(CYAN+"|••••••LEVEL 5••••••|".center(55))
            print(HEADER+"=====================".center(55))
            time.sleep(2)
            print(RED+"Pertanyaan:\n",CYAN+ level5)
            time.sleep(2)
            while (True):
                jb5=input(YELLOW+"Jawaban: ")
                if jawaban5 == jb5:
                    time.sleep(2)
                    print(RED+"GOOD BOY")
                    time.sleep(2)
                    print("NEXT -->")
                    break
                else:
                    print("SALAH CUK")
        
        #lvl 6
            time.sleep(2)
            os.system('clear')
            print(HEADER+"=====================".center(55))
            print(CYAN+"|••••••LEVEL 6••••••|".center(55))
            print(HEADER+"=====================".center(55))
            time.sleep(2)
            print(RED+"Pertanyaan:\n",CYAN+ level6)
            time.sleep(2)
            while (True):
                jb6=input(YELLOW+"Jawaban: ")
                if jawaban3 == jb3:
                    time.sleep(2)
                    print(RED+"GOOD BOY")
                    time.sleep(2)
                    print("NEXT -->")
                    break
                else:
                    print("SALAH CUK")
        
        #lvl 7
            time.sleep(2)
            os.system('clear')
            print(HEADER+"=====================".center(55))
            print(CYAN+"|••••••LEVEL 7••••••|".center(55))
            print(HEADER+"=====================".center(55))
            time.sleep(2)
            print(RED+"Pertanyaan:\n",CYAN+ level7)
            time.sleep(2)
            while (True):
                jb7=input(YELLOW+"Jawaban: ")
                if jawaban7 == jb7:
                    time.sleep(2)
                    print(RED+"GOOD BOY")
                    time.sleep(2)
                    print("NEXT -->")
                    break
                else:
                    print("SALAH CUK")     
        
        #lvl 8
            time.sleep(2)
            os.system('clear')
            print(HEADER+"=====================".center(55))
            print(CYAN+"|••••••LEVEL 8••••••|".center(55))
            print(HEADER+"=====================".center(55))
            time.sleep(2)
            print(RED+"Pertanyaan:\n",CYAN+ level8)
            time.sleep(2)
            while (True):
                jb8=input(YELLOW+"Jawaban: ")
                if jawaban8 == jb8:
                    time.sleep(2)
                    print(RED+"MANTUL")
                    time.sleep(2)
                    print("NEXT -->")
                    break
                else:
                    print("SALAH CUK")        
        #lvl 9
            time.sleep(2)
            os.system('clear')
            print(HEADER+"=====================".center(55))
            print(CYAN+"|••••••LEVEL 9••••••|".center(55))
            print(HEADER+"=====================".center(55))
            time.sleep(2)
            print(RED+"Pertanyaan:\n",CYAN+ level9)
            time.sleep(2)
            while (True):
                jb9=input(YELLOW+"Jawaban: ")
                if jawaban9 == jb9:
                    time.sleep(2)
                    print(RED+"NICE")
                    time.sleep(2)
                    print("Ayo lebih semangat ini yang terakhir")
                    time.sleep(1)
                    print("NEXT -->")
                    break
                else:
                    print("SALAH CUK")        
        # lvl 10
            time.sleep(2)
            os.system('clear')
            print(HEADER+"=======================".center(55))
            print(CYAN+"|•••••••LEVEL 10••••••|".center(55))
            print(HEADER+"=======================".center(55))
            time.sleep(2)
            print(RED+"Pertanyaan:\n",CYAN+ level10)
            time.sleep(2)
            while (True):
                jb10=input(YELLOW+"Jawaban: ")
                if jawaban10 == jb10:
                    time.sleep(2)
                    print(RED+"BAGUS BOSS")
                    time.sleep(2)
                    print("NEXT -->")
                    time.sleep(2)
                    os.system('clear')
                    time.sleep(2)
                    print(RED+"================================".center(55))
                    print(CYAN+"|•••••••KERJA YANG BAGUS•••••••|".center(55))
                    print(CYAN+"|•SAYA TANTANG KAMU DIMODE HARD•|".center(55))
                    print(RED+"================================".center(55))
                    time.sleep(4)
                    break
                else:
                    print("SALAH CUK? MUDAH LO ITU")
            
        elif jwb == '2':
          time.sleep(2)
          print(CYAN+"Yah Ayo dong Dicoba jangan nyerah")
          time.sleep(1)
          print("Karena Menyerah itu Bukanlah jalan yg terbaik")
          time.sleep(1)
          print("HAYUK SEMANGAT")
          time.sleep(2)
          
        else:
          time.sleep(2)
          print(YELLOW+"AU AH AKU TEH PENGEN SEBLAK")
          print(":)")
          break
    elif menu == '2':
        os.system('clear')
        print(RED+"==============================".center(55))
        print(CYAN+"|+++++++Are You ready?+++++++|".center(55))
        print(RED+"==============================".center(55))
        print(CYAN+"•> HARD <•".center(55))
        print(GREEN+"++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
        print(HEADER+"1.SIAP\n")
        print("2.Belum Siap\n")
        jwb=input("|•> ")
        #tugas ready
        #lvl 1
        if jwb == '1':
            os.system('clear')
            time.sleep(1)
            print(HEADER+"=====================".center(55))
            print(CYAN+"|••••••LEVEL 1••••••|".center(55))
            print(HEADER+"=====================".center(55))
            time.sleep(1)
            print(RED+"Pertanyaan:\n",CYAN+ lvl1)
            time.sleep(1)
            while (True):
              jw1=input(YELLOW+"Jawaban: ")
              if jwb1 == jw1:
                time.sleep(2)
                print(RED+"Hmm Sepertinya ini terlalu mudah")
                time.sleep(1)
                print("oke NEXT ==>")
                time.sleep(2)
                break
              else:
                print("NO..NO..NO.. SALAH ")
        #lvl 2
            os.system('clear')
            time.sleep(1)
            print(HEADER+"=====================".center(55))
            print(CYAN+"|••••••LEVEL 2••••••|".center(55))
            print(HEADER+"=====================".center(55))
            time.sleep(2)
            print(RED+"Pertanyaan:\n",CYAN+ lvl2)
            time.sleep(2)
            while (True):
              jw2=input(YELLOW+"Jawaban: ")
              if jwb2 == jw2:
                time.sleep(1)
                print(ulasan2)
                time.sleep(1)
                print(RED+"Wah HEBAT")
                time.sleep(1)
                print("NEXT •>")
                time.sleep(3)
                break
              else:
                print("COBA LAGI")
                    
        #LVL 3
            os.system('clear')
            time.sleep(1)
            print(HEADER+"=====================".center(55))
            print(CYAN+"|••••••LEVEL 3••••••|".center(55))
            print(HEADER+"=====================".center(55))
            time.sleep(2)
            print(RED+"Pertanyaan:\n",CYAN+ lvl3)
            time.sleep(2)
            while (True):
              jw3=input(YELLOW+"Jawaban: ")
              if jwb3 == jw3:
                time.sleep(1)
                print(RED+"TRIPLE KILL")
                time.sleep(1)
                print("NEXT •> ")
                time.sleep(2)
                break
              else:
                print("COBA LAGI")
                
        #LVL 4
            os.system('clear')
            time.sleep(1)
            print(HEADER+"=====================".center(55))
            print(CYAN+"|••••••LEVEL 4••••••|".center(55))
            print(HEADER+"=====================".center(55))
            time.sleep(2)
            print(RED+"Pertanyaan:\n",CYAN+ lvl4)
            time.sleep(2)
            while (True):
              jw4=input(YELLOW+"Jawaban: ")
              if jwb4 == jw4:
                time.sleep(1)
                print(ulasan4)
                time.sleep(1)
                print(RED+"MANIAC")
                time.sleep(1)
                print(RED+"NEXT •> ")
                time.sleep(3)
                break
              else:
                print("COBA LAGI")
                
          #lvl 5
            os.system('clear')
            time.sleep(1)
            print(HEADER+"=====================".center(55))
            print(CYAN+"|••••••LEVEL 5••••••|".center(55))
            print(HEADER+"=====================".center(55))
            time.sleep(2)
            print(RED+"Pertanyaan:\n",CYAN+ lvl5)
            time.sleep(2)
            while (True):
              jw5=input(YELLOW+"Jawaban: ")
              if jwb5 == jw5:
                time.sleep(1)
                print(RED+"SAVAGE")
                time.sleep(1)
                print(RED+"NEXT •> ")
                time.sleep(2)
                break
              else:
                print("COBA LAGI")
                
          #lvl 6
            os.system('clear')
            time.sleep(1)
            print(HEADER+"=====================".center(55))
            print(CYAN+"|••••••LEVEL 6••••••|".center(55))
            print(HEADER+"=====================".center(55))
            time.sleep(2)
            print(RED+"Pertanyaan:\n",CYAN+ lvl6)
            time.sleep(2)
            while (True):
              jw6=input(YELLOW+"Jawaban: ")
              if jwb6 == jw6:
                time.sleep(1)
                print(RED+"KILLING SPREE")
                time.sleep(1)
                print("NEXT •> ")
                time.sleep(2)
                break
              else:
                print("COBA LAGI")
                
          #lvl 7
            os.system('clear')
            time.sleep(1)
            print(HEADER+"=====================".center(55))
            print(CYAN+"|••••••LEVEL 7••••••|".center(55))
            print(HEADER+"=====================".center(55))
            time.sleep(2)
            print(RED+"Pertanyaan:\n",CYAN+ lvl7)
            time.sleep(2)
            while (True):
              jw7=input(YELLOW+"Jawaban: ")
              if jwb7 == jw7:
                time.sleep(1)
                print(RED+"TRIPLE KILL")
                time.sleep(1)
                print("NEXT •> ")
                time.sleep(2)
                break
              else:
                print("COBA LAGI")
                
          #lvl 8
            os.system('clear')
            time.sleep(1)
            print(HEADER+"=====================".center(55))
            print(CYAN+"|••••••LEVEL 8••••••|".center(55))
            print(HEADER+"=====================".center(55))
            time.sleep(2)
            print(RED+"Pertanyaan:\n",CYAN+ lvl8)
            time.sleep(2)
            while (True):
              jw8=input(YELLOW+"Jawaban: ")
              if jwb8 == jw8:
                time.sleep(1)
                print(RED+"GODLIKE")
                time.sleep(1)
                print("NEXT •> ")
                time.sleep(2)
                break
              else:
                print("COBA LAGI")
                
          #lvl 9
            os.system('clear')
            time.sleep(1)
            print(HEADER+"=====================".center(55))
            print(CYAN+"|••••••LEVEL 9••••••|".center(55))
            print(HEADER+"=====================".center(55))
            time.sleep(2)
            print(RED+"Pertanyaan:\n",CYAN+ lvl9)
            time.sleep(2)
            while (True):
              jw9=input(YELLOW+"Jawaban: ")
              if jwb9 == jw9:
                time.sleep(1)
                print("Kukang es\nKukang martabak\nKukang PHP\nDLL")
                time.sleep(2)
                print(RED+"MONSTER KILL")
                time.sleep(1)
                print("NEXT •> ")
                time.sleep(2)
                break
              else:
                print("COBA LAGI")
                
          #lvl 10
            os.system('clear')
            time.sleep(2)
            print(HEADER+"=======================".center(55))
            print(CYAN+"|•••••LEVEL 10•••••|".center(55))
            print(CYAN+"|••••••• END •••••••|".center(55))
            print(HEADER+"=======================".center(55))
            time.sleep(2)
            print(RED+"Pertanyaan:\n",CYAN+ lvl10)
            time.sleep(2)
            while(True):
              jw10=input(YELLOW+"Jawaban: ")
              if jwb10 == jw10:
                time.sleep(2)
                print(RED+"LEGENDARIS")
                time.sleep(1)
                print("KERJA YANG BAGUS")
                time.sleep(2)
                os.system('clear')
                time.sleep(1)
                print(HEADER+"========================".center(55))
                print(CYAN+"+•••KERJA YANG BAGUS•••+".center(55))
                print(CYAN+"+••••••YOU WINNER••••••+".center(55))
                print(HEADER+"========================".center(55))
                time.sleep(1)
                print(YELLOW+"•>BRAIN OUT BY:MR.G2M8N05<•".center(55))
                print(CYAN+"•>SORRY JIKA ADA KATA ATAU TAMPILAN YG KURANG INDAH<•".center(55))
                time.sleep(4)
                break
              else:
                print("COBA LAGI")
                
            
        
        elif jwb == '2':
          os.system('clear')
          time.sleep(2)
          print(CYAN+"AYO AYO SEMANGAT KAMU PASTI BISA")
          time.sleep(1)
          print("MARI KITA COBA SEKALI LAGI •>")
          time.sleep(3)
  
    else:
        os.system('clear')
        time.sleep(1)
        print("IKAN HIU MAKAN TOMAT")
        time.sleep(2)
        print("GOBLOK!")
        time.sleep(2)
        break