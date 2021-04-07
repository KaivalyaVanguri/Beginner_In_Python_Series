def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
n = int(input('Enter a number for perfect number, a perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself.'))
print(perfect_number(n))