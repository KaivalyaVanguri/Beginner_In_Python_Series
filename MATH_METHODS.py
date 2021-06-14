import math 
print("\nMath functions\n")
a, b, c, d, e, f, g = 7, 5, -20, 10.0, 2.9, True, 4,
lis1 = [2,3,5,6,7]
print(math.acos(-1),math.acosh(1),math.asin(-1),math.asinh(2.45))
print(math.atan(-21),math.atan2(20,10),math.atanh(0.59))
print(math.cos(3.14159265359),math.cosh(8.90),math.sin(-1),math.sinh(1),math.tan(-90),math.tanh(-6.2))
print(math.ceil(-5.3),math.floor(-6.1),math.sqrt(g)) 
print(math.comb(a,b))#returns the number of ways of selecting k unordered outcomes from n possiblities without repetition-combinations
print(math.copysign(c,a),math.factorial(b))
print(math.degrees((math.pi)/4), math.radians(90))
#*print(math.dist(a,b))
print(math.erf(b),math.erfc(a),math.fabs(c),math.exp(b))#E^x
print(math.expm1(32),math.fmod(a,b),math.frexp(d))#E^x - 1
print(math.fsum(lis1),math.gamma(d),math.lgamma(d))
print(math.gcd(a,b),math.pow(b,g))#only int arguments
print(math.hypot(3,4),math.remainder(d,e))#int or float
print(math.isclose(d,e),math.isfinite(c),math.isinf(c),math.isnan(f))
#nan argument cant be a string or None but can be boolean 
print(math.isqrt(g),math.ldexp(e,g),math.lgamma(e))
print(math.log(d,10),math.log10(d),math.log1p(e),math.log2(e)) 
print(math.perm(7,5))#Returns the number of ways to choose k items from n items with order and without repetition
print(math.prod(lis1))
print(math.trunc(e))
print("\nMath Constants\n")
print(math.e)
print(math.inf)
print(math.nan)
print(math.pi)
print(math.tau)
