import hashlib as hash
import os
import sys

# from Crypto.Hash import SHA256

test = ''
if(test) :
    print('yes')


def main():
	block_size = 1024 #bytes

	file_target = "w3/target.mp4"

	file_check = "w3/check.mp4"
	hash_check = "03c08f4ee0b576fe319338139c045c89c3e8e9409633bea29442e21425006ea8"


	h0_check = calculate_hash(file_check, block_size)

	h0_check_hex = h0_check.hex()
	print("calculated h0 for",file_check,":",h0_check_hex," == ",hash_check,"? ",hash_check==h0_check_hex)

	h0_target = calculate_hash(file_target, block_size)

	# h0_target_hex = h0_target.hex()
	print("calculated h0 for",file_target,":",h0_target.hex())


def calculate_hash(file_path, block_size):
	# Get file size in bytes
	file_size = os.path.getsize(file_path)
	# The last block size 
	last_block_size = file_size % block_size

	
	print("Opening file:",file_path, " ; ",file_size,"bytes; ")
	fp = open(file_path, 'rb')

	last_hash = ''
	# read the chuncks
	print(type(read_reversed_chunks(fp, file_size, last_block_size, block_size)))
	for chunk in read_reversed_chunks(fp, file_size, last_block_size, block_size):
		# SHA-256 obj
		sha = hash.sha256()
		sha.update(chunk)
		if(last_hash):
			sha.update(last_hash)
		last_hash = sha.digest()
	fp.close()

	# Return the last hash (h0)
	return last_hash


def read_reversed_chunks(file_object, file_size, last_chuck_size, chunk_size):
	iter = 0
	last_pos = file_size
	while last_pos>0:
		size = chunk_size
		if(iter == 0):
			size = last_chuck_size

		#print "read from",last_pos - size,"to",last_pos
		file_object.seek(last_pos - size)
		data = file_object.read(chunk_size)
		# print(data)
		if not data:
			break

		iter = iter + 1
		last_pos -= size
		yield data

main()
