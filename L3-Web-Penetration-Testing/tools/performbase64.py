import sys, argparse, base64

def encode(data):
    data_bytes = data.encode('ascii')
    base64_bytes = base64.b64encode(data_bytes)
    base64_message = base64_bytes.decode('ascii')
    print(base64_message)

def decode(data):
    base64_bytes = data.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    print(message)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', action='store_true', help='decode base64 string')
    parser.add_argument('string', help='string that you want to transform')
    args = parser.parse_args()

    if (args.d):
        decode(args.string)
    else:
        encode(args.string)