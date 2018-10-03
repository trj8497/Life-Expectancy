"""
File Name: ranking.py
Author's Name: Tejaswini Jagtap
"""

from utils import *

CountryValue = struct_type("CountryValue",
                           (str, "country"),
                           (float, "value"))

def sorted_ranking_data(data,year):
    """
    sorts from higher to lower the countries according to the life expectancies
    :param data: data dictionary containing country name as key
    :param year: year between 1960 to 2015
    :return: sorted list with country name and its life expectancy
    """
    CountryValueTemp={}
    CountryValue=[]
    for k,v in data.items():
        if v[3][year]!='':
            CountryValueTemp[v[3][year]]=k
    a=list(CountryValueTemp.keys())
    a.sort(reverse=True)
    for i in a:
        CountryValue.append([CountryValueTemp[i],i])
    return CountryValue

def main():
    """
    prints top and bottom 10 life expectancies as sorted
    """
    (entries, larger, meta, data, reg, inc) = read_data('worldbank_life_expectancy')
    year=int(input('Enter year of interest (-1 to quit): '))
    while year!=-1:
        if year>1959 and year<2016:
            reg=input("Enter region (type 'all' to consider all): ")
            reg_data=filter_region(data,reg)
            if reg_data:
                inc = input("Enter income category (type 'all' to consider all): ")
                inc_data=filter_income(reg_data,inc)
                if inc_data:
                    cv_data=sorted_ranking_data(inc_data,year)
                    i=0
                    print("")
                    print("Top 10 Life Expectancy for", year)
                    while i!=10 and i!=len(cv_data):
                        print(cv_data[i])
                        i+=1
                    i=len(cv_data)-1
                    print("")
                    print("Bottom 10 Life Expectancy for", year)
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
        year = int(input('Enter year of interest (-1 to quit): '))

if __name__=='__main__':
    main()

