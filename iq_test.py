def iq_test(numbers):
    list1 = []
    list2 = []
    aa = numbers.split(" ")
    for b in aa:
        if int(b)%2==0:
            list1.append(b)
        elif int(b)%2!=0:
            list2.append(b)
    if len(list1)==1: return aa.index(list1[0])+1
    return aa.index(list2[0])+1
    


print(iq_test("1 2 1 1"))