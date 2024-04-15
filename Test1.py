import pandas as pd
import os


ClearScr = lambda : os.system('cls')

def TakeCommonInputs():

    print('\n' + "*"*50)
    print("Enter the Common Inputs:--\n")
    inputs = ['Storage_Group', ' Storage_Array', 'Purpose', 'Host_Group']
    common = {}
    for inpt in inputs:
        common[inpt] = input(f'Enter the {inpt}: ')
        print('')

    print("*"*50 + '\n')
    return common

def TakeUniqueInputs(n = None):

    UniqueDataGen = {'LUN_ID': [], 'UUID' : [],
                'RAID_Level' : [], 'Capacity' : []}

    try:
        n = int(n)
    except:
        print('\n'  + '*'*20)
        print("The number of unique entries should be a +ve Integer")
        print('\n'  + '*'*20)
        return None

    print('\n' + "*"*50)
    for i in range(n):

        print(f'Enter Details for LUN number {i+1}:--\n')

        for k,v in UniqueDataGen.items():
            UniqueDataGen[k].append(input(f"Enter {k}: "))
            print('')

    return UniqueDataGen


def GetFinalData(n = None, UniqueDataGen = None, common = None):

    if n is None or UniqueDataGen is None:
        print('\n'  + '*'*20)
        print("The number of unique entries should be a +ve Integer")
        print('\n'  + '*'*20)
        return None

    Data = {'LUN_ID': None, 'UUID' : None,
            'RAID_Level' : None, 'Storage_Group' : None,
            'Storage_Array' : None, 'Purpose' : None,
            'Capacity' : None , 'Host_Group' : None}

    for k,v in Data.items():

        if k in common.keys():
            Data[k] = [common[k] for i in range(int(n))]

        elif k in UniqueDataGen.keys():
            Data[k] = UniqueDataGen[k]

        else:
            continue

    df = pd.DataFrame(data=Data)

    return df[['LUN_ID', 'UUID', 'RAID_Level',
            'Storage_Group', 'Storage_Array',
            'Host_Group', 'Purpose', 'Capacity']]

if __name__ == "__main__":

    common = TakeCommonInputs()

    n = input("Enter Number of Unique Entries Required: ")
    UniqueDataGen = TakeUniqueInputs(n)

    df = GetFinalData(n = n, UniqueDataGen = UniqueDataGen, common = common)

    ClearScr()
    print("Final Results: \n")
    print(df)
