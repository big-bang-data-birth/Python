'''
This is my father's: Azmat Bhatti's Math vision confirmed...

Try yourself, amazing fact.

This python program

The program will demonstrate the following,
1. Take an integer input from the user.
2. Make a number as combination of,
(a) Given number, followed by consecutive two consecutive integers, e.g. 10, 11, 12 => final number=101112
    or skipping the next integers by 2,3,... e.g.
    skip by 2		=> 	10, 12, 14 => 101214
    e.g. skip by 3	=>	10, 13, 16 => 101316
    e.g. skip by 10	=>	10, 20, 30 => 102030

Result: Check if the the final number is divisible by 3
'''

int_UserTyped = int(input("Enter Any Integer: "))
int_UserConsecutiveSkip = int(input("Input Skipping Consecutive Integers By ? (Default = 1): "))

int_NextNumber_1=int_UserTyped+int_UserConsecutiveSkip
int_NextNumber_2=int_NextNumber_1+int_UserConsecutiveSkip

print("Three consecutive Numbers Are: " + str(int_UserTyped)+ ","+ str(int_NextNumber_1)+ ","+ str(int_NextNumber_2))

if(int_UserTyped < 1):
  str_Numbers_Combined_In_Sequence = "-"+str(int_UserTyped*-1)+str(int_NextNumber_1*-1)+str(int_NextNumber_2*-1)
else:
  str_Numbers_Combined_In_Sequence = str(int_UserTyped)+str(int_NextNumber_1)+str(int_NextNumber_2)


print("The combined integer to test = " + str_Numbers_Combined_In_Sequence +"\n\n")

int_Numbers_Combined_In_Sequence=int(str_Numbers_Combined_In_Sequence)

Quotient	=	int_Numbers_Combined_In_Sequence / 3
Remainder	=	int_Numbers_Combined_In_Sequence % 3

print(str_Numbers_Combined_In_Sequence+" / 3 => " + "Quotient = " + str(Quotient) + ", Remainder = " + str(Remainder) )
