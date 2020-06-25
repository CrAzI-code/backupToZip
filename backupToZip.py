#! python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile, os

def backupToZip(folder):
    #back up the entire contents of 'folder' into a zip file

    folder = os.path.abspath(folder) #make sure folder is absolute

    #Figure out the filename this code should use based on
    #what file already  exist

    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    # TODO : Create the ZIP file

    print(f'Creating {zipFilename}...')
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # TODO : Walk the entire folder tree and compress the file in each folder

    for foldername, subfoldersl, filenames in os.walk(folder):
        print(f'Adding files in {foldername}...')
        #Add the current Folder to ZIP file

        backupZip.write(foldername)

        #Add all the files in this folder to the Zip file
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue    #dont back up the backup ZIP files
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()


    print('Done.')


backupToZip('/home/meme/python2/delicious')

