import os
import sys
import shutil


def main():
    i = 1
    for x in os.listdir(sys.argv[1]):
        filename = 'a{}.jpg'.format(i)
        filename = os.path.join(sys.argv[1], filename)
        src = os.path.join(sys.argv[1], x)
        shutil.move(src, filename)
        i += 1

    i = 1
    for x in os.listdir(sys.argv[1]):
        filename = '{}.jpg'.format(i)
        filename = os.path.join(sys.argv[1], filename)
        src = os.path.join(sys.argv[1], x)
        shutil.move(src, filename)
        i += 1

main()
