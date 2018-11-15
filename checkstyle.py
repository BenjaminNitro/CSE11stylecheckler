import re
import sys

s = sys.argv
y = 0
n = 1
save = False
if len(sys.argv) == 1:
    print("please enter the file name")
    sys.exit(1)

print("the file you are style-checking is " + s[1])

if(input("is this correct? enter y/n ") == 0):
    print("great")
else:
    sys.exit(1)

if(input("do you wanna save it to a file?  enter y/n ") == 0):
    save = True


toolong = {}
magicNum = {}
tabs = {}
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

def contain_magic(line):
    if ("final" in line) or ("//" in line) or ("*" in line) or ("class" in line):
        return True
    if len(re.findall(r'\d+', line)) > 0:
        x = (re.findall(r'\d+', line))
        x = remove_values_from_list(x, "1")
        x = remove_values_from_list(x, "-1")
        x = remove_values_from_list(x, "0")
        x = remove_values_from_list(x, -1)
        x = remove_values_from_list(x, 0)
        x = remove_values_from_list(x, 1)
        if len(x) > 0:
            return x
    else:
        return False

def style_checker(filename, case = "all"):

    flen = file_len(filename)

    with open(filename, "rt") as fo:
        for x in range(flen):
            oneLine = fo.readline()
            if len(oneLine) > 80:
                toolong[x]=oneLine
            if type(contain_magic(oneLine)) == list:
                magicNum[x] = oneLine
            if "\t" in oneLine:
                tabs[x] = oneLine



style_checker(s[1])

if save:
    with open("style.txt", "wt") as fi:
        fi.write("")

for k,v in toolong.items():
    ln = "line " + str(k) + " is over 80!!!: \n" + v + "\n"
    print(ln)
    if save:
        with open("style.txt", "a+") as fi:
            fi.write(ln)

for k,v in magicNum.items():
    ln = "line " + str(k) + " is magic!: \n" + v+ "\n"
    print(ln)
    if save:
        with open("style.txt", "a+") as fi:
            fi.write(ln)

for k,v in tabs.items():
   ln = "line " + str(k) + " contain tab! \n" + v+ "\n"
   print(ln)
   if save:
       with open("style.txt", "a+") as fi:
           fi.write(ln)
if save:
    print("All style errors are saved into style.txt in the same folder")


