import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plot

covid_data= pd.read_csv('COVID_county_data.csv')
acs17_data= pd.read_csv('acs2017_census_tract_data.csv')


# Part A - Aggregate Census Data to County Level

counties=["Loudoun", "Washington", "Harlan", "Malheur"]
states=["Virginia", "Oregon", "Kentucky", "Oregon"]

allrecords=[]
each=[]

for i in range(len(counties)):
  check_county=acs17_data[acs17_data['County']==counties[i]+" County"]
  county=check_county[check_county['State']==states[i]]

  each.append(counties[i])
  each.append(states[i])
  each.append(county['TotalPop'].sum(axis=0))
  each.append(county['Poverty'].mean(axis=0))
  each.append(county['IncomePerCap'].mean(axis=0))
  allrecords.append(each)
  each=[]

aggregated_df=pd.DataFrame.from_records(allrecords)
aggregated_df.round({"3":3,"4":3})
aggregated_df.columns = ['County','State','Population','Poverty','PerCapitaIncome']
#print(aggregated_df)


# Part B - Simplify the COVID Data

allrecords=[]
each=[]
for i in range(len(counties)):
  check_county1=covid_data[covid_data['county']==counties[i]]
  c_county=check_county1[check_county1['state']==states[i]]
  dec=c_county[c_county['date'].between("2020-12-01","2020-12-31")]

  each.append(counties[i])
  each.append(states[i])
  each.append(c_county['cases'].sum(axis=0))
  each.append(dec['cases'].sum(axis=0))
  each.append(c_county['deaths'].sum(axis=0))
  each.append(dec['deaths'].sum(axis=0))

  allrecords.append(each)
  each=[]

covid_df=pd.DataFrame.from_records(allrecords)
covid_df.columns = ['County','State', 'TotalCases','Dec2020Cases','TotalDeaths','Dec2020Deaths']
#print(covid_df)


# Part C - Integrate COVID Data with ACS Data

integrate_df = pd.merge(aggregated_df,covid_df,on='County',how='inner')
del integrate_df['State_y']
integrate_df.rename(columns = {'State_x':'State'}, inplace = True)
oregon_r = integrate_df[integrate_df['State']=='Oregon']
oregon_r['TotalCases'] = (oregon_r['TotalCases']*100000)/oregon_r['Population']
oregon_r['TotalDeaths'] = (oregon_r['TotalDeaths']*100000)/oregon_r['Population']
#print(oregon_r)


# Part D1 - Analysis

allrecords.clear()
each.clear()

state = covid_data[covid_data['state'] == 'Oregon']
d_allcounties = state['county'].unique()
allcounties = list(d_allcounties)

for i in range(len(allcounties)):
    each.append('Oregon')
    acs_county = acs17_data[acs17_data['County'] == allcounties[i] + " County"]
    covid_county = covid_data[covid_data['county'] == allcounties[i]]
    each.append(allcounties[i])

    totalcases = covid_county['cases'].sum(axis=0)
    dec = covid_county[covid_county['date'].between("2020-12-01", "2020-12-31")]
    deaths = covid_county['deaths'].sum(axis=0)
    totalpopulation = acs_county['TotalPop'].sum(axis=0)
    totalcases = (totalcases * 100000) / totalpopulation
    each.append(totalcases)
    each.append(dec['cases'].sum(axis=0))
    totaldeath = (deaths * 100000) / totalpopulation
    each.append(totaldeath)
    each.append(dec['deaths'].sum(axis=0))
    each.append(totalpopulation)
    each.append(acs_county['Poverty'].mean(axis=0))
    each.append(acs_county['IncomePerCap'].mean(axis=0))

    allrecords.append(each)
    each = []

oregon_df = pd.DataFrame.from_records(allrecords)
oregon_df = oregon_df.dropna(axis=0)
oregon_df.columns = ['State', 'County', 'TotalCases', 'Dec2020Cases', 'TotalDeaths', 'Dec2020Deaths', 'Population',
                     'Poverty', 'PerCapitaIncome']
#print(oregon_df)


# Part D2 - Analysis

#print(oregon_df['TotalCases'].corr(oregon_df['Poverty']))
#print(oregon_df['TotalDeaths'].corr(oregon_df['Poverty']))
#print(oregon_df['TotalCases'].corr(oregon_df['PerCapitaIncome']))
#print(oregon_df['TotalDeaths'].corr(oregon_df['PerCapitaIncome']))
#print(oregon_df['Dec2020Cases'].corr(oregon_df['Poverty']))
#print(oregon_df['Dec2020Deaths'].corr(oregon_df['Poverty']))
#print(oregon_df['Dec2020Cases'].corr(oregon_df['PerCapitaIncome']))
#print(oregon_df['Dec2020Deaths'].corr(oregon_df['PerCapitaIncome']))


# Part D3 - Analysis

allrecords.clear()
each.clear()

d_allcounties = covid_data['county'].unique()
allcounties = list(d_allcounties)

for i in range(len(allcounties)):
    acs_county = acs17_data[acs17_data['County'] == allcounties[i] + " County"]
    covid_county = covid_data[covid_data['county'] == allcounties[i]]
    each.append(allcounties[i])

    totalcases = covid_county['cases'].sum(axis=0)
    dec = covid_county[covid_county['date'].between("2020-12-01", "2020-12-31")]
    deaths = covid_county['deaths'].sum(axis=0)

    totalcases = (totalcases * 100000) / totalpopulation
    each.append(totalcases)
    each.append(dec['cases'].sum(axis=0))
    totaldeath = (deaths * 100000) / totalpopulation
    each.append(totaldeath)
    each.append(dec['deaths'].sum(axis=0))
    each.append(acs_county['TotalPop'].sum(axis=0))
    each.append(acs_county['Poverty'].mean(axis=0))
    each.append(acs_county['IncomePerCap'].mean(axis=0))

    allrecords.append(each)
    each.clear()

allcounties_df = pd.DataFrame.from_records(allrecords)
allcounties_df.columns = ['County', 'TotalCases', 'Dec2020Cases', 'TotalDeaths', 'Dec2020Deaths', 'Population',
                          'Poverty', 'PerCapitaIncome']
#print(allcounties_df)


# Part D4 - Analysis

#print(allcounties_df['TotalCases'].corr(allcounties_df['Poverty']))
#print(allcounties_df['TotalDeaths'].corr(allcounties_df['Poverty']))
#print(allcounties_df['TotalCases'].corr(allcounties_df['PerCapitaIncome']))
#print(allcounties_df['TotalDeaths'].corr(allcounties_df['PerCapitaIncome']))
#print(allcounties_df['Dec2020Cases'].corr(allcounties_df['Poverty']))
#print(allcounties_df['Dec2020Deaths'].corr(allcounties_df['Poverty']))
#print(allcounties_df['Dec2020Cases'].corr(allcounties_df['PerCapitaIncome']))
#print(allcounties_df['Dec2020Deaths'].corr(allcounties_df['PerCapitaIncome']))