import os, sys
import os.path as osp
import argparse
import json 
import pandas as pd
import sys
import random
def main():
    script_dir = osp.dirname(__file__)
    out_file = sys.argv[2]
    json_file = sys.argv[3]
    num_post_to_output = sys.argv[4] 
    num_post_to_output = int(num_post_to_output)
    data_path = osp.join(script_dir,out_file)
    json_file = osp.join(script_dir,json_file)
    with open(json_file) as f: 
        x = f.readlines()
        if (num_post_to_output > 100):
            num_post_to_output = 100
        json_random = random.sample(x, num_post_to_output)
        list_list = [] 
        for dict in json_random: 
            new_list = []
            record = json.loads(dict)
            new_list.append(record["data"]["author_fullname"])
            new_list.append(record["data"]["title"])
            new_list.append("")
            list_list.append(new_list)
    result = pd.DataFrame(list_list, columns=['Name', 'title', 'coding'])
    result.to_csv(data_path, sep="\t", index=False, encoding="utf-8")

if __name__ == '__main__':
    main()