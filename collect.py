import json 
import os, sys 
import requests
MY_ID = 'Hp8QNla-vR9uDri5HCYdmg'
SECRET_KEY = 'vchK_I3hvEG0xeqONp7StCthddka4w'
def main(): 
    auth =requests.auth.HTTPBasicAuth(MY_ID, SECRET_KEY)
    data = {
        'grant_type': 'password',
        'username' : 'Comp598_STUDENT',
        'password' : 'IWILLSUEYOU'
    }
    headers = {'User-Agent': 'MyBot/0.0.1'}
    res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, 
    data=data, headers=headers)
    TOKEN = res.json()['access_token']
    headers['Authorization'] = f'bearer {TOKEN}' 
    list_of_topic = ['funny', 'AskReddit', 'gaming', 'aww', 'pics', 'Music', 'science', 'worldnews', 'videos', 'todayilearned']
    list_of_topic2 = ['AskReddit', 'memes', 'politics', 'nfl', 'nba', 'wallstreetbets', 'teenagers',
     'PublicFreakout', 'leagueoflegends','unpopularopinion']
    #print(len(list_of_topic))
    result_path = r'C:\Users\88691\Desktop\Comp598\hw6\comp598-2021-main\hw6\submission_template\sample1.json'
    result_path2 = r'C:\Users\88691\Desktop\Comp598\hw6\comp598-2021-main\hw6\submission_template\sample2.json'
    #print(result_path)
    with open(result_path, "w") as k:
        for x in range(len(list_of_topic)):
            r = requests.get(f'https://oauth.reddit.com/r/{list_of_topic[x]}/new.json?limit=100', headers=headers)
            root_element = r.json()
            ess_data = root_element['data']['children']
            for y in ess_data:
                json.dump(y, k)
                k.write('\n')
    with open(result_path2, "w") as a:
        for x in range(len(list_of_topic2)):
            r = requests.get(f'https://oauth.reddit.com/r/{list_of_topic2[x]}/new.json?limit=100', headers=headers)
            root_element = r.json()
            ess_data = root_element['data']['children']
            for y in ess_data:
                json.dump(y, a)
                a.write('\n')
    return


if __name__ == '__main__':
    main()

