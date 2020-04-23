import random
import click
from progress.bar import IncrementalBar
from art import *

def randombyte():
    byte = ''
    for i in range(8):
        byte = byte + str(random.getrandbits(1))
    return byte
def bytestring(size):
    bstr = ""
    increment = 100
    trues = size/increment
    bar = IncrementalBar('Creating...', max=trues,suffix='%(percent)d%%')
    for i in range(size):
        bstr = bstr+randombyte()
        if(i%trues == 0):
            bar.next()
    bar.finish()

Art = text2art("Corruptor.py")
print(Art)


@click.command()
@click.option('--size', default=1000000, help="size of the file in bytes")
@click.option('--filename', prompt='File Name with ext: ' , help='Name of the file you want, with the extention (ex: test.txt)')



def corrupt(size, filename):
    """Simple program that creates a corrupt file of any size, and of any type"""

   
    size = int(size/100)*100
    with open(filename, "wb") as file:
        file.write(str(bytestring(size)).encode())
    

if __name__ == "__main__":
    corrupt()
