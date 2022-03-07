import string
import os
import urllib.request
import numbers
import sys
from pathlib import Path

letters = list(string.ascii_uppercase)

print("This program shows all possible zipcodes in a range")
print("Made by Volkan Welp out of boredom")
print("\n")

while True:
    start = input("Start zipcode range(4 numbers): ")
    if len(start) == 4 and start.isdigit():
        break
    print("Invalid input")
print("\n")

while True:
    end = input("last zipcode(4 numbers): ")
    if len(end) == 4 and end.isdigit():
        break
    print("Invalid input")
print("\n")

f = open("zipcode_temp.txt", "w")

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
print("\n")

print("Removing temporary files...")
print("\n")
os.remove("zipcode_temp.txt")
os.remove("zipcodes.txt")

print("Done.")
print("The output file can be found on your desktop.")
input("Press Enter to close this terminal. Thanks for using my script!")
