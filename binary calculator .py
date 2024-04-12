#Abdullah Islam Fathy Ibrahim    20230225      
#Ibrahim Sayed Muhammed Hamza    20230002  
def check_if_binary(w) :  #a function to make sure that the number given by the user can be only binary 
  while True :         #"W" is the number that the function checking if it's binary and it will be changed by the user if it was not 
    for i in w : 
      if i == '0' or i == '1' :
        z = True
      else : 
        z = False    
        break   
    if z == False : 
      print("please insert a valid binary number")    
      w = input()
    elif z == True :
     break
  return w    
    
def ones_complement(t) :     #a function that computes the first complement to b binary number "only if the number is binary"
  string = "" 
  for i in range(0 , len(t)):
        if t[i] == "1":
            string += "0"
        else :
            string += "1"
  return string

def addition_between_binary(num1, num2):  #a function that add two binary numbers (num1,num2)
    num1 = int(num1)
    num2 = int(num2)
    result = ""
    carry = 0
    while num1 != 0 or num2 != 0:
        x = num1 % 10
        y = num2 % 10
        w = x + y + carry
        carry = w // 2
        result += str(w%2)
        num1 //= 10
        num2 //= 10
    if carry :
        result += str(carry)  
    result = result[::-1]
    return result

def twos_complement(num1) :
  num1 = ones_complement(num1) 
  num1 = addition_between_binary(num1,1) 
  return num1 

def subtraction_between_binary(num1,num2) :  #a function that subtract two binary numbers (num1,num2)
   if len(num1) > len(num2) :                #this function subtract num2 - num1 (if num1 was bigger than num2 the result will be invalid)
     num2= num2[::-1]                        #num2 must be bigger than num1 !!!!!
     while len(num1) > len(num2) :
       num2 += '0' 
     num2 = num2[::-1] 
   elif   len(num2) > len(num1) :
     num1= num1[::-1]
     while len(num2) > len(num1) :
       num1 += '0'
     num1 = num1[::-1] 
   num1 = twos_complement(num1)                              
   x = addition_between_binary(num1,num2)                 
   if len(x) > len(num1) or len(x) > len(num2) :            
     x = str(x)                                               
     x = x[1:]                                                     
   return x                                               

 


 


    ####   main program   ####



print("** binary calculator **")
while True :
  print("A) Insert new numbers")
  print("B) Exit")
  x = input()                    #x is just a variable to know if the user wants to continue or exit 
  if x == 'B' or x == 'b' :
     break 
  elif x == 'A' or x == 'a' :
      print("please insert a number")
      num1 = input()             #num1 is a binary number given by the user that we will make the operation on 
      num1 = check_if_binary(num1)
           
      print("** please select the operation **")
      print("A) Compute one's complement")
      print("B) Compute two's complement")
      print("C) addition")
      print("D) subtraction")
      while True :
       y = input()     #y is also just a variable to know what operation the user want to do 
       if y == 'A' or y == 'a' :
        print(ones_complement(num1)) 
        break
       elif y == 'B' or y == 'b' :
        print(twos_complement(num1))
        break
       elif y == 'C' or y == 'c' :
        print("please insert the second number") 
        num2 = input()      #num2 is the number that will be added to num1 s
        num2 = check_if_binary(num2)
        print(addition_between_binary(num1,num2))
        break
       elif y == 'D' or y == 'd' : 
        print("please insert the second number")
        num2 = input()       #num2 here is the number that num1 will be subtract from
        num2 = check_if_binary(num2)
        print(subtraction_between_binary(num1,num2))
        break
       else : 
        print("please select a valid choice")   
        
      
  else :
   print("please select a valid choice")
print("")
