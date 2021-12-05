import pandas as pd
import networkx as nx
import numpy as np
import os, sys
import os.path as osp
import argparse
import json  
import re
from networkx.readwrite import json_graph

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input')
    parser.add_argument('-o', '--output')
    args = parser.parse_args()
    Input_String = f'{args.input}'
    Output_String = f'{args.output}'
    #print(Input_String)
    #print(Output_String)
    dirname = os.path.dirname(Output_String)
    if (osp.exists(dirname) == False and (dirname != "")):
        os.makedirs(dirname)

    with open(Input_String, 'r') as d:
        Ori_Dict = json.load(d)

    max_edge = {}
    max_weight = {}
    for i in Ori_Dict:
        sum = 0
        max_edge[i] = len(Ori_Dict[i])
        for num in Ori_Dict[i]:
            sum = sum + int(Ori_Dict[i][num])
        max_weight[i] = sum 
    G = nx.Graph()
    for i in Ori_Dict:
        for num in Ori_Dict[i]:
            if (G.has_edge(i, num)):
                continue
            G.add_edge(i , num, weight = Ori_Dict[i][num])
    between_us = nx.betweenness_centrality(G)
    most_edge = []
    most_weight = []
    most_between = []
    for i in range(3):
        max_key1 = max(max_edge , key=max_edge.get)
        most_edge.append(max_key1)
        del max_edge[max_key1]
        max_key2 = max(max_weight , key=max_weight.get)
        most_weight.append(max_key2)
        del max_weight[max_key2]
        max_key3 = max(between_us , key=between_us.get)
        most_between.append(max_key3)
        del between_us[max_key3]
    result = {}
    result['most_connected_by_num'] = most_edge
    result['most_connected_by_weight'] =  most_weight
    result['most_central_by_betweenness'] = most_between
    with open(Output_String, 'w') as d:
        json.dump(result, d, indent=2)



if __name__ == '__main__':
    main()