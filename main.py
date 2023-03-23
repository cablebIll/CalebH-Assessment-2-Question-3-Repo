userChoice = input('for ascii to unicode type "a"\nfor unicode to ascii type "b"\n') #ask user to select which conversion
if userChoice == 'a' or userChoice == 'A':
    inputString = input('type the string you want converted:\n') #specific instructions for each conversion
elif userChoice == 'b' or userChoice == 'B':
    inputString = input('type the string you want converted with each codepoint seperated by a space\ne.g. 97 98 99 100\n') 
    #specific instructions for each conversion
def convert():
    if userChoice == 'a' or userChoice == 'A':#if user selected ascii to unicode do...
        unicodeString = '' #initialize string for converted unicode
        for i in inputString: #do process for each value in string
            i = ord(i) #do the conversion
            unicodeString += ' ' #add a space between each value in the conversion for clarity
            unicodeString += str(i) #add converted value to the output string
        return unicodeString    #return output string to convert() function
    elif userChoice == 'b' or userChoice == 'B': #if user selected unicode to ascii do...
        inputList = inputString.split() #initialize list containing each value user wants converted
        ASCIIlist = [] #initailize string that will contain converted data
        for i in inputList: #for each entry in list do...
            if i.isnumeric() == False: #check if the value is a number
                print('invaid input') #provide error message
                quit() #quit the program
            if int(i) not in range(1,1114111): #check if the value is in the convertable range
                print('invalid input') #provide error message.
                quit() #quit
            ASCIIlist.append(chr(int(i))) #add converted value to output list
            ASCIIstring = ' '.join(ASCIIlist)#create a string with the values of the output list
        return ASCIIstring #return output string to the convert() function
    else: #if user did not select a or b do this...
        print('please select a valid option')# provide error message
        quit() #quit program
    
convert()

print(f'{inputString} was converted to {convert()}')
