# Big WIP 
# Currently accepts SHA1,SHA224, SHA256, SHA384, and SHA512
# Program can identify if a invalid hash type was entered and terminate
# Written by Checkn8

import hashlib

# Prints the welcome banner
def banner():
    print("************************************************************************")
    print("                     Welcome to Hash Check SHA")
    print("          _   _   _____   _____   _   _            ___  ")
    print("         | | | | |  _  | |  ___| | | | |          /  /  ")
    print("         | |_| | | |_| | | |___  | |_| |         /  /   ")
    print("         |  _  | |  _  | |___  | |  _  |   ___  /  /    ")
    print("         | | | | | | | |  ___| | | | | |   \  \/  /     ")
    print("         |_| |_| |_| |_| |_____| |_| |_|    \____/      ")
    print("")
    print("                             Version 1.0                          ")
    print("                          Writen by Checkn8")
    print("[+] Acceptable hashe types are SHA1, SHA224, SHA256, SHA384, and SHA512")
    print("*************************************************************************")

#Preps the hash and compares
def hashConversion(file, hash_1, hash_version_find): 

    BLOCK_SIZE = 65536 # The size of each read from the file
    with open(file, 'rb') as f: # Open the file to read it's bytes
        print(f"[+] Checking hash")
        # Determines the type of hash entered by the user with this if else statement
        valid_hash = False
        if hash_version_find == "sha512":
            file_hash = hashlib.sha512() # Create the hash object
            print(f"[+] You have entered a {hash_version_find} hash.")
            valid_hash = True
        if hash_version_find == "sha384":
            file_hash = hashlib.sha384() # Create the hash object
            print(f"[+] You have entered a {hash_version_find} hash.")
            valid_hash = True
        if hash_version_find == "sha256":
            file_hash = hashlib.sha256() # Create the hash object
            print(f"[+] You have entered a {hash_version_find} hash.")
            valid_hash = True
        if hash_version_find == "sha224":
            file_hash = hashlib.sha224() # Create the hash object
            print(f"[+] You have entered a {hash_version_find} hash.")
            valid_hash = True
        if hash_version_find == "sha1":
            file_hash = hashlib.sha1() # Create the hash object
            print(f"[+] You have entered a {hash_version_find} hash.")
            valid_hash = True
        if valid_hash == False:
            print("[-] You have entered an unsupported hash type") # Terminates the code if the hash type isn't supported
            return

        fb = f.read(BLOCK_SIZE) # Read from the file. Take in the amount declared above
        while len(fb) > 0: # While there is still data being read from the file
            file_hash.update(fb) # Update the hash
            fb = f.read(BLOCK_SIZE) # Read the next block from the file
    print("[+] Preparing hash")
    hash_2 = file_hash.hexdigest() # Get the hexadecimal digest of the hash
    hash_2 = hash_2.upper()
    print("[+] Comparing hashes")
    if hash_1 == hash_2:
        hashes = "match"
    if hash_1 != hash_2:
        hashes = "do not match"
    print(f"[+] The hashes you have entered {hashes}")
    

 
# Prorgam start

banner()

while True:
    hash_1 = input("Enter known good hash: ")
    hash_input = hash_1.upper()
    hash_version = input("Enter the hash type (Example: sha512 etc..): ")
    hash_version = hash_version.lower()
    file = input("Enter the File Path you wish to hash: ")
    hashConversion(file, hash_input, hash_version)
    user_input = input('Type "q" or "Q" to quit. If you would like to compare another hash, press ENTER.')
    if user_input.upper() == "Q":
        break
