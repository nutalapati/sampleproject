# program to demonstrate input and output 
pin,cash = input('enter your pin and cash:').split('*')
print ('pin and cash are ', pin,cash)
cashAmount=int(cash)
print('type of cash is :',type(cashAmount))
atmValue = 50000
remainingAmount = atmValue - cashAmount
print ('take your cash 1000', cash ,remainingAmount,sep="->", end="======")
print ('thank you visit again')
