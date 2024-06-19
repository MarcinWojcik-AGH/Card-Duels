import Colors

alphabet = {
    'A':[],
    'B':[],
    'C':[],
    'D':[],
    'E':[],
    'F':[],
    'G':[],
    'H':[],
    'I':[],
    'J':[],
    'K':[],
    'L':[],
    'M':[],
    'N':[],
    'O':[],
    'P':[],
    'Q':[],
    'R':[],
    'S':[],
    'T':[],
    'U':[],
    'V':[],
    'W':[],
    'X':[],
    'Y':[],
    'Z':[]
}
file = open("Letters.txt","r")
lines = file.readlines()
keys = list(alphabet.keys())


for i in range(26):
    start = i * 9
    end = start + 9
    for line in lines:
        fragment = line[start:end]  
        if keys[i] in alphabet:
            alphabet[keys[i]].append(fragment)

#Used to print huge letters
def printTitle(string,type="Normal",fgcolor="Grey",bgcolor="Black",tittle=True):
    for i in range(9):
        temp = ""
        for letter in string:
            if(letter==' '):
                temp=temp+"         "
            elif(letter.upper() in keys):
                temp=temp+alphabet[letter.upper()][i]            
            else:
                temp=temp+"Error!"
        print(Colors.AddColor(temp,type,fgcolor,bgcolor,tittle))   
