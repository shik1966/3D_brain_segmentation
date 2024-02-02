import os
import re
os.chdir("BraTS2021/")

case = 1
def increment(): #count parameter is beginning case
    global case
    case = case +1
    
def count_number(num):
    count = 0

    while num != 0:
        num //= 10
        count += 1
    return count
    
def case_show(case):
    dict= {
        1: "0000"+ str(case),
        2: "000"+ str(case),
        3: "00"+ str(case),
        4: "0"+ str(case),
        5: str(case)
    }
    result=""
    if(count_number(case) == 1):
        result = dict.get(1)
    elif(count_number(case) == 2):
        result = dict.get(2)
    elif(count_number(case) == 3):
        result = dict.get(3)
    elif(count_number(case) == 4):
        result = dict.get(4)
    elif(count_number(case) == 5):
        result = dict.get(5)
    else:
        result = "Invalid"
        
    return result
    
def rename_folder(src_folder):
    d_name = "BraTS2021_"+ str(case_show(case))
    os.rename(src_folder, d_name)
    
    print("Folder is renamed")
    
#rename_folder()

def rename_files():
    src = "BraTS2021_"+str(case_show(case))
    i =0
    obj_list = os.listdir(src)
    flair_root = obj_list[0]
    flair = src + "_flair"
    seg = src + "_seg"
    t1 = src + "_t1"
    t1ce = src + "_t1ce"
    t2 = src + "_t2"
    new_name_list=[flair, seg, t1, t1ce, t2]
    for f in obj_list:
        f_name, f_ext = os.path.splitext(f)
        f_name = new_name_list[i]
        i =i+1
        
        new_name = '{}{}'.format(f_name, f_ext)
        #print(f)
        os.rename(src+"/"+f, src+"/"+new_name)
    print("All files are renamed")
    
#rename_files()

for f in os.listdir():
    #print(f)
    rename_folder(f)
    rename_files()
    increment()
    
    print("BraTS2021_"+str(case)+" is completed")
    
print("Data processing is completed")
        