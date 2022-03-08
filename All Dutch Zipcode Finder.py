import string
import os
import urllib.request
import tkinter as tk
from pathlib import Path

def submit (start_input, end_input):
    check = digitCheck(start_input, end_input)
    if check == 0:
        label_error = tk.Label(root, text= 'Not 4 numbers entered in field', fg='green', font=('helvetica', 12, 'bold'))
        canvas1.create_window(150, 200, window=label_error)
    else:
        generateFile()

def digitCheck (start, end):
    if len(start) == 4 and start.isdigit():
        check = 1
        if len(end) == 4 and end.isdigit():
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
            for n in range(int(start), (int(end) + 1)):
                f.write(str(n) + l + e + "\n")
    f.close

    print("loading...")
    print("\n")

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
    print("output generated")

    print("Removing temporary files...")
    os.remove("zipcode_temp.txt")
    os.remove("zipcodes.txt")
    print("Done.")
    print("The output file can be found on your desktop.")
    input("Press Enter to close this terminal. Thanks for using my script!")

root= tk.Tk()

canvas1 = tk.Canvas(root)
canvas1.pack()

info1 = tk.Label(text="This program shows all possible dutch zipcodes in a range")
info2 = tk.Label(text="Made by Volkan Welp out of boredom")

start_info = tk.Label(text="Start zipcode range(4 numbers): ")
start_box = tk.Entry()
start_input = start_box.get()

end_info = tk.Label(text="last zipcode(4 numbers): ")
end_box = tk.Entry()
end_input = end_box.get()

submit = tk.Button(text='submit',command=submit(start_input, end_input), bg='brown',fg='white')

info1.pack()
info2.pack()
start_info.pack()
start_box.pack()
end_info.pack()
end_box.pack()
submit.pack()

canvas1.mainloop()