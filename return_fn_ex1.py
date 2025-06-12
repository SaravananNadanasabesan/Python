# function hello_world
def hello_world(name:str = "Optimus Prime",
location:str = "Cybertron"):
# print Hello, World
    print("Hello, World!")
    return True
# print name, Welcome to Location!
    print(name + ", welcome to " + location + "!")
# Calling function hello_world
printed = hello_world()
