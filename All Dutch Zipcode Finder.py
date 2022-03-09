import string
import os
import urllib.request
import tkinter as tk
from pathlib import Path

def submit ():
    check = digitCheck()
    if check == 0:
        message_value["text"] = f'Not 4 numbers entered in field'
        message_value.pack()
    else:
        message_value["text"] = f''
        message_value.pack()
        generateFile()

def digitCheck ():
    if len(start_input) == 4 and int(start_input).isdigit():
        check = 1
        if len(end_input) == 4 and int(end_input).isdigit():
            check = 1
        else:
            check = 0
    else:
        check = 0
    return check

def generateFile ():
    f = open("zipcode_temp.txt", "w")

    letters = list(string.ascii_uppercase)

    for l in letters:
        for e in letters:
            for n in range(int(start_input), (int(end_input) + 1)):
                f.write(str(n) + l + e + "\n")
    f.close

    message_value["text"] = f'Loading...'
    message_value.pack()

    url = 'https://volkanwelp.com/documents/zipcodes.txt'
    urllib.request.urlretrieve(url, 'zipcodes.txt')

    with open('zipcodes.txt', 'r') as file1:
        with open('zipcode_temp.txt', 'r') as file2:
            same = set(file1).intersection(file2)

    same.discard('\n')

    home = str(Path.home())
    path = os.path.join(home, "Desktop/zipcode_output.txt")

    f = open(path, "w")

    for line in same:
        f.write(line)

    f.close
    message_value["text"] = f'Output Generated.'
    message_value.pack()

    message_value["Removing temporary files..."] = f''
    message_value.pack()
    os.remove("zipcode_temp.txt")
    os.remove("zipcodes.txt")    
    message_value["text"] = f'The output file can be found on your desktop.\nYou can close this window. Thanks for using my script!'
    message_value.pack()

root= tk.Tk()

root.title("All Dutch Zipcode Finder")

canvas1 = tk.Canvas(root, width = 400, height = 0)
canvas1.pack()

tk.Label(text="This program shows all possible dutch zipcodes in a range\nMade by Volkan Welp out of boredom").pack()

tk.Label(text="Start zipcode range(4 numbers): ").pack()
start_box = tk.Entry()
start_box.pack()
start_input = start_box.get()

tk.Label(text="last zipcode(4 numbers): ").pack()
end_box = tk.Entry()
end_box.pack()
end_input = end_box.get()

tk.Button(text='submit',command=submit).pack()
message_value = tk.Label(text="", fg='red', font=('helvetica', 12, 'bold'))
message_value.pack()

canvas1.mainloop()