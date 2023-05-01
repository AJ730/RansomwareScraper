from colorama import Fore, Style


def info(text):
    print(f"{Fore.GREEN}Info: {text} {Style.RESET_ALL}")


def warning(text):
    print(f"{Fore.BLUE}Warning: {text} {Style.RESET_ALL}")


def alert(text):
    print(f"{Fore.RED}Alert: {text} {Style.RESET_ALL}")



def unsupported(text):
    print(f"{Fore.CYAN}Unsupported: {text} {Style.RESET_ALL}")


def conclusion(text):
    print(f"{Fore.MAGENTA}\n ------------- Conclusion ------------- \n{text} {Style.RESET_ALL}")
