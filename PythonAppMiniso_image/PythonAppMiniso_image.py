import urllib.request
import os
import re

import sys
import time

# ProgressBar function
def updt(total, progress):
    """
    Displays or updates a console progress bar.

    Original source: https://stackoverflow.com/a/15860757/1391441
    """
    barLength, status = 20, ""
    progress = float(progress) / float(total)
    if progress >= 1.:
        progress, status = 1, "\r\n"
    block = int(round(barLength * progress))
    text = "\r[{}] {:.0f}% {}".format(
        "#" * block + "-" * (barLength - block), round(progress * 100, 0),
        status)
    sys.stdout.write(text)
    sys.stdout.flush()

# Input full file name
fname = input("Enter file name: ")
if (len(fname) < 1): fname = "d:\\gospoduro\\OneDrive\\work\\miniso\\image\\python\\2021-07-29_no_image_1245_local_python_2.txt"
#
fhand = open(fname)
#
for line in fhand:
    url = line
    img = urllib.request.urlopen(url).read()
    filenamejpg = url.split('/')[-1]
    filenamejpg = re.sub(r"-1.jpg\n", "-1.jpg", filenamejpg)
    path = "d:\\gospoduro\\OneDrive\\work\\miniso\\image\\python\\test8\\"
    sku = re.sub(r"-1.jpg", "", filenamejpg)
    os.mkdir("d:\\gospoduro\\OneDrive\\work\\miniso\\image\\python\\test8\\"+ sku)
    fullfilename = path + sku + "\\" + filenamejpg
    out = open(fullfilename , "wb")
    out.write(img)
    out.close

# ProgressBar
    runs = 1
    for run_num in range(runs):
        print(sku)
        time.sleep(.1)
        updt(runs, run_num + 1)
# End
print("End of list in file: " + fname)



'''
test data
#url = "https://miniso-pic.oss-cn-shenzhen.aliyuncs.com/4891403011047-1.jpg"

https://miniso-pic.oss-cn-shenzhen.aliyuncs.com/4891403011047-1.jpg
https://miniso-pic.oss-cn-shenzhen.aliyuncs.com/4516722355695-1.jpg
https://miniso-pic.oss-cn-shenzhen.aliyuncs.com/4516722355657-1.jpg
https://miniso-pic.oss-cn-shenzhen.aliyuncs.com/4516722355671-1.jpg
https://miniso-pic.oss-cn-shenzhen.aliyuncs.com/4516722355688-1.jpg

'''




