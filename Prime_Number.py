# This function is designed to find prime numbers up to a given number n. A prime number is a number greater than 1 that can only be divided by 1 and itself (for example, 2, 3, 5, 7, etc.).
def find_primes(n):#n: The upper limit (exclusive) up to which we want to find prime numbers.
    primes=[]#Initialize an empty list called primes to store the prime numbers.
    for num in range(2,n):
        is_prime=True
        for i in range(2,int(num**0.5)+1):#Now, check if num can be divided by any number between 2 and the square root of num
            if num %i==0:
                is_prime =False#If num is divisible evenly by any number i, then it’s not a prime number, so set is_prime = False and stop checking further by using break.
                break
            if is_prime:
                primes.append(num)
    return primes

print(find_primes(100))