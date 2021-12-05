import os, sys
import os.path as osp
import argparse
import json  
import re
import pandas as pd
def main():
    script_dir = osp.dirname(__file__)
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input')
    parser.add_argument('-o', '--output')
    args = parser.parse_args()
    Input_String = f'{args.input}'
    Output_String = f'{args.output}'
    data_path = osp.join(script_dir,Input_String)
    Real_Path = f'{data_path}' 
    Result_Path = Output_String
    if(Result_Path == "None"): 
        mode = 1
    else: 
        mode = 0
        data_path2 = osp.join(script_dir,Output_String)
        Result_Path = f'{data_path2}' 
        dirname = os.path.dirname(Result_Path)
        if (osp.exists(dirname) == False and (dirname != "")):
            os.makedirs(dirname)
    df = pd.read_csv(Real_Path, delimiter='\t', encoding="ISO-8859-1")
    d1 = df.loc[df['coding'].str.contains("o")]
    c1 = len(d1)
    d2 = df.loc[df['coding'].str.contains("f")]
    c2 = len(d2)
    d3 = df.loc[df['coding'].str.contains("c")]
    c3 = len(d3)
    d4 = df.loc[df['coding'].str.contains("r")]
    c4 = len(d4)
    data = {}
    data = {
        "course-related": c3,
        "food-related": c2,
        "residence-related": c4,
        "other": c1
    }
    if (mode == 1):
        print(data)
    else:
        with open(Result_Path, 'w') as d:
            json.dump(data, d, indent=1)
    
if __name__ == '__main__':
    main()