#An example to dictionary 
dir0 = {id: 1, 'name':'Nora', 'size': 37}

# An empty dictionary 
dir0 = {}

#create a dictionary via dict() function
d1 = dict(id=1, name="Noor", size=37)
d2 = dict({"id": 1, "name": "Noor", "size": 37})
d3 = dict([("id", 1), ("name", "Noor"), ("size", 37)])
d4 = dict(zip(("id", "name", "size"), (1, "Noor", 37)))
print(d1)
print(d2)
print(d3)
print(d4)

#create a dictionary via fromkeys() f function with specified keys  
l = ['id', 'name', 'size']
x = dict.fromkeys(l)
print(x)
# using fromkeys() for dictionary specified keys and values 
y = dict.fromkeys(l, 0)
print(y)