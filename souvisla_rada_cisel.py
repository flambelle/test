# Input: Textovy soubor souvisla_rada_cisel-input.txt, na kazdem radku jedno cislo
# Output: Vytiskne seznam chybejicich cisel

count = open("souvisla_rada_cisel-input.txt", "r");

seznam_cisel = []
chybejici_cisla = []

for line in count:
    line = int(line)
    seznam_cisel.append(line)

for i in range(len(seznam_cisel)-1):
    if seznam_cisel[i] + 1 != seznam_cisel[i+1]:
        if seznam_cisel[i] != seznam_cisel[i+1]:
            chybejici_cisla.append(seznam_cisel[i]+1)

print(chybejici_cisla)
count.close()



