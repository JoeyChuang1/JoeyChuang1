import os, sys
import os.path as osp
import argparse
import json  
import re
import pandas as pd
import math


def find_fin(twilight_result2, Output_String):
    a = []
    for x in range(Output_String):
        if (len(list(twilight_result2.keys())) == 0):
            return a
        max_key = max(twilight_result2, key=twilight_result2.get)
        a.append(max_key)
        del twilight_result2[max_key]
    return a

def find_tfidf(pony_dict, pony_idf):
    a = {}
    for key in pony_dict:
        a[key] = round(pony_dict[key] * pony_idf[key], 4)
    return a

def find_idf(Ori_Dict, pony_dict):
    Dict_TS = Ori_Dict['twilight sparkle']
    Dict_FS = Ori_Dict['fluttershy']
    Dict_RR = Ori_Dict['rarity']
    Dict_PP = Ori_Dict['pinkie pie']
    Dict_AJ = Ori_Dict['apple jack']
    Dict_RD = Ori_Dict['rainbow dash']
    a = {}
    for b in pony_dict:
        counter = 0 
        if (b in Dict_TS):
            counter = counter + 1
        if (b in Dict_FS):
            counter = counter + 1
        if (b in Dict_RR):
            counter = counter + 1
        if (b in Dict_PP):
            counter = counter + 1
        if (b in Dict_AJ):
            counter = counter + 1
        if (b in Dict_RD):
            counter = counter + 1
        a[b] = math.log(6/counter)

    return a

def main():
    ######## Initialization ########
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--input')
    parser.add_argument('-n', '--output')
    args = parser.parse_args()
    Input_String = f'{args.input}'
    Output_String = int(args.output)




    
    with open(Input_String, 'r') as d:
        Ori_Dict = json.load(d)
    

    fluttershy_result1 = find_idf(Ori_Dict, Ori_Dict['fluttershy'])
    fluttershy_result2 = find_tfidf(Ori_Dict['fluttershy'], fluttershy_result1)
    maximum_list_fs = find_fin(fluttershy_result2, Output_String)

    rarity_result1 = find_idf(Ori_Dict, Ori_Dict['rarity'])
    rarity_result2 = find_tfidf(Ori_Dict['rarity'], rarity_result1)
    maximum_list_rr = find_fin(rarity_result2, Output_String)

    pinkie_result1 = find_idf(Ori_Dict, Ori_Dict['pinkie pie'])
    pinkie_result2 = find_tfidf(Ori_Dict['pinkie pie'], pinkie_result1)
    maximum_list_pp = find_fin(pinkie_result2, Output_String)

    apple_result1 = find_idf(Ori_Dict, Ori_Dict['apple jack'])
    apple_result2 = find_tfidf(Ori_Dict['apple jack'], apple_result1)
    maximum_list_aj = find_fin(apple_result2, Output_String)

    Rainbow_result1 = find_idf(Ori_Dict, Ori_Dict['rainbow dash'])
    Rainbow_result2 = find_tfidf(Ori_Dict['rainbow dash'], Rainbow_result1 )
    maximum_list_rd = find_fin(Rainbow_result2, Output_String)

    twilight_result1 = find_idf(Ori_Dict, Ori_Dict['twilight sparkle'])
    twilight_result2 = find_tfidf(Ori_Dict['twilight sparkle'], twilight_result1)
    maximum_list_ts = find_fin(twilight_result2, Output_String)
    
    a = {}
    a['twilight sparkle'] = maximum_list_ts
    a['fluttershy'] = maximum_list_fs
    a['rarity'] = maximum_list_rr
    a['pinkie pie'] = maximum_list_pp
    a['apple jack'] = maximum_list_aj
    a['rainbow dash'] = maximum_list_rd

    print(a)

    #print(type(Input_String))
    #print(Input_String)
    #print(type(Output_String))
    #print(Output_String)
if __name__ == "__main__":
    main()