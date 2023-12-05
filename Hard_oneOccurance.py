number=13      #taking input

def oneOccurance(number):
    numberString=""            #Create an empty string
    for i in range(number+1):   #iterating the numbers from 0 to inut number 
        numberString+=str(i)           #adding all numbers to empty string created
    out=numberString.split("1")         #splitting string whenever number 1 occurs
    result=len(out)-1                   #returning number of items in list minus 1
    return result
result=oneOccurance(number)
print(result)