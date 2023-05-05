#words, sans smaller ones

wordic = {#'L1': ['A', 'I'],
          #'L2': ['TO', 'BE', 'tE', 'DO', 'OR', 'IS', 'OF', 'IT', 'AN', 'WE', 'GO', 'HE', 'AM', 'SO', 'BY', 'IF', 'VS', 'IN', 'MY', 'NO', 'ON'],
          #'L3': ['tIS', 'YOV', 'D)t', 'NOT', 'FOR', 'ALL', 'ARE', 'tgS', 'END', ')SY', 'BVT', 'WHO', 'WAY', 'ONE', 'AND', 'tAT', 'OVR', 'GOg', 'MAY', 'BEg', 'LAW', ')CH', 'OWN', 'MAN', 'WIt', 'HIS', 'WAS', 'SAY', 'OFF', 'LOg', 'tEN', 'DAY', 'TOO', 'TWO', 'NOW', 'W)C', 'tEM', 'CAN', 'tVS', 'H)D', 'WEB', 'OVT'],
          #'L4': ['NOtg', 'FROM', 'BOOC', 'WHAT', 'CNOW', 'TRVE', 'TEST', 'FIND', 'YOVR', 'TRVt', 'EDIT', 'tEIR', 'SOME', 'VOID', 'FORM', 'GR)T', 'TRIP', 'tOSE', 'HERE', 'ALOg', 'WILL', 'SELF', 'DEEP', 'LICE', 'ONLY', 'VNTO', 'HOLY', 'COAN', 'WENT', 'DOOR', 'TOLD', 'NAME', 'MORE', 'BODY', 'tINC', 'ELSE', 'COME', 'FOVR', 'LOSS', 'tREE', 'MVCH', 'HAVE', 'tERE', 'LVCC', 'NEED', 'MOST', 'WORt', 'LOSE', 'GAIN', 'W)Lt', 'MIND', 'DVRg', 'SAID', 'WHEN', 'M)NT', 'DONT', 'HAND', 'TELL', 'JVST', 'WERE', 'PAGE', 'DVTY', 'SEEC', 'MVST', 'SHED'],
          'L5': ['WARNg', 'CHAgE', 'WItIN', 'EItER', 'WORDS', 'CABAL', 'SHAPE', 'LIVES', 'STVDY', 'ASCED', 'AGAIN', 'HVMAN', 'AFTER', 'GETTg', 'COVLD', 'ANYtg', 'PAVSE', 'WHICH', 'CAVSE', 'STROg', 'LATER', 'DOGMA', 'BELOg', 'RIGHT', 'R)SON', 'ABOVT', 'AMASS', 'NEVER', 'VOICE', 'OtERS', 'EVERY'],
          'L6': ['EXCEPT', 'SACRED', 'WISDOM', 'PRIMES', 'SHOVLD', '(tER)L', 'CARNAL', 'MOBIVS', 'ANALOG', 'TOWARD', 'R)LITY', 'tROVGH', 'ARRIVE', 'INSTAR', 'EMERGE', 'WIDSOM', 'MASTER', 'WISHES', 'CALLED', 'tOVGHT', 'MOMENT', 'MERELY', 'ERRORS', 'ENOVGH', 'OBTAIN', 'FOLLOW', 'BECOME', 'LESSON', 'INSIDE', 'RAISED', 'IMPOSE', 'EXISTS', 'HASHES'],
          'L7': ['BELIEVE', 'MESSAGE', 'NVMBERS', 'TOTIENT', 'FVNCTiN', 'SHADOWS', 'BVFFERS', 'OBSCVRA', 'WELCOME', 'PILGRIM', 'JOVRNEY', 'SVFFERg', 'OVTSIDE', 'COMMAND', 'DECIDED', 'STVDENT', 'REPLIED', 'FINALLY', 'SPECIES', 'STARTED', 'TRAILED', 'CONSVME', 'BECAVSE', 'BELEIVE', 'FOLLOWg', 'CONSVMg', 'DESTROY', 'PROGRAM', 'EXPLAIN', 'STOPPED', 'CWESTiN', 'PARABLE', 'TVNNELg', 'SVRFACE'],
          'L8': ['MOVRNFVL', 'STRVGGLE', 'ILLVSiNS', 'DISCOVER', 'R)LITIES', 'YOVRSELF', 'CONFVSED', 'ANSWERED', 'INHABITg', 'DIVINITY', 'BEHAViRS', 'DECEPTiN', 'PRESERVE', 'PRESERVg', 'ATTACHED', 'PREPARED', 'STVDENTS'],
          'L9': ['CNOWLEDGE', 'CONTAINED', 'ENCRYPTED', 'NECESSARY', 'INNOCENCE', 'CERTAINTY', 'OVRSELVES', 'PROFESSOR', 'ARBITRARY', 'IRRITATED', 'PRACTICES', 'ADHERENCE', 'PRIMALITY', 'EXPLAINED'],#, 'WORLDTREE', 'YGGDRASIL'],
          'L10': ['EXPERIENCE', 'VLTIMATELY', 'PILGRIMAGE', 'INSTRVCTiN', 'CONSVMPTiN'],
          'L11': ['VNR)SONABLE', 'PRESERVATiN', 'ENLIGHTENED'],
          'L12': ['INTELLIGENCE', 'CONSCiVSNESS'],
          'L13': ['CIRCVMFERENCE'],
          'L14': ['CIRCVMFERENCES']}

pseudo  = ["F", "V",  "t", "O", "R", "C", "G", "W", "H", "N", "I", "J",  "e", "P", "X",
           "S", "T", "B", "E", "M", "L",  "g",  "o", "D", "A",  "(", "Y",  "i",  ")"]

folder = 'bpages/'

def encr(strn, key):
    return pseudo[ (pseudo.index(strn) + pseudo.index(key))%29 ]

def decr(strn, key):
    return pseudo[ pseudo.index(strn) - pseudo.index(key) ]

def dekey(strn, key):
    return pseudo[ pseudo.index(key) - pseudo.index(strn) ]


def caesar_section(fn):#lol
    file = open(folder + fn + '.txt','r')
    text = ""
    for m in file:
        text += m
    file.close()

    #29 fucking arrays
    arreys = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]

    #perform some basic actions
    for char in text:
        if char in pseudo:
            for e in range(0,29):
                arreys[e] += decr(char, pseudo[e])
        else:
            for e in range(0,29):
                arreys[e] += char

    #brute
    for n in range(0,29):
        #for dic in wordic: for word in dic: arreys[n].find(word)...
        for dic in wordic:
            for word in wordic[dic]:
                if arreys[n].find(word) > 0:
                    print(n)
                    print(word)
    print("done")

def vig_section(fn, key):
    file = open(folder + fn + '.txt','r')
    text = ""
    for m in file:
        text += m
    file.close()
    k = 0
    q = len(key)

    #also 'rotate' key to try for it being part of a key, offset by skips, ...
    arreys = []
    for n in range(0,q):
        arreys.append('')
    
    for char in text:
        if char in pseudo:
            for m in range(0,q):
                arreys[m] += decr( char, key[(k+m)%q])
            k = (k+1)%q
        else:
            for m in range(0,q):
                arreys[m] += char
    #brute
    for n in range(0,q):
        #for dic in wordic: for word in dic: arreys[n].find(word)...
        for dic in wordic:
            for word in wordic[dic]:
                #next: surround word in dashes and dots...
                worb = ['-'+word+'-',
                        '.'+word+'-',
                        '-'+word+'.',
                        ' '+word+' ',
                        '.'+word+' ',
                        ' '+word+'.',
                    ]
                for worg in worb:
                    if arreys[n].find(worg) > 0:
                        print(key,fn,n,word)
    #print("done")

#some primes

def primal(fn):
    file = open(folder + fn + '.txt','r')
    text = ""
    for m in file:
        text += m
    file.close()
    k = 0
    q = len(key)#primes

    #this is just one string thankfully


######main#######

a = ['lt','tl','nt','tn']
b = ['00sec','03sec','08sec','15sec cut','23sec','27sec','33sec','40sec cut']

for n in b:
    for m in a:
        for wurd in wordic['L14']+wordic['L13']+wordic['L12']+wordic['L11']:
        #for wurd in wordic['L10']+wordic['L9']+wordic['L8']+wordic['L7']+wordic['L14']+wordic['L13']+wordic['L12']+wordic['L11']:
            vig_section(n+m,wurd)

vig_section('test','FIRFVMFERENFE')#cool
