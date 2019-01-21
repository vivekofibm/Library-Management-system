# text = "abcdefghijklmnopqrstuvwxyz"
# key = int(input("enter the key : "))
# newtext =''
# message = input("enter any message")
# for character in message:
#     if character in text:
#         postion = text.find(character)
#         newposition = (postion+key)%26
#         newcharacter = text[newposition]
#         newtext += newcharacter
#
#     else:
#         newtext+=character
#
# print("the message is encrypted:",newtext)

##################################

from tkinter import *

text = "abcdefghijklmnopqrstuvwxyz"
key = int(input("enter the key : "))



# def encrypt():
#     key = int(input("enter the key : "))
#     newtext = ''
#     message = input("enter any message")
#     for character in message:
#         if character in text:
#             postion = text.find(character)
#             newposition = (postion + key) % 26
#             newcharacter = text[newposition]
#             newtext += newcharacter
#
#         else:
#             newtext += character
#
#     print("the message is encrypted:", newtext)


# def decrypt():
#     key = int(input("enter the key : "))
#     newtext = ''
#     message = input("enter any message")
#     for character in message:
#         if character in text:
#             postion = text.find(character)
#             newposition = (postion - key) % 26
#             newcharacter = text[newposition]
#             newtext += newcharacter
#
#         else:
#             newtext += character
#
#     print("the message is encrypted:", newtext)


def encrypt():

    newtext = ''
    message = input("enter any message")
    for character in message:
        if character in text:
            postion = text.find(character)
            newposition = (postion + key) % 26
            newcharacter = text[newposition]
            newtext += newcharacter

        else:
            newtext += character

    print("the message is encrypted:", newtext)
def decrypt():
    okey =
    newtext = ''
    message = input("enter any message")
    for character in message:
        if character in text:
            postion = text.find(character)
            newposition = (postion - key) % 26
            newcharacter = text[newposition]
            newtext += newcharacter

        else:
            newtext += character

    print("the message is encrypted:", newtext)


cc=Tk()
cc.geometry('100x100')

btnencyp=Button(cc,text='encrypt',command = encrypt).place(x=10,y=10)
btndecyp=Button(cc,text='decrypt',command = decrypt).place(x=50,y=50)

cc=mainloop()


print(decrypt())



















































# key = 'abcdefghijklmnopqrstuvwxyz'
#
# def encrypt(n, plaintext):
#     """Encrypt the string and return the ciphertext"""
#     result = ''
#
#     for l in plaintext.lower():
#         try:
#             i = (key.index(l) + n) % 26
#             result += key[i]
#         except ValueError:
#             result += l
#
#     return result.lower()
#
#
# def decrypt(n, ciphertext):
#     """Decrypt the string and return the plaintext"""
#     result = ''
#
#     for l in ciphertext:
#         try:
#             i = (key.index(l) - n) % 26
#             result += key[i]
#         except ValueError:
#             result += l
#
#     return result
#
# def show_result(plaintext, n):
#     """Generate a resulting cipher with elements shown"""
#     encrypted = encrypt(n, plaintext)
#     decrypted = decrypt(n, encrypted)
#
#     print('Rotation: %s' % n)
#     print('Plaintext: %s' % plaintext)
#     print('Encrytped: %s' % encrypted)
#     print('Decrytped: %s' % decrypted)








###############################################################################################





























# # Caesar Cipher
#
#
#
# MAX_KEY_SIZE = 26
#
#
#
# def getMode():
#
#      while True:
#
#          print('Do you wish to encrypt or decrypt a message?')
#
#          mode = input().lower()
#          if mode in 'encrypt e decrypt d'.split():
#
#             return mode
#
#          else:
#
#              print('Enter either "encrypt" or "e" or "decrypt" or "d".')
#
#
#
# def getMessage():
#
#      print('Enter your message:')
#
#      return input()
#
#
#
# def getKey():
#
#      key = 0
#
#      while True:
#
#          print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
#
#          key = int(input())
#
#          if (key >= 1 and key <= MAX_KEY_SIZE):
#
#              return key
#
#
#
# def getTranslatedMessage(mode, message, key):
#
#      if mode[0] == 'd':
#
#          key = -key
#
#      translated = ''
#
#
#
#      for symbol in message:
#
#          if symbol.isalpha():
#
#              num = ord(symbol)
#
#              num += key
#
#
#
#              if symbol.isupper():
#
#                  if num > ord('Z'):
#                      num -= 26
#                  elif num < ord('A'):
#
#                      num += 26
#
#              elif symbol.islower():
#
#                  if num > ord('z'):
#
#                      num -= 26
#
#                  elif num < ord('a'):
#
#                      num += 26
#
#
#
#             translated += chr(num)
#
#          else:
#
#              translated += symbol
#
#      return translated
#
#
#
# mode = getMode()
#
# message = getMessage()
#
# key = getKey()
#
#
#
# print('Your translated text is:')
# print(getTranslatedMessage(mode, message, key))