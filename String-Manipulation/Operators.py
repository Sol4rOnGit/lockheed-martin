string = "Hello World!"
stringNum = "4 5 185 310"

#  ---- .SPLIT() ----

print(string.split())
#Cut a string list by whitespace... or:

new = "Ha.Ha" 
print(new.split("."))
#split by a "Determiner", the full stop sign for example

#.lstrip() and .rstrip() for each side

# ---- .REPLACE() ----
helloWorld = "Hello World"
helloWorld.replace("world", "Python") #Replaces every "world" with Python

new = "peas are better than carrots. Type peas if you agree"
new.replace("peas", "potatoes")
print(new)

# ---- .JOIN() ----

separator = " "
helloWorld = separator.join("Hello World")
print(helloWorld)