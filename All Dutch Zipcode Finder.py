import string
import os
import urllib.request
import tkinter as tk
from pathlib import Path

start_input = ''
end_input = ''


class Functions:
    def submit():
        start_input = start_box.get()
        end_input = end_box.get()
        check = Functions.digitCheck(start_input, end_input)
        if check == 0:
            message_value["text"] = f'Not 4 numbers entered in field'
            message_value.pack()
        elif check == 1:
            message_value["text"] = f"Start value can't be higher than end value"
            message_value.pack()
        elif check == 2:
            message_value["text"] = f"Start and end value can't be the same"
            message_value.pack()
        elif check == 3:
            message_value["text"] = f'Not 4 numbers entered in field'
            message_value.pack()
            Functions.generateFile(start_input, end_input)

    def digitCheck(start, end):
        if (start > end):
            check = 1
        elif (start == end):
            check = 2
        elif len(start) == 4 and start.isdigit() and len(end) == 4 and end.isdigit():
            check = 3
        else:
            check = 0
        return check

    def generateFile(start, end):
        home = str(Path.home())
        path_check = 0

        i1 = 0
        i2 = 0

        temp1 = "zipcode_temp.txt"
        temp2 = "zipcodes.txt"

        while path_check != 1:
            path_temp1 = Path(temp1)
            path_temp2 = Path(temp2)
            temp1_check = path_temp1.is_file()
            temp2_check = path_temp2.is_file()
            if (temp1_check == True):
                i1 = i1 + 1
                newtemp1 = temp1.split('.')
                newtemp1[0] = newtemp1[0] + str(i1) + '.'
                temp1 = ''
                for v in newtemp1:
                    temp1 += v

            elif (temp2_check == True):
                i2 = i2 + 1
                newtemp2 = temp2.split('.')
                newtemp2[0] = newtemp2[0] + str(i2) + '.'
                temp2 = ''
                for v in newtemp2:
                    temp2 += v
            else:
                path_check = 1

        f = open(temp1, "w")

        letters = list(string.ascii_uppercase)

        for l in letters:
            for e in letters:
                for n in range(int(start), (int(end) + 1)):
                    f.write(str(n) + l + e + "\n")
        f.close

        message_value["text"] = f'Loading...'
        message_value["fg"] = 'green'
        message_value.pack()

        url = 'https://volkanwelp.com/documents/zipcodes.txt'
        urllib.request.urlretrieve(url, temp2)

        with open(temp2, 'r') as file1:
            with open(temp1, 'r') as file2:
                same = set(file1).intersection(file2)

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
root.tk.call('wm', 'iconphoto', root._w,
             tk.PhotoImage(file='Icons/favicon.ico'))

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
message_value = tk.Label(text="", fg='red', font=('helvetica', 12, 'bold'))
message_value.pack()

canvas1.mainloop()
