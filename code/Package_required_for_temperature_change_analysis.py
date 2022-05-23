import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings 
warnings.filterwarnings('ignore')
import plotly.graph_objects as go
from matplotlib.pyplot import figure
import matplotlib.ticker as mticker
import bar_chart_race as bcr
import os
import pickle
import matplotlib.animation as animation
from matplotlib import style
import plotly
import plotly.express as px
import time

continent_country = pd.read_excel("../datasets/raw-datasets/country_Continent.xlsx", usecols=['country','code_3','continent'])
continent_country.columns = ['Country','Code','Continent']
continent_country_dict = continent_country.set_index('Country').to_dict()

Temperature_Data_Of = pickle.load(open( "./../datasets/cleaned-datasets/Temperature_Data_Of_World.p", "rb" ) )

# bplotdf = Temperature_Data_Of['India'].copy()


# bplotdf.drop(bplotdf.iloc[:, 101:], axis=1, inplace=True)
# bplotdf = bplotdf[12:]
# bplotdf = bplotdf.transpose()
# bplotdf.columns = bplotdf.iloc[0]
# bplotdf = bplotdf[1:]
# bplotdf = bplotdf.reset_index()
# bplotdf = bplotdf.drop(columns=["index"])

# bplotdf = bplotdf.groupby(bplotdf.index // 10).sum()
# bplotdf = (bplotdf / 10).round(2)
# bplotdf.insert(0, 'Year', 'Null')
# bplotdf['Year'] = ['1912-1921','1922-1931','1932-1941','1942-1951','1952-1961','1962-1971',
#                                         '1972-1981', '1982-1991', '1992-2001', '2002-2011']
# bplotdf = bplotdf.transpose()
# bplotdf.columns = bplotdf.iloc[0]
# bplotdf = bplotdf[1:]
# # display(bplotdf)
# print(bplotdf)

# print('checkpoint 2')

# min1 = bplotdf.iloc[1]
# max1 = bplotdf.iloc[2]
# median1 = bplotdf.iloc[3]
# average1 = bplotdf.iloc[0]

# fig1 = go.Figure()
# fig1.add_trace(go.Box(y = min1, name ='Minimum'))
# fig1.add_trace(go.Box(y = max1, name ='Maximun'))
# fig1.add_trace(go.Box(y = median1, name ='Median'))
# fig1.add_trace(go.Box(y = average1, name ='Mean'))
# fig1.update_layout(title = "Boxplot for minimum, maximum, median and mean temperature for " + cname + " with respect to last 100 years                                     is ",)
# fig1.show()

# #Now lets see how Median and Average temperature values are varying in the past 100 years for asked country

# print('checkpoint 3')

# figure1_df = bplotdf.copy()
# years_arr = bplotdf.columns.values

# average_df = figure1_df.iloc[0]
# average_df = average_df.values

# min_df = figure1_df.iloc[1]
# min_df = min_df.values

# max_df = figure1_df.iloc[2]
# max_df = max_df.values

# median_df = figure1_df.iloc[3]
# median_df = median_df.values

# fig = figure(figsize=(10, 8), dpi = 80)
# ax = fig.add_subplot(2,1,1)

# plt.plot(years_arr, average_df, label = "Average Temperature")
# plt.plot(years_arr, median_df, label = "Median Temperature")
# ax = plt.gca()
# plt.xticks(rotation = 45)
        
# print('checkpoint 4')

# plt.legend()
# plt.xlabel('Year')
# plt.ylabel('Temperature in Fahrenheit')
# plt.title("Below graph shows how median and average temperature values of " + cname + " got varied in past 100 years with respect to 10-10 years time frame")
# plt.show()

# #Now lets see how Minimum temperature value is varying in the past 100 years for asked country

# figure(figsize=(10, 8), dpi = 80)
# ax1 = fig.add_subplot(2,1,1)
# ax1.grid()

# plt.plot(years_arr, min_df, label = "Minimum Temperature")
# ax1 = plt.gca()
# plt.xticks(rotation = 45)
        
# plt.legend()
# plt.xlabel('Year')
# plt.ylabel('Temperature in Fahrenheit')
# plt.title("Below graph shows how minimum temperature value of " + cname + " got varied in past 100 years with respect to 10-10 years time frame")
# plt.show()

# #Now lets see how Maximum temperature value is varying in the past 100 years for asked country

# figure(figsize=(10, 8), dpi = 80)
# ax2 = fig.add_subplot(2,1,1)
# ax2.grid()

# plt.plot(years_arr, max_df, label = "Maximum Temperature")
# ax2 = plt.gca()
# plt.xticks(rotation = 45)
# plt.legend()
# plt.xlabel('Year')
# plt.ylabel('Temperature in Fahrenheit')
# plt.title("Below graph shows how maximum temperature value of " + cname + " got varied in past 100 years with respect to 10-10 years time frame")
# plt.show()

# fig.tight_layout()



def Run_All():  
    try:
        print("\nShowing analysis no 1.\n")
        Function_1()
    except:
        Country_names()
    try:
        print("\nShowing analysis no 2.\n")
        Function_2()
    except:
        Country_names()
    print("\nShowing analysis no 3...\n")    
    Function_3()
    print("\nShowing analysis no 4...\n")
    Function_4()

def Country_names():
    Temperature_Data_By_Country = pd.read_csv('./../datasets/raw-datasets/GlobalLandTemperatures_GlobalLandTemperaturesByCountry.csv',
                                                error_bad_lines=False)
    Temperature_Data_By_Country = Temperature_Data_By_Country[3239:]
    Temperature_Data_By_Country = Temperature_Data_By_Country.dropna()
    Countries_name = list(Temperature_Data_By_Country.Country.unique())
    print("\nYou typed wrong country name..choose from any one of these.. \n\n",Countries_name)
    
def Function_3():
    Average_TCW = pd.read_csv('../datasets/cleaned-datasets/Average_temperature_Country_Wise.csv',
                                error_bad_lines=False)
    Minimum_TCW = pd.read_csv('../datasets/cleaned-datasets/Minimum_temperature_Country_Wise.csv',
                                 error_bad_lines=False)
    Maximum_TCW = pd.read_csv('../datasets/cleaned-datasets/Maximum_temperature_Country_Wise.csv',
                                 error_bad_lines=False)
    Median_TCW = pd.read_csv('../datasets/cleaned-datasets/Median_temperature_Country_Wise.csv',
                                 error_bad_lines=False)

    Average_TCW = Average_TCW.drop(columns=["Month/Year"])
    Minimum_TCW = Minimum_TCW.drop(columns=["Month/Year"])
    Maximum_TCW = Maximum_TCW.drop(columns=["Month/Year"])
    Median_TCW = Median_TCW.drop(columns=["Month/Year"])

    datasets =  [Average_TCW, Minimum_TCW, Maximum_TCW, Median_TCW]

    def Get_value(value,country):
        try:
            return continent_country_dict[value][country]
        except:
            return 'null'
    n = 0
    for value in datasets:
        result1 = value.transpose()
        result1 = result1.reset_index()
        result1.rename(columns = {'index': 'Country'}, inplace = True)
        result1.insert(1, 'Code', 'Null')
        result1.insert(2, 'Continent name', 'Null')
        
        for i in result1.index:
            country  = result1.iat[i,0]
            result1.iat[i,1] = Get_value('Code',country)
            result1.iat[i,2] = Get_value('Continent',country)
            
        result1 = result1.loc[(result1['Code'] != 'null') & (result1['Continent name'] != 'null')]
        result1 = result1.dropna()
        result1 = result1.reset_index()
        result1 = result1.drop(columns=["index"])

        list = ['Country','Code','Continent name','Year','Temp_value']
        new = pd.DataFrame(columns=list)
        new_df = pd.DataFrame()
        for i in range(1912,2012):
            for j in range(0,182):
                new['Country'] = [result1.iat[j,0]]
                new['Code']    = result1.iat[j,1]
                new['Continent name'] = result1.iat[j,2]
                new['Year'] = str(i)
                new['Temp_value'] = result1.iat[j,i-1909]
                new_df = new_df.append(new,ignore_index = True)
        if(n == 0):
            title_map = 'MAP 1: Below map shows average temperature data over last 100 years for every country world-wide'
        elif(n == 1):
            title_map = 'MAP 2: Below map shows minimum temperature data over last 100 years for every country world-wide'
        elif(n == 2):
            title_map = 'MAP 3: Below map shows maximum temperature data over last 100 years for every country world-wide'
        elif(n == 3):
            title_map = 'MAP 4: Below map shows median temperature data over last 100 years for every country world-wide'

        n += 1
        fig = px.choropleth(new_df, 
                            locations = 'Code', 
                            color = 'Temp_value',
                            color_continuous_scale = "reds",
                            animation_frame = 'Year',
                            title = title_map,
                            hover_data = ['Country']
                           )
        fig.update_geos(fitbounds="locations", visible=False)
        fig.show()

def Function_4():
    Average_10_10 = pd.read_csv('../datasets/cleaned-datasets/Average_temperature_Country_Wise_10_10_years.csv',
                                error_bad_lines=False)
    Minimum_10_10 = pd.read_csv('../datasets/cleaned-datasets/Minimum_temperature_Country_Wise_10_10_years.csv',
                                 error_bad_lines=False)
    Maximum_10_10 = pd.read_csv('../datasets/cleaned-datasets/Maximum_temperature_Country_Wise_10_10_years.csv',
                                 error_bad_lines=False)
    Median_10_10 = pd.read_csv('../datasets/cleaned-datasets/Median_temperature_Country_Wise_10_10_years.csv',
                                 error_bad_lines=False)

    Average_10_10 = Average_10_10.drop(columns=["Year"])
    Minimum_10_10 = Minimum_10_10.drop(columns=["Year"])
    Maximum_10_10 = Maximum_10_10.drop(columns=["Year"])
    Median_10_10 = Median_10_10.drop(columns=["Year"])

    datasets =  [Average_10_10, Minimum_10_10, Maximum_10_10, Median_10_10 ]
    years_value = ['1912-1921','1922-1931','1932-1941','1942-1951','1952-1961','1962-1971','1972-1981', '1982-1991',
                   '1992-2001', '2002-2011']
  
    def Get_value(value,country):
        try:
            return continent_country_dict[value][country]
        except:
            return 'null'
    n = 0
    for value in datasets:
        result1 = value.transpose()
        
        result1 = result1.reset_index()
        result1.rename(columns = {'index': 'Country'}, inplace = True)
        result1.insert(1, 'Code', 'Null')
        result1.insert(2, 'Continent name', 'Null')
        
        for i in result1.index:
            country  = result1.iat[i,0]
            result1.iat[i,1] = Get_value('Code',country)
            result1.iat[i,2] = Get_value('Continent',country)
            
        result1 = result1.loc[(result1['Code'] != 'null') & (result1['Continent name'] != 'null')]
        result1 = result1.dropna()
        result1 = result1.reset_index()
        result1 = result1.drop(columns=["index"])

        list = ['Country','Code','Continent name','Year','Temp_value']
        new = pd.DataFrame(columns=list)
        new_df = pd.DataFrame()
        for i in range(0,10):
            for j in range(0,182):
                new['Country'] = [result1.iat[j,0]]
                new['Code']    = result1.iat[j,1]
                new['Continent name'] = result1.iat[j,2]
                new['Year'] = years_value[i]
                new['Temp_value'] = result1.iat[j,i+3]
                new_df = new_df.append(new,ignore_index = True)
                
        if(n == 0):
            title_map = 'MAP 1: Average temperature data over last 100 years for every country in a 10-10 years time frame'
        elif(n == 1):
            title_map = 'MAP 2: Minimum temperature data over last 100 years for every country in a 10-10 years time frame'
        elif(n == 2):
            title_map = 'MAP 3: Maximum temperature data over last 100 years for every country in a 10-10 years time frame'
        elif(n == 3):
            title_map = 'MAP 4: Median temperature data over last 100 years for every country in a 10-10 years time frame'

        n += 1
        fig = px.choropleth(new_df, 
                            locations = 'Code', 
                            color = 'Temp_value',
                            color_continuous_scale = "reds",
                            animation_frame = 'Year',
                            title = title_map,
                            hover_data = ['Country']
                           )
        fig.update_geos(fitbounds="locations", visible=False)
        fig.show()
        
def Function_2():

    print("Enter country name : ")
    cname = input()
    print("\nTemperature data for last 100 years with 10-10 years time frame  for country ",cname," is : ")
    # Displaying dataset of last 100 years of asked country
    bplotdf = Temperature_Data_Of[cname].copy()
    bplotdf.drop(bplotdf.iloc[:, 101:], axis=1, inplace=True)
    bplotdf = bplotdf[12:]
    bplotdf = bplotdf.transpose()
    bplotdf.columns = bplotdf.iloc[0]
    bplotdf = bplotdf[1:]
    bplotdf = bplotdf.reset_index()
    bplotdf = bplotdf.drop(columns=["index"])
    bplotdf = bplotdf.groupby(bplotdf.index // 10).sum()
    bplotdf = (bplotdf / 10).round(2)
    bplotdf.insert(0, 'Year', 'Null')
    bplotdf['Year'] = ['1912-1921','1922-1931','1932-1941','1942-1951','1952-1961','1962-1971',
                                           '1972-1981', '1982-1991', '1992-2001', '2002-2011']
    bplotdf = bplotdf.transpose()
    bplotdf.columns = bplotdf.iloc[0]
    bplotdf = bplotdf[1:]
    display(bplotdf)
    min1 = bplotdf.iloc[1]
    max1 = bplotdf.iloc[2]
    median1 = bplotdf.iloc[3]
    average1 = bplotdf.iloc[0]
    fig1 = go.Figure()
    fig1.add_trace(go.Box(y = min1, name ='Minimum'))
    fig1.add_trace(go.Box(y = max1, name ='Maximun'))
    fig1.add_trace(go.Box(y = median1, name ='Median'))
    fig1.add_trace(go.Box(y = average1, name ='Mean'))
    fig1.update_layout(title = "Boxplot for minimum, maximum, median and mean temperature for " + cname + " with respect to last 100 years                                     is ",)
    fig1.show()
    #Now lets see how Median and Average temperature values are varying in the past 100 years for asked country
    figure1_df = bplotdf.copy()
    years_arr = bplotdf.columns.values
    average_df = figure1_df.iloc[0]
    average_df = average_df.values
    min_df = figure1_df.iloc[1]
    min_df = min_df.values
    max_df = figure1_df.iloc[2]
    max_df = max_df.values
    median_df = figure1_df.iloc[3]
    median_df = median_df.values
    fig = figure(figsize=(10, 8), dpi = 80)
    ax = fig.add_subplot(2,1,1)
    plt.plot(years_arr, average_df, label = "Average Temperature")
    plt.plot(years_arr, median_df, label = "Median Temperature")
    ax = plt.gca()
    plt.xticks(rotation = 45)
    plt.legend()
    plt.xlabel('Year')
    plt.ylabel('Temperature in Fahrenheit')
    plt.title("Below graph shows how median and average temperature values of " + cname + " got varied in past 100 years with respect to 10-10 years time frame")
    plt.show()
    #Now lets see how Minimum temperature value is varying in the past 100 years for asked country
    figure(figsize=(10, 8), dpi = 80)
    ax1 = fig.add_subplot(2,1,1)
    ax1.grid()
    plt.plot(years_arr, min_df, label = "Minimum Temperature")
    ax1 = plt.gca()
    plt.xticks(rotation = 45)
    plt.legend()
    plt.xlabel('Year')
    plt.ylabel('Temperature in Fahrenheit')
    plt.title("Below graph shows how minimum temperature value of " + cname + " got varied in past 100 years with respect to 10-10 years time frame")
    plt.show()
    #Now lets see how Maximum temperature value is varying in the past 100 years for asked country
    figure(figsize=(10, 8), dpi = 80)
    ax2 = fig.add_subplot(2,1,1)
    ax2.grid()
    plt.plot(years_arr, max_df, label = "Maximum Temperature")
    ax2 = plt.gca()
    plt.xticks(rotation = 45)
    plt.legend()
    plt.xlabel('Year')
    plt.ylabel('Temperature in Fahrenheit')
    plt.title("Below graph shows how maximum temperature value of " + cname + " got varied in past 100 years with respect to 10-10 years time frame")
    plt.show()
    fig.tight_layout()
    
    
    
def Function_1():
    print("Enter country name : ")
    time.sleep(0.05)
    cname = input()
    print("\nTemperature data for last 100 years for country ",cname," is : ")

    # Displaying dataset of last 100 years of asked country

    display(Temperature_Data_Of[cname])

    #Making boxplot for showing how minimum, maximum, median and mean temperature values are varying for last 100 years 

    bplotdf = Temperature_Data_Of[cname].copy()
    min1 = bplotdf['Minimum']
    min1 = min1[0:12]
    max1 = bplotdf['Maximum']
    max1 = max1[0:12]
    median1 = bplotdf['Median']
    median1 = median1[0:12]
    average1 = bplotdf['Average']
    average1 = average1[0:12]

    fig1 = go.Figure()
    fig1.add_trace(go.Box(y = min1, name ='Minimum'))
    fig1.add_trace(go.Box(y = max1, name ='Maximun'))
    fig1.add_trace(go.Box(y = median1, name ='Median'))
    fig1.add_trace(go.Box(y = average1, name ='Mean'))
    fig1.update_layout(title = "Boxplot for minimum, maximum, median and mean temperature for " + cname + " with respect to last 100 years                                    is ",)
    fig1.show()

    #Now lets see how Median and Average temperature values are varying in the past 100 years for asked country

    figure1_df = Temperature_Data_Of[cname].copy()
    years_arr = figure1_df.columns.values
    years_arr = years_arr[1:-4]

    average_df = figure1_df.iloc[12]
    average_df = average_df[1:-4]
    average_df = average_df.values

    min_df = figure1_df.iloc[13]
    min_df = min_df[1:-4]
    min_df = min_df.values

    max_df = figure1_df.iloc[14]
    max_df = max_df[1:-4]
    max_df = max_df.values

    median_df = figure1_df.iloc[15]
    median_df = median_df[1:-4]
    median_df = median_df.values

    fig = figure(figsize=(10, 8), dpi = 80)
    ax = fig.add_subplot(2,1,1)

    plt.plot(years_arr, average_df, label = "Average Temperature")
    plt.plot(years_arr, median_df, label = "Median Temperature")
    ax = plt.gca()
    plt.xticks(rotation = 45)
    for label in ax.get_xaxis().get_ticklabels()[::2]:
        label.set_visible(False)

    for label in ax.get_xaxis().get_ticklabels()[::2]:
        label.set_visible(False)

    for label in ax.get_xaxis().get_ticklabels()[::5]:
        label.set_visible(False)

    plt.legend()
    plt.xlabel('Year')
    plt.ylabel('Temperature in Fahrenheit')
    plt.title("Below graph shows how median and average temperature values of " + cname + " got varied in past 100 years")
    plt.show()

    #Now lets see how Minimum temperature value is varying in the past 100 years for asked country

    figure(figsize=(10, 8), dpi = 80)
    ax1 = fig.add_subplot(2,1,1)
    ax1.grid()

    plt.plot(years_arr, min_df, label = "Minimum Temperature")
    ax1 = plt.gca()
    plt.xticks(rotation = 45)
    for label in ax1.get_xaxis().get_ticklabels()[::2]:
        label.set_visible(False)

    for label in ax1.get_xaxis().get_ticklabels()[::2]:
        label.set_visible(False)

    for label in ax1.get_xaxis().get_ticklabels()[::5]:
        label.set_visible(False)

    plt.legend()
    plt.xlabel('Year')
    plt.ylabel('Temperature in Fahrenheit')
    plt.title("Below graph shows how minimum temperature value of " + cname + " got varied in past 100 years")
    plt.show()

    #Now lets see how Maximum temperature value is varying in the past 100 years for asked country

    figure(figsize=(10, 8), dpi = 80)
    ax2 = fig.add_subplot(2,1,1)
    ax2.grid()

    plt.plot(years_arr, max_df, label = "Maximum Temperature")
    ax2 = plt.gca()
    plt.xticks(rotation = 45)
    for label in ax2.get_xaxis().get_ticklabels()[::2]:
        label.set_visible(False)

    for label in ax2.get_xaxis().get_ticklabels()[::2]:
        label.set_visible(False)

    for label in ax2.get_xaxis().get_ticklabels()[::5]:
        label.set_visible(False)

    plt.legend()
    plt.xlabel('Year')
    plt.ylabel('Temperature in Fahrenheit')
    plt.title("Below graph shows how maximum temperature value of " + cname + " got varied in past 100 years")
    plt.show()

    fig.tight_layout()