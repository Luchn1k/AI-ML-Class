
def _print():
    print("hello")


_print()

def _add(num1,num2):
    print(num1 + num2)

# add 2 numbers 
_add("10","20")



def _multi(num1,num2):
    return num1 * num2



print(_multi("#",2))







#variables


name = "abc"


def print_name():
    name = "xyz"
    print(name) #1 

print(name) #2 
print_name()
print(name) #3


def change_name(new_name):
    global name
    name = new_name

change_name("saman")
print(name)



def use_profile():
    print(name)


def customet_profile():

    #local  name = ""
    name = "tyx" 
    name = name + " as cust"
    print(name)


use_profile()
customet_profile()




def _abc():
    customer = "cust 1"
    print(customer)


_abc()
# print(customer)




name = "xyz"

print("="*50)
if name == "xyz":
    print("ok")


total = 100


if total >= 100:
    print("large")




for i in range(0,5):
    print(i)

