from Crypto.Cipher import DES, AES
import binascii
UID="119151556"
Last_name="devaladakere arvind"
First_Name="Dhanush"
def aes_input_av_test(inputblock, key,blist):
    cc = binascii.hexlify(key.encode())
    ccc = cc.decode('utf-8')
    diff_bit=[]
    count=0
    #blist=[5,29,38]
    aa=inputblock.encode()
    key1 = bytes.fromhex(ccc)
    #print(key1)
    #print(len(key1))
    aes_cipher = AES.new(key1, AES.MODE_ECB)
    aesciphertext = aes_cipher.encrypt(aa)
    #print(aesciphertext)
    cipher_bit = ''.join(bin(byte)[2:].zfill(8) for byte in aesciphertext)
    #print("cipher bit :" +cipher_bit)
    cipher_list = [b for b in cipher_bit]
    #print(cipher_list)


    original_bits = [int(bit) for bit in ''.join(format(ord(c), '08b') for c in inputblock)]#convert to bits
    original_list = [b for b in original_bits] #then to a list of bits
    #print("original bit")
    #print(original_list)
    for f in blist:
        original_list[f] ^= 1
        #diff_bit.append(original_list[b] ^ 1)
        #print("filpped")
        #print(original_list)
        diff = ""
        for b in original_list:
          diff += str(b)
        #diff = ''.join(original_list)
        #print(diff)
        byte_string = bytes(int(diff[i:i + 8], 2) for i in range(0, len(diff), 8))#convert the string of bits to bytes
        modifiedtext = aes_cipher.encrypt(byte_string)
        #print(modifiedtext)
        modified_bit= ''.join(bin(byte)[2:].zfill(8) for byte in modifiedtext)
        #print(modified_bit)
        modified_list = [b for b in modified_bit]
        #print(modified_list)
        for i in range(len(modified_list)):
           if(modified_list[i]!=cipher_list[i]):
            count+=1
        diff_bit.append(count)
        count=0
        original_list[f] ^= 1
    print("change when AES input bit is changed:")
    print(diff_bit)
    #print([abs(modified_bit[i] - original_biy[i]) for i in range(len(original_list))][:len(blist)])

def aes_key_av_test(inputblock, key, blist):
    cc = binascii.hexlify(key.encode())
    ccc = cc.decode('utf-8')
    diff_bit = []
    count = 0
    # blist=[5,29,38]
    #print(key)
    #print(inputblock)
    aa = inputblock.encode()
    key1 = bytes.fromhex(ccc)
    #print(key1)
    keyyy=key1.decode("utf-8")
    # print(len(key1))
    aes_cipher = AES.new(key1, AES.MODE_ECB)
    aesciphertext = aes_cipher.encrypt(aa)
    # print(aesciphertext)

    cipher_bit = ''.join(bin(byte)[2:].zfill(8) for byte in aesciphertext)
    #print("cipher bit :" + cipher_bit)
    cipher_list = [b for b in cipher_bit]
    #print(cipher_list)

    key_bits = [int(bit) for bit in ''.join(format(ord(c), '08b') for c in keyyy)]  # convert to bits
    key_list = [b for b in key_bits]  # then to a list of bits
    #print("key bit")
    #print(key_list)
    for f in blist:
        key_list[f] ^= 1
        # diff_bit.append(original_list[b] ^ 1)
        #print("filpped")
        #print(key_list)
        diff = ""
        for b in key_list:
            diff += str(b)
        # diff = ''.join(original_list)
        #print(diff)
        byte_string = bytes(int(diff[i:i + 8], 2) for i in range(0, len(diff), 8)) # convert the string of bits to bytes
        #print("byte string :")
        #print(byte_string)
        modifiedcipher=AES.new(byte_string, AES.MODE_ECB)
        modifiedtext = modifiedcipher.encrypt(aa)
        #print(modifiedtext)
        modified_bit = ''.join(bin(byte)[2:].zfill(8) for byte in modifiedtext)
        #print(modified_bit)
        modified_list = [b for b in modified_bit]
        #print(modified_list)
        for i in range(len(modified_list)):
            if (modified_list[i] != cipher_list[i]):
                count += 1
        diff_bit.append(count)
        count = 0
        key_list[f] ^= 1
    print("change when AES key bit is changed:")
    print(diff_bit)
    # print([abs(modified_bit[i] - original_biy[i]) for i in range(len(original_list))][:len(blist)])





def des_input_av_test(inputblock, key, blist):
    kk = binascii.hexlify(key.encode())
    kkk = kk.decode('utf-8')
    diff_bit = []
    count = 0
    # blist=[5,29,38]
    aa = inputblock.encode()
    key1 = bytes.fromhex(kkk)
    #print(key1)
    # print(len(key1))
    des_cipher = DES.new(key1, DES.MODE_ECB)
    desciphertext = des_cipher.encrypt(aa)
    # print(aesciphertext)
    cipher_bit = ''.join(bin(byte)[2:].zfill(8) for byte in desciphertext)
    #print("cipher bit :" + cipher_bit)
    cipher_list = [b for b in cipher_bit]
    #print(cipher_list)

    original_bits = [int(bit) for bit in ''.join(format(ord(c), '08b') for c in inputblock)]  # convert to bits
    original_list = [b for b in original_bits]  # then to a list of bits
    #print("original bit")
    #print(original_list)
    for f in blist:
        original_list[f] ^= 1
        # diff_bit.append(original_list[b] ^ 1)
        #print("filpped")
        #print(original_list)
        diff = ""
        for b in original_list:
            diff += str(b)
        # diff = ''.join(original_list)
        #print(diff)
        byte_string = bytes(
            int(diff[i:i + 8], 2) for i in range(0, len(diff), 8))  # convert the string of bits to bytes
        modifiedtext = des_cipher.encrypt(byte_string)
        #print(modifiedtext)
        modified_bit = ''.join(bin(byte)[2:].zfill(8) for byte in modifiedtext)
        #print(modified_bit)
        modified_list = [b for b in modified_bit]
        #print(modified_list)
        for i in range(len(modified_list)):
            if (modified_list[i] != cipher_list[i]):
                count += 1
        diff_bit.append(count)
        count = 0
        original_list[f] ^= 1
    print("change when DES input bit is changed:")
    print(diff_bit)
    # print([abs(modified_bit[i] - original_biy[i]) for i in range(len(original_list))][:len(blist)])
def des_key_av_test(inputblock, key, blist):
    kk = binascii.hexlify(key.encode())
    kkk = kk.decode('utf-8')
    diff_bit = []
    count = 0
    # blist=[5,29,38]
    #print(key)
    #print(inputblock)
    aa = inputblock.encode()
    key1 = bytes.fromhex(kkk)
    #print(key1)
    keyyy=key1.decode("utf-8")
    # print(len(key1))
    aes_cipher = DES.new(key1, DES.MODE_ECB)
    aesciphertext = aes_cipher.encrypt(aa)
    # print(aesciphertext)

    cipher_bit = ''.join(bin(byte)[2:].zfill(8) for byte in aesciphertext)
    #print("cipher bit :" + cipher_bit)
    cipher_list = [b for b in cipher_bit]
    #print(cipher_list)

    key_bits = [int(bit) for bit in ''.join(format(ord(c), '08b') for c in keyyy)]  # convert to bits
    key_list = [b for b in key_bits]  # then to a list of bits
    #print("key bit")
    #print(key_list)
    for f in blist:
        key_list[f] ^= 1
        # diff_bit.append(original_list[b] ^ 1)
        #print("filpped")
        #print(key_list)
        diff = ""
        for b in key_list:
            diff += str(b)
        # diff = ''.join(original_list)
        #print(diff)
        byte_string = bytes(int(diff[i:i + 8], 2) for i in range(0, len(diff), 8)) # convert the string of bits to bytes
        #print("byte string :")
        #print(byte_string)
        modifiedcipher=DES.new(byte_string, DES.MODE_ECB)
        modifiedtext = modifiedcipher.encrypt(aa)
        #print(modifiedtext)
        modified_bit = ''.join(bin(byte)[2:].zfill(8) for byte in modifiedtext)
        #print(modified_bit)
        modified_list = [b for b in modified_bit]
        #print(modified_list)
        for i in range(len(modified_list)):
            if (modified_list[i] != cipher_list[i]):
                count += 1
        diff_bit.append(count)
        count = 0
        key_list[f] ^= 1
    print("change when DES key is changed:")
    print(diff_bit)
    # print([abs(modified_bit[i] - original_biy[i]) for i in range(len(original_list))][:len(blist)])
a="thisoneis16bytes" #input value,can change to check for other values
d=[5,29,38]
dd=[3,25,36]
#b= str(input("enter the key of 16 bytes for DES: "))
#a= str(input("enter the string of 32 bytes for AES: "))
#b= str("0f1571c947d9e859")
c= str("veryverylongkey!") #AES key,can check to change for othert values
k= str("deskey!!") #DES key,can change to check for other values
#kk=binascii.hexlify(k.encode())
#cc=binascii.hexlify(c.encode())
#ccc=cc.decode('utf-8')
#kkk=kk.decode('utf-8')
aes_input_av_test(a,c,d)
aes_key_av_test(a, c, d)
des_input_av_test(a,k,dd)
des_key_av_test(a, k, dd)