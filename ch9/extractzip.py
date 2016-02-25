#! python3

import zipfile, os
os.chdir('c:\\Test')
exampleZip = zipfile.ZipFile('artofwar.zip')
exampleZip.extractall()
exampleZip.close()
print("Your zip file has been extracted!")