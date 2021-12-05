import os, sys
import os.path as osp
import argparse
import json  
import re
import pandas as pd


def big_five(Pony_Script, List_SWords):
    TwoD = list(Pony_Script['dialog'].str.lower().str.split(" "))
    OneD = [] 
    for inlist in TwoD:
         OneD += inlist
    result = [] 
    for words in OneD: 
        words = words.replace("()", " ").replace("(", " ").replace(")"," ").replace("[", " ").replace("]"," ").replace("[]"," ").replace("-"," ").replace(","," ").replace("."," ").replace("?"," ").replace("!"," ").replace(":"," ").replace(";"," ").replace("#"," ").replace("&"," ")
        if ( (words.strip().isalpha() == True) and (words.strip() not in List_SWords)):
            result.append(words.strip())
    a = []
    for word in result: 
        if ((result.count(word)) < 5):
            continue
        else:
            a.append(word)
    return a

def result_library(Pony_Script, List_SWords, more_than_five):
    #print(Pony_Script)
    #print(List_SWords)
    TwoD = list(Pony_Script['dialog'].str.lower().str.split(" "))
    OneD = [] 
    for inlist in TwoD:
        OneD += inlist
    result = [] 
    for words in OneD: 
        words = words.replace("()", " ").replace("(", " ").replace(")"," ").replace("[", " ").replace("]"," ").replace("[]"," ").replace("-"," ").replace(","," ").replace("."," ").replace("?"," ").replace("!"," ").replace(":"," ").replace(";"," ").replace("#"," ").replace("&"," ")
        if ( (words.strip().isalpha() == True) and (words.strip() not in List_SWords)):
            result.append(words.strip())
    a = {}
    for word in result: 
        if (word in more_than_five):
            a[word] = result.count(word)
        else:
            continue
    return a

def main():
    ######## Initialization ########
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--input')
    parser.add_argument('-o', '--output')
    args = parser.parse_args()
    Input_String = f'{args.input}'
    Output_String = f'{args.output}'
    #print(Input_String)
    #print(Output_String)
    dirname = os.path.dirname(Output_String)
    if (osp.exists(dirname) == False and (dirname != "")):
        os.makedirs(dirname)
    #######################################################
    ############# Input_String = Input_file ###############
    ########### Output_String = Output_file ###############
    #######################################################
    
    #stop_words = pd.read_csv("../data/stopwords.txt") 
    #stop_words_list = list(stop_words['Num_of'])
    #print(stop_words_list)
    stop_words_list = ['a', 'about', 'above', 'across', 'after', 'again', 'against', 'all', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'among', 'an', 'and', 'another', 'any', 'anybody', 
        'anyone', 'anything', 'anywhere', 'are', 'area', 'areas', 'around', 'as', 'ask', 'asked', 'asking', 'asks', 'at', 'away', 'b', 'back', 'backed', 'backing', 'backs', 'be', 'became', 'because', 'become', 'becomes', 'been', 'before', 'began', 'behind', 'being', 'beings', 'best', 'better', 'between', 'big', 'both', 'but', 'by', 'c', 'came', 'can', 'cannot', 'case', 'cases', 'certain', 'certainly', 'clear', 'clearly', 'come', 'could', 'd', 'did', 'differ', 'different', 'differently', 'do', 'does', 'done', 'down', 'down', 'downed', 'downing', 'downs', 'during', 'e', 'each', 'early', 'either', 'end', 'ended', 'ending', 'ends', 'enough', 'even', 'evenly', 'ever', 'every', 'everybody', 'everyone', 'everything', 'everywhere', 'f', 'face', 'faces', 'fact', 'facts', 'far', 'felt', 'few', 'find', 'finds', 'first', 'for', 'four', 'from', 'full', 'fully', 'further', 'furthered', 'furthering', 'furthers', 'g', 'gave', 'general', 'generally', 'get', 'gets', 'give', 'given', 'gives', 'go', 'going', 'good', 'goods', 'got', 'great', 'greater', 'greatest', 'group', 'grouped', 'grouping', 'groups', 'h', 'had', 'has', 'have', 'having', 'he', 'her', 'here', 'herself', 'high', 'high', 'high', 'higher', 'highest', 'him', 'himself', 'his', 'how', 'however', 'i', 'if', 'important', 'in', 'interest', 'interested', 'interesting', 'interests', 'into', 'is', 'it', 'its', 'itself', 'j', 'just', 'k', 'keep', 'keeps', 'kind', 'knew', 'know', 'known', 'knows', 'l', 'large', 'largely', 'last', 'later', 'latest', 'least', 'less', 'let', 'lets', 'like', 'likely', 'long', 'longer', 'longest', 'm', 'made', 'make', 'making', 'man', 'many', 'may', 'me', 'member', 'members', 'men', 'might', 'more', 'most', 'mostly', 'mr', 'mrs', 'much', 'must', 'my', 'myself', 'n', 'necessary', 'need', 'needed', 'needing', 'needs', 'never', 'new', 'new', 'newer', 'newest', 'next', 'no', 'nobody', 'non', 'noone', 'not', 'nothing', 'now', 'nowhere', 'number', 'numbers', 'o', 'of', 'off', 'often', 'old', 'older', 'oldest', 
        'on', 'once', 'one', 'only', 'open', 'opened', 'opening', 'opens', 'or', 'order', 'ordered', 'ordering', 'orders', 'other', 'others', 'our', 'out', 'over', 'p', 'part', 'parted', 'parting', 
        'parts', 'per', 'perhaps', 'place', 'places', 'point', 'pointed', 'pointing', 'points', 'possible', 'present', 'presented', 'presenting', 'presents', 'problem', 'problems', 'put', 'puts', 'q', 'quite', 'r', 'rather', 'really', 'right', 'right', 'room', 'rooms', 's', 'said', 'same', 'saw', 'say', 'says', 'second', 'seconds', 'see', 'seem', 'seemed', 'seeming', 'seems', 'sees', 'several', 'shall', 'she', 'should', 'show', 'showed', 'showing', 'shows', 'side', 'sides', 'since', 'small', 'smaller', 'smallest', 'so', 'some', 'somebody', 'someone', 'something', 'somewhere', 'state', 'states', 'still', 'still', 'such', 'sure', 't', 'take', 'taken', 'than', 'that', 'the', 'their', 'them', 'then', 'there', 'therefore', 'these', 'they', 'thing', 'things', 'think', 'thinks', 'this', 'those', 'though', 'thought', 'thoughts', 'three', 'through', 'thus', 'to', 'today', 'together', 'too', 'took', 'toward', 'turn', 'turned', 'turning', 'turns', 'two', 
        'u', 'under', 'until', 'up', 'upon', 'us', 'use', 'used', 'uses', 'v', 'very', 'w', 'want', 'wanted', 'wanting', 'wants', 'was', 'way', 'ways', 'we', 'well', 'wells', 'went', 'were', 'what', 'when', 'where', 'whether', 'which', 'while', 'who', 'whole', 'whose', 'why', 'will', 'with', 
        'within', 'without', 'work', 'worked', 'working', 'works', 'would', 'x', 'y', 'year', 'years', 
        'yet', 'you', 'young', 'younger', 'youngest', 'your', 'yours', 'z']

    pf = pd.read_csv(Input_String)
    
    main_script =  pf.loc[pf['pony'].str.contains("^Twilight Sparkle$|^Applejack$|^Rarity$|^Pinkie Pie$|^Rainbow Dash$|^Fluttershy$", regex=True, case = False)]
    more_than_five = big_five(main_script, stop_words_list)

    TS_script = pf.loc[pf['pony'].str.contains("^Twilight Sparkle$", regex=True, case = False)]
    Twilight_Sparkle = result_library(TS_script, stop_words_list, more_than_five)

    AJ_script = pf.loc[pf['pony'].str.contains("^Applejack$", regex=True, case = False)]
    Apple_Jack = result_library(AJ_script, stop_words_list, more_than_five)

    RT_script = pf.loc[pf['pony'].str.contains("^Rarity$", regex=True, case = False)]
    Rarity = result_library(RT_script, stop_words_list, more_than_five)

    PP_script = pf.loc[pf['pony'].str.contains("^Pinkie Pie$", regex=True, case = False)]
    Pinkie_Pie = result_library(PP_script, stop_words_list, more_than_five)

    RD_script = pf.loc[pf['pony'].str.contains("^Rainbow Dash$", regex=True, case = False)]
    Rainbow_dash = result_library(RD_script, stop_words_list, more_than_five)

    FS_script = pf.loc[pf['pony'].str.contains("^Fluttershy$", regex=True, case = False)]
    Fluttershy = result_library(FS_script, stop_words_list, more_than_five)

    Fin_result = {}
    Fin_result["twilight sparkle"] = Twilight_Sparkle
    Fin_result["apple jack"] = Apple_Jack
    Fin_result["rarity"] = Rarity
    Fin_result["pinkie pie"] = Pinkie_Pie  
    Fin_result["rainbow dash"] = Rainbow_dash
    Fin_result["fluttershy"] = Fluttershy
    
    with open(Output_String, 'w') as d:
        json.dump(Fin_result, d, indent=1)



    


if __name__ == '__main__':
    main()