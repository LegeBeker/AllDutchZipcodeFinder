import string
import os
import urllib.request
import tkinter as tk
from pathlib import Path

def submit (start_input, end_input):
    check = digitCheck(start_input, end_input)
    if check == 0:
        label_error = tk.Label(root, text= 'Not 4 numbers entered in field', fg='green', font=('helvetica', 12, 'bold'))
        canvas1.create_window(200, 210, window=label_error)
    else:
        generateFile(start_input, end_input)

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

def generateFile (start, end):
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

canvas1 = tk.Canvas(root, width = 400, height = 220)
canvas1.pack()

info1 = tk.Label(text="This program shows all possible dutch zipcodes in a range")
info2 = tk.Label(text="Made by Volkan Welp out of boredom")

start_info = tk.Label(text="Start zipcode range(4 numbers): ")
start_box = tk.Entry()
start_input = start_box.get()

end_info = tk.Label(text="last zipcode(4 numbers): ")
end_box = tk.Entry()
end_input = end_box.get()

submit = tk.Button(text='submit',command=submit(start_input, end_input))

canvas1.create_window(200, 10, window=info1)
canvas1.create_window(200, 30, window=info2)
canvas1.create_window(200, 60, window=start_info)
canvas1.create_window(200, 90, window=start_box)
canvas1.create_window(200, 120, window=end_info)
canvas1.create_window(200, 150, window=end_box)
canvas1.create_window(200, 180, window=submit)

canvas1.mainloop()