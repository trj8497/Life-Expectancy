"""
File Name: utils.py
Author's Name: Tejaswini Jagtap
"""
from rit_lib import *
def read_data(filename):
    """
    reads the file
    :param filename: name of the file
    :return: number of entities, number of countries/territories, metadata dic, data dic, set of only countries in the file, set of income of countries only in the file
    """
    file_meta='data/'+filename+"_metadata.txt"
    file_data='data/'+filename+'_data.txt'
    num_entries=0
    larger_teritories=0
    reg_countries=[]
    income=[]
    dic_metadata = {}
    dic_data = {}
    with open(file_meta) as f:
        i=0
        for line in f:
            if i!=0:
                line = line.strip().split(",")
                dic_metadata[line[0]]=line[1:3]
                #print(dic_metadata)
                if line[1]=='' and line[2]=='':
                    larger_teritories+=1
                else:
                    reg_countries.append(line[1])
                    income.append(line[2])
                num_entries+=1
            i=1
        i=0
    with open(file_data) as f:
        for line in f:
            if i != 0:
                line = line.strip().split(",")
                dic_data[line[0]]=dic_metadata[line[1]]+[line[1]]
                #print(dic_data)
                years={}
                line_no=2
                year=1960
                while year!=2016:
                    years[year]=line[line_no]
                    line_no+=1
                    year+=1
                dic_data[line[0]].extend([years])
                #print(dic_data)
            i=1
    return (num_entries,larger_teritories,dic_metadata,dic_data,set(reg_countries),set(income))

def filter_region(data,region):
    """
    filter the data as per the input
    :param data: data dictionary containing country name as key
    :param region: region from the list reg_countries
    :return: new data restricted to input region
    """
    new_data = {}
    if region=='all':
        for k, v in data.items():
            if not(v[0]== '' and v[1]==''):
                new_data[k] = data[k]
    else:
        for k,v in data.items():
            if v[0]==region:
                new_data[k]=data[k]
    return new_data

def filter_income(data,income):
    """
    filter the data as per the given
    :param data: data: data dictionary containing
    :param income: income from the list income
    :return: new data restricted to input income category
    """
    new_data = {}
    if income=='all':
        for k, v in data.items():
            if not(v[0]== '' and v[1]==''):
                new_data[k] = data[k]
    else:
        for k,v in data.items():
            if v[1]==income:
                new_data[k]=data[k]
    return new_data

def main():
    """
    prints number of entities, number of countries, regions and their country count, income categories and their country count, countries in specific income category, countries in specific region, life expectancies of countries.
    """
    (entries, larger, meta, data, reg, inc) = read_data('worldbank_life_expectancy')
    print("Total number of entities: ",entries)
    print("Number of countries/territories: ",entries - larger)
    print("")
    print("Regions and their country count:")
    for i in reg:
        region_data = filter_region(data, i)
        print(i, len(region_data.keys()))
    print("")
    print("Income categories and their country count:")
    for i in inc:
        income_data = filter_income(data, i)
        #print(income_data)
        print(i, len(income_data.keys()))
    print("")
    region_name = input('Enter region Name: ')
    print("Countries in the", region_name, "region:")
    region_data = filter_region(data, region_name)
    for k, v in region_data.items():
        print(k + '(' + v[2] + ')')
    print("")
    income_cat = input('Enter income category: ')
    print("Countries in the", income_cat, "income category:")
    income_data = filter_income(data, income_cat)
    for k, v in income_data.items():
        print(k + '(' + v[2] + ')')
    print("")
    life_expectancy = input("Enter name of country or country code (Enter to quit): ")
    print("Data for", life_expectancy, ":")
    while life_expectancy != "":
        if life_expectancy not in data.keys() and life_expectancy not in meta.keys():
            print(life_expectancy + 'is not a valid country name or code')
        elif life_expectancy in data.keys():
            v = data[life_expectancy]
            year = 1960
            while year != 2016:
                if v[3][year] != '':
                    print("Year:",year, " Life expectancy:",v[3][year])
                year += 1
        elif life_expectancy in meta.keys():
            for k, v in data.items():
                if v[2] == life_expectancy:
                    year = 1960
                    while year != 2016:
                        if v[3][year] != '':
                            print("Year: ", year, " Life expectancy: ", v[3][year])
                        year += 1
        print("")
        life_expectancy = input("Enter name of country or country code (Enter to quit): ")
        print("Data for", life_expectancy, ":")

if __name__ == '__main__':
    main()
