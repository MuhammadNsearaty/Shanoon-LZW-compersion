import base64
from struct import unpack, pack
import numpy as np
#from partd import numpy
import os
from PIL import Image

class LZW:
    def decompress(self, input_file):
        n = 1024
        maximum_table_size = pow(2, int(n))
        file = open(input_file, "rb")
        compressed_data = []
        next_code = 256
        decompressed_data = ""
        string = ""

        lines = file.readlines()
        fileExtension = lines[len(lines)-1].decode('utf-8')
        lines = lines[:-1]
        file.close()
        with open(input_file, 'wb') as fr:
            for line in lines:
                fr.write(line)
        fr.close()

        # Reading the compressed file.
        file = open(input_file, "rb")
        while True:
            rec = file.read(2)
            if len(rec) != 2:
                break
            (data,) = unpack('>H', rec)
            compressed_data.append(data)

        print("co",compressed_data)
        # Building and initializing the dictionary.
        dictionary_size = 256
        dictionary = dict([(x, chr(x)) for x in range(dictionary_size)])
        print("dictionary", dictionary)
        # iterating through the codes.
        # LZW Decompression algorithm
        for code in compressed_data:
            if not (code in dictionary):
                dictionary[code] = string + (string[0])
            decompressed_data += dictionary[code]
            if not (len(string) == 0):
                dictionary[next_code] = string + (dictionary[code][0])
                next_code += 1
            string = dictionary[code]

        if fileExtension == ".txt":
            # storing the decompressed string into a file.
            out = input_file.split(".")[0]
            fileName = out+".txt"
            output_file = open(fileName, "w")
            for data in decompressed_data:
                output_file.write(data)
            output_file.close()
            file.close()
            return output_file

        else:
            out = input_file.split(".")[0]
            imageName = out+fileExtension
            imgdata = base64.b64decode(decompressed_data)
            with open(imageName, 'wb') as f:
                f.write(imgdata)
            return "hello"

    def compress(self, input_file):
        # input_file = "New Text Document (6).txt"
        n = 1024
        maximum_table_size = pow(2, int(n))
        fileName, fileExtension = os.path.splitext(input_file)
        if fileExtension == ".txt":
            file = open(input_file)
            data = file.read()
            file.close()
        else:
            with open(input_file, "rb") as img_file:
                data = base64.b64encode(img_file.read())
                data = str(data,'utf-8')

            #data = self.get_image_values(input_file)

        print("data : ",data,"\nsize before : ",len(data))
        dictionary_size = 256
        dictionary = {chr(i): i for i in range(dictionary_size)}
        string = ""  # String is null.
        compressed_data = []  # variable to store the compressed data.

        # iterating through the input symbols.
        # LZW Compression algorithm
        for symbol in data:
            string_plus_symbol = string + symbol  # get input symbol.
            if string_plus_symbol in dictionary:
                string = string_plus_symbol
            else:
                compressed_data.append(dictionary[string])
                if len(dictionary) <= maximum_table_size:
                    dictionary[string_plus_symbol] = dictionary_size
                    dictionary_size += 1
                string = symbol

        if string in dictionary:
            compressed_data.append(dictionary[string])
        print("compressed",compressed_data,"\nsize after : ",len(compressed_data))
        # storing the compressed string into a file (byte-wise).

        out = input_file.split(".")[0]
        output_file = open(out + ".lzw", "wb")

        for data in compressed_data:
            output_file.write(pack('>H', int(data)))
        output_file.write(("\n"+fileExtension).encode('utf-8'))

        return out
