user = input("Enter comma seperated binary digits : ")
list1 = user.split(",")
list2 = []
i = 0
while(i<len(list1)):
    if(list1[i] == "1010" or list1[i] == "0101" or list1[i] == "1111"):
        list2.append(list1[i])

    i += 1
print(' '.join(list2))