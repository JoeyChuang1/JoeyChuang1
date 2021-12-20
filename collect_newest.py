import os, sys
import os.path as osp
import argparse
import json 
import pandas as pd
import requests
MY_ID = 'Hp8QNla-vR9uDri5HCYdmg'
SECRET_KEY = 'vchK_I3hvEG0xeqONp7StCthddka4w'
def main():
    ##################################Get Authentication
    auth =requests.auth.HTTPBasicAuth(MY_ID, SECRET_KEY)
    data = {
        'grant_type': 'password',
        'username' : 'Comp598_STUDENT',
        'password' : ''
    }
    headers = {'User-Agent': 'MyBot/0.0.1'}
    res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, 
    data=data, headers=headers)
    TOKEN = res.json()['access_token']
    headers['Authorization'] = f'bearer {TOKEN}' 
    ##################################Receieve Input
    script_dir = osp.dirname(__file__)
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--input')
    parser.add_argument('-o', '--output')
    args = parser.parse_args()
    Input_String = f'{args.input}'
    Output_String = f'{args.output}'
    data_path = "https://oauth.reddit.com" + Input_String + "/new.json?limit=100"
    data_path2 = osp.join(script_dir,Output_String)
    Result_Path = f'{data_path2}' 
    Real_Link = f'{data_path}' 
    with open(Result_Path, "w") as k:
         r = requests.get(Real_Link , headers=headers)
         root_element = r.json()
         ess_data = root_element['data']['children']
         for y in ess_data:
                json.dump(y, k)
                k.write('\n')
if __name__ == '__main__':
    main()
