#!C:\Users\david.quiroz\Desktop\Develop\Personal\Cursos\Paquete_Propio\python_package\env\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pk-dogsApi==0.0.3','console_scripts','pydogs'
__requires__ = 'pk-dogsApi==0.0.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pk-dogsApi==0.0.3', 'console_scripts', 'pydogs')()
    )
