import jinja2
from jinja2 import FileSystemLoader
from jinja2.environment import Environment
import os
import shutil

IGNORE = (
    './.git',
    './deploy'
)

DEST = './deploy'
    

def main():
    env = Environment()
    env.loader = FileSystemLoader('.')
    for root, dirs, files in os.walk('.'):
        if not reduce(lambda acc, x: acc or root.startswith(x), IGNORE, False):
            for f in files: 
                source = os.path.join(root, f)
                dest_root = os.path.join(DEST, root)
                if not os.path.exists(dest_root):
                    os.makedirs(dest_root)
                if os.path.splitext(f)[1] == '.html':
                    with open(os.path.join(dest_root, f), 'w') as df:
                        temp = env.get_template(source)
                        df.write(temp.render())

                else:
                    shutil.copy(source, dest_root)
if __name__ == '__main__':
    main()
