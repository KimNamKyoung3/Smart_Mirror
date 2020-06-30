import xlrd
from xlutils.copy import copy

wb = xlrd.open_workbook('whereRU.xlsx')
sheet = wb.sheet_by_index(0)


def get_local():
    i=1
    j=1
    k=1
    m=1
    
    city_names=set()
    state_names=set()
    town_names=set()

    while True:
        try:
            keyword = sheet.cell(i,2).value
            city_names.add(keyword)
            i = i + 1
            
        except IndexError:
            break

    city_names1 = list(city_names)
    city_names1.sort()
    print(city_names1)


    while True:
        flag = False
        i=0
        print(" ")
        city = input("1단계 선택 : ")
        for i in range(len(city_names1)):
            if city_names1[i] == city:
                flag = True
                break
        if flag == True:
            break
        else:
            print("정확히 입력하세요")

       
    while True:
        try:
            city1=sheet.cell(j,2).value
            keyword = sheet.cell(j,3).value
            if city1 == city:
                if keyword == "":
                    state_names.add(city1)
                else:
                    state_names.add(keyword)
            
            j = j + 1
                        
        except IndexError:
            break

    state_names1 = list(state_names)
    state_names1.sort()
    print(state_names1)
        
    while True:
        flag = False
        i=0
        print(" ")
        state = input("2단계 선택 : ")
        for i in range(len(state_names1)):
            if state_names1[i] == state:
                flag = True
                break
        if flag == True:
            break
        else:
            print("정확히 입력하세요")


    while True:
        try:
            city1=sheet.cell(k,2).value
            state1 = sheet.cell(k,3).value
            keyword = sheet.cell(k,4).value
            if city1 == city:
                if state1 == state:
                    if keyword == "":
                        town_names.add(state1)
                    else:
                        town_names.add(keyword)
            k = k + 1
                        
        except IndexError:
            break

    town_names1 = list(town_names)
    town_names1.sort()
    print(town_names1)

    while True:
        flag = False
        i=0
        print(" ")
        town = input("2단계 선택 : ")
        for i in range(len(town_names1)):
            if town_names1[i] == town:
                flag = True
                break
        if flag == True:
            break
        else:
            print("정확히 입력하세요")


    while True:
        try:
            city1=sheet.cell(m,2).value
            state1 = sheet.cell(m,3).value
            town1 = sheet.cell(m,4).value
            if city1 == city:
                if state1 == state:
                    if town1 == town:
                        nx = sheet.cell(m,5).value
                        ny = sheet.cell(m,6).value
            m = m + 1
                        
        except IndexError:
            break

    return nx, ny

