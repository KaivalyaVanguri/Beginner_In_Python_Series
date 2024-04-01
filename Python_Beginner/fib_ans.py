def calc_fib(n):
  count = 0
  i = 2
  a,b=0,1
  if n<=1:
	  return n
  while i<=n:
	  count = a+b
	  a,b = b,count
	  i += 1
  return count

n = int(input())
print(calc_fib(n))