# Typical Maury Show intro

print ('Hello and welcome to Maury!')
print ('What is your name?')
# for our string we use single quotation marks ‘ and not “. Always use single quotations for print

MyName = input()
# do not put a value in the the brackets of “input()” note that input means the user inputs their answer
# naming inputs like myAge we can identify it as whatever is easiest for us to recall whatever we’re classifying

print ('That is quite the name ' + str(len(MyName)) + ' letters.')
# our code begins in lower case and is consistent for “print”, none of them are spelt “Print” to avoid Syntax error, avoid uppercase at all times
# for quotes there is sometimes a space before or after the quotation when using an input like myName or str(int(myAge) + 1) for proper sentence structure
# adding inputs like myName or myAge as a part of the sentence you must include a “+” to incorporate into the bracket
# quotations do not include input but end before or after it, the input is never included into the quotation marks
# remember to close the bracket

print ('How old are you?')
MyAge = input ()
MyAge = int(MyAge)
# incorporating an integer we must identify it as so, if not then it will display an error because it is expecting a string


print ('Wow you will be ' + str(int(MyAge)+ 2) + ' in two next years')
# for us to add an integer into a string we must identify the integer as a string
# place int(myAge) + 1 into its own bracket and placing “str” to convert the integer so it can be identified by the editor as a string.


print ('It is nice to meet you ' + MyName + '. Why are you here today?')
input ()

print ('What is your girlfriends name?')
HerName = input ()

print ('How old is she?')
HerAge = input ()

print ('Well ' + MyName + ' hope you are comfortable, because ' + HerName + ' has been watching backstage this whole time. Common out!')
print ('Welcome ' + HerName + ', so is he really ' + str(int(MyAge) - int(HerAge)) + ' older than you?')
input ()


