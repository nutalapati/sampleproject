# if-else if ladder example
rank = int (input('enter your rank:'))
if (rank == 37400):
    print ('you are eligible for college 1 ')
elif(rank<=1000):
    print('you are eligible for college 2')
elif(rank>=1000 and rank<=10000):
    print ('you are eligible for college 3')
elif(rank>=10000 and rank<=40000):
    print ('you are eligible for college 4')
else:
    print ('sorry no college available for you')
        