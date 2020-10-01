#!/usr/bin/env python3
from argparse import ArgumentParser
from base64 import b64decode as b64d
from zlib import decompressobj,MAX_WBITS
from os import path

parser = ArgumentParser()
parser.add_argument('-f', '--file', required=False, help="File to decompress")
parser.add_argument('-d', '--decode', required=False, help="Base64 encoded gzip/zlib to decompress")
args = parser.parse_args()

#----------------------------------------------
#Define Funcitons
#----------------------------------------------
def parsefile(fname):
  if not path.isfile(fname):
    print("[*] File not found")
    exit()
  
  file = open(fname, 'rb').read()
  if type(file) is not bytes:
    print("[*] String not bytes detected in file. Compressed content is always bytes.")
    exit()
  
  return file

def decompress(compressed):
  output=""
  try:
    z = decompressobj()
    output = z.decompress(compressed)
    if output:
      print(output.decode())
  except:
    pass
  if output:
    exit()
    
  try:
    z = decompressobj(16+MAX_WBITS)
    output = z.decompress(compressed)
    if output:
      print(output.decode())
      exit()
  except:
    pass
  if output:
    exit()
  
  #if it got this far, it didn't work.
  print("[!] Unable to decompress with zlib, or gzip methods")
  exit()
  
#----------------------------------------------
#Start script
#----------------------------------------------
if args.file:
  c = parsefile(args.file)
elif args.decode:
  c = b64d(args.decode)

decompress(c)




  
