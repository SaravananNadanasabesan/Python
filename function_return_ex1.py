# function hello_world
def hello_world(name:str = "Optimus Prime", location:str = "Cybertron"):
# print Hello, World
    print("Hello, World!")
# print name, Welcome to Location!
    print(name + ", welcome to " + location + "!")
    return True
# Calling function hello_world
printed = hello_world()
result = hello_world()
print(result)