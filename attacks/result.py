import os
import numpy as np
from acc import *
a = 'Bi-XCor'
b = 'Wa-kNN'
c = 'Pa-CUMUL'
d = 'Pa-FeaturesSVM'
def get_mean_var(attack_name):
    recalls = []
    pr20s = []
    pr1000s = []
    pr1s = []
    
    rstf = open('./output/'+attack_name+'.rst', "r")

    for line in rstf.readlines()[-10:]: 
        print(line)
        ls = line.split('\t')
        # recall = np.double(ls[-1])
        # precisionorg = np.double(ls[-2])
        # precision = np.double(ls[-3])
        tp = np.double(ls[1])
        wp = np.double(ls[2])
        fp = np.double(ls[3])
        p = np.double(ls[6])
        n = np.double(ls[7])
        acc = [tp, wp, fp, p, n]
        pr1 = acc_to_pr(acc,1)
        pr20 = acc_to_pr(acc,20)
        pr1000 = acc_to_pr(acc,1000)
        recall = acc_to_recall(acc)
        recalls.append(recall)
        pr1s.append(pr1)
        pr20s.append(pr20)
        pr1000s.append(pr1000)
        print(pr20,pr1000,recall)
    rst = "{}\t{}\t{}\t{}\n".format(np.mean(pr1s), np.mean(pr20s), np.mean(pr1000s),np.mean(recalls))

    rstf.close()
    
    rstf = open('./output/'+attack_name+'.rst', "a+")
    rstf.write(rst)
    rstf.close()
    return rst.replace('\t',' ')
# print(get_mean_var(a))
# print(get_mean_var(b))
# print(get_mean_var(c))
print(get_mean_var(d))