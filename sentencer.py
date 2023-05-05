

folder = 'runepages/'
def sent(fn):
    #open file etc
    file = open(folder + fn + '.txt','r',encoding="utf8")
    text = ""
    for m in file:
        text += m
    file.close()

    #strip certain chars...
    things = ""
    for char in text:
        if char not in ['\n','/']:#and others...
            things += char

    fings = things.split('.')

    n = 0
    for fing in fings:
        print(fn, str(n), fing + '.')#and number
        n += 1



sent('sect03')
