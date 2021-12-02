from algorithms import *
import glob
import os
#Step 1: Read file
pathInput = './input/'
pathOutput = './output/'
count = 1
resultArr = []
for filename in glob.glob(os.path.join(pathInput,'*.txt')):
    with open(os.path.join(os.getcwd(),filename),'r') as file:
        lines = file.readlines()
        values = list(map(lambda x: x.strip(), lines))

        alpha = values[0]
        N = int(values[1])
        kbValues = values[2:]

        check = "YES" if plResolution(kbValues, alpha, resultArr) else "NO" 
        resultArr.append(check)

        fout = open(os.path.join(pathOutput,'output'+str(count)+'.txt'),'w')
        print('Done writing in output'+str(count)+'.txt')
        for res in resultArr:
            fout.write(res)
            fout.write('\n')
        resultArr = []
        count += 1
