Number = int(input("\nEnter the Range Number: "))
First_number = 0
Second_number = 1
for Num in range(0, Number):
           if(Num <= 1):
                      Next = Num
           else:
                      Next = First_number + Second_number
                      First_number = Second_number
                      Second_number = Next
           print(Next)
           
Output:
Enter the Range Number: 5
0
1
1
2
3
