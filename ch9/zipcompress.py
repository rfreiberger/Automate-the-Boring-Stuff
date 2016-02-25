#! python3

# Zip and compress

import zipfile, os
os.chdir('C:\\Test')   # move to the folder with example.zip
exampleZip = zipfile.ZipFile('spam.zip')
exampleZip.namelist()
spamInfo = exampleZip.getinfo('spam.txt')
spamInfo.file_size
spamInfo.compress_size
print('Compress file is %sx smaller!' % (round(spamInfo.file_size / spamInfo.compress_size, 2)))
exampleZip.close()