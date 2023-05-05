import random

wordic = {'L1': ['A', 'I'],
          'L2': ['TO', 'BE', 'tE', 'DO', 'OR', 'IS', 'OF', 'IT', 'AN', 'WE', 'GO', 'HE', 'AM', 'SO', 'BY', 'IF', 'VS', 'IN', 'MY', 'NO', 'ON'],
          'L3': ['tIS', 'YOV', 'D)t', 'NOT', 'FOR', 'ALL', 'ARE', 'tgS', 'END', ')SY', 'BVT', 'WHO', 'WAY', 'ONE', 'AND', 'tAT', 'OVR', 'GOg', 'MAY', 'BEg', 'LAW', ')CH', 'OWN', 'MAN', 'WIt', 'HIS', 'WAS', 'SAY', 'OFF', 'LOg', 'tEN', 'DAY', 'TOO', 'TWO', 'NOW', 'W)C', 'tEM', 'CAN', 'tVS', 'H)D', 'WEB', 'OVT'],
          'L4': ['NOtg', 'FROM', 'BOOC', 'WHAT', 'CNOW', 'TRVE', 'TEST', 'FIND', 'YOVR', 'TRVt', 'EDIT', 'tEIR', 'SOME', 'VOID', 'FORM', 'GR)T', 'TRIP', 'tOSE', 'HERE', 'ALOg', 'WILL', 'SELF', 'DEEP', 'LICE', 'ONLY', 'VNTO', 'HOLY', 'COAN', 'WENT', 'DOOR', 'TOLD', 'NAME', 'MORE', 'BODY', 'tINC', 'ELSE', 'COME', 'FOVR', 'LOSS', 'tREE', 'MVCH', 'HAVE', 'tERE', 'LVCC', 'NEED', 'MOST', 'WORt', 'LOSE', 'GAIN', 'W)Lt', 'MIND', 'DVRg', 'SAID', 'WHEN', 'M)NT', 'DONT', 'HAND', 'TELL', 'JVST', 'WERE', 'PAGE', 'DVTY', 'SEEC', 'MVST', 'SHED'],
          'L5': ['WARNg', 'CHAgE', 'WItIN', 'EItER', 'WORDS', 'CABAL', 'SHAPE', 'LIVES', 'STVDY', 'ASCED', 'AGAIN', 'HVMAN', 'AFTER', 'GETTg', 'COVLD', 'ANYtg', 'PAVSE', 'WHICH', 'CAVSE', 'STROg', 'LATER', 'DOGMA', 'BELOg', 'RIGHT', 'R)SON', 'ABOVT', 'AMASS', 'NEVER', 'VOICE', 'OtERS', 'EVERY'],
          'L6': ['EXCEPT', 'SACRED', 'WISDOM', 'PRIMES', 'SHOVLD', '(tER)L', 'CARNAL', 'MOBIVS', 'ANALOG', 'TOWARD', 'R)LITY', 'tROVGH', 'ARRIVE', 'INSTAR', 'EMERGE', 'WIDSOM', 'MASTER', 'WISHES', 'CALLED', 'tOVGHT', 'MOMENT', 'MERELY', 'ERRORS', 'ENOVGH', 'OBTAIN', 'FOLLOW', 'BECOME', 'LESSON', 'INSIDE', 'RAISED', 'IMPOSE', 'EXISTS', 'HASHES'],
          'L7': ['BELIEVE', 'MESSAGE', 'NVMBERS', 'TOTIENT', 'FVNCTiN', 'SHADOWS', 'BVFFERS', 'OBSCVRA', 'WELCOME', 'PILGRIM', 'JOVRNEY', 'SVFFERg', 'OVTSIDE', 'COMMAND', 'DECIDED', 'STVDENT', 'REPLIED', 'FINALLY', 'SPECIES', 'STARTED', 'TRAILED', 'CONSVME', 'BECAVSE', 'BELEIVE', 'FOLLOWg', 'CONSVMg', 'DESTROY', 'PROGRAM', 'EXPLAIN', 'STOPPED', 'CWESTiN', 'PARABLE', 'TVNNELg', 'SVRFACE'],
          'L8': ['MOVRNFVL', 'STRVGGLE', 'ILLVSiNS', 'DISCOVER', 'R)LITIES', 'YOVRSELF', 'CONFVSED', 'ANSWERED', 'INHABITg', 'DIVINITY', 'BEHAViRS', 'DECEPTiN', 'PRESERVE', 'PRESERVg', 'ATTACHED', 'PREPARED', 'STVDENTS'],
          'L9': ['CNOWLEDGE', 'CONTAINED', 'ENCRYPTED', 'NECESSARY', 'INNOCENCE', 'CERTAINTY', 'OVRSELVES', 'PROFESSOR', 'ARBITRARY', 'IRRITATED', 'PRACTICES', 'ADHERENCE', 'PRIMALITY', 'EXPLAINED'],
          'L10': ['EXPERIENCE', 'VLTIMATELY', 'PILGRIMAGE', 'INSTRVCTiN', 'CONSVMPTiN'],
          'L11': ['VNR)SONABLE', 'PRESERVATiN', 'ENLIGHTENED'],
          'L12': ['INTELLIGENCE', 'CONSCiVSNESS'],
          'L13': ['CIRCVMFERENCE'],
          'L14': ['CIRCVMFERENCES']}
#lol



def lol(fn):
    file = open(fn + ".txt",'r')
    st = ""
    for m in file:
        st += m
    file.close()

    sn = st.split()
    #print(sn[0:9])

    #fun time
    sr = ""
    sevenflag = False
    for n in sn:
        match n[0]:
            case '7':
                sr += '7'#chance to transform next L1 into th...
                sevenflag = random.choice([False,False,True])
            case 'L':
                if n == 'L1' and sevenflag:
                    sr += ' t'#keep the spacing consistent for now
                    sevenflag = False
                #pick random from...
                else:
                    sr += random.choice(wordic[n])
            case '-':
                if not sevenflag: sr += ' '
            case _:
                sr += n + ' '
    print(sr)

lol('08L')
