BLOCK_SIZE = 16
pos = 11    
pad = (bytearray((1,)) * (BLOCK_SIZE - pos)) + (bytearray((pos,)) * pos)
print(pad)
def xor_bytes(bytes_a, bytes_b):
    #XOR two byte arrays against each other byte by byte
    
    return bytes(x ^ y for (x, y) in zip(bytes_a, bytes_b))
    

fist = bytearray((0,)) * 4
print(fist)
second =  bytearray((1,)) *16
result = xor_bytes(fist, second)
print (result)