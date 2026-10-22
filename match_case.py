marks=80

match marks:
    case 40|50|60|70|75|55:
        print(" Grade A")
    case 50|60|70|75|65:
        print(" Grade B")
    case 30|35|40|45|50|60|65|70:
        print(" Grade C")
    case 40|50|60|70|75:
        print("Grade D")
    case 32|45|67|77:
         print("Invaild Input")   

Quater=12

match  Quater :
    case 1:
        print("Jan, Feb, Mar")
    case 2:
        print("Apr, May, Jun")
    case 3:
       print("Jul, Aug, Sep")
    case 4:
        print("Oct, Nov, Dec")
    case _ :
        print("Invaild Input")

#marks for grade
grade="A"
match grade:
 case "A":
  print("marks between 90 to 100")
 case "B":
   print("marks between 80 to 99")
 case "C":
  print("marks between 70 to 89")
 case "D":
  print("marks between 60 to 79") 
 case "E":
  print("marks between 50 to 69")
 case _:
  print("marks below 50")      
                
#taffic signal
color="Red" 
match color.lower():
 case "red" : 
  print("stop")
 case "yellow":
  print("ready to go")
 case "green":
  print("go")
 case _:
  print("invalid output") 

color="Red" 
match color.replace("Red","yellow"):
 case "red" : 
  print("stop")
 case "yellow":
  print("ready to go")
 case "green":
  print("go")
 case _:
  print("invalid output")   


day=3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6 | 7:
        print("Weekend!")
    case _:
        print("Invalid day")

# airthmetic operator

num1=20
num2=10
operator="+"
match operator:
   case"+":
        print("Addition result:", num1+num2)
   case"-":
        print("Substraction result:", num1-num2)
   case"*":
         print("Multification result:", num1*num2)
   case"/":
          print("Division result:", num1/num2)
   case"%":
           print("Module result:", num1%num2)
   case _ :  
      print("Invaild Airthmetic operator") 

status = 404

match status:
    case 200:
        print("Success")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown Status")          

stream = "BCA"
match stream.upper():
    case "BCA" | "BSC":
        print("Computer & Science Field")
    case "BCOM" | "BBA":
        print("Commerce Field")
    case "BA":
        print("Arts Field")
    case _:
        print("Unknown Course")  

fruit = "apple"
match fruit:
    case "apple":
        print("Red")
    case "banana":
        print("Yellow")
    case _:
        print("Unknown fruit")
          