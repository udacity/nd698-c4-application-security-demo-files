import sys, os, requests, argparse, time, random
from colorama import Fore, Style 

payloads = []
hidestatuscodes = []
hidecontentlen = 0
showstatuscodes = []
showcontentlen = 0

def loadfiles(filename):
    data = []
    with open(filename,'r') as f:
        lines = f.readlines()
        for line in lines:
            data.append(line.strip())
    return data

def header(url):
    print('********************************************************')
    print('***      Fuzzing 1.0.0 - Demo tool for training      ***')
    print('********************************************************')
    print('')
    print('Target: {}'.format(url))
    print('Total Requests: {}'.format(str(len(payloads))))
    print('========================================================')
    print('{0} {1}  {2}'.format('StatusCode','Len','Request'))
    print('========================================================')

def footer():
    print('')
    print('********************************************************')
    print('***   This is a demo code used for this training.    ***')
    print('********************************************************')

def main(url):
    counter = 0
    for payload in payloads:
        time.sleep(random.randint(1, 3)/10)
        requesturl = url.replace("^FUZZ^", payload)
        response = requests.get(requesturl, allow_redirects=False, stream=True)
        try:
            contentlen = response.headers['Content-length']
        except:
            contentlen = "0"
        statuscode = response.status_code

        if len(showstatuscodes) != 0 and str(statuscode) not in showstatuscodes:
            continue

        if str(showcontentlen) != "0" and str(contentlen) != str(showcontentlen):
            continue

        if len(hidestatuscodes) != 0 and str(statuscode) in hidestatuscodes:
            continue

        if str(hidecontentlen) != "0" and str(contentlen) == str(hidecontentlen):
            continue

        if statuscode != 200:
            print(Fore.YELLOW + '[-] {0} {1:>7} {2}'.format(statuscode,contentlen + 'b',requesturl) + Style.RESET_ALL)
        else:
            counter += 1
            print(Fore.GREEN + '[+] {0} {1:>7} {2}'.format(statuscode,contentlen + 'b',requesturl) + Style.RESET_ALL)

    print('========================================================')
    print('Found: {} pages'.format(str(counter)))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Fuzzing Web Application"
    )

    parser.add_argument("-sc", "--showstatuscode", type=str, help="Show url with the following status codes, csv is supported")
    parser.add_argument("-hc", "--hidestatuscode", type=str, help="Hide url with the following status codes, csv is supported")
    parser.add_argument("-sl", "--showcontentlen", type=str, help="Show url with the following content length")
    parser.add_argument("-hl", "--hidecontentlen", type=str, help="Hide url with the following content length")
    parser.add_argument("payload", metavar="PAYLOAD", help="File for fuzzing web site")
    parser.add_argument("siteurl", metavar="SITEURL", help="Website url with the ^FUZZ^ keyword")

    args = parser.parse_args()

    if args.payload:
        payloads += (loadfiles(args.payload))

    if args.showstatuscode:
        for s in args.showstatuscode.split(','):
            showstatuscodes.append(s)

    if args.showcontentlen:
        showcontentlen = args.showcontentlen

    if args.hidestatuscode:
        for h in args.hidestatuscode.split(','):
            hidestatuscodes.append(h)

    if args.hidecontentlen:
        hidecontentlen = args.hidecontentlen

    header(args.siteurl)
    main(args.siteurl)
    footer()