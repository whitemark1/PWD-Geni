from termcolor import colored
import os
import sys
import time
import random
from os import system, name


logo = """
██╗    ██╗██╗  ██╗██╗████████╗███████╗███╗   ███╗ █████╗ ██████╗ ██╗  ██╗
██║    ██║██║  ██║██║╚══██╔══╝██╔════╝████╗ ████║██╔══██╗██╔══██╗██║ ██╔╝
██║ █╗ ██║███████║██║   ██║   █████╗  ██╔████╔██║███████║██████╔╝█████╔╝ 
██║███╗██║██╔══██║██║   ██║   ██╔══╝  ██║╚██╔╝██║██╔══██║██╔══██╗██╔═██╗ 
╚███╔███╔╝██║  ██║██║   ██║   ███████╗██║ ╚═╝ ██║██║  ██║██║  ██║██║  ██╗
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
                                                                         
"""
for i in logo:
    for a in i:
        b=colored(a,'yellow')
        print(b,end="")
        sys.stdout.flush()
        time.sleep(0.01)
print("   ")
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
clear()
logo ="""
██████╗ ██╗    ██╗██████╗             
██╔══██╗██║    ██║██╔══██╗            
██████╔╝██║ █╗ ██║██║  ██║            
██╔═══╝ ██║███╗██║██║  ██║            
██║     ╚███╔███╔╝██████╔╝            
╚═╝      ╚══╝╚══╝ ╚═════╝             
                                      
         ██████╗ ███████╗███╗   ██╗██╗
        ██╔════╝ ██╔════╝████╗  ██║██║
        ██║  ███╗█████╗  ██╔██╗ ██║██║
        ██║   ██║██╔══╝  ██║╚██╗██║██║
        ╚██████╔╝███████╗██║ ╚████║██║
         ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚═╝
                                      
"""
for i in logo:
    for a in i:
        b=colored(a,'red')
        print(b,end="")
        sys.stdout.flush()
        time.sleep(0.001)
logo = """                 *+*+Created by MR.WhiteMark+*+*
                       *+*+Member of CW+*+*
"""
for i in logo:
    for a in i:
        b=colored(a,'blue')
        print(b,end="")
        sys.stdout.flush()
        time.sleep(0.001)

print("          ")
print("          ")

time.sleep(0.5)
print(colored("                 [1].CREATE PASSWORD",'yellow'))
print("          ")
time.sleep(0.5)
print(colored("                 [2].CONVERT RANDOM PASSWORD",'yellow'))
print("          ")
time.sleep(0.5)
print(colored("                 [3].COMMENT A BUG!",'yellow'))
time.sleep(0.5)
print("   ")
in1 = input(colored("Enter your choice(enter number): ",'yellow'))
print("   ")

if in1=="1":
    clear()
    print(" ")
    from termcolor import colored
    import os
    import sys
    import time
    import random
    #inputs

    name = input(colored("Enter your name: ",'yellow'))
    print("   ")
    birthday = input(colored("Enter your birthday: ",'yellow'))
    print("   ")
    p_number = input(colored("Enter your phone number: ",'yellow'))
    print("   ")
    lenth = int(input(colored("Enter lenght of password: ",'red')))
    print("   ")
    amount = int(input(colored("Enter amount of passwords: ",'red')))
    print("   ")
    save = input(colored("Enter name for file save passwords: ","yellow"))
    print("  ")

    #jenis
    upperl = name.upper()
    lowerl = name.lower()
    numbers = p_number
    symbols = "/*][{}!@#$%&"

    upper, lower, nums, sys = True, True, True, True,

    pwd=""

    if upper:
        pwd += upperl
    if upper:
        pwd += lowerl
    if upper:
        pwd += numbers
    if upper:
        pwd += symbols

    lent = lenth
    amnt = amount

    x = 0
    while x < 10:
        time.sleep(0.2)
        x += 1
        text = '*+*+*+**+*+*+*Genareting your password+*+*+*+*+*+*'
        print(colored(text,'yellow'))
        print("")
        
    print(colored("Here your passwords: ",'blue'))
    print("  ")

    with open(save,'a') as f:
        for x in range(amnt):
            time.sleep(0.5)
            password = "".join(random.sample(pwd, lent))
            x = password
            print(colored(x,'green'))
            print("")
            f.write(password+'\n')
    f.close()

elif in1=="2":
    clear()
    print(" ")
    from termcolor import colored
    import os
    import sys
    import time
    import random
    #inputs


    lenth = int(input(colored("Enter lenght of password: ",'red')))
    print("   ")
    amount = int(input(colored("Enter amount of passwords: ",'red')))
    print("   ")
    save = input(colored("Enter name for file save passwords: ","yellow"))
    print("  ")

    #jenis
    upperl = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowerl = upperl.lower()
    numbers ="0123456789"
    symbols = "/*][{}!@#$%&"

    upper, lower, nums, sys = True, True, True, True,

    pwd=""

    if upper:
        pwd += upperl
    if upper:
        pwd += lowerl
    if upper:
        pwd += numbers
    if upper:
        pwd += symbols

    lent = lenth
    amnt = amount

    x = 0
    while x < 10:
        time.sleep(0.2)
        x += 1
        text = '*+*+*+**+*+*+*Genareting your password+*+*+*+*+*+*'
        print(colored(text,'yellow'))
        print("")
        
    print(colored("Here your passwords: ",'blue'))
    print("  ")

    with open(save,'a') as f:
        for x in range(amnt):
            time.sleep(0.5)
            password = "".join(random.sample(pwd, lent))
            x = password
            print(colored(x,'green'))
            print("")
            f.write(password+'\n')
    f.close()
