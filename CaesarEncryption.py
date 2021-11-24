codelist=("a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z")

def listline(linea):
    lineaLista=[]
    for x in linea:
        lineaLista.append(x)
    return lineaLista
def encrypt(linea,shift=0):
    list = listline(linea)
    linea =""
    for x in range(len(list)):
        char = list[x]
        char = shiftletter(char,shift)
        list.remove[x]
        linea = linea +char
    return linea
def shiftletter(letter,shift):
    count = int(0)
    for x in codelist:
        if x == letter:
            letter = codelist[count+shift]
        count = count + 1
    return letter

word = input("One word")
shift = int(input("Shift input"))
print(encrypt(word,shift))
