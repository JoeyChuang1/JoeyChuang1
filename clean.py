import os, sys
import os.path as osp
import argparse
import json 
import datetime 
import re
import pytz
from dateutil.parser import isoparse
from dateutil.tz import UTC

def title_title_text_check(record):
    if(("title_text" in record) or ("title" in record)):
        return True
    else:
        return False 

def title_text_into_text(record):
    if(("title_text" in record)):
        record["title"] = record.pop("title_text")
        return record
    else:
        return record
def Converting_to_UTC(record):
    dt = isoparse(record.get('createdAt'))
    dt = dt.astimezone(UTC)
    record['createdAt'] = dt.isoformat()
    return record

def validate_iso_standard_time(created_at):
    pattern = "\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+\d{4}"
    return re.compile(pattern).match(created_at) is not None

def check_author(record):
    if((record.get('author') == "") or (record.get('author') == "N/A") or (record.get('author') == None)):
        return False
    else: 
        return True

def Turning_String_Int(record):
    try: 
        record["total_count"] = int(record.get("total_count"))
        return True
    except ValueError: 
        return False

def Check_if_str_int_float(record):
    return isinstance(record.get("total_count"), str) or isinstance(record.get("total_count"), int) or isinstance(record.get("total_count"), float)

def Check_list(record):
    Dummy = []
    for x in record.get('tags'):
        a = list(x.split(' '))
        Dummy += a
    record["tags"] = Dummy
    return record

def processes(json_line):
    try:
        json.loads(json_line)
        return True
    except ValueError: 
        return False


def main():
    # Reading data into a path
    script_dir = osp.dirname(__file__)
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input')
    parser.add_argument('-o', '--output')
    args = parser.parse_args()
    Input_String = f'{args.input}'
    Output_String = f'{args.output}'
    data_path = osp.join(script_dir,Input_String)
    Real_Path = f'{data_path}' 
    data_path2 = osp.join(script_dir,Output_String)
    Result_Path = f'{data_path2}' 

    #i = 0
    # Iterate the file example.json (line by line)
    with open(Result_Path, "w") as k:
        with open(Real_Path) as f:
            for json_line in f: 
                try:
                    record = json.loads(json_line)
                    Test_1 = title_title_text_check(record)
                    if (Test_1 == False):
                        continue
                    record = title_text_into_text(record)
                    if("createdAt" in record):
                        Test_2 = validate_iso_standard_time(record.get('createdAt'))
                    if (Test_2 == False):
                        continue
                    if("createdAt" in record):
                         record = Converting_to_UTC(record)
                    if("author" in record):
                        Test_3 = check_author(record)
                    if(Test_3 == False):
                        continue
                    if ("total_count" in record):
                        Test_4 = Check_if_str_int_float(record)
                    if (Test_4 == False):
                        continue
                    if ("total_count" in record):
                        Test_5 = Turning_String_Int(record)
                    if (Test_5 == False):
                        continue
                    if ("tags" in record):
                        record = Check_list(record)
                    json.dump(record, k)
                    k.write('\n')
                except ValueError: 
                      continue 



if __name__  == '__main__':
    main()