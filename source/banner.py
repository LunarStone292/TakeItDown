from colorama import Fore
from source import print_slow, logs

def banner():
    print(Fore.GREEN + "▄▄▄▄▄ ▄▄▄· ▄ •▄ ▄▄▄ .▪  ▄▄▄▄▄·▄▄▄▄        ▄▄▌ ▐ ▄▌ ▐ ▄ \n•██  ▐█ ▀█ █▌▄▌▪▀▄.▀·██ •██  ██▪ ██ ▪     ██· █▌▐█•█▌▐█\n ▐█.▪▄█▀▀█ ▐▀▀▄·▐▀▀▪▄▐█· ▐█.▪▐█· ▐█▌ ▄█▀▄ ██▪▐█▐▐▌▐█▐▐▌\n ▐█▌·▐█ ▪▐▌▐█.█▌▐█▄▄▌▐█▌ ▐█▌·██. ██ ▐█▌.▐▌▐█▌██▐█▌██▐█▌\n ▀▀▀  ▀  ▀ ·▀  ▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀▀•  ▀█▄▀▪ ▀▀▀▀ ▀▪▀▀ █▪" + Fore.RESET)

def commands():
    print_slow.slow_type(Fore.LIGHTRED_EX + "\n 1. set monitor mode\n 2. set managed mode\n 3. show wifi\n 4. deauth bssid\n 5. deauth device\n 6. spam AP\n 7. flood\n 8. show logs\n 9. arp scan\n 10. exit" + Fore.RESET)

def bannerDeauth():
    print(Fore.GREEN + "·▄▄▄▄  ▄▄▄ . ▄▄▄· ▄• ▄▌▄▄▄▄▄ ▄ .▄▪   ▐ ▄  ▄▄ • \n██▪ ██ ▀▄.▀·▐█ ▀█ █▪██▌•██  ██▪▐███ •█▌▐█▐█ ▀ ▪\n▐█· ▐█▌▐▀▀▪▄▄█▀▀█ █▌▐█▌ ▐█.▪██▀▐█▐█·▐█▐▐▌▄█ ▀█▄\n██. ██ ▐█▄▄▌▐█ ▪▐▌▐█▄█▌ ▐█▌·██▌▐▀▐█▌██▐█▌▐█▄▪▐█\n▀▀▀▀▀•  ▀▀▀  ▀  ▀  ▀▀▀  ▀▀▀ ▀▀▀ ·▀▀▀▀▀ █▪·▀▀▀▀ " + Fore.RESET)

def flood():
    print(Fore.GREEN + "·▄▄▄▄▄▌              ·▄▄▄▄  ▪   ▐ ▄  ▄▄ • \n▐▄▄·██•  ▪     ▪     ██▪ ██ ██ •█▌▐█▐█ ▀ ▪\n██▪ ██▪   ▄█▀▄  ▄█▀▄ ▐█· ▐█▌▐█·▐█▐▐▌▄█ ▀█▄\n██▌.▐█▌▐▌▐█▌.▐▌▐█▌.▐▌██. ██ ▐█▌██▐█▌▐█▄▪▐█\n▀▀▀ .▀▀▀  ▀█▄▀▪ ▀█▄▀▪▀▀▀▀▀• ▀▀▀▀▀ █▪·▀▀▀▀ " + Fore.RESET)
