# Copying a file
from os import strerror

# Reading the source file
sourcename = input("Source file name?: ")
try:
    src = open(sourcename, 'rb') # open in read-bytes mode
except IOError as e: # Open file error
    print("Cannot open source file: ", strerror(e.errno))
    exit(e.errno)
'''Note: use the exit() function to stop program execution and to pass
the completion code to the OS; any completion code other than 0 says
that the program has encountered some problems.
use the errno value to specify the nature of the issue.'''
    
# Making a copy into a destination file
dstname = input("Destination file name?: ")
try:
    dst = open(dstname, 'wb')
except Exception as e:
    print("Cannot create destination file: ", strerror(e.errno))
    exit(e.errno)

buffer = bytearray(65536) # 64 KB buffer - it's the memory size for transfering data
total = 0

try:
    reading = src.readinto(buffer) # reading the contents inside source file (it's an integer)
    while reading > 0: # number of bytes read
        written = dst.write(buffer[:reading]) # writing what was read into destination file
        # requires a bytes-like object to write
        # we used a slice to limit the number of bytes being written to the output file
        # if you don't slice it, your outpute file will be 64 kb
        total += written # counts the number of bytes copied
        reading = src.readinto(buffer)# read the next file chunk
except IOError as e:
    print("Cannot create destination file: ", strerr(e.errno))
    exit(e.errno)

print(total, 'byte(s) succesfully written')
src.close()
dst.close()
                   
