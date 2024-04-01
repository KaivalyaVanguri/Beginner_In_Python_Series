string = '  kaIVALya LoVes chocOLates {} LoVes  '
print('\nString Functions\n')
a = string.capitalize()
print(a)
b = string.casefold()
print(b)#*in c function requires two parameters,the width and fill 
c = string.center(8,'h') #character latter must be one character long
print(c)
d = string.count('a')#this function requires atleast one parameter
print('p',d)
e = string.encode() 
print('ENCODE',e)
print(string.endswith('a',2,10),string.endswith(' '))
f = string.expandtabs(8)#def tab size is 8
print('Tab Size is 8',f)
g = string.find('h')#print(string.format_map(26)) map takes
print('print',g,string.rfind('IVAL',2,32))#exactly one argument
print(string.format(g))
h = string.index('e',2,26)#if the substring not present
print(h,string.rindex('c',10,30)) #value error appears
print(string.isalnum(),string.isalpha(),string.isascii())
print(string.isdecimal(),string.isdigit(),string.isidentifier())
print(string.islower(),string.isnumeric(),string.isprintable())
print(string.isspace(),string.istitle(),'UPPER',string.isupper())
i = string.join('more')
print(i)#it joins one char at a time requires atleast one int
print(string.ljust(40,'S'))# argument length
print(string.lower(),string.rjust(40,'V'))
print(string.lstrip(),string.lstrip('k'))#*
j = string.partition(' LoVes ') #*print(string.maketrans(''))
print(j,string.rpartition(' LoV'))
k = string.replace('LoVes','HaTes',1)#*
print(k)
l = string.split()
print(l,string.rsplit('{}',2))
m = string.strip()
print('printtt',m,string.rstrip(),string.splitlines(), string.splitlines(True))
print(string.startswith(''))
print(string.swapcase())
n = string.title()
print(n, string.upper()) #string.translate()
o = string.zfill(39)
print(o)#if the value is less than len of string no filling is done 
