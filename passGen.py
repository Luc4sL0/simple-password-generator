import tkinter as ui
from tkinter import Menu, messagebox

import random
import os
import pyperclip as p


defaultCharSet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
complexCharSet = "!@#$%&*()[]+-=;,.:<>"

path = './password.txt'

def generatedPassWindowImplementation(password):
    p.copy(password)
    messagebox.showinfo(title='RESULT', message='(The password is already backed up to your clipboard) Your new password is: ' + password)

def errorWindowImplementation():
    messagebox.showerror(title='ERROR', message='The value on text box is invalid or empty!')

def generatePassword(numOfChars, isComplex = False, isSaved = False):

    try:
        numCharsInt = int(numOfChars)
        selectedCharSet =''
        tempStr = ''

        tempCounter = 1

        if isComplex == True:
            selectedCharSet = defaultCharSet + complexCharSet
        else:
            selectedCharSet = defaultCharSet

        while tempCounter <= numCharsInt:
            randomChoice = random.randint(0, len(selectedCharSet) - 1)
            tempStr += selectedCharSet[randomChoice]
            tempCounter += 1      

        generatedPassWindowImplementation(tempStr)

        if isSaved == True:
            file = open('password.txt', 'w')
            file.write(tempStr)
            file.close()

    except ValueError:
        errorWindowImplementation()
        return

def loadSavedFileWindowImplementation():
    if os.path.isfile(path):
        file = open('password.txt', 'r')
        messagebox.showinfo(title="SAVED PASSWORD", message="(The password is already backed up to your clipboard) The last password saved in this application is: " + file.read())
        p.copy(file.read())
        file.close()
    else:
        messagebox.showwarning(title='NO SAVED PASSWORD', message="You don't have any saved password!")

def creditsWindowImplementation():
    messagebox.showinfo(title="DEVELOPERS", message="Lucas Lopes Baroni")

def mainWindowImplementation():
    mainWindow = ui.Tk()
    mainWindow.title('Password Generator')
    mainWindow.iconbitmap("passwordLogo.ico") 

    menubar = Menu()
    
    menubar.add_command(label = 'Saved',command=loadSavedFileWindowImplementation)
    menubar.add_command(label = 'Credits', command=creditsWindowImplementation)
    menubar.add_command(label = 'Exit', command=quit)
 
    mainWindow.config(menu = menubar)
    
    descriptionLabel = ui.Label(text='Complete the boxes bellow to generate your new password!')
    descriptionLabel.grid(column=0,row=0,padx=20,pady=20)

    numTextTitleLabel = ui.Label(text='Password Chars', font='Impact')
    numTextTitleLabel.grid(column=0, row=2, padx=5, pady=5)

    numTextDecriptionLabel = ui.Label(text='Insert the number of password chars.')
    numTextDecriptionLabel.grid(column=0, row=3, padx=5, pady=5)

    numText = ui.Entry()
    numText.grid(column=0, row=4, padx=5, pady=5)

    stateValue = ui.BooleanVar()
    complexState = ui.Checkbutton(text="Complex Chars", font='Impact', variable=stateValue)
    complexState.grid(column=0, row=6, padx= 5, pady=5)
    complexStateDescription = ui.Label(text='If this options was marked, complex chars can appear in your password.')
    complexStateDescription.grid(column=0, row=7, padx= 5, pady=5)

    savePassValue = ui.BooleanVar()
    complexState = ui.Checkbutton(text="Save Password", font='Impact', variable=savePassValue)
    complexState.grid(column=0, row=9, padx= 5, pady=5)
    complexStateDescription = ui.Label(text='If this options was marked, your password will be saved in a file.')
    complexStateDescription.grid(column=0, row=10, padx= 5, pady=5)

    ui.Button(text='Generate password', command= lambda: generatePassword(numText.get(), stateValue.get(), savePassValue.get())).grid(column=0, row=12, padx= 20, pady=20)
    mainWindow.resizable(False, False)
    mainWindow.mainloop()

mainWindowImplementation()