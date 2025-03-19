from colorama import init, Fore, Style

init()
def print_banner(creator_name, email):
    banner = f'''
{Fore.GREEN}{Style.BRIGHT}
███████╗██╗   ██╗████████╗██╗   ██╗██████╗ ███████╗
██╔════╝██║   ██║╚══██╔══╝██║   ██║██╔══██╗██╔════╝
█████╗  ██║   ██║   ██║   ██║   ██║██████╔╝█████╗  
██╔══╝  ██║   ██║   ██║   ██║   ██║██╔══██╗██╔══╝  
███████╗╚██████╔╝   ██║   ╚██████╔╝██████╔╝███████╗
╚══════╝ ╚═════╝    ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝

                Created by: {Fore.YELLOW}{creator_name}{Fore.GREEN}

    {Style.RESET_ALL}Welcome to the ultimate Password Combination Calculator Tool!
    This tool is designed to help you estimate password combination possibilities based on
    character set and length. Please use it responsibly and ethically.
    
    {Fore.RED}Note: This tool is for educational purposes only!{Style.RESET_ALL}
    
    Contact me: {Fore.CYAN}{email}{Style.RESET_ALL}
    
    Visit my blog: {Fore.CYAN}https://tinyurl.com/46jmmmre{Style.RESET_ALL}
    My website: {Fore.CYAN}https://tinyurl.com/9axb3wr8{Style.RESET_ALL}
    GitHub: {Fore.CYAN}https://tinyurl.com/bdz5n8hu{Style.RESET_ALL}
    Linkedin: {Fore.CYAN}https://tinyurl.com/3sp66jr8{Style.RESET_ALL}
    Facebook: {Fore.CYAN}https://tinyurl.com/2enj8xh9{Style.RESET_ALL}


'''
    print(banner)

def print_hacker_banner(email):
    hacker_banner = f'''
{Fore.MAGENTA}{Style.BRIGHT}
██████╗  █████╗ ███████╗████████╗███████╗██████╗ ███████╗███████╗████████╗
██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗██╔════╝██╔══██║╚══██╔══╝
██████╔╝███████║   ██║      ██║   █████╗  ██████╔╝█████╗  ██║  ██║   ██║
██╔═══╝ ██╔══██║   ██║      ██║   ██╔══╝  ██╔══██╗██╔══╝  ██║  ██║   ██║
██║     ██║  ██║   ██║      ██║   ███████╗██║  ██║███████╗██║  ██║   ██║
╚═╝     ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝

            * Ethical Hacking Tool *
        Created by: {Fore.YELLOW}Fouad Az{Fore.MAGENTA}

    {Style.RESET_ALL}Welcome to the Ultimate Hacking Tool! Here’s how you can use it:
    
    [💡 TIP] The tool calculates the possible password combinations based on your input.
    [🔒 TIP] Make sure your passwords are strong by using mixed characters.
    
    {Fore.RED}⚠️ DISCLAIMER: This tool is for educational purposes only. Do not use it for malicious activities. Always obtain permission before testing any system!{Style.RESET_ALL}

    Visit my blog: {Fore.CYAN}https://tinyurl.com/46jmmmre{Style.RESET_ALL}
    My website: {Fore.CYAN}https://tinyurl.com/9axb3wr8{Style.RESET_ALL}
    GitHub: {Fore.CYAN}https://tinyurl.com/bdz5n8hu{Style.RESET_ALL}
    Linkedin: {Fore.CYAN}https://tinyurl.com/3sp66jr8{Style.RESET_ALL}
    Facebook: {Fore.CYAN}https://tinyurl.com/2enj8xh9{Style.RESET_ALL}

    Contact me: {email}
'''
    print(hacker_banner)

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
    creator_name = "Fouad Az"
    email = "jihgeharverserv@gmail.com" 
    print_hacker_banner(email)  
    print_banner(creator_name, email) 
    calculate_combinations()

if __name__ == "__main__":
    # Call the main function to start the program
    main()
