runes = ["ᚠ", "ᚢ", "ᚦ", "ᚩ", "ᚱ", "ᚳ", "ᚷ", "ᚹ", "ᚻ", "ᚾ", "ᛁ", "ᛄ", "ᛇ", "ᛈ", "ᛉ", "ᛋ", "ᛏ", "ᛒ", "ᛖ", "ᛗ", "ᛚ", "ᛝ", "ᛟ", "ᛞ", "ᚪ", "ᚫ", "ᚣ", "ᛡ", "ᛠ"]
letters = ["F", "V", "th", "O", "R", "C", "G", "W", "H", "N", "I", "J", "eo", "P", "X", "S", "T", "B", "E", "M", "L", "ng", "oe", "D", "A", "ae", "Y", "ia", "ea"]
pseudo  = ["F", "V",  "t", "O", "R", "C", "G", "W", "H", "N", "I", "J",  "e", "P", "X", "S", "T", "B", "E", "M", "L",  "g",  "o", "D", "A",  "(", "Y",  "i",  ")"]
#pseudo  = ["F", "V",  "#", "O", "R", "C", "G", "W", "H", "N", "I", "J",  "@", "P", "X", "S", "T", "B", "E", "M", "L",  "&",  "0", "D", "A",  "(", "Y",  "!",  ")"]
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109]

word = "DIVINITY"#pseudo
word2="CIRCVMFERENCE"
chunk= "ᚢᛠᛝᛋᛇᚠᚳᚱᛇᚢᚷᛈᛠᛠ-ᚠᚹᛉ/"#welcome welcome pil, key divinity

exclude = "abcdefABCDEF1234567890\n&%/"

#since numerical values are sent in, this is alp-agnostic
def enc(strn, key):
    return (strn+key)%29

def dec(strn, key):
    return(strn-key +29)%29

def atb(strn):
    return(28-strn)

def runestopseudo(strn):
    q = len(strn)
    st = ""
    for n in range(0,q):
        if strn[n] in runes:
            st += pseudo[ runes.index( strn[n] ) ]
        else:
            st += strn[n]
    return st


#lmao why
class m:
    PSEUDO = 0
    RUNE = 1
    NUMBER = 2

def matcher(mm):
    match mm:
        case m.PSEUDO:
            return pseudo
        case m.RUNE:
            return runes
        #case m.NUMBER:
            #hmm


def simpledecode(strn, key, inp = m.PSEUDO, kt = m.PSEUDO, oup = m.PSEUDO):
    p = len(key)
    k = 0
    q = len(strn)
    st = ""
    
    inpt = matcher(inp)
    keyt = matcher(kt)
    outp = matcher(oup)
    
    #strip key of non-keyt chars

    for n in range(0,q):
        if strn[n] in inpt:
            b = inpt.index(strn[n])
            c = keyt.index(key[k])
            st += outp[dec(b,c)]
            k = (k+1)%p
        else:
            st += strn[n]

    return st

#the same except call enc
def simpleencode(strn, key, inp = m.PSEUDO, kt = m.PSEUDO, oup = m.PSEUDO):
    p = len(key)
    k = 0
    q = len(strn)
    st = ""
    
    inpt = matcher(inp)
    keyt = matcher(kt)
    outp = matcher(oup)
    
    #next: strip key of non-keyt chars

    for n in range(0,q):
        if strn[n] in inpt:
            b = inpt.index(strn[n])
            c = keyt.index(key[k])
            st += outp[enc(b,c)]
            k = (k+1)%p
        else:
            st += strn[n]

    return st


#extract key from vig, p to p
#nonchars in both strings need to be considered, formatting of strn is kept
def dekey(strn, crib):
    p = len(crib)
    c = 0
    q = len(strn)
    st = ""

    for n in range(0,q):
        while c < p-1 and crib[c] not in pseudo:
            c += 1
        if c == p:#fix this
            return st

        if strn[n] in pseudo:
            b = pseudo.index(strn[n])
            b -= pseudo.index(crib[c]) + 29
            b %= 29
            c += 1
            st += pseudo[b]
        #else:
            #st += strn[n]

def simpleatbash(strn, inp = m.PSEUDO, oup = m.PSEUDO):
    q = len(strn)
    st = ""
    
    inpt = matcher(inp)
    outp = matcher(oup)

    for n in range(0,q):
        if strn[n] in inpt:
            st += outp[atb(inpt.index(strn[n]))]
        else:
            st += strn[n]
        #print(st)
    return st


def convertatbpg(fl, plus = 'F'):
    fn = "srpages/" + fl + ".txt"
    file = open(fn, 'r', encoding="utf8")
    strn = ""

    for c in file:#lines
        for d in c:
            if d in runes:
                strn += simpledecode( simpleatbash( d, m.RUNE ), plus)
            elif d == '-' or d == '.':
                strn += ' '
            elif d != chr(65279) and d not in exclude:
                strn += d
    print(strn)

def convertrtp(fl):
    fn = "srpages/" + fl + ".txt"
    file = open(fn, 'r', encoding="utf8")
    strn = ""

    for c in file:#lines
        for d in c:
            if d in runes:
                strn += pseudo[runes.index(d)]
            elif d == '-' or d == '.':
                strn += ' '
            elif d != chr(65279) and d not in exclude:
                strn += d
    print(strn)

def convertdecf(fl, key):
    fn = "srpages/" + fl + ".txt"
    file = open(fn, 'r', encoding="utf8")
    strn = ""
    p = len(key)
    k = 0
    q = 0

    for c in file:#lines
        for d in c:
            if d == 'ᚠ' and q in [62,102,115,181,217,218,333,565,595,624,688,68,81]:
                strn += 'F'
            elif d in runes:
                strn += pseudo[ dec( runes.index(d), pseudo.index(key[k]) )]
                k = (k+1)%p
            elif d == '-' or d == '.':# or d == '/':
                strn += ' '
            elif d != chr(65279) and d not in exclude:
            #d!= '\n' and d != '/'and d != '&'and d != '%':
                strn += d
            q += 1
    print(strn)

someprimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
          67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137,
          139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
          211, 223, 227, 229, 233, 239, 241, 251, 257, 263,1, 269, 271, 277,
          281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359,
          367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443,
          449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541,
          547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619,
          631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719,
          727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821,
          823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911,
          919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

def convertprimes(fl):
    fn = "srpages/" + fl + ".txt"
    file = open(fn, 'r', encoding="utf8")
    strn = ""
    k = 0
    
    for c in file:#lines
        for d in c:
            if d in runes:
                strn += pseudo[ dec( runes.index(d), someprimes[k]-1 )]
                k += 1
            elif d == '-' or d == '.':# or d == '/':
                strn += ' '
            elif d != chr(65279) and d not in exclude:
            #d!= '\n' and d != '/'and d != '&'and d != '%':
                strn += d
    print(strn)
            






#print( simpleatbash( 'ᚱ-ᛝᚱᚪᛗᚹ.ᛄᛁᚻᛖᛁᛡᛁ-ᛗᚫᚣᚹ-ᛠᚪᚫᚾ-/', m.RUNE) )
convertatbpg('01')
print('')
convertrtp('04')
print('')
convertdecf('02-03', word)#divinity
print('')
convertatbpg('05-08', 'Y')
print('')
convertrtp('09-12')
#FIRFVMFERENFE 
print('')
convertdecf('13-14', 'FIRFVMFERENFE')
print('')
convertrtp('15')
print('')
convertprimes('56')
print('')
convertrtp('57')





