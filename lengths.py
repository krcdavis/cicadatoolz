#convert pages to length-coded pages

runes   = ["ᚠ", "ᚢ",  "ᚦ", "ᚩ", "ᚱ",  "ᚳ", "ᚷ", "ᚹ", "ᚻ", "ᚾ", "ᛁ",  "ᛄ",  "ᛇ",  "ᛈ", "ᛉ", "ᛋ", "ᛏ", "ᛒ", "ᛖ", "ᛗ", "ᛚ",   "ᛝ",  "ᛟ", "ᛞ", "ᚪ",  "ᚫ",  "ᚣ",  "ᛡ",  "ᛠ"]
letters = ["F", "V", "th", "O", "R", "C", "G", "W", "H", "N", "I", "J", "eo", "P", "X", "S", "T", "B", "E", "M", "L", "ng", "oe", "D", "A", "ae", "Y", "ia", "ea"]
pseudo  = ["F", "V",  "t", "O", "R", "C", "G", "W", "H", "N", "I", "J",  "e", "P", "X", "S", "T", "B", "E", "M", "L",  "g",  "o", "D", "A",  "(", "Y",  "i",  ")"]
#pseudo  = ["F", "V",  "#", "O", "R", "C", "G", "W", "H", "N", "I", "J",  "@", "P", "X", "S", "T", "B", "E", "M", "L",  "&",  "0", "D", "A",  "(", "Y",  "!",  ")"]
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109]

def convert(fn):
    file = open("ppages/" + fn + ".txt",'r')
    shnorg = ""
    for m in file:
        shnorg += m
    file.close()
    
    #length engine
    L = 0
    strn=""
    ex=""
    for n in shnorg:
        for m in n:
            if m in '12345':
                strn += m+': '
            elif m == '7':
                #sth
                strn += '7'
            elif m in pseudo:
                L += 1
            else:
                if m == '/' or m =='\n':#'/\n&'
                    continue
                elif L > 0:
                    #commit 'l'+str(l)
                    strn += 'L'+str(L)+' '
                L = 0
                #next
                #/ and \n are ignored
                if m in ".-/&%$":
                    strn += m+' '
                else:
                    ex += m
    print(fn)
    print(strn)
    print('')





convert('00sec')
convert('03sec')
convert('08sec')#7t

convert('15sec cut')
convert('23sec')
convert('27sec')

convert('33sec')#numbers 1-5
convert('40sec cut')
