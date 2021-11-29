import os
import sys

sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=40, cols=125))
print('TOKEN : ', os.environ.get('TOKEN'))
print('URL :', os.environ.get('URL'))
