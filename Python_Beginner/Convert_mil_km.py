n = int(input("choose a number:\n1 Miles to Kilometres\n2 Kilometres to Miles\n"))
if(n==1):#miles to kilometres
  mls = int(input("please enter miles"))
  print("1 mile = 1.6093 kms")
  print(mls*1.6093,"kilometres")
  
if(n==2):#kilometres to miles
  kms = int(input("please enter kms: "))
  print("1 km = 0.621 miles")
  print(kms*0.621,"miles")
