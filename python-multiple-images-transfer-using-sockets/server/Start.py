import requests
import sys
import time
from termcolor import colored

def startDownload():
    try:
        for i in range(1):
            print(colored("1. Start program \n2. Exit \n", "yellow"))
            user_input_auswahl = int(input("\n* Enter your choise: \n"))
            if user_input_auswahl == 1:
                user_input_anzahl = int(input("Enter the number of URL's you want to enter: "))
                if user_input_anzahl == 1:
                    url1_input = input("\n* Enter the First URL: \n")
                    name_input_url1 = input("\n* Under what name should the first URL be saved? \n")
                    r1 = requests.get(url1_input) # URL1
                    open(name_input_url1, 'wb').write(r1.content)
                    if r1.status_code == 200:
                        print(colored("\n* First URL: Successful! \n", "yellow"))
                    else:
                        print(colored("\n* First URL: Error! \n", "red"))
                if user_input_anzahl == 2:
                    url1_input = input("\n* Enter the First URL: \n")
                    url2_input = input("\n* Enter the Second URL: \n")
                    name_input_url1 = input("\n* Under what name should the first URL be saved? \n")
                    name_input_url2 = input("\n* Under what name should the second URL be saved? \n")
                    r1 = requests.get(url1_input) # URL1
                    r2 = requests.get(url2_input) # URL2
                    open(name_input_url1, 'wb').write(r1.content)
                    open(name_input_url2, 'wb').write(r2.content)
                    if r1.status_code == 200:
                        print(colored("\n* First URL: Successful! \n", "yellow"))
                    else:
                        print(colored("\n* First URL: Error! \n", "red"))
                    if r2.status_code == 200:
                        print(colored("\n* Second URL: Successful! \n", "yellow"))
                    else:
                        print(colored("\n* Second URL: Error! \n", "red"))
                if user_input_anzahl == 3:
                    url1_input = input("\n* Enter the First URL: \n")
                    url2_input = input("\n* Enter the Second URL: \n")
                    url3_input = input("\n* Enter the Third URL: \n")
                    name_input_url1 = input("\n* Under what name should the first URL be saved? \n")
                    name_input_url2 = input("\n* Under what name should the second URL be saved? \n")
                    name_input_url3 = input("\n* Under what name should the third URL be saved? \n")
                    r1 = requests.get(url1_input) # URL1
                    r2 = requests.get(url2_input) # URL2
                    r3 = requests.get(url3_input) # URL3
                    open(name_input_url1, 'wb').write(r1.content)
                    open(name_input_url2, 'wb').write(r2.content)
                    open(name_input_url3, 'wb').write(r3.content)
                    if r1.status_code == 200:
                        print(colored("\n* First URL: Successful! \n", "yellow"))
                    else:
                        print(colored("\n* First URL: Error! \n", "red"))
                    if r2.status_code == 200:
                        print(colored("\n* Second URL: Successful! \n", "yellow"))
                    else:
                        print(colored("\n* Second URL: Error! \n", "red"))
                    if r3.status_code == 200:
                        print(colored("\n* Third URL: Successful! \n", "yellow"))
                    else:
                        print(colored("\n* Third URL: Error! \n", "red"))
                if user_input_anzahl == 4:
                    url1_input = input("\n* Enter the First URL: \n")
                    url2_input = input("\n* Enter the Second URL: \n")
                    url3_input = input("\n* Enter the Third URL: \n")
                    url4_input = input("\n* Enter the Fourth URL: \n")
                    name_input_url1 = input("\n* Under what name should the first URL be saved? \n")
                    name_input_url2 = input("\n* Under what name should the second URL be saved? \n")
                    name_input_url3 = input("\n* Under what name should the third URL be saved? \n")
                    name_input_url4 = input("\n* Under what name should the fourth URL be saved?\n")
                    r1 = requests.get(url1_input) # URL1
                    r2 = requests.get(url2_input) # URL2
                    r3 = requests.get(url3_input) # URL3
                    r4 = requests.get(url4_input) # URL4
                    open(name_input_url1, 'wb').write(r1.content)
                    open(name_input_url2, 'wb').write(r2.content)
                    open(name_input_url3, 'wb').write(r3.content)
                    open(name_input_url4, 'wb').write(r4.content)
                    if r1.status_code == 200:
                        print(colored("\n* First URL: Successful! \n", "yellow"))
                    else:
                        print(colored("\n* First URL: Error! \n", "red"))
                    if r2.status_code == 200:
                        print(colored("\n* Second URL: Successful! \n", "yellow"))
                    else:
                        print(colored("\n* Second URL: Error! \n", "red"))
                    if r3.status_code == 200:
                        print(colored("\n* Third URL: Successful! \n", "yellow"))
                    else:
                        print(colored("\n* Third URL: Error! \n", "red"))
                    if r4.status_code == 200:
                        print(colored("\n* Fourth URL: Successful! \n", "yellow"))
                    else:
                        print(colored("\n* Fourth URL: Error! \n", "red"))     
            if user_input_anzahl == 2:
                print(colored("\n* Program Stopped! \n", "red"))
                time.sleep(3)
                break
    except KeyboardInterrupt:
        print(colored("\n* User use CTRL + C Program Stopped! \n", "red"))
    except UnboundLocalError:
        print(colored("\n* Enter a valid number! Only 1 or 2 possible! \n", "red"))
        time.sleep(3)
        sys.exit(0)

    finally:
        print(colored("\n* Download task complete! Next task: Start Server! \n", "blue"))