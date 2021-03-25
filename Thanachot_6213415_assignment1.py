number = {"0":"zero", "1":"one", "2":"two", "3":"three", "4":"four", "5":"five", "6":"six", "7":"seven", "8":"eight", "9":"nine" }
phone = input("Please input your phone number >> ")

##print(number[phone[0]], number[phone[1]], number[phone[2]], number[phone[3]], number[phone[4]], number[phone[5]], 
       ## number[phone[6]], number[phone[7]], number[phone[8]], number[phone[9]])
i = 0
for i in range(10) :
    print(number[phone[i]])
    i+=1

#Thanachot Thavornmongkol