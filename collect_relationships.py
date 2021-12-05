import os, sys
import argparse
import bs4
import os.path as osp
import re
from os import path 
import hashlib
import json
import wget
def check_if_dir_exit(cache_directory): 
    return osp.exists(cache_directory) 
def check_if_file_exist(File_in_Hash):
    return osp.exists(File_in_Hash)
def main(): 
    script_dir = osp.dirname(__file__)
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--input')
    parser.add_argument('-o', '--output')
    args = parser.parse_args()
    Input_String = f'{args.input}'
    Output_String = f'{args.output}'
    data_path = osp.join(script_dir,Input_String)
    Input_Path = f'{data_path}' 
    data_path2 = osp.join(script_dir,Output_String)
    Result_Path = f'{data_path2}' 
    d = {}
    with open(Input_Path, 'r') as k:
        #assume only one line
        input = json.load(k)
        cache_directory = osp.join(script_dir, input['cache_dir'])
        target_people_list = input['target_people']
    check1 = check_if_dir_exit(cache_directory)
    if (check1 == False):
        os.makedirs(cache_directory)
    with open(Result_Path, 'w') as kp:
        for Cele_Name in target_people_list:
            Name_To_Website = f"https://www.whosdatedwho.com/dating/{Cele_Name}"
            hash = hashlib.sha1(Name_To_Website.encode("UTF-8")).hexdigest()
            File_in_Hash = osp.join(cache_directory, hash)
            check2 = check_if_file_exist(File_in_Hash)
            if (check2 == False):
                wget.download(Name_To_Website, out=File_in_Hash)
            soup = bs4.BeautifulSoup(open(File_in_Hash, 'r'), 'html.parser')
            data_content = soup.find('div', id = 'ff-dating-history-table')
            pattern = "/.*/dating/.*"
            a = []
            try:
                datingwho = data_content.find_all('a', href = re.compile(pattern))
            except AttributeError: 
                d[Cele_Name] = a
                continue
            for x in datingwho:
                if(x.get_text().strip() == ""):
                        continue
                else:
                    a.append(x.get_text().strip())
            d[Cele_Name] = a    
        json.dump(d, kp, indent=2)
        
    
if __name__ == '__main__':
    main()