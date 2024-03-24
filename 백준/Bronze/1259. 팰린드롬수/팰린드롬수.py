while(True) :
  num1 = input()

  if num1 == "0" :
    break
  elif num1 == num1[::-1] :
    print("yes")

  else :
    print("no")
