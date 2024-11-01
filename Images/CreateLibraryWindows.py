### This may work on all platforms? needs to be tested
###
import datetime
import os

path = "G:\\apache\\Apache24\\htdocs\\Images\\"

#mt = os.path.getmtime(path)
#print(mt)
#modify_date = datetime.datetime.fromtimestamp(mt)
#print('Modified on:', modify_date)

for f in os.listdir(path):
    file = os.path.join(path, f)
    if os.path.isfile(file):
        print("fileName: " + file)
        print('Modified on: ',datetime.datetime.fromtimestamp(os.path.getmtime(file)))
        #use some sorting alogrithm with a comparator to sort all of these photos
        #and create thresholds for when to split folders
        #and make sure folders have some sort of naming that the server can read easily when returning