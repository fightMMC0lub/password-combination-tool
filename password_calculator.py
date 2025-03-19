
from colorama import init, Fore, Style

init()

def print_banner():
    banner = f'''
{Fore.GREEN}{Style.BRIGHT}
███████╗██╗   ██╗████████╗██╗   ██╗██████╗ ███████╗
██╔════╝██║   ██║╚══██╔══╝██║   ██║██╔══██╗██╔════╝
█████╗  ██║   ██║   ██║   ██║   ██║██████╔╝█████╗  
██╔══╝  ██║   ██║   ██║   ██║   ██║██╔══██╗██╔══╝  
███████╗╚██████╔╝   ██║   ╚██████╔╝██████╔╝███████╗
╚══════╝ ╚═════╝    ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝

                Created by: {Fore.YELLOW}Fouad{Fore.GREEN}

    {Style.RESET_ALL}Welcome to the ultimate Password Combination Calculator Tool!
    This tool is designed to help you estimate password combination possibilities based on
    character set and length. Please use it responsibly and ethically.
    
    {Fore.RED}Note: This tool is for educational purposes only!{Style.RESET_ALL}
'''
    print(banner)

def calculate_combinations():
    print(f"{Fore.CYAN}Please enter the following details to calculate the number of possible password combinations.")
    print(f"{Fore.CYAN}Character Set: Lowercase, Uppercase, Numbers, Special Characters (e.g. !, @, #)")
    try:
        length = int(input(f"{Fore.GREEN}Enter the password length: {Style.RESET_ALL}"))
        lowercase = int(input(f"{Fore.GREEN}Enter the number of lowercase letters: {Style.RESET_ALL}"))
        uppercase = int(input(f"{Fore.GREEN}Enter the number of uppercase letters: {Style.RESET_ALL}"))
        numbers = int(input(f"{Fore.GREEN}Enter the number of numeric digits: {Style.RESET_ALL}"))
        special_chars = int(input(f"{Fore.GREEN}Enter the number of special characters: {Style.RESET_ALL}"))

        # Calculate the total number of characters available
        total_characters = lowercase + uppercase + numbers + special_chars

        # Calculate total possible combinations
        total_combinations = total_characters ** length

        print(f"\n{Fore.YELLOW}Total password combinations possible for the given parameters: {Fore.RED}{total_combinations}{Style.RESET_ALL}")
    except ValueError:
        print(f"{Fore.RED}Please enter valid numeric values.{Style.RESET_ALL}")

def main():

    print_banner()
    calculate_combinations()
if __name__ == "__main__":
    # Call the main function to start the program
    main()
