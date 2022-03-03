import pandas as pd
import glob
import re
import os

map_dict = {0:'Amsterdam Navigator', 1:'Lagerbier Hell', 2:'Bayreuther Hell', 3:'Budweiser', 4:'Corona Extra', 5:'London Pride', 6:'Grolsch Premium Lager', 7:'Heineken', 8:'Hoegaarden Wit / Blanche', 9:'Hamovniki Venskoe (Хамовники Венское)', 10:'1664 Blanc', 11:'Miller Genuine Draft', 12:'Newcastle Brown Ale', 13:'Okhota Krepkoe (Охота Крепкое)', 14:'Sapporo Premium Beer', 15:'Helle Weisse (TAP01)', 16:'Original (TAP07)', 17:'Spaten München / Münchner Hell / Premium Lager', 18:'Weihenstephaner Hefeweissbier', 19:'Zhiguli Barnoe (Жигули Барное)'}

def extract_number(f):
    s = re.findall("\d+$",f)
    return (int(s[0]) if s else -1,f)

def get_prediction():
    os.system('python3 yolov5/detect.py --weights runs/train/exp/weights/best.pt --img 416 --conf 0.1 --source input.jpg --save-txt --save-conf')

def get_txtpath():
    list_of_folders = [f.path for f in os.scandir('yolov5/runs/detect/') if f.is_dir()]
    letest = max(list_of_folders,key=extract_number)
    txtpath = glob.glob(letest + "/*/*.txt")
    return txtpath[0]

def yolo2classname(txtpath):
  df = pd.read_csv(txtpath, sep = ' ', header=None)
  df.sort_values(by=5, ascending=False, inplace=True)
  df.reset_index(inplace=True)
  index = df[0][0]
  return map_dict[index]

def classname2info(classname):
    info = pd.read_csv('beerdata.csv')
    subset = info[info['Название пива'] == classname]
    return subset.values.tolist()


def getinfo():
    return classname2info(yolo2classname(get_txtpath())) 
