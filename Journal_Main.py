from subprocess import check_output, call, list2cmdline
import glob, shutil, os, errno, time


# location = (some piece fo shit python module that converts city input to coordinates)

# scriptPath is the current location of this .py file
scriptPath = os.path.dirname(os.path.realpath(__file__))
# scriptPath =

#Create a directory & assign to variable. maybe in the form of a string. (Not doing this for now)
# try:
#     os.mkdir(path)
# except OSError as exc: # Guard against race condition
#     if exc.errno != errno.EEXIST:#andos.path.isdir(path):
#         pass
#     else:
#         raise

# sShotPath = os.path.abspath(path)

# print 'sShotPath is: ', sShotPath
print 'Start program...'

dateVar = '0'
dateVarPrior = '0'

while True:
    i = 1
    while i <= 5:
        #in = raw_input('If you\'re done, enter 0; if not hit any key)
        print 'Starting new scan. You just scanned date ', dateVarPrior
        # This needs to break out of while loop somehow if the user hits esc during the screencapture interface
        # nameToSave = os.path.join(sShotPath,  + i + '.jpg'
        pathi = os.path.join(scriptPath, 'photo' + str(i) + '.jpg')
        print 'scriptPath = {}'.format(scriptPath)
        print 'path{} = {}'.format(i, pathi)
        call( ['screencapture', '-T', '0', '-W', pathi ])
        time.sleep(1)

        i +=1
    # Get date and assign the input to the variable dateVar. I need to put in some text processing to allow me to omit slashes for speed.
    if dateVar != 0:
        dateVar = '"' + str(raw_input('Enter the fucking date (like this: MM/DD/YY) > ')) + '"'
        print "dateVar variable is: ", dateVar

        # formattedDateVar =
    # Calls the dayone2 commands that create entries, pulling in photos and date. May need to put commas around sShotPath b/c os.listdir needs input wrapped in commas
    # allSShotsList = os.path.abspath('/Users/evanhendrix1/Google Drive/programming/python/JournalPhotos/TempSShotDir/*')

    # We need the file names without the file paths
    # Deletes existing .jpg files in folder
    # filelist = glob.glob("*.jpg")
    # for f in filelist:
    #     os.remove(f)

    # finds all .jpg files in this dir, puts them in list
    filesGlob = glob.glob(scriptPath + '/*.jpg')
    print 'filesGlob = {}'.format(filesGlob)

    # takes the path off and leaves just the file names, in the form of strings in a list
    # filesWoPath = [os.path.basename(x) for x in filesGlob]
    # print 'filesWoPath = {}'.format(filesWoPath)

    # Takes out commas, leaves spaces. (Makes each 'x' ..?
    # spacedFiles = '"' + '" "'.join([str(x) for x in filesGlob]) + '"'
    # #spacedFiles2 =
    # print 'spacedFiles = {}'.format(spacedFiles)
    #
    #
    # for j in range(0,i):
    #     filesString = []
    #     filesString.append(filesGlob[j])
    #     print 'filesString variable is: {}'.format(filesString)

    # In the command line, this formating works: dayone2 -d '05/17/17' -p "/Users/evanhendrix1/Google Drive/programming/python/JournalPhotos/photo1.jpg" "/Users/evanhendrix1/Google Drive/programming/python/JournalPhotos/photo2.jpg" -- new x
    call( [ 'dayone2', '-d', dateVar, '-p', filesGlob[0], filesGlob[1], filesGlob[2], filesGlob[3], filesGlob[4], '--', 'new', 'x' ])
    # print list2cmdline([ 'dayone2', '-d', dateVar, '-p', spacedFiles, '--', 'new', 'x' ])

    # Delete directory created earlier
    # shutil.rmtree('/Users/evanhendrix1/Google Drive/programming/python/JournalPhotos/TempSShotDir')
    dateVarPrior = dateVar
    dateVar = '0'
    if raw_input('Type 0 if you\'re done, or any other key to do another entry ') == 0:
        break # returns control to if statement
    else:
        continue # executed if the loop ended normally (no break)
    break # executed if 'continue' was skipped (break)
