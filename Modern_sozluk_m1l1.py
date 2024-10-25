meme_dict = {"CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "SHEESH" : "onaylamamak",
             "CREEPY" : "korkunç"
            }

word = input("Bilmediniğiniz bir kelimeyi yazın (girilen kelimelerin hepsi büyük olmalı!)")

if word in meme_dict.keys():
    print(meme_dict[word])

else:
    print("Henüz bu kelimeye sahip değiliz, sözlüğümüzü geliştiriyoruz")
