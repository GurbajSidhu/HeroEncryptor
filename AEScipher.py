
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encryptor():
    a = input('Enter message to be encrypted: ')
    data= bytes(a, encoding='utf8')
    key = get_random_bytes(16)
    with open('test.bin', 'wb') as keyfile:
        keyfile.write(key)
    print("random key generated:\n",key, "\n SAVED TO 'test.bin'")
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    file_out = open("encrypted.bin", "wb")
    [file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]
    file_out.close()





def decryptor():
    file_in = open("encrypted.bin", "rb")
    nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]
    with open('test.bin', 'rb') as keyfile:
        key = keyfile.read()
    #key =open('test.bin', 'r').read()
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    print("Decrypted data: ", data)



msg= int(input('press 1 to encrypt and 2 to decrypt:'))
if msg==1:
    encryptor()
elif msg==2:
    decryptor()

