import accumulate_everything
import numpy as np
import _pickle as cPickle



a=accumulate_everything.Data()
print (len(a.data[0]))
print (len(a.data))
for r in range(6037):
    np.random.shuffle(a.data)

f=open(r"C:\Users\Megha Agrawal\Desktop\project\codes\total_data_set\suffle_data_set.csv","w")
for line in a.data:
    a=''
    for item in line:
        a+=str(item)
        a+=","
    a=a.rstrip(',')
    a+="\n"
    f.write(a)
f.close()
