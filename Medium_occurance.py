listOfNo=[1,2,3,2,3]        #taking input
def occurance(lists):
    dict={i:0 for i in lists}       #creating dictionary and initializing all item in the list to 0
    for i in lists:
        dict[i]+=1      #counting number of occurance of each number
    max=dict[1]         #initializing max to 1st item
    for i in dict: 
        if dict[i]>max:
            max=dict[i]     #finding maximum occurance
    out=[]
    for i in dict:
        if dict[i]==max:        
            out.append(i)       #adding numbers with maximum occurance to output list
    return out
result=occurance(listOfNo)
print(result)
