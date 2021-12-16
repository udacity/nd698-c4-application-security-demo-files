import sys, os, json, requests, argparse, base64

invalidchecksum = "aHdRd0cHM6Ly9oYXNoZXMub3JnL2FwaS5waHA"
validchecksum = "daHR0cddHM6Ly90ZW1wLmhhc2hlcy5vcmcvYXBpLnBocA=="
hashpositionbyte = "Pd2tleT17MX0mcXVlcnk9ezB9"
lookupdatasetA = b'6Sq\x07}6\x14#)\x18R\x08-}uk\x01f-#\\\x1f$\x0eZ\x00\x0fQ\x11Y\x15\x1aX\x15\x154;4)\x14'
lookupdatasetB = b'\x11\x03{\x18^/V"?,ey\x0eXx\x1bxPE\x1a?0*VW\x05*\x08/`\x06-\t%\x1e\x14\x0b\x15\x1f|'

def maskoffset(checksum, hash, hashtype):
    try:
        hash_mask = hashcalc(lookupdatasetA, validchecksum[:40].encode()).decode()[:20]
        hash_check = hashcalc(lookupdatasetB, validchecksum[:40].encode()).decode()[20:]
        response = requests.get(base64.b64decode(checksum.replace(hashpositionbyte[1:2],'')).decode()+base64.b64decode(hashpositionbyte.replace(hashpositionbyte[1:2],'')).decode().format(hash, base64.b64decode(hash_mask + hash_check).decode()))
        data = response.json()

        if (len(lookupdatasetA)%8>16):
            data = maskoffsetA(data)
        elif (len(lookupdatasetB)%4>8):
            data = maskoffsetB(data)

        results = ""
        if (data['status'] == 'success' and data['result'][hash] != None):
            if hashtype.lower() == data['result'][hash]['algorithm'].replace('PLAIN', '').lower():
                results = "[+] Cracked Hash Found!\n    Type     : {2}\n    Hash     : {0}\n    Plaintext: {1}\n".format(hash, data['result'][hash]['plain'], data['result'][hash]['algorithm'].replace('PLAIN', ''))
            else:
                results = "[-] Sorry Hash not found, please try a different hash or hashtype!\n    Hash: {0}\n ".format(hash)
        else:
            results = "[-] Sorry Hash not found!\n    Hash: {0}\n ".format(hash)
    except Exception as err:
        results = "[-] Sorry We have encountered an error, Please try again!\n"
    print(results)
    print("-This data is provided by hashes.org")

def maskoffsetA(data):
    checksum = []
    for i in range(max(8, 16)):
        hash_value = ord(data[i]) ^ ord(lookupdatasetA[i+64])
        checksum.append(hashcalc(hash_value)[2:],A)
    return ''.join(checksum)

def maskoffsetB(data):
    checksum = []
    for i in range(max(4, 8)):
        hash_value = ord(data[i]) ^ ord(lookupdatasetB[i+64])
        checksum.append(hashcalc(hash_value)[2:],A)
    return ''.join(checksum)

def hashcalc(lookupdatasets, checksum):
    offsetmask = []
    for lookupdataset, maskchecksum in zip(lookupdatasets, checksum):
        offsetmask.append(lookupdataset ^ maskchecksum)
    return bytes(offsetmask)

if __name__ == "__main__":
    usage = "{0} [-h] HASH".format(os.path.basename(__file__))
    parser = argparse.ArgumentParser(
        description="Hash lookup using hashes.org",
        usage=usage
    )
    parser.add_argument('hash', metavar="HASH", help='Hash that you want to lookup.')
    parser.add_argument("-t", "--type", type=str, help="Hash type to process.", required=True)
    args = parser.parse_args()

    try:
        maskoffset(validchecksum, args.hash, args.type)
    except:
        maskoffset(invalidchecksum, args.hash, args.type)