import sys
from struct import pack, unpack
import base64
import os

class SHANNON:
    # get the divide postion
    def findDivide(self, flist):
        diflist = []
        for k in range(len(flist)):
            sumA = 0
            sumB = 0
            for i in range(k):
                sumA += flist[i][1]  # first sum
            for i in range(k, len(flist)):
                sumB += flist[i][1]  # second sum
            dif = abs(sumA - sumB)  # difference
            diflist.append((k, dif))  # creat a diflist
        sdiflist = sorted(diflist, key=lambda dif: dif[1])
        return sdiflist[0][0]  # wall is the dividing line

    # shannon-fano-encode the bytelist
    def sfencoder(self, byteList, d):
        if len(byteList) == 2:  # return condition for recursive call
            byteList[0][2] += '0'
            byteList[1][2] += '1'
            return True
        if len(byteList) == 1:
            if d == 'l':
                byteList[0][2] += '0'
            elif d == 'r':
                byteList[0][2] == '1'
            else:
                print
            "illegal parameter"
            return True
        divpos = self.findDivide(byteList)
        for i in range(divpos):
            byteList[i][2] += '0'
        for i in range(divpos, len(byteList)):
            byteList[i][2] += '1'
        self.sfencoder(byteList[:divpos], 'l')
        self.sfencoder(byteList[divpos:], 'r')  # recursive call
        return byteList

    def compress(self, input_file):
        if len(sys.argv) == 2:
            print("no file input")
        else:
            fileName,fileExtension = os.path.splitext(input_file)
            if fileExtension == ".txt":
                fi = open(input_file, "rb")
                infile = bytearray(fi.read())  # turn input into arrays of bytes
            else:
                with open(input_file, "rb") as imageFile:
                    str1 = base64.b64encode(imageFile.read())
                    infile = bytearray(str1)
            size = len(infile)  # size of the bytes array
            print("before encoding the size of the file is", size)
            # print infile
            print("infile", infile)
            # calculate the probability of each byte
            freq = [0] * 256  # initiate the list of probability
            for b in infile:
                freq[b] += 1
            # create a list of lists containing the information
            tuplist = []
            for i in range(256):
                tuplist.append([i, freq[i], ''])

            # sort the freq by probability from most to least
            stuplist = sorted(tuplist, key=lambda tup: tup[1], reverse=True)
            # delete all the elements with possibility zero
            for i in range(len(stuplist)):
                if stuplist[i][1] == 0:
                    indzero = i
                    break
            # map of encoding
            encodedlist = self.sfencoder(stuplist[:indzero], 'l')
            # creat a dictionary for the encoding
            sfdic = {}
            for i in range(len(encodedlist)):
                sfdic[encodedlist[i][0]] = encodedlist[i][2]
            # print sfdic

            # encode the input file
            newfile = ""
            for bite in infile:
                newfile += sfdic[bite]
                # divide the string into substrings of 8 elements
            listofbytes = []
            for i in range(len(newfile) // 8):
                listofbytes.append(newfile[(i * 8):(i * 8 + 8)])
            lstlen = len(listofbytes[len(listofbytes) - 1])
            # append the last element to 8 bits
            if lstlen != 8:
                for i in range(8 - lstlen):
                    listofbytes[len(listofbytes) - 1].append('0')
            dcmlst = []
            for strbyte in listofbytes:
                strbyte = bytearray(strbyte, 'utf8')
                u = 0
                for i in range(8):
                    u += (strbyte[i] - 48) * 2 ** (7 - i)
                dcmlst.append(u)
            flst = bytearray(dcmlst)
            print(infile)
            print(flst)
            out = input_file.split(".")[0]
            output_file = open(out + ".fano", "wb")
            for data in flst:
                output_file.write(pack('>H', int(data)))
            output_file.close()
            if fileExtension == ".txt":
                fi.close()
            print("\nafter the compression the size of the file is", len(flst))