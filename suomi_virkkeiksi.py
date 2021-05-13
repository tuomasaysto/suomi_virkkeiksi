# -*- coding: utf-8 -*-

'''
Tekijä: Tuomas Äystö

Pätkii suomenkielisen tekstin virkkeiksi isojen välimerkkien
(!?.) avulla. Huomioi tavallisimmat pisteelliset lyhenteet siten, että
katkaisee lauseen vain, jos lyhennettä seuraa iso kirjain.
Ei täydellinen. Esimerkiksi rivinvaihtoja ei huomioida, jolloin otsikot
(kirjotetaan usein ilman .!? -merkkejä) eivät useinkaan tule pätkityksi 
omaksi virkkeekseen.

Käyttö: teksti_virkkeiksi(str)

'''

import re

# Kiitos lyhenteistä Kotukselle
lyhenteet = ["agrol", "agron", "aik", "alik", "alil", "am", "amir", "ao", "ap", "ark", "art", "arv", 
             "as", "assist", "ass", "au", "ausk", "br", "cf", "co", "corp", "dem", "dipl", "dos",
             "e", "eht", "ekon", "ekr", "elintarviket", "el", "eläinlääket", "eläk", "em", "emt",
             "erikoiseläinl", "erikoishammasl", "erikoisl", "erikoist", "esik", "esim", "et", "ev",
             "evp", "f", "farmas", "farm", "fil", "ft", "hallinton", "hallintot", "hammaslääket",
             "hl", "hp", "id", "in", "inc", "ip", "jkr", "jms", "jne", "joht", "jr", "julk", "jälj",
             "jääk", "k", "ka", "kad", "kal", "kamr", "kand", "kansaned", "kantt", "kappal", "kapt",
             "kasvatust", "kat", "kauppat", "kd", "kenr", "kirj", "kv", "käsit", "l", "leht", "liikuntak", 
             "lk", "lkm", "lkv", "lm", "ltk", "lyh", "läh", "länt", "lääk", "lääket", "m", "mm",
             "ma", "maan", "maat", "metsät", "maist", "maj", "maks", "matr", "mhy", "miel", "milj",
             "min", "ml", "mom", "mot", "mp", "mpm", "mr", "mrd", "mpy", "mrs", "m", "mts","mus", 
             "mv", "mvs", "myöh", " n", "neuv", "nid", "nim", "nimim", "nyk", "oa", "obs", "oik",
             "ok", "om", "op", "opp", "ork", "o", "oto", "ovh", "oy", "p", "pa", "par", "perj", "perusk",
             "ph", "pk", "pl", "p", "po", "prik", "ps", "psykol", "puh", "pursim", "pv", "pääl",
             "r", "rak", "reht", "rek", "res", "rkm", "rov", "rtg", "ruots", "rykm", "s", "sacr", 
             "sairaanh", "sair", "sd", "s", "sh", "sid", "sl", "so", "sos", "sp", "sr", "srk", "sunn",
             "svh", "synt", "t", "tait", "tal", "taloust", "tanssit", "tark", "tb", "tekn", "teol", 
             "terveydenh", "terveystiet", "terv", "th", "tiist", "til", "tj", "tjs", "tk", "tlk", "toht",
             "tms", "toim", "toht", "toim", "torst", "tp", "ts", "tv", "urk", "ups", "us", "va",
             "valt", "var", "varan", "varat", "vas", "vast", "vihr", "virk", "vk", "vm", "vpn", "v",
             "voim", "vp", "vpj", "vrt", "vt", "vv", "vänr", "vääp", "www", "x", "ye", "yhd", "yht", "yhteiskuntat"
             "yl", "ylik", "ylil", "ylim", "ylimatr", "yliop", "yliopp", "ylip", "yliv", "ym", "yms",
             "yo", "yp", "yt", "yv", "äo"
             ]

# lyhenteille piste perään
lyhenteet = [i +"." for i in lyhenteet]

    
# Ottaa tekstimassan stringinä ja palauttaa listan virkkeitä.
def teksti_virkkeiksi(text):
  
    text = text + "."    # piste tekstimassan loppuun   
    
    text = text.replace("-\n","")   # poistaa tavuviivalliset rivinvaihdot
    
    text = text.replace("\n"," ")    # poistaa rivinvaihdot
   
    # poistaa peräkkäiset välimerkit .!?  
    text = re.sub(r'(\.)\1+', r'\1', text)
    text = re.sub(r'(\!)\1+', r'\1', text)
    text = re.sub(r'(\?)\1+', r'\1', text)
                

    # pätkii tekstimassan sanalistalksi
    sanalista = text.split()
    sanalista2 = []
    
    # Käy sanalista läpi 
    for index, elem in enumerate(sanalista):
       
        # varmistaa, että listan index ei mene yli
        if(index<(len(sanalista)-1)): 
        
            # jos sana EI ole lyhenne...
            if elem not in lyhenteet:
                
                # lisää ko. sana listalle, ja korvaa mahd. piste katkaisumerkillä 
                elem = elem.replace(".",".<katkaise>")
                sanalista2.append(elem)
                
            # jos sana ON lyhenne    
            elif elem in lyhenteet:

                # .. ja jos seuraavan sanan eka kirjain on iso
                a = sanalista[index+1]
                if a[0].isupper():
                               
                    # lisää sana listalle katkaisumerkin kanssa
                    elem = elem.replace(".",".<katkaise>")
                    sanalista2.append(elem)
             
                else:
                    # muutoin lisää sana vain listalle
                    sanalista2.append(elem)
 
        # listan viimeinen sana
        else:
            elem = elem.replace(".",".<katkaise>")
            sanalista2.append(elem)
        
    text = ' '.join(sanalista2)

    # Katkaisumerkki !- ja ? -merkkien kohdalle
    text = text.replace("?","?<katkaise>")
    text = text.replace("!","!<katkaise>")
 
    virkkeet = text.split("<katkaise>")     # teksti virkkeiksi
 
    # listan siivousta
    virkkeet = list(filter(None, virkkeet)) 
    virkkeet = [x.strip() for x in virkkeet]
    
    return virkkeet


'''
# DEMO
f = open('testi.txt', encoding='utf-8').read()
print (teksti_virkkeiksi(f))
'''