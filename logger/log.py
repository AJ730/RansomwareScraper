from colorama import Fore


def info(text):
    print(f"{Fore.GREEN}Info: {text}")


def warning(text):
    print(f"{Fore.BLUE}Warning: {text}")


def alert(text):
    print(f"{Fore.RED}Alert: {text}")



def unsupported(text):
    print(f"{Fore.CYAN}Unsupported: {text}")


def conclusion(text):
    print(f"{Fore.MAGENTA}\n ------------- Conclusion ------------- \n{text}")
