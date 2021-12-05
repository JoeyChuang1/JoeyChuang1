import argparse
import os, sys
import json 

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('sample_file')
    args = parser.parse_args()
    path = args.sample_file
    num_of_line = 0
    num_of_word = 0
    with open(path, 'r') as f:
        for json_line in f: 
            try:
                num_of_line = num_of_line + 1
                record = json.loads(json_line)
                num_of_word = num_of_word + len(record['data']['title'])
            except ValueError: 
                      continue 

    print(num_of_word/num_of_line)
if __name__ == '__main__':
    main()