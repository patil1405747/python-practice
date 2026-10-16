#string

s="python"
print(s[0])
print(s[-1])
print(len(s))

s="kiran"
x=s
s=s +"academy"
print(x)
print(s)

s="python"
print(s[-2])
print(s[3])

s="academy"
print(s[0] +s[-1])
print(s[2] +s[-3])

s="python"
s[0] ="j"
print(s)

#indexing and slicing

s="kiranacademy"
print(s[0:5])
print(s[5:])
print(s[:5])

s="kiranacademy"
print(s[::2])
print(s[1::2])

s="python"
print(s[::-1])
print(s[-1::-2])

s="kiranacademy"
print(s[-2:1:-2])

s="abcdefghij"
print(s[8:2:-2])
print(s[2:8:2])

#string inbuilt methods

s="python programming"
print(s.upper())
print(s.capitalize())
print(s.title())

s=" python "
print(len(s.strip()))
print(s.strip())

s="java python java"
print(s.find("python"))
print(s.find("sql"))

s="kiran academy"
print(s.replace("academy", "classes"))
print(s.lower())

s="java, python,sql"
x=s.spilt(",")
print(x)
print(x[1])

#expert/tricky strings
s="python"
print(s[5:1:-2])
print(s[1:5:2])

s="kiranacademy"
print(s[-1:-8:-2])
print(s[3::-3])

s="pythonprogramming"
print(s.lower()[::-2])

s=" kiran academy "
print(s.strip().title().replace(" ", "_"))

s="banana"
print(s.sfind("a"))
print(s.rfind("a"))
print(s.count("an"))



