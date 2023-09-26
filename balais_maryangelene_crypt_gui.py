#BALAIS, MARY ANGELENE V. - BSIS-NS-2B-M
#OOP ACTIVITY #5 - MODIFICATION OF ACTIVITY #1(CRYPTOGRAM) WITH GUI IMPLEMENTATION

from tkinter import *
from tkinter import messagebox as x
#import os

class GUI:
    def __init__(self):
        #MAIN SCREEN OR PAGE
        self.screen=Tk()
        self.screen.geometry("500x570")
        self.screen.resizable(False,False)
        self.screen.title("Ceasar Cipher - Cryptography") #TAB/WINDOW TITLE
        self.screen.configure(bg="#FCFFE0")

        #TITLE OF THE PROGRAM
        Label(text="     ENCRYPTION AND DECRYPTION     ", fg="black", bg="#F3DCD4", font=("courier", 20)).place(x=40,y=10)

        #Encryption Labels, Text Widgets, Button   
    #Plain Text Input to Be Converted to Ceasar Cipher Text
        Label(text="Enter Word/s to Encrypt", fg="black", bg="#ACDDDE", font=("courier new", 14)).place(x=155,y=55)
        self.box1 = Text(self.screen, font=("courier, 14"), width=40, height=2)
        self.box1.place(x=50, y=80)

    #Ceasar Cipher Shift Key Number Input 1 to 25    
        Label(text="Caesar Cypher Shift Number", fg="black", bg="#E1F8DC",font=("courier new", 14)).place(x=150,y=135)
        self.box2 = Text(self.screen, font=("courier, 14"), width=2, height=1)
        self.box2.place (x=240, y=160)
        
        #BUTTON FOR ENCRYPTION
        Button(command=self.Encryption, text="ENCRYPT",height="1", width=7, font="courier", fg="black", bg="blue" ).place(x=205, y=195) 

    #Converted plain text to cipher text    
        Label(text="CODE:", fg="black", bg="#FCFFE0", font=("Arial ", 14)).place(x=230,y=225)
        self.EncryptedText = StringVar()
        self.box3 = Entry(self.screen,textvariable=self.EncryptedText, font=("courier, 14")).place (x=100, y=245, width=300, height=30)
    
        #Decryption Labels, Text Widgets, Button
    #Converting of Cipher text to Plain or Original Text    
        Label(text="Enter Code to Decrypt Word/s", fg="black", bg="#ACDDDE", font=("courier new", 14)).place(x=140,y=310)
        self.box4 = Text(self.screen, font=("courier, 14"), width=40, height=2)
        self.box4.place (x=70, y=335)

    #Ceasar Cipher Shift Key Number Input    
        Label(text="Enter Decryption Integer", fg="black", bg="#E1F8DC", font=("courier new", 14)).place(x=170,y=390)
        self.box5 = Text(self.screen, font=("courier, 14"), width=2, height=1)
        self.box5.place (x=240, y=415)
        
        #BUTTON FOR DECRYPTION
        Button(command=self.Decryption, text="DECRYPT", height="1", width=7, font="courier", fg="black").place(x=205, y=450) 

    #Converted cipher text to plain text    
        Label(text="DECRYPTED WORD/S:", fg="black", bg="#FCFFE0", font=("Arial ", 14)).place(x=175,y=480)
        self.DecryptedText = StringVar()
        self.box6 = Entry(self.screen, textvariable=self.DecryptedText, font=("courier, 14")).place (x=100, y=500, width=300, height=60)
    
        self.screen.mainloop()

#ENCRYPTION BUTTON COMMAND FUNCTION
    def Encryption(self):
        encoded_character = self.box1.get('1.0', 'end-1c')
            #Error Message if shift key input is invalid/not an integer.
        while True:
                try:
                    number_shift = int(self.box2.get('1.0', 'end-1c'))
                    break
                except ValueError:
                    self.error = x.showerror(message="You are X to me...", title="Error!")
                    self.box2.delete('1.0', 'end-1c')
                    number_shift = int(self.box2.get('1.0', 'end-1c'))

        print(encoded_character,number_shift)
        encrypt = ' ' #ENCODING
        for number in range(len(encoded_character)):
    
    #Uppercase and Lowercase Conditions
            char = encoded_character[number]
            if (char.isupper()): 
                encrypt = encrypt + chr((ord(char) + number_shift - 65) % 26 + 65)
            elif (char.islower()):
                encrypt = encrypt + chr((ord(char) + number_shift - 97) % 26 + 97)
    
    #Special characters or Symbols
            else:
                symbol = ord(char)
                if (symbol> 31) and (symbol < 65): 
                    encrypt = encrypt + chr((ord(char) + number_shift - 32) % 33 + 32)
                elif (symbol > 90) and (symbol < 97): 
                    encrypt = encrypt + chr((ord(char) + number_shift - 90) % 6 + 90)
                else: 
                    encrypt = encrypt + chr((ord(char) + number_shift - 122) % 4 + 122)       

#Printing of Encrypted Code
    #Converted plain text to cipher text = encryption process
        self.EncryptedText.set(encrypt)

#DECRYPTION BUTTON COMMAND FUNCTION
    def Decryption(self):
        decoded_character = self.box4.get('1.0', 'end-1c')
            #Error Message if shift key input is invalid/not an integer.
        while True:
                try:
                    decryption_key = int(self.box5.get('1.0', 'end-1c'))
                    break
                except ValueError:
                    self.error = x.showerror(message="You are X to me...", title="Error!")
                    self.box5.delete('1.0', 'end-1c')
                    decryption_key = int(self.box5.get('1.0', 'end-1c'))
        print(decoded_character,decryption_key)

        decrypt = ' ' #DECODING
        for number in range(len(decoded_character)):
            char = decoded_character[number]

    #Uppercase and Lowercase Conditions
            if (char.isupper()): 
                decrypt += chr((ord(char) - decryption_key - 65) % 26 + 65)
            elif (char.islower()): 
                decrypt += chr((ord(char) - decryption_key - 97) % 26 + 97)
    
    #Special characters or Symbols
            else:
                symbol = ord(char) 
                if (symbol > 31) and (symbol < 65):
                    decrypt += chr((ord(char) - decryption_key - 32) % 33 + 32)
                elif (symbol > 90) and (symbol < 97):
                    decrypt += chr((ord(char) - decryption_key - 90) % 6 + 90)
                else:
                    decrypt += chr((ord(char) - decryption_key - 122) % 4 + 122)

#Printing of Decrypted Texts
    #Converted cipher text to plain text = decryption process
        self.DecryptedText.set(decrypt)    
GUI()