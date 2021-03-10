#!C:\Users\iparv\Desktop\SoftUni\Python\Text_Processing\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'reverse==0.1.0','console_scripts','reverse'
__requires__ = 'reverse==0.1.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('reverse==0.1.0', 'console_scripts', 'reverse')()
    )
