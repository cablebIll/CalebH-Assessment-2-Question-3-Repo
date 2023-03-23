prompt user to select 'ascii to unicode' or 'unicode to ascii'.
prompt user to type the string they want converted

beginConvertFunction
  if user chose 'ascii to unicode':
    initialize an empty unicode string
    for each letter in the user's input string:
      convert the letter to unicode
      add the converted letter to the unicode string
    return the unicode string
  if user chose 'unicode to ascii':
    split the values from the input string into a new input list
    initialize an empty ascii list
    for every value in the input list do:
      if the value is not a number:
        print an error message
        quit program
      if the value is not within the convertable limits:
        print an error message
        quit program
      convert the value to ascii
      add the converted value to the ascii list
      create a string with the values from the ascii list
    return the created string
  if user did not choose either option:
    print an error message
    quit program
endConvertFunction

do convertFunction

print that the input string was converted to the output string and provide values for both