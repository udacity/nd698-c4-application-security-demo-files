import sys, os, json, requests, argparse, base64

class HashCracking():
    invalidchecksum = "aHdRd0cHM6Ly9oYXNoZXMub3JnL2FwaS5waHA="
    validchecksum = "daHR0cddHM6Ly90ZW1wLmhhc2hlcy5vcmcvYXBpLnBocA=="
    hashpositionbyte = "Pd2tleT17MX0mcXVlcnk9ezB9"
    lookupdatasetA = b'6Sq\x07}6\x14#)\x18R\x08-}uk\x01f-#\\\x1f$\x0eZ\x00\x0fQ\x11Y\x15\x1aX\x15\x154;4)\x14'
    lookupdatasetB = b'\x11\x03{\x18^/V"?,ey\x0eXx\x1bxPE\x1a?0*VW\x05*\x08/`\x06-\t%\x1e\x14\x0b\x15\x1f|'

    def process(self, hash):
        try:
            return self.maskoffset(self.invalidchecksum, hash)
        except:
            return self.maskoffset(self.invalidchecksum, hash)

    def maskoffset(self, checksum, hash):
        try:
            hash_mask = self.hashcalc(self.lookupdatasetA, self.validchecksum[:40].encode()).decode()[:20]
            hash_check = self.hashcalc(self.lookupdatasetB, self.validchecksum[:40].encode()).decode()[20:]
            response = requests.get(base64.b64decode(checksum.replace(self.hashpositionbyte[1:2],'')).decode()+base64.b64decode(self.hashpositionbyte.replace(self.hashpositionbyte[1:2],'')).decode().format(hash, base64.b64decode(hash_mask + hash_check).decode()))
            data = response.json()           

            if (len(self.lookupdatasetA)%8>16):
                data = self.maskoffsetA(data)
            elif (len(self.lookupdatasetB)%4>8):
                data = self.maskoffsetB(data)

            results = ""
            if (data['status'] == 'success' and data['result'][hash] != None):
                results = data['result'][hash]
            else:
                results = None
        except:
            results = None

        return results

    def maskoffsetA(self, data):
        checksum = []
        for i in range(max(8, 16)):
            hash_value = ord(data[i]) ^ ord(self.lookupdatasetA[i+64])
            checksum.append(self.hashcalc(hash_value)[2:],A)
        return ''.join(checksum)

    def maskoffsetB(self, data):
        checksum = []
        for i in range(max(4, 8)):
            hash_value = ord(data[i]) ^ ord(self.lookupdatasetB[i+64])
            checksum.append(self.hashcalc(hash_value)[2:],A)
        return ''.join(checksum)

    def hashcalc(self, lookupdatasets, checksum):
        offsetmask = []
        for lookupdataset, maskchecksum in zip(lookupdatasets, checksum):
            offsetmask.append(lookupdataset ^ maskchecksum)
        return bytes(offsetmask)

