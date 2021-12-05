import pandas as pd
import networkx as nx
import numpy as np
import os, sys
import os.path as osp
import argparse
import json  
import re

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

    pf = pd.read_csv(Input_String)
    speakers = list(pf.itertuples())
    one_or_one_top = False
    G = nx.Graph()
    pattern = "^and$"
    pattern2 = "^others$"
    pattern3 = "^ponies$"
    pattern4 = "^all$"
    for i in range(len(speakers) - 1):
        if ((' all ' in speakers[i][3].lower()) or (' others ' in speakers[i][3].lower()) or (' ponies ' in speakers[i][3].lower()) or (' and ' in speakers[i][3].lower())):
            continue
        if ((' all ' in speakers[i + 1][3].lower()) or (' others ' in speakers[i + 1][3].lower()) or (' ponies ' in speakers[i + 1][3].lower()) or (' and ' in speakers[i][3].lower())):
            continue
        if ((re.compile(pattern).match(speakers[i][3].lower()) is not None) or 
        (re.compile(pattern2).match(speakers[i][3].lower()) is not None) or
        (re.compile(pattern3).match(speakers[i][3].lower()) is not None) or
        (re.compile(pattern4).match(speakers[i][3].lower()) is not None)):
            continue
        if ((re.compile(pattern).match(speakers[i + 1][3].lower()) is not None) or 
        (re.compile(pattern2).match(speakers[i + 1][3].lower()) is not None) or
        (re.compile(pattern3).match(speakers[i + 1][3].lower()) is not None) or
        (re.compile(pattern4).match(speakers[i + 1][3].lower()) is not None)):
            continue
        if (speakers[i][3].lower() == speakers[i+1][3].lower()):
            continue
        if (speakers[i][1] != speakers[i+1][1]):
            continue
        first_node = speakers[i][3]
        second_node = speakers[i + 1][3]
        if (G.has_edge(first_node, second_node) == True):
            G.get_edge_data(first_node, second_node)['weight'] += 1
        if (G.has_edge(first_node, second_node) == False):
            G.add_edge(first_node, second_node, weight = 1)

    list_of_edge = sorted(G.edges(data=True),key= lambda x: x[2]['weight'],reverse=True)
    list_count = []
    actual_list = []
    print(list_of_edge[0:200])
    #print(G.edges('Big Daddy McColt'))
    for x in list_of_edge:
        #if (len(list_count) == 101):
        #    print(list_co
        #if (x[0] == 'Big Daddy McColt' or x[1] == 'Big Daddy McColt'):
        #    print(len(list_count))
        #    print(x)
        if((len(list_count) == 100) and (x[0] not in list_count) and (x[1] not in list_count)):
            continue
        if((len(list_count) >= 101) and (x[0] not in list_count) and (x[1] not in list_count)):
            continue
        if((len(list_count) >= 101) and (x[0] not in list_count) and (x[1] in list_count)):
            continue
        if((len(list_count) >= 101) and (x[0] in list_count) and (x[1] not in list_count)):
            continue
        if((len(list_count) >= 101) and (x[0] in list_count) and (x[1] in list_count)):
            actual_list.append(x)
            continue
        if(x[0] not in list_count):
            list_count.append(x[0])
        if(x[1] not in list_count):
            list_count.append(x[1]) 
        actual_list.append(x)

    result = {}

    for v in  actual_list:
        if (v[0] in result):
            result[v[0]][v[1]] = int(v[2]['weight'])
        else:
            result2 = {}
            result2[v[1]] = int(v[2]['weight'])
            result[v[0]] = result2

    for v in actual_list:
        if (v[1] in result):
             result [v[1]][v[0]] = int(v[2]['weight'])
        else:
            result2 = {}
            result2[v[0]] = int(v[2]['weight'])
            result[v[1]] = result2
    with open(Output_String, 'w') as d:
        json.dump(result, d, indent=4)
    #test1 = 'twigh'
    #test2 = 'twigh spa'
    #print(test1.lower() == test2.lower())
    #F = nx.Graph()
    #F.add_edge('a', 'b', weight = 0)
    ##print(G.degree('a')) 
    #print(F.has_edge('a', 'b'))
    #print(F.has_edge('b', 'a'))
    #print(F.has_edge('C', 'a'))
    #print(F.get_edge_data('b', 'a')['weight'])
    #print(F.get_edge_data('a', 'b')['weight'])
    #F.get_edge_data('b', 'a')['weight'] += 1
    #F.get_edge_data('a', 'b')['weight'] += 1
    #print(F.get_edge_data('b', 'a')['weight'])
    #print(F.get_edge_data('a', 'b')['weight'])
    #G.has_edge(subject_id, object_id)
    ##print(G.get_edge_data('a', 'b')['weight'])
    ##print(G.get_edge_data('b', 'a')['weight'])
    ##G.get_edge_data('b', 'a')['weight'] += 1
    ##print(G.get_edge_data('b', 'a')['weight'])
if __name__ == '__main__':
    main()