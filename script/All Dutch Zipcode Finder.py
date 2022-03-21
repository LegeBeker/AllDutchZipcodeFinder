import string
import os
import urllib.request
import tkinter as tk
from pathlib import Path

start_input = ''
end_input = ''

home = str(Path.home())


class Functions:
    def submit():
        start_input = start_box.get()
        end_input = end_box.get()
        check = Functions.digitCheck(start_input, end_input)
        if check == 0:
            message_value["text"] = f'Not 4 numbers entered in field(s)'
            message_value.pack()
        elif check == 1:
            message_value["text"] = f"Start value can't be higher than end value"
            message_value.pack()
        elif check == 2:
            message_value["text"] = f''
            message_value.pack()
            Functions.generateFile(start_input, end_input)

    def digitCheck(start, end):
        if (start > end):
            check = 1
        elif len(start) == 4 and start.isdigit() and len(end) == 4 and end.isdigit():
            check = 2
        else:
            check = 0
        return check

    def generateFile(start, end):
        temp1 = os.path.join(
            home, "Desktop/zipcode_temp_" + str(start) + "+" + str(end) + ".txt")
        temp2 = os.path.join(
            home, "Desktop/zipcodes_" + str(start) + "+" + str(end) + ".txt")

        f = open(temp1, "w")

        letters = list(string.ascii_uppercase)

        for n in range(int(start), (int(end) + 1)):
            for l in letters:
                for e in letters:
                    f.write(str(n) + l + e + "\n")
        f.close

        message_value["text"] = f'Loading...'
        message_value["fg"] = 'green'
        message_value.pack()

        url = 'https://volkanwelp.com/documents/zipcodes.txt'
        urllib.request.urlretrieve(url, temp2)

        with open(temp1, 'r') as file1:
            with open(temp2, 'r') as file2:
                same = set(file1) & set(file2)

        same.discard('\n')

        output = os.path.join(
            home, "Desktop/zipcode_output_" + str(start) + "+" + str(end) + ".txt")

        f = open(output, "w")

        for line in same:
            f.write(line)

        f.close
        message_value["text"] = f'Output Generated.'
        message_value.pack()

        message_value["text"] = f'Removing temporary files...'
        message_value.pack()

        os.remove(temp1)
        os.remove(temp2)

        message_value["text"] = f'The output file for ' + str(start) + " to " + str(
            end) + ' can be found on your desktop.\nYou can close this window, or you can get another result.\nThanks for using my program! See my other projects on Github: LegeBeker.'
        message_value.pack()


root = tk.Tk()

root.title("All Dutch Zipcode Finder")

canvas1 = tk.Canvas(root, width=400, height=0)
canvas1.pack()

tk.Label(text="This program shows all possible dutch zipcodes in a range\nMade by Volkan Welp out of boredom.").pack()

tk.Label(text="Start zipcode range(4 numbers): ").pack()
start_box = tk.Entry()
start_box.pack()


tk.Label(text="last zipcode(4 numbers): ").pack()
end_box = tk.Entry()
end_box.pack()

tk.Button(text='submit', command=Functions.submit).pack()
message_value = tk.Label(text="", fg='red')
message_value.pack()

canvas1.mainloop()