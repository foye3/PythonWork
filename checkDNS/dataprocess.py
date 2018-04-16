import re
import matplotlib.pyplot as plt
import numpy as np

def dataprocess(filepath):
    gap = []
    f = open(filepath)
    line = f.readline()

    count = 0
    while line:
        pre = line
        line = f.readline()
        if(pre[:1] == "#"):
            if(line[:1] =="#"):
                count += 1
            elif(count!=0):
                gap.append(count)
                count =0
    f.close()
    return gap
   

gap1 = dataprocess("./digfile1")
gap2 = dataprocess("./digfile2")
gap3 = dataprocess("./digfile3")

plt.plot(np.sort(gap1), np.linspace(0, 1, len(gap1), endpoint=False),label = "www.google.com")
plt.plot(np.sort(gap2), np.linspace(0, 1, len(gap2), endpoint=False),label = "www.bilibili.com")
plt.plot(np.sort(gap3), np.linspace(0, 1, len(gap3), endpoint=False),label = "www.douban.com")


plt.suptitle('CDF')
plt.xlabel('Gap Time(Seconds)')
plt.ylabel('Probability')
plt.legend()
plt.show()