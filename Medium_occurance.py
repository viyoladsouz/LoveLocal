listOfNo=[1]        #taking input
def occurance(lists):
    dict={i:0 for i in lists}       #creating dictionary and initializing all item in the list to 0
    for i in lists:
        dict[i]+=1      #counting number of occurance of each number
    max=dict[1]         #
    for i in dict:
        if dict[i]>max:
            max=dict[i]
    out=[]
    for i in dict:
        if dict[i]==max:
            out.append(i)
    return out
result=occurance(listOfNo)
print(result)