from subprocess import check_output, call
import glob, shutil, os, errno


# location = (some piece fo shit python module that converts city input to coordinates)

# scriptPath is the current location of this .py file
scriptPath = os.path.dirname(os.path.realpath(__file__))
# scriptPath = '/Users/evanhendrix1/Google Drive/programming/python/JournalPhotos/'

'''Create a directory & assign to variable. maybe in the form of a string. (Not doing this for now)'''
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

''' Por que esta while loop esta haciendo por siempre? '''
while True:
    i = 1
    while i <= 5:
        # This needs to break out of while loop somehow if the user hits esc during the screencapture interface
        # nameToSave = os.path.join(sShotPath,  + i + '.jpg'
        pathi = os.path.join(scriptPath, 'photo' + str(i) + '.jpg')
        print 'scriptPath = {}'.format(scriptPath)
        print 'path{} = {}'.format(i, pathi)
        call( ['screencapture', '-T', '0', '-W', pathi ])

        i +=1
    ''' Get date and assign the input to the variable dateVar '''
    if dateVar != 0:

        dateVar = str(raw_input('Enter the fucking date (like this: YEAR-MM-DD) > '))
    # Calls the dayone2 commands that create entries, pulling in photos and date. May need to put commas around sShotPath b/c os.listdir needs input wrapped in commas
    # allSShotsList = os.path.abspath('/Users/evanhendrix1/Google Drive/programming/python/JournalPhotos/TempSShotDir/*')

    # We need the file names without the file paths

    # finds all .jpg files in this dir, puts them in list
    filesGlob = glob.glob(scriptPath + '/*.jpg')
    print 'filesGlob = {}'.format(filesGlob)

    # # takes the path off and leaves just the file names, in the form of strings in a list
    # filesWoPath = [os.path.basename(x) for x in filesGlob]
    # print 'filesWoPath = {}'.format(filesWoPath)

    # Takes out commas, leaves spaces. (Looks at each path (x) which currently are seperated with commas- then it 'joins' them with spaces in between
    spacedFilesWPath = ' '.join(x for x in filesGlob)
    print 'spacedFilesWPath = {}'.format(spacedFilesWPath)

    # call( "dayone2 -d" dateVar, '-p  /Users/evanhendrix1/Google Drive/programming/python/JournalPhotos/', '--', 'new', 'blah'] )

    call( ['dayone2', '-d', dateVar, '-p',  '/Users/evanhendrix1/Google\ Drive/programming/python/JournalPhotos/photo1.jpg', '--', 'new', 'blah'] )

    # Delete directory created earlier
    # shutil.rmtree('/Users/evanhendrix1/Google Drive/programming/python/JournalPhotos/TempSShotDir')

    dateVar = 0
    if raw_input('Type 0 if you\'re done, or any other key to do another entry ') == 0:
        break # returns control to if statement
    else:
        continue # executed if the loop ended normally (no break)
    break # executed if 'continue' was skipped (break)
