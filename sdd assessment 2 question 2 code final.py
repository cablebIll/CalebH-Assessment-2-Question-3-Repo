userChoice = input('for ascii to unicode type "a"\nfor unicode to ascii type "b"\n')
if userChoice == 'a' or userChoice == 'A':
    inputString = input('type the string you want converted:\n')
elif userChoice == 'b' or userChoice == 'B':
    inputString = input('type the string you want converted with each codepoint seperated by a space\ne.g. 97 98 99 100\n')

def convert():
    if userChoice == 'a' or userChoice == 'A':
        unicodeString = ''
        for i in inputString:
            i = ord(i)
            unicodeString += ' '
            unicodeString += str(i)
        return unicodeString    
    elif userChoice == 'b' or userChoice == 'B':
        inputList = inputString.split()
        ASCIIlist = []
        for i in inputList:
            if i.isnumeric() == False:
                print('invaid input')
                quit()
            ASCIIlist.append(chr(int(i)))
            ASCIIstring = ' '.join(ASCIIlist)
        return ASCIIstring
    else:
        print('please select a valid option')
        quit()
    
convert()

print(f'{inputString} was converted to {convert()}')