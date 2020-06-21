userInput = input("Enter any string: ")

letterCount=0
digitCount=0

for letter in userInput:
    if letter.isdigit():
        digitCount=digitCount+1
    else:
        letterCount=letterCount+1
        
print("The Letter Count is: "+str(letterCount))
print("The Digit Count is: "+str(digitCount))