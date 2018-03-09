import re
import matplotlib.pyplot as plt
import numpy as np

routes = []
f = open("./traceFile2")
line = f.readline()
while line:
    pre = line
    line = f.readline()
    if(line == "~~~\n"):
        res = re.findall('\d+\.\d{3} ms',pre)
        for num in res:
            a =  num.strip(' ms')
            routes.append(float(num.strip(' ms')))
f.close()

plt.plot(np.sort(routes), np.linspace(0, 1, len(routes), endpoint=False))
plt.suptitle('Delay time CDF')
plt.xlabel('delay time(ms)')
plt.ylabel('probability')
plt.show()
