"""
File Name: drop.py
Author's Name: Tejaswini Jagtap
"""

from utils import *


Range = struct_type("Range",
                    (str, "country"),
                    (int, "year1"),
                    (int, "year2"),
                    (float, "value1"),
                    (float, "value2"))

def sorted_drop_data(data):
    """
    sorts the drops of life expectancies from year1 to year2
    :param data: data dictionary containing country name as key
    :return: sorted list of drops in life expectancies from year1 to year2
    """
    drop_data={}
    final_drop_data=[]
    for k,v in data.items():
        min_num1=float(100000)
        min_year1=0
        max_num1=float(-1)
        max_year1=0
        year=1960
        while year!=2016:
            if v[3][year]!='' and v[3][year]<min_num1:
                min_num1=v[3][year]
                min_year1=year
            year+=1

        year = 1960
        while year != min_year1 and year!=2016:
            if v[3][year] != '' and v[3][year] > max_num1:
                max_num1 = v[3][year]
                max_year1 = year
            year += 1
        min_num2=float(100000)
        min_year2=0
        max_num2=float(-1)
        max_year2=0
        year=1960
        while year!=2016:
            if v[3][year]!='' and v[3][year]>max_num2:
                max_num2=v[3][year]
                max_year2=year
            year+=1
        year = max_year2
        while year!=2016 and year!=0:
            if v[3][year] != '' and v[3][year] < min_num2:
                min_num2 = v[3][year]
                min_year2 = year
            year += 1
        if min_num1-max_num1>min_num2-max_num2:
            min_num=min_num2
            max_num=max_num2
            max_year=max_year2
            min_year=min_year2
        else:
            min_num=min_num1
            max_num=max_num1
            max_year=max_year1
            min_year=min_year1

        drop_data[min_num-max_num]=Range(k,max_year,min_year,max_num,min_num)

    d=list(drop_data.keys())
    d.sort()
    for i in d:
        final_drop_data.append(drop_data[i])
    return final_drop_data


def main():
    """
    prints the 10 worst drops in life expectancies from year1 to year2
    """
    (entries, larger, meta, data, reg, inc) = read_data('worldbank_life_expectancy')
    # data=filter_region(data,'all')
    drop_data=sorted_drop_data(data)
    print("Worst life expectancy drops: 1960 to 2015")
    for  i in range(10):
        print(drop_data[i].country+' from '+str(drop_data[i].year1)+'( '+str(drop_data[i].value1)+') to '+str(drop_data[i].year2)+'( '+str(drop_data[i].value2)+') :'+str(drop_data[i].value2-drop_data[i].value1))



if __name__=='__main__':
    main()

