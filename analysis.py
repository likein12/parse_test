# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 12:08:31 2019

@author: miz18
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = []
for line in open("output1.txt","r"):
    data.append(float(line[:-1].split()[0]))

mode = ["0","random"]
mn = len(mode)
input_type = ["horizontal","vertical"]
itn = len(input_type)
parse = ["parsers","default1","default2"]
pn = len(parse)
size = ["1","1e2","1e4","1e5","5e5","1e6","2e6"]
sn = len(size)

#inputの様式ごとに所要時間のグラフを描画
for i in range(mn):
    for j in range(itn):
        df_dat = [[] for _ in range(2)]
        for k in range(pn):
            temp = []
            temp_std = []
            for l in range(sn):
                d = data[i*itn*pn*sn+j*pn*sn+k*sn+l::mn*itn*pn*sn]
                temp.append(np.mean(d))
                temp_std.append(np.std(d,ddof=1))
            left = [3.5*l+0.8*k for l in range(len(size))]
            plt.bar(left,temp,yerr=temp_std)
            df_dat[0].append(temp)
            df_dat[1].append(temp_std)
        plt.title("mode:"+mode[i]+" input type:"+input_type[j],fontsize=16)
        plt.legend(parse,fontsize=16)    
        plt.xlabel("input",fontsize=16)
        plt.ylabel("sec",fontsize=16)
        left = [3.5*l+0.8 for l in range(len(size))]
        plt.xticks(ticks = left, labels = size,fontsize=16)
        plt.savefig("fig_"+mode[i]+"_"+input_type[j]+".png",bbox_inches="tight")
        plt.show()
        df1=pd.DataFrame(df_dat[0])
        df2=pd.DataFrame(df_dat[1])
        df1.index=parse
        df1.columns=size
        df2.index=parse
        df2.columns=size
        df1.to_csv("mean_"+mode[i]+"_"+input_type[j]+".csv")
        df2.to_csv("std_"+mode[i]+"_"+input_type[j]+".csv")

#入力サイズ1e5にのみ注目し、inputの様式ごとに所要時間のグラフを描画
for i in range(mn):
    for j in range(itn):
        plt.figure(figsize=(3, 4))
        for k in range(pn):
            temp = []
            temp_std = []
            l = 3
            d = data[i*itn*pn*sn+j*pn*sn+k*sn+l::mn*itn*pn*sn]
            temp.append(np.mean(d))
            temp_std.append(np.std(d,ddof=1))
            left = [0.8*k]
            plt.bar(left,temp,yerr=temp_std)
        plt.title("mode:"+mode[i]+" input type:"+input_type[j],fontsize=16)
        plt.legend(parse,fontsize=16)    
        plt.xlabel("input",fontsize=16)
        plt.ylabel("sec",fontsize=16)
        plt.ylim(0,0.8)
        left = [0.8]
        plt.xticks(ticks = left, labels = [size[3]],fontsize=16)
        plt.savefig("fig_"+mode[i]+"_"+input_type[j]+"_1e5.png",bbox_inches="tight")
        plt.show()

#using Parsersの所要時間
data = []
for line in open("output2.txt","r"):
    data.append(float(line[:-1].split()[0]))

print("mean: "+str(np.mean(data))+" std: " + str(np.std(data,ddof=1)))