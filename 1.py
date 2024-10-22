	#1. Given a positive integer, write a program to calculate the difference between the sum of digit at odd position and the sum of digit at even position. The position counting starts from 1(rightmost is position 1). You must not convert the number into a string at any point.
	#• Taken  an input (positive integer)
	#• Print x-y where, x=sum of odd digit and y= sum of even digit
	#• NOTE:- Position start from 1
	#• Sample Input=12345
	#• x=Odd=3+5+1=9
	#• y=Even=2+4=6
	#• x-y=3
 
 
#using integer method	
'''n=int(input())
oddSum,evenSum=0,0
temp=n
pos=1

while temp>0:
    digit=temp%10
    
    if pos&1:
        oddSum=oddSum+digit
        pos=pos+1
    else:
        evenSum=evenSum+digit
        pos=pos+1
    temp=temp//10
print(oddSum-evenSum)'''



#using string method

'''n=input()
oddSum,evenSum=0,0
for i, digit in enumerate(n[::-1],1):
    if i %2==1:
        oddSum+=int(digit)
    else:
        evenSum+=int(digit)
        
print(oddSum-evenSum)'''
