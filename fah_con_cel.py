n = int(input("Choose a number:\n1 Fahrenheit to celsius\n2 Celsius to Fahrenheit\n"))
if(n==1):
  fahrenheit = float(input("please enter temperature in fahrenheit "))
  celsius = (fahrenheit - 32)*5/9
  print(celsius,"celsius")

elif(n==2):
  celsius = float(input("please enter temperature in celsius "))
  Fahrenheit = (celsius*(9/5)) + 32
  print(Fahrenheit,"fahrenheit")
