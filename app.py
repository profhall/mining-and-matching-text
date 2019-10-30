"""
title: app
author: Phillip Hall
date: 2019-10-29 13:13
"""
import json


def main():
    matchInfoAndKeys()




def matchInfoAndKeys():
    """
    This module reads two files one that has a list of possible keys and
    the other has the keys with data about the key on each line until the next key is reached.
    until that next key is reached the current key and its data will be created

    :return:
    """
    # newFlavorREached will be changed to True every time we reach a line that is new Key in our big file
    newFlavorREached = False
    keys_and_info_dict = {}
    keys = "keys.txt"
    infoKeys = 'info_and_keys2.txt'


    with open(keys, 'r') as file1:
        #This is a problem because some keys have the spaces after the comma and some dont in big file, maybe i should
        #regenerate a new big file to see if that fixes the commas
        data = [line.strip() for line in file1.readlines() if line!='\n' and len(line.strip()) > 1]

        for i, currKey  in enumerate(data):
            currKey = currKey
            inCurrFlav = False
            # if len(currKey) < 2:
            #     break

            if i+1 < len(data):
                 nextKey = data[i + 1].strip()
                 print(f'The Current key is: {currKey}\nThe next key is: {nextKey}')
            else:
                nextKey = None

            with open(infoKeys, 'r') as file:
                data2 =file.readlines()

                for i,line in  enumerate(data2):
                    line = line.strip()
                    lastline = data2[i-1]

                    if line==currKey and lastline =='\n' and line != '\n':
                        # print(f'Start of a new Key: {line} !n----')
                        keys_and_info_dict[currKey] ={}
                        keys_and_info_dict[currKey]["data"] = []

                        newFlavorREached =False
                        inCurrFlav = True

                    elif line ==nextKey and lastline == '\n':
                        # print(f"------\nnew key reached {nextKey}")

                        newFlavorREached = True
                        break

                    elif newFlavorREached is False and inCurrFlav is True and line !='\n' and line != '' :
                        # print(f'in Key: {currKey} >>> line: {line} ')
                        keys_and_info_dict[currKey]["data"].append(line)

                # print("------->\n")

    # print(json.dumps(keys_and_info_dict, indent=4, ensure_ascii=False))
    with open('data.json', 'w') as f:
        json.dump(keys_and_info_dict, f, indent=4, ensure_ascii=False)
if __name__ == '__main__':
    main()




