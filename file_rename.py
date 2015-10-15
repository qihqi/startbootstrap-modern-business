import os
import sys
import shutil


def main():
    i = 2 
    for x in os.listdir(sys.argv[1]):
        if x.startswith('IMG'):
            filename = '{}.jpg'.format(i)
            filename = os.path.join(sys.argv[1], filename)
            src = os.path.join(sys.argv[1], x)
            shutil.move(src, filename)
            i += 1

main()
