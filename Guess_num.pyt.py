import random

def getSum(n): 
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum


PRNG=random.randint(1000,9999);
total_PRNG=getSum(PRNG);




for i in range(0,5):
    n = random.randint(1,30)


for attempt in range(1,10):
    print('Attempt',attempt);
    x=input('Guess and Enter a Random number:');
    total_X=getSum(x);
    
    if((x==PRNG)&&(total_PRNG==total_X))
        print('R')

    if(x!=PRNG)
        if(total_PRNG==total_X)









