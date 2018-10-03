"""
File Name: growth.py
Author's Name: Tejaswini Jagtap
"""

from utils import *

def sorted_growth_data(data,year1,year2):
    """
    sorts from higher to lower the countries according to the growth in life expectancies from year1 to year2
    :param data: data dictionary containing country name as key
    :param year1: starting year
    :param year2: ending year
    :return: sorted list with country name and its growth in life expectancies from year1 to year2
    """
    CountryValueTemp={}
    CountryValue=[]
    for k,v in data.items():
        if v[3][year1]!='' and v[3][year2]!='':
            CountryValueTemp[abs(v[3][year1]-v[3][year2])]=k
    #print(CountryValueTemp)
    a=list(CountryValueTemp.keys())
    a.sort(reverse=True)
    for i in a:
        CountryValue.append([CountryValueTemp[i],i])
    return CountryValue

def main():
    """
    prints top and bottom 10 growth in life expectancies from year1 to year2 as sorted
    :return:
    """
    (entries, larger, meta, data, reg, inc) = read_data('worldbank_life_expectancy')
    year1=int(input('Enter starting year of interest (-1 to quit): '))
    year2 = int(input('Enter ending year of interest (-1 to quit): '))
    while year1!=-1 and year2!=-1:
        if year1>1959 and year1<2016 and year2>1959 and year2<2016:
            reg=input("Enter region (type 'all' to consider all): ")
            reg_data=filter_region(data,reg)
            #print(reg_data)
            if reg_data:
                inc = input("Enter income category (type 'all' to consider all): ")
                inc_data=filter_income(reg_data,inc)
                if inc_data:
                    cv_data=sorted_growth_data(inc_data,year1,year2)
                    i=0
                    print("")
                    print("Top 10 Life Expectancy Growth:", year1, " to", year2)
                    while i!=10 and i!=len(cv_data):
                        print(cv_data[i])
                        i+=1
                    i=len(cv_data)-1
                    print("")
                    print("Bottom 10 Life Expectancy Growth:", year1, " to", year2)
                    while i != len(cv_data)-11 and i != -1:
                        print(cv_data[i])
                        i-=1
                else:
                    print(inc+' not a valid income')
            else:
                print(reg+' not a valid region')

        else:
            print('Valid years are 1960-2015')
        print("")
        year1 = int(input('Enter starting year of interest (-1 to quit): '))
        if year1==-1:
            break
        year2 = int(input('Enter ending year of interest (-1 to quit): '))

if __name__=='__main__':
    main()

