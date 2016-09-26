"""
Name: Rahul Patil

"""
from sys import argv
from struct import *
import os
#Take the input from the lzw file and bit length as command line arguments and store the
#contents of the file
script, filename, N= argv
max_table_size =  2**int(N)
txt = open(filename, "rb")
compressed_data = []
while True:
    rec = txt.read(2) 
    if len(rec) != 2:
        break
    (pos,) = unpack('>H', rec)
    print pos
    compressed_data.append(pos)
#Create the dictionary
strings = dict([(x, chr(x)) for x in range(256)])
#Initialization
next_code = 256
decompressed_string = ""
previous_string = ""
#While there are codes to receive
for c in compressed_data:
#If symbol not in dictionary new string is substring else use the table entry to decode
    if not (strings.has_key(c)):
        strings[c] = previous_string + (previous_string[0])
    decompressed_string += strings[c]
#If length of previous string is not zero then output is previous string plus new string
    if not(len(previous_string) == 0):
        strings[next_code] = previous_string + (strings[c][0])
        next_code +=1
    previous_string = strings[c]
print decompressed_string
#output the decompressed file
file =  os.path.splitext(filename)[0]
output = open(file+'_decoded.txt', 'w+')
for data in decompressed_string:
	output.write(data)
#close all the opened files
output.close()
txt.close()
