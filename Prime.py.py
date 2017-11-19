#Accept user input
user_input = int(input("please enter the number:"))

#Initialise two variables. K is a switch and i is an incrementor
k=0
i=2
#While incrementor is less than the user input data or till the swicth is turned off repeast the code within while loop 
#check whether the reminder is zero after dividing user input with each incremented values
#when the reminder is zero, stop checking the remoaning entries as the number is identified as  non prime
    
while(i<user_input and k<1):
    if (user_input%i==0 ):
        print("This is not a prime number")
        k=k+1
    i=i+1
#If the incremeontor exhausted and reached one less than the user input value, then it confirms that the user input is a prime number.  
if (k==0):    
    print("This is a prime number")