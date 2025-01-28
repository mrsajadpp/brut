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