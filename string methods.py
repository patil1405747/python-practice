#string methods

#capitalize
name="gayatri"
print(name.capitalize()) #it used to convert first character into upper case

#casefold
name="anuja"
print(name.casefold())#casefold() method converts a string into lowercase more aggressively

#upper
name="muttu"
print(name.casefold())#casefold() it is used to convert string into uppercase

#lower
name="sangeetha"
print(name.lower())#it is used to convert string into loewr case

#islower
name="swati"
print(name.islower())# it return result in true or false

#index
name="shubhangi"
print(name.index())# it return index position of a string character

#isalnum
age="sa22"
print(name.isalnum())# it check value and return true if value is alhabets or numeric

#isnumeric
age=22
print(name.isnumeric())#it check value and return if a value is numeric

#title
text="python"
print(name.title())# capitalizes the first letter of evrery word

#count
name=input("enter your name:")
print(name.count("a"))#it return count of specific character of string
      
#endwith
name="gayatri patil"
print(name.endwith("patil"))#it check string ending value

#replace
name="gayatri patil"
print(name.replace("gayatri","swati"))# it used to replace values with variable value

#startwith
name="sangeetha muttu"
print(name.startswith("sangeetha"))#it check starting value of a string

#how to print output
name="gayatri"
city="pune"
print("my name is " ,name,"my city is",city)
print("my name is {name} ,my city is {city}")
