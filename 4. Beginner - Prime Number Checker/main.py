#Write your code below this line 👇
def prime_checker(number):
  veces = 0
  check = number - 1
  while check > 1:
    if number % check == 0:
      #print(f"{number} % {check} = {number % check}")
      veces += 1
    check -= 1

  if veces == 0:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



