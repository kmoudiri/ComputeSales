from copy import deepcopy
import operator
# import time

ans=True
afm=0
flag = 0
mistake = 0
case = 0
flagsynolo = 0
monimo_d2 = {}
tmp_d2 = {}
monimo_d3 = {}
tmp_d3 = {}
tmp_d={}
tmp_3={}
check_total_price = 0
while ans:
    # print ("Give your preference: (1: read new input file, 2: print statistics for a specific product, 3: print statistics for a specific AFM, 4: exit the program)")
    ans=input("Give your preference: (1: read new input file, 2: print statistics for a specific product, 3: print statistics for a specific AFM, 4: exit the program)")
    if ans=="1":
        InvalidFile = 0
        flagsynolo = 0
        case = 0
        mistake = 0
        filename = input("Give new file\n")
        try:
            f = open(filename, 'r', encoding='utf_8')
        except:
            InvalidFile = 1
        if InvalidFile == 0:
            l = f.readline()
            while l:
                payles=1
                x = l.split()
                if len(x) == 1:
                    #number of '-'
                    for i in range(len(l)-1):
                        if l[i] != '-':
                            payles = 0
                else:
                    payles = 0
                if payles == 1:
                    case = 0
                    if mistake == 0 and flagsynolo == 1:
                        monimo_d2 = deepcopy(tmp_d2)
                        monimo_d3 = deepcopy(tmp_d3)
                        # print('Swsti apodeiksi')
                    else:
                        tmp_d2 = deepcopy(monimo_d2)
                        tmp_d3 = deepcopy(monimo_d3)
                        # print('Lathos apodeiksi')
                        mistake = 0
                    flagsynolo=0
                if case == 0:
                    x = l.split()
                    if len(x) == 1:
                         #number of '-'
                        for i in range(len(l)-1):
                            if l[i] != '-':
                                mistake = 1
                        case = 1
                    else:
                        mistake = 2
                elif case == 1:
                    case = 2
                    x = l.split(':')
                    y = l.split()

                    if len(x) != 2 or len(y) != 2 or x[0].upper() != 'ΑΦΜ' or len(y[1]) != 10:
                        mistake = 3
                    else:
                        try:
                            float(x[1])
                        except :
                            mistake = 4
                elif case == 2:                 #first item
                    case = 3
                    y = l.split()
                    x = l.split(':')
                    item_spaces = len(x[0].split()) - 1
                    if len(x) == 1:
                        mistake = 5
                    if len(x) != 2 or len(y) != (4 + item_spaces):
                        mistake = 6
                    else:
                        try:
                            y1 = float(y[1+item_spaces])
                            y2 = float(y[2+item_spaces])
                            y3 = float(y[3+item_spaces])
                        except:
                            mistake = 7
                    if mistake == 0 :
                        if round(y1 * y2, 2) != round(y3,2):
                            mistake = 301
                        else:
                            check_total_price = y3
                elif case == 3:
                    y = l.split()
                    x = l.split(':')
                    item_spaces = len(x[0].split()) - 1
                    # print(y, len(y), item_spaces)
                    if len(y) == 2:      #check synolo
                        case = 0
                        flagsynolo = 1
                        if y[0].upper() != 'ΣΥΝΟΛΟ:':
                            mistake = 8
                        else:
                            try:
                                synolo = float(x[1])
                            except:
                                mistake = 9
                        if mistake == 0 :
                            if (synolo != check_total_price):
                                mistake = 401
                    elif len(y) == (4 + item_spaces):      #check items
                        x = l.split(':')
                        if len(x) == 1:
                            mistake = 5

                        if len(x) != 2 or len(y) != (4 + item_spaces):
                            mistake = 66
                        else:
                            try:
                                y1 = float(y[1+ item_spaces])
                                y2 = float(y[2+ item_spaces])
                                y3 = float(y[3+ item_spaces])
                            except:
                                mistake = 77
                        if mistake == 0 :
                            if round(y1 * y2, 2) != round(y3,2):
                                mistake = 301
                            else:
                                check_total_price = round(y3 + check_total_price,2)
                    else:
                        mistake = 10



                    y = l.split()
                # print('mistake' ,mistake)
                # print('check_total_price' ,check_total_price)
                #twra akolou8ei h apo8hkeysh stoixeiwn apodeiksewn me katallhla leksika wste na boleyei gia ta erwthmata 2 kai 3
                if mistake == 0:
                    x = l.split(":")
                    x[0] = x[0].upper()     # onoma proiontos tis grammis stin opoia vriskomaste
                    if x[0] == "ΑΦΜ":
                        j = x[1].split()
                        afm = j[0]          # AFM tis apodeiksis stin opoia vriskomaste

                    if x[0] != "ΑΦΜ" and x[0] != "ΣΥΝΟΛΟ" and len(x)>1:
                        if x[0] in tmp_d2:
                            tmp_d=tmp_d2[x[0]]
                        else:
                            tmp_d={}
                        if afm in tmp_d3:
                            tmp_3=tmp_d3[afm]
                        else:
                            tmp_3={}
                        stoixeia = x[1].split()
                        total_price = stoixeia[2]

                        if afm in tmp_d: #
                            # print (count, float(tmp_d[afm]), float(total_price)
                            tmp_d[afm] = round(float(tmp_d[afm]) + float(total_price),2)
                        else:
                            tmp_d[afm] = total_price
                        # print(total_price, float(total_price))

                        if x[0] in tmp_3:
                            # print (count, float(tmp_d[afm]), float(total_price) )
                            tmp_3[x[0]] = round(float(tmp_3[x[0]]) + float(total_price),2)
                        else:
                            tmp_3[x[0]] = total_price

                        tmp_d2[x[0]]=deepcopy(tmp_d)
                        tmp_d3[afm]=deepcopy(tmp_3)
                l = f.readline()
    elif ans=="2":
        item = input("Give product name\n")
        item = item.upper()
        #print("item: ",item)
    elif ans=="3":
        given_afm = input("Give AFM\n")
    elif ans=="4":
        ans = 0


    if ans == "2" or ans == "3":        #check files


        # start_time = time.time()
        # sort by afm
        if ans=="2":
            if item in monimo_d2:
                lexiko2=monimo_d2[item]
                sorted_d = sorted(lexiko2.items(), key=operator.itemgetter(0))
                d = dict(sorted_d)
                for i in d:
                    print(i, "{0:.2f}".format(float(d[i])))
        if ans=="3":
            if given_afm in monimo_d3:
                lexiko3=monimo_d3[given_afm]
                sorted_d = sorted(lexiko3.items(), key=operator.itemgetter(0))
                d = dict(sorted_d)
                for i in d:
                    print(i, "{0:.2f}".format(float(d[i])))
        # elapsed_time = time.time() - start_time
        #print('time:',elapsed_time)
