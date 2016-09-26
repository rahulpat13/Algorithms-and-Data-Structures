"""
Name: Rahul Patil

"""
from sys import argv
from struct import *
import math
import os
#Take the input from the text file as a command line argument and store it.
script, filename, N= argv
max_table_size = 2**int(N)
txt = open(filename)
string = txt.read()

#Define the dictionary and its size
dict_size = 256
codes = dict([(chr(x), x) for x in range(dict_size)])
#Initialize
compressed_data = []       
current_string = ""
#If code present in dictionary then current string is substring
#else output the code for the substring and update the dictionary.
#If table size exceeds the maximum table size then use old codes 
#and don't create any new ones.
for c in string:                            #get code
    wcurrent_string = current_string + c
    if (codes.has_key(wcurrent_string)):
        current_string = wcurrent_string
    else:
        compressed_data.append(codes[current_string])
        if(len(codes) <= max_table_size):
            codes[wcurrent_string] = dict_size
            dict_size +=1
        current_string = c
if current_string:
    compressed_data.append(codes[current_string])

#Take the data from compressed_data and store it in binary format bit by bit
file =  os.path.splitext(filename)[0]
output = open(file+'.lzw', 'wb')
for data in compressed_data:
    print data
    output.write(pack('>H', data))

output.close()
txt.close()
