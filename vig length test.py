runes = ["ᚠ", "ᚢ", "ᚦ", "ᚩ", "ᚱ", "ᚳ", "ᚷ", "ᚹ", "ᚻ", "ᚾ", "ᛁ", "ᛄ", "ᛇ", "ᛈ", "ᛉ", "ᛋ", "ᛏ", "ᛒ", "ᛖ", "ᛗ", "ᛚ", "ᛝ", "ᛟ", "ᛞ", "ᚪ", "ᚫ", "ᚣ", "ᛡ", "ᛠ"]
letters = ["F", "V", "th", "O", "R", "C", "G", "W", "H", "N", "I", "J", "eo", "P", "X", "S", "T", "B", "E", "M", "L", "ng", "oe", "D", "A", "ae", "Y", "ia", "ea"]
pseudo  = ["F", "V",  "t", "O", "R", "C", "G", "W", "H", "N", "I", "J",  "e", "P", "X", "S", "T", "B", "E", "M", "L",  "g",  "o", "D", "A",  "(", "Y",  "i",  ")"]

exclude = "abcdefABCDEF1234567890\n&%/"

def dec(strn, key):
    return(strn-key +29)%29

def convertdecf(fl):
    fn = "srpages/" + fl + ".txt"
    file = open(fn, 'r', encoding="utf8")
    strn = ""
    q = 0

    for c in file:#lines
        for d in c:
            if d == 'ᚠ' and q in [62,102,115,181,217,218,333,565,595,624,688,68,81]:
                pass
                #strn += pseudo[ runes.index(d) ]
            elif d in runes:
                strn += pseudo[ runes.index(d) ]
                
            elif d == '-' or d == '.':# or d == '/':
                strn += ' '
            elif d != chr(65279) and d not in exclude:
                strn += d
            q += 1
    print(strn)



def convertdec(fl, key):
    fn = "srpages/" + fl + ".txt"
    file = open(fn, 'r', encoding="utf8")
    strn = ""
    p = len(key)
    k = 0
    q = 0

    for c in file:#lines
        for d in c:
            if d in pseudo:
                strn += pseudo[ dec( pseudo.index(d), pseudo.index(key[k]) )]
                k = (k+1)%p
            elif d == '-' or d == '.':# or d == '/':
                strn += ' '
            elif d != chr(65279) and d not in exclude:
                strn += d
            q += 1
    print(strn)

def viggery(fl, ln):
    fn = fl + ".txt"
    file = open(fn, 'r', encoding="utf8")
    #array of strings for each skip set
    arry = []
    for n in range(0, ln):#+1?
        arry.append("")

    q = 0

    for c in file:#lines
        for d in c:
            if d in pseudo:
                arry[ q%ln ] += d
                q += 1

    ioct = 0
    for vv in arry:
        if len(vv) == 0: continue
        #print(vv)
        #ioc i guess
        arrayn = []
        for m in pseudo:
            arrayn.append(0)

        for char in vv:
            #it's all pseuds
            arrayn[ pseudo.index(char) ] += 1

        ioc = 0
        N = len(vv)
        for cc in arrayn:
            ioc += (cc/N) * ((cc-1)/(N-1))
        ioct += ioc

    print( ioct / 29 )
    


#convertdecf('02-03')
#convertdec('02-03f', "DIVINITY")#confirmed functional cipher-key pair


for n in range (2,14):
    print(n)
    viggery('srpages/02-03f',n)
    print('')

#convertdecf('13-14')
#convertdec('13-14f','FIRFVMFERENFE')#confirmed


for n in range (5,17):
    print(n)
    viggery('srpages/13-14f',n)
    print('')

for n in range(2,30):
    print(n)
    viggery('bpages/00seclt 60',n)
    print('')
