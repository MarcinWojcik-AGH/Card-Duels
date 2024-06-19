types = {
    "Normal":0,
    "Brighter":1,
    "Darker":2,
    "Italiks":3,
    "Underscore":4,
    "Blinking":5,
    "Reverse":7,
    "Crossed":9,
}
colors = {
    "Red":31,
    "Brown":33,
    "Green":32,
    "Cyan":36,
    "Blue":34,
    "Magenta":35,
    "Grey":37,
    "Black":30
}
i = 0
#Formats a string to be in given color and type.
def AddColor(string,type="Normal",textcolor="Grey",bgcolor="Black",tittle=False):
    global i
    temp=""
    keys = list(colors.keys())
    if(type=="Rainbow"):
        i = 0
        for letter in string:
            if(i>7):
                i=0 
            if(keys[i]=="Black" and bgcolor=="Black"):
                i=i+1
            if(i>7):
                i=0 
            if(letter==" " and tittle==False):
                temp = temp + AddColor(letter,"Blinking",keys[i],bgcolor)
                i -= 1      
            else:
                temp = temp + AddColor(letter,"Blinking",keys[i],bgcolor)
            i=i+1
        i = 0
        return temp
    elif(type == "LoreRainbow"):
        if(i>7):
            i=0 
        if(keys[i]=="Black" and bgcolor=="Black"):
            i=i+1
        if(i>7):
            i=0 
        if(string==" "):
            return " "      
        else:
            temp = AddColor(string,"Blinking",keys[i],bgcolor)
            i += 1
            return temp
    else:
        return "\033["+str(types[type])+";"+str(colors[textcolor])+";"+str(colors[bgcolor]+10)+"m" + string
