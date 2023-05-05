#one-gap buffer test

pseudo  = ["F", "V",  "t", "O", "R", "C", "G", "W", "H", "N", "I", "J",  "e", "P", "X", "S", "T", "B", "E", "M", "L",  "g",  "o", "D", "A",  "(", "Y",  "i",  ")"]

def encr(strn, key):
    return pseudo[ (pseudo.index(strn) + pseudo.index(key))%29 ]

def decr(strn, key):
    return pseudo[ pseudo.index(strn) - pseudo.index(key) ]

def dekey(strn, key):
    return pseudo[ pseudo.index(key) - pseudo.index(strn) ]


def section(fn):
    file = open('ppages/' + fn + '.txt')
    text = ""
    for m in file:
        text += m
    file.close()

    lastrune = 'S'
    #finding last rune char is hard, so hardcode per file
    match fn:
        case '00sec':
            lastrune = 'W'
        case '03sec':
            lastrune = 'M'
        case '08sec':
            lastrune = 'H'
        case '15sec cut','15sec':
            lastrune = 'X'
        case '23sec':
            lastrune = 'g'
        case '27sec':
            lastrune = 'e'
        case '33sec':
            lastrune = 'J'
        case '40sec','40sec cut':
            lastrune = 'I'

    #in the case of whole-book version, lastrune is the last rune of the
    #prevs section, of last section for first. neg

    tl = ""
    tn = ""
    lt = ""
    nt = ""
    
    #key is strn set forward one. punct from key means punct set forward one...
    #actually it means key set back one rather than forward, relatively
    for n in range(0, len(text)):
        if text[n] in pseudo:#this but different
            #scrub forward for nextrune
            i=1
            while text[(n+i) % len(text)] not in pseudo:
                i += 1
            nextrune = text[(n+i) % len(text)]
            
            tl += decr(text[n], lastrune)
            tn += decr(text[n], nextrune)
            lt += decr(lastrune, text[n])
            nt += decr(nextrune, text[n])
            
            lastrune = text[n]
        elif text[n] != '\n' and text[n] != '/':
            tl += text[n]
            tn += text[n]
            lt += text[n]
            nt += text[n]



    #write four pages
    f2 = open("bpages/" + fn + "tl.txt", 'w')#this overwrites file
    print(tl, file=f2)
    f2.close()
    f3 = open("bpages/" + fn + "tn.txt", 'w')
    print(tn, file=f3)
    f3.close()
    f4 = open("bpages/" + fn + "lt.txt", 'w')#this overwrites file
    print(lt, file=f4)
    f4.close()
    f5 = open("bpages/" + fn + "nt.txt", 'w')
    print(nt, file=f5)
    f5.close()

    #ignore this for now
    iocdic = {}
    count = {}
    for c in pseudo:
        iocdic[c] = {}
        count[c] = 0
        for m in pseudo:
            iocdic[c][m] = 0

    
    for n in lt:
        if n in pseudo:
            count[n] +=1

    print(count)
        
        

    

section('00sec')
section('03sec')
section('08sec')
section('15sec cut')
section('23sec')
section('27sec')
section('33sec')
section('40sec cut')

