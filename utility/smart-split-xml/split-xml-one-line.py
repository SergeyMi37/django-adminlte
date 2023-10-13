#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
# использование - split.py имя_файла splitsizeinkb tag starttag
# .\split.py c:\!\SpecCharacteritics.xml 100000 specCharacteritics SpecCharacteriticsS
# python3 split-xml-one-line.py SpecCharacteritics.xml 800000 specCharacteritics SpecCharacteriticsS
def getfilesize(filename):
   with open(filename,"rb") as fr:
       fr.seek(0,2) # move to end of the file
       size=fr.tell()
       print(f"getfile: {filename} size: {size}")
       return fr.tell()

def addfile(filename,added_str):
   with open(filename,"a") as fra:
       fra.seek(0,2) # move to end of the file
       fra.write(added_str)
       print(" added ",added_str)
       fra.close()

def splitfile(filename, splitsize, tag_del, start_tag):
   # Open original file in read only mode
   if not os.path.isfile(filename):
       print("No such file as: \"%s\"" % filename)
       return

   filesize=getfilesize(filename)
   with open(filename,"rb") as fr:
    counter=1
    orginalfilename = filename.split(".")
    readlimit = 5000 #read 5kb at a time
    n_splits = filesize//splitsize
    print("splitfile: No of splits required: %s" % str(n_splits))
    for i in range(n_splits+1):
        chunks_count = int(splitsize)//int(readlimit)
        data_5kb = fr.read(readlimit) # read
        str_tag=str(data_5kb)
        str_tag=str_tag.split("<"+tag_del+">")[0]

        if str("<"+start_tag+">") not in str(str_tag):
            print(counter, type(str_tag), str_tag)
            data_5kb=bytes("<"+start_tag+">",'utf-8')+data_5kb[len(str_tag)-2:]
            #data_5kb=bytes("<"+start_tag+">",'raw_unicode_escape')+data_5kb[len(str_tag)-2:]
            addfile(fname,str_tag[2:]+"</"+start_tag+">")
        # Create split files
        print("chunks_count: %d" % chunks_count)
        fname=orginalfilename[0]+".xml_{id}.".format(id=str(counter))+orginalfilename[1]
        #with open(orginalfilename[0]+"_{id}.".format(id=str(counter))+orginalfilename[1],"ab") as fw:
        with open(fname,"ab") as fw:
            fw.seek(0) 
            fw.truncate()# truncate original if present
            while data_5kb:                
                fw.write(data_5kb)
                if chunks_count:
                    chunks_count-=1
                    data_5kb = fr.read(readlimit)
                else: break
            fw.close()
        counter+=1 

if __name__ == "__main__":
   if len(sys.argv) < 3:
       print("Filename or splitsize not provided:\n Usage: filesplit.py filename splitsizeinkb tag")
   else:
       filesize = int(sys.argv[2]) * 1000 #make into kb
       filename = sys.argv[1]
       tag_del = sys.argv[3]
       start_tag = sys.argv[4]
       splitfile(filename, filesize, tag_del, start_tag)