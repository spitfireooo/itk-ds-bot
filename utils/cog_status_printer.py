from colorama import Style, Fore

def status_printer(cog_name, is_ok=True):
    print(
        f"{Fore.YELLOW + Style.BRIGHT}{cog_name}{Fore.RESET + Style.RESET_ALL}\tCog status: \t{Fore.GREEN if is_ok else Fore.RED}[{"OK" if is_ok else "ERROR"}]{Fore.RESET}")