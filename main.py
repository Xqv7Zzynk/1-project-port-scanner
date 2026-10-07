# Port Scanner v2.0
# Created: 03.07.2026
# Updated: 07.10.2026
import socket

# Windows category includes Active Directory
web = [80, 443, 8080]
admin = [22, 3389]
windows = [135, 139, 445, 389, 636, 88]
database = [1433, 3306, 5432]
network = [53, 123, 161, 7777, 7776]
infrastructure = [6443, 2375, 2376, 9090, 3000]

company_infrastructure = [web, admin, windows, database, network, infrastructure]

exit_code2 = True
exit_code = True
open_Port = []
custom_port = []

def scanning():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((ip_answer, port))
    s.close()
    if result == 0:
        open_Port.append(f"[+]Open:{port}")
    
while exit_code:
    
    while True:
        print("=" * 45)
        print("1 = basic scan                2 = custom scan")
        print("EXIT       what will you choose?: ")
        print("=" * 45)

        user_answer = input()
        if user_answer.lower() == "exit":
            exit_code = False
            break
            
        try:
            answer = int(user_answer)

            if answer == 1 or answer == 2:
                break
            else:
                print("You must choose 1 or 2: ")
        except ValueError:
            print("Error: You entered letters or symbols. Must be 1 or 2!")
    
    if not exit_code:
        break

    while True:
        ip_answer = input("Which IP to use for scanning?: ")
        
        if "." in ip_answer:
            print("Great, correct IP (probably)")
            break
        else:
            print("IP is probably incorrect")

    
    if answer == 1:
        for categories in company_infrastructure:
            for port in categories:
                scanning()
    print(open_Port)
    open_Port.clear()

    if answer == 2: 
        while True:
            print("=" * 31)    
            print("Type ports for scanning:")
            print("        yes to exit")
            print("=" * 31)
            print(custom_port)
            port_answer = input()
            try:
                if "yes" in port_answer:
                    break
                else:
                    port_answer1 = int(port_answer) 
                    custom_port.append(port_answer1)
                            
            except ValueError:
                print("Error: You typed a letter or symbol!")
        
        for port in custom_port:
            scanning()
        print(open_Port)
        custom_port.clear()
        open_Port.clear()
