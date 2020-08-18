# python3
#my solution
def max_pairwise_product(numbers):
    n=len(numbers)
    maxNumber=0
    manNumber=0
    indexMax=0
    for nu in range(n):
        if numbers[nu]>=maxNumber:
            maxNumber=numbers[nu]
            indexMax=nu
    for nu in range(n):
        if numbers[nu]>manNumber and numbers[nu]<=maxNumber and nu!=indexMax:manNumber=numbers[nu]
    return maxNumber*manNumber

if __name__ == '__main__':  
    #input_numbers=[]    
    #for x in range(20):
    #    input_numbers.append(random.randint(1,100))
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))    
    print (input_numbers)