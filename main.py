sozluk={"LOL":"komik bir şeye verilen cevap","CRINGE":"garip ya da utandırıcı bir şey","ROFL":"bir şakaya karşılık cevap","SHEESH":"onaylamamak","CREEPY":"korkunç","AGGRO":"agresifleşmek/sinirlenmek"}
word = input("Anlamadığınız bir kelime yazın: ")
if word.upper() in sozluk.keys():
    print(sozluk[word.upper()])
else:
    print("bu kelime sözlükte yok")
