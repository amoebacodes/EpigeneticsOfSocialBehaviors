# %%
import numpy as np
import pandas as pd

top = np.array(pd.read_table("slope_topD1.txt", header=None).iloc[:, 0])
bottom = np.array(pd.read_table("slope_bottomD1.txt", header=None).iloc[:, 0])
all_of_them = np.array(pd.read_table("all_peaksD1.txt", header=None).iloc[:,0])
# print(np.size(top), np.size(bottom), np.size(all_of_them))
def break_string(matrix):
    new_string = []
    for chromosome in matrix:
        chr = chromosome.split(":")[1:-1]
        chr[1], stop = chr[1].split("-")[0], chr[1].split("-")[1]
        chr.append(stop)
        new_string.append(chr)

    df = pd.DataFrame(new_string, index = matrix, columns=["chromosome", "start", "stop"])
    return df


top = break_string(top)
bottom = break_string(bottom)
all_of_them = break_string(all_of_them)
# print(np.size(top), np.size(bottom), np.size(all_of_them))
np.savetxt("posD1.bed", top, delimiter="\t", fmt='%s')
np.savetxt("negD1.bed", bottom, delimiter="\t", fmt='%s')
np.savetxt("allD1.bed", all_of_them, delimiter="\t", fmt='%s')


top = np.array(pd.read_table("slope_topD2.txt", header=None).iloc[:, 0])
bottom = np.array(pd.read_table("slope_bottomD2.txt", header=None).iloc[:, 0])
all_of_them = np.array(pd.read_table("all_peaksD2.txt", header=None).iloc[:,0])
# print(np.size(top), np.size(bottom), np.size(all_of_them))
top = break_string(top)
bottom = break_string(bottom)
all_of_them = break_string(all_of_them)
# print(np.size(top), np.size(bottom), np.size(all_of_them))
np.savetxt("posD2.bed", top, delimiter="\t", fmt='%s')
np.savetxt("negD2.bed", bottom, delimiter="\t", fmt='%s')
np.savetxt("allD2.bed", all_of_them, delimiter="\t", fmt='%s')
# %%
# np.size(np.array(pd.read_table("slope_bottomD2.txt", header=None).dropna().iloc[:, 0]))
# # %%
# all = pd.read_table("all_peaksD1.txt", header=None)
# all.iloc[:,0].size
# # %%
# np.size(np.array(pd.read_table("slope_topD1.txt", header=None).iloc[:, 0]))
# # %%
