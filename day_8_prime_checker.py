#Write your code below this line ๐
def prime_checker(number):
  divisor = 2
  while divisor <= number:
    if number % divisor == 0:
      break
    else:
      divisor += 1
  if(divisor == number):
    print(f' The number {number} is a prime.')
  else:
    print(f' The number {number} is not a prime.')
#Write your code above this line ๐
    
#Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)
