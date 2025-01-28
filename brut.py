from colorama import Fore, Back, Style

brut_ascii_art = """___.                 __   
\\_ |_________ __ ___/  |_ 
 | __ \\_  __ \\  |  \\   __\\
 | \\_\\ \\  | \\/  |  /|  |  
 |___  /__|  |____/ |__|  
     \\/                   """
print(Fore.YELLOW + brut_ascii_art)
message = """
Program developed and maintained by mrsajadpp
-------------------------------------------------
GitHub Repository: https://github.com/mrsajadpp/brut.git

If you are interested to collaborate,
please contribute to the repository.
"""
warning_message = """
This program is developed only for educational and legal purposes.
"""
print(message + Fore.RED + warning_message)
print(Fore.RESET)

def handle_cahoice():
    message = """
Choose which brute force you need:
-------------------------------------------------
1 : SSH
-------------------------------------------------
More options are coming soon!
    """
    print(Fore.GREEN +message)
    choice = input(Fore.RESET + "Enter your choice: ")

    if choice == "1":
        from sub_probs.ssh import ssh_bruteforce
        ip = input("Enter IP Address: ").strip()
        username = input("Enter Username: ").strip()
        password_list = input("Enter Password List: ").strip()
        
        try:
            ssh_bruteforce(ip, username, password_list)
        except FileNotFoundError:
            print(Fore.RED + "Password list file not found. Please provide a valid path.")
        except KeyboardInterrupt:
            print(Fore.RED + "\nExiting.")
    else:
        print(Fore.RED + "Invalid choice. Exiting.")
        return  

if __name__ == "__main__":
    handle_cahoice()