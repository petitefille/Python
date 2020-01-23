# 6.7

humans = {}

initialized = False

with open("human_evolution.txt", "r") as f :
    for line in f :
        line = line.strip()
		# sjekker om man har en linje med kun bindestreker 
        if line == len(line) * "-" :
            if initialized :
                break
            else :
                initialized = True
                continue
            
        if initialized :
            name =   line[0:21].strip()   # 21 ikke inkludert 
            when =   line[21:37].strip()
            height = line[37:50].strip()
            weight = line[50:62].strip()
            volume = line[62:].strip()

            humans[name] = {"height" : height,
                            "when"   : when,
                            "weight" : weight,
                            "volume" : volume}
print humans

"""

python humans.py
{'H. neanderthalensis': {'volume': '1200 - 1700', 'when': '0.35 - 0.03', 
'weight': '55 - 70', 'height': '1.6'}, 'H. sapiens sapiens': 
{'volume': '1000 - 1850', 'when': '0.2 - present', 'weight': '50 - 100', 
'height': '1.4 - 1.9'}, 'H. heidelbergensis': {'volume': '1100 - 1400', 
'when': '0.6 - 0.35', 'weight': '60', 'height': '1.8'}, 'H. erectus': 
{'volume': '850 (early) - 1100 (late)', 'when': '1.4 - 0.2', 'weight': '60', 
'height': '1.8'}, 'H. floresiensis': {'volume': '400', 'when': '0.10 - 0.012', 
'weight': '25', 'height': '1.0'}, 'H. ergaster': {'volume': '700 - 850', 
'when': '1.9 - 1.4', 'weight': '', 'height': '1.9'}, 'H. habilis': 
{'volume': '660', 'when': '2.2 - 1.6', 'weight': '33 - 55', 'height': '1.0 - 1.5'}}


"""

# Versjon 2:


infile = open("human_evolution.txt", "r")

humans = {}

initialized = False

for line in infile: 
    line = line.strip()
    if line == len(line) * "-" :
        if initialized :
            break
        else :
            initialized = True
            continue
            
    if initialized :
        name =   line[0:21].strip()
        when =   line[21:37].strip()
        height = line[37:50].strip()
        weight = line[50:62].strip()
        volume = line[62:].strip()

        humans[name] = {"height" : height,
                        "when"   : when,
                        "weight" : weight,
                        "volume" : volume}
print humans    

