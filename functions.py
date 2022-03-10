import pandas as pd
import glob
import re
import os

#map_dict20 = {0:'Amsterdam Navigator', 1:'Lagerbier Hell', 2:'Bayreuther Hell', 3:'Budweiser', 4:'Corona Extra', 5:'London Pride', 6:'Grolsch Premium Lager', 7:'Heineken', 8:'Hoegaarden Wit / Blanche', 9:'Hamovniki Venskoe (Хамовники Венское)', 10:'1664 Blanc', 11:'Miller Genuine Draft', 12:'Newcastle Brown Ale', 13:'Okhota Krepkoe (Охота Крепкое)', 14:'Sapporo Premium Beer', 15:'Helle Weisse (TAP01)', 16:'Original (TAP07)', 17:'Spaten München / Münchner Hell / Premium Lager', 18:'Weihenstephaner Hefeweissbier', 19:'Zhiguli Barnoe (Жигули Барное)'}

map_dict199 = {0	:'Abk Hell', 1	:'Adnams Ghost Ship', 2	:'Adnams Jack Brand Mosaic', 3	:'Ahornberger Landbrauerei Marzen', 4	:'Aldaris 1865', 5	:'Amstel Premium', 6	:'Amstel', 7	:'Amsterdam Navigator', 8	:'Apostel Brau', 9	:'Arcobrau Mooser Liesl', 10	:'Arcobrau Urfass', 11	:'Asahi Super DRY', 12	:'Augustijn', 13	:'Bakalar Medovy', 14	:'Baltika -0', 15	:'Baltika -3', 16	:'Baltika -7', 17	:'Baltika -9', 18	:'Bavaria Malt Non-Alcoholic', 19	:'Bavaria', 20	:'Bayreuther Hell', 21	:'Belgian Kriek', 22	:'Belhaven Black Scottish Stout', 23	:'Belhaven McCallum-s Sweet Scottish Stout', 24	:'Belle Vue Kriek Extra', 25	:'Bely Medved Krepkoe', 26	:'Benediktiner Hell', 27	:'Berliner Kindl Jubilaums Pilsener', 28	:'Bernard Cherny Lezak', 29	:'Bernard Cvatecni Lezak', 30	:'Bishops Finger', 31	:'Bitburger Drive 0-0- Alkoholfreies Pils', 32	:'Bitburger Premium Pils', 33	:'Blanche De Namur', 34	:'Blue Moon', 35	:'Boddingtons Pub Ale', 36	:'Bowler IPA', 37	:'Brewdog Punk IPA', 38	:'Bud Light', 39	:'Bud Zero', 40	:'Budweiser Budvar', 41	:'Burg Lager', 42	:'CARLSBERG', 43	:'Carlsberg 0.0', 44	:'Carlsberg Unfiltered', 45	:'Cernovar Cerne', 46	:'Chang Classic', 47	:'Clausthaler Original Non-Alcoholic', 48	:'Corona Extra', 49	:'Delirium Argentum', 50	:'Delirium Red', 51	:'Delirium Tremens', 52	:'Duvel', 53	:'Eboshi Original', 54	:'Edelweiss Wheat Beer', 55	:'Efes Pilsener', 56	:'Erdinger Alkoholfrei', 57	:'Erdinger Weisbier', 58	:'Estrella Damm', 59	:'FAXE Premium', 60	:'FRUH Kolsch', 61	:'Fischer Tradition', 62	:'Freak Kriek Zero Point Three Feel Free Merry Cherry Beer', 63	:'Fullers London Pride', 64	:'Gletcher Milk of Amnesia', 65	:'Gletcher Nut Butter', 66	:'Gorkovskaya Brewery American Amber Lager', 67	:'Gorkovskaya Brewery Bohemian Pils', 68	:'Grevensteiner Natutrubes Helles', 69	:'Grevensteiner Original', 70	:'Grimbergen Blanche', 71	:'Grimbergen Blonde', 72	:'Grimbergen Double Ambree', 73	:'Grolsch Premium Lager', 74	:'Grolsch Premium Pilsner', 75	:'Grossmeister Wheat Beer', 76	:'Grossmeister', 77	:'Grotwerg Bayerisch Hell', 78	:'Guinness Draught', 79	:'Gulden Draak Classic', 80	:'Gulden Draak Quadruple', 81	:'Hacker Pschorr Kellerbier', 82	:'Hacker Pschorr Munchner gold', 83	:'Hamovniki Venskoe', 84	:'Hasen Augsburger Original', 85	:'Heineken 0.0', 86	:'Heineken', 87	:'Hobgoblin Gold', 88	:'Hobgoblin IPA', 89	:'Hobgoblin Ruby', 90	:'Hoegaarden ROSEE', 91	:'Hoegaarden Wit Blanche', 92	:'Hoegaarden', 93	:'Hofbrau Munchner Weisse', 94	:'Hofbraun Original', 95	:'Hollandia', 96	:'Holsten Premium', 97	:'Iron Woods Milk Stout', 98	:'Kedrwood', 99	:'Kilikia', 100	:'Kilkenny Draught', 101	:'Kirin Ichiban', 102	:'Klaster Svetle', 103	:'Klaster Tmave', 104	:'Klinskoe Svetloe', 105	:'Koff', 106	:'Kometa IPA', 107	:'Konigsbarcher Weizen', 108	:'Kozel Cerny', 109	:'Kozel Svetly', 110	:'Kriekenbier', 111	:'Krombacher Hell', 112	:'Kronenbourg Blanc', 113	:'Kronenbourg', 114	:'Krusovice Cherne', 115	:'Krusovice Svetle', 116	:'Landbier Bayreuther Dunkel', 117	:'Landbier Zwickl Kellerbier', 118	:'Lapin Kulta', 119	:'Leffe Ambree', 120	:'Leffe Blonde', 121	:'Leffe Brune', 122	:'Leffe Ruby', 123	:'Liebenbrau Helles', 124	:'Love Memories', 125	:'Lowenbrau Original', 126	:'Lowenbrau Wheat 0.0', 127	:'Maisels Weisse Original', 128	:'Miller Genuine Draft', 129	:'Newcastle Brown Ale', 130	:'Okhota Krepkoe', 131	:'Otto Von Schrodder Hefeweizen', 132	:'Otto Von Schrodder Premium Lager', 133	:'Oyster Stout', 134	:'PERONI Nastro Azzurro', 135	:'Pabst Blue Ribbon', 136	:'Paulaner Weissbier Non-Alcoholic', 137	:'Paulaner Weissbier', 138	:'Pauwel Kwak', 139	:'Petrus Aged RED', 140	:'Petrus Bordo', 141	:'Pilsner Urquell', 142	:'Praga Dark Lager', 143	:'Praga Premium Pils', 144	:'ROUGE DE FLEUR Cherry', 145	:'Radeberger Pilsner', 146	:'Red Stripe', 147	:'SAMUEL ADAMS Boston Lager', 148	:'STIEGL Goldbrau', 149	:'Saint-Omer Biere Blonde De Luxe', 150	:'Sapporo', 151	:'Schlitz Helles', 152	:'Schlitz Non-Alcoholic', 153	:'Schneider Weisse Helle Weisse', 154	:'Schofferhofer Grapefruit', 155	:'Schofferhofer Weizen', 156	:'Sheperd Neame 1698', 157	:'Sheperd Neame DOUBLE STOUT', 158	:'Sheperd Neame India Pale Ale', 159	:'Sint Gummarus Dubbel', 160	:'Sint Gummarus Tripel', 161	:'Smithwick-s RED', 162	:'Spaten Munchen Dunkel', 163	:'Spaten Munchen', 164	:'Spitfire Kentish Ale', 165	:'St. Peters Cream Stout', 166	:'St.Pierre Blond', 167	:'St.Pierre Brune', 168	:'Stanley Cooper', 169	:'Staroceske Tradicni', 170	:'Staropramen', 171	:'Stella Artois 0.0', 172	:'Stella Artois', 173	:'Svyturys Tradicinis', 174	:'THRON LAGER', 175	:'THRON WEIZEN', 176	:'Thistle Draught', 177	:'Thistle Strong', 178	:'Toute L-Annee Doux Cerise', 179	:'Tripel Karmeliet', 180	:'Tucher Urbrau Hell', 181	:'VAN STEENBERGE PIRAAT', 182	:'VELVET', 183	:'VanderGhinste Oud Bruin', 184	:'Veltins Pilsener', 185	:'Warsteiner Double Hopped', 186	:'Warsteiner Fresh Non-Alcoholic', 187	:'Warsteiner Premium', 188	:'Weihenstephaner Original', 189	:'White Moon', 190	:'Wolf-s Brewery Blanche De Mazay', 191	:'Wolf-s Brewery IPA', 192	:'Wolf-s Brewery Svetlachok', 193	:'Wolpertinger Alkoholfrei', 194	:'Wolpertinger', 195	:'Wolters Pilsener', 196	:'Zatecky Gus Cherne', 197	:'Zatecky Gus Svetly', 198	:'Zhiguli Barnoe'}

def extract_number(f):
    s = re.findall("\d+$",f)
    return (int(s[0]) if s else -1,f)

def get_prediction():
    os.system('python3 yolov5/detect.py --weights runs/train/exp/weights/v7.pt --img 416 --conf 0.1 --source input.jpg --save-txt --save-conf')

def get_txtpath():
    list_of_folders = [f.path for f in os.scandir('yolov5/runs/detect/') if f.is_dir()]
    letest = max(list_of_folders,key=extract_number)
    txtpath = glob.glob(letest + "/*/*.txt")
    try:
        return txtpath[0]
    except:
        return 404

def yolo2classname(txtpath):
  df = pd.read_csv(txtpath, sep = ' ', header=None)
  df.sort_values(by=5, ascending=False, inplace=True)
  df.reset_index(inplace=True)
  index = df[0][0]
  return map_dict199[index]

def classname2info(classname):
    info = pd.read_csv('beerdata.csv')
    subset = info[info['name'] == classname]
    return subset.values.tolist()


def getinfo():
    txt_path = get_txtpath()
    if txt_path == 404:
        return 'Я не вижу пиво'
    print(txt_path)
    result = classname2info(yolo2classname(txt_path))
    name = result[0][0]
    style = result[0][1]
    ABV = result[0][2]
    IBU = result[0][3]
    rating = result[0][4]
    description = result[0][5]
    return name, style, ABV, IBU, rating, description 


