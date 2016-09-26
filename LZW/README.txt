Name: Rahul Patil

Program Description: Lempel-Ziv-Welch Compression/Decompression Algorithm

File description: encodeLZW.py is the LZW encoder and decodeLZW.py is the LZW decoder.
Programming Language used: Python 2.7.6
Compiler version: GCC 4.8.2


The program takes the scriptname, text file to be compressed/decompressed 
and bit length of the code as arguments in the command line.

encodeLZW.py encodes the given text file and writes the encoded file into
a output file encoded as fileName.lzw. Each encoded output is saved as 2 bytes.
encodeLZW.py takes the input from the text file and creates an initial dictionary
of all the extended ascii characters.
The data structure used to create and maintain the dictionary is the native 
python Dictionary.
For the encoder the dictionary has characters as the key and ascii value as the value.

decodeLZW.py decodes the lzw file and writes the decoded output to a fileName_decoded.txt file. The program creates an initial dictionary of all the extended ascii characters.
The data structure used to create and update the dictionary is the native python Dictionary.
For the decoder the dictionary has ascii values as the key and the character as the value. 

Both the encoder and decoder work for all the test inputs provided. The speed of execution depends on the size of the input.

To run the program:
1. Navigate to the directory containing the inputs and the scripts.
2. For the encoder :
	$python encodeLZW.py fileName.txt <bit length of code>
3. For the decoder:
	$python decodeLZW.py fileName.lzw <bit length of code>