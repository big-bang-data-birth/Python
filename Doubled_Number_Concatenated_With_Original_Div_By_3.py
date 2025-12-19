'''
This is my father's: Azmat Bhatti's Math vision confirmed...

Try yourself, amazing fact.

This python program

The program will demonstrate the following,
1. Take an integer input from the user.
2. Double the number 
    e.g. 	3	=> 2*3 = 6
            10	=>	2*10= 20
            365 => 2*365=730
3. Concatenate the doubled number with original on left or right,
    e.g.	36			or 		63
            1020		or		2010
            365730		or		730365
            
Result: Check if the the final number is divisible by 3
'''

int_NumberGiven = int(input("Enter Any Integer: "))


int_NextNumber_Doubled=2*int_NumberGiven

str_NumberContatenatedWithDoubled_OnLeft=str(int_NextNumber_Doubled)+str(int_NumberGiven)
str_NumberContatenatedWithDoubled_OnRight=str(int_NumberGiven)+str(int_NextNumber_Doubled)

print("The Doubled Number: " + str(int_NextNumber_Doubled))

print("The Doubled Number, Concatenated With Original On Right= " + str_NumberContatenatedWithDoubled_OnRight+"\n\n")
int_NumberContatenatedWithDoubled_OnRight=int(str_NumberContatenatedWithDoubled_OnRight)
Quotient	=	int_NumberContatenatedWithDoubled_OnRight / 3
Remainder	=	int_NumberContatenatedWithDoubled_OnRight % 3
print(str_NumberContatenatedWithDoubled_OnRight+" / 3 => " + "Quotient = " + str(Quotient) + ", Remainder = " + str(Remainder) +"\n\n")


print("The Doubled Number, Concatenated With Original On Left= " + str_NumberContatenatedWithDoubled_OnLeft+"\n\n")
int_NumberContatenatedWithDoubled_OnLeft=int(str_NumberContatenatedWithDoubled_OnLeft)
Quotient	=	int_NumberContatenatedWithDoubled_OnLeft / 3
Remainder	=	int_NumberContatenatedWithDoubled_OnLeft % 3
print(str_NumberContatenatedWithDoubled_OnLeft+" / 3 => " + "Quotient = " + str(Quotient) + ", Remainder = " + str(Remainder) )


