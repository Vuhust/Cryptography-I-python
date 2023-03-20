import urllib.request, urllib.error, urllib.parse
import sys

TARGET = 'http://crypto-class.appspot.com/po?er='
#--------------------------------------------------------------
# padding oracle
#--------------------------------------------------------------
class PaddingOracle(object):
    def query(self, q):
        target = TARGET + urllib.parse.quote(q)    # Create query URL
        req = urllib.request.Request(target)         # Send HTTP request to server
        try:
            f = urllib.request.urlopen(req)          # Wait for response
        except urllib.error.HTTPError as e:          
            print("We got: %d" % e.code)       # Print response code
            if e.code == 404:
                print("good padding")
                return True # good padding
            print("bad padding")
            return False # bad padding

# if __name__ == "__main__":

def xor( a , b):
    # return "".join([chr(ord(b) ^ ord(a))])
    return a ^ b

    
    
    
def main():
    po = PaddingOracle()
    po.query(    "f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4")       # Issue HTTP query with the given argument
    ciphertext = "f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4"
    # print (xor("ax".encode('utf-8').hex(), "ff".encode('utf-8').hex()))
    # test = 'ab'.encode()
    # test = "as".decode('utf8').hex()
    # print(type(test))
    # print(test)
    print(xor(int("11",16) , int("ff",16)))
    print(17 ^ 255)
    print(len(ciphertext))


main()