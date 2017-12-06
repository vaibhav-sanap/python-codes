from sys import stdin

def toggle( str ):
    slist = list(str)

    for i in range(0,len(str)):
        if(slist[i].isupper()):
            slist[i] = slist[i].lower()
        else:
            slist[i] = slist[i].upper()
    
    return "".join(slist)

str = raw_input()
print(toggle(str))
