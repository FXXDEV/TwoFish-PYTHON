#encoding: utf-8
import chilkat
import sys

# set ck acess key
glob = chilkat.CkGlobal()
glob.UnlockBundle("Anything for 30-day trial")

crypt = chilkat.CkCrypt2()
crypt.put_CryptAlgorithm("twofish")

# "ecb" / "cbc"
crypt.put_CipherMode("ecb")

# KeyLength [128, 192, 256]
crypt.put_KeyLength(128)

crypt.put_PaddingScheme(0)

crypt.put_EncodingMode("hex")


keyHex = "6E3272357538782F413F4428472B4B62"
crypt.SetEncodedKey(keyHex,"hex")
# Encrypt a string...
# The input string is 44 ANSI characters (i.e. 44 bytes), so
# the output should be 48 bytes (a multiple of 16).
# Because the output is a hex string, it should
# be 96 characters long (2 chars per byte).
str = input('Encrypt the string: ')

encStr = crypt.encryptStringENC(str)

print('Encripty input string')
print('-'*30)
print(f'String: {str} \nCript:{encStr}')
print('-'*30)
print('\nEncripty static strs(ECB/128)\n\n')
group = [
    '1111111111111111',
    '0000000000000000', 
    '0000000000000001', 
    '0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF',#128block
    '0x00000000000000000000000000000000', #128block
    '0x00000000000000000000000000000001'#128block 
]
for x in range(len(group)):
  encStrL = crypt.encryptStringENC(group[x])
  print(f'String:{group[x]}\nEncrypted:{encStrL}\nDecrypted:{crypt.decryptStringENC(encStrL)}')
  print('-'*30) 
  print('\n') 


