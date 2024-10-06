import pandas as pd
import datetime


def get_prefix(sample_id):
  return sample_id[:2]

dataCSV = pd.read_csv("no_tolerance.csv", delimiter=',')
usda_pdp = pd.read_csv("USDA_PDP_AnalyticalResults.csv", delimiter=',')
dataCSV['Prefix'] = dataCSV['Sample ID'].apply(get_prefix)
pesticide_counts = dataCSV.groupby(['Prefix', 'Pesticide Name'])['Pesticide Name'].count().reset_index(name='Frequency')
pesticide_counts = pesticide_counts.sort_values(by=['Frequency'], ascending = False)
#print(pesticide_counts)
pesticide_prefix_counts = dataCSV.groupby('Pesticide Name')['Prefix'].nunique()
top_3_pesticides = pesticide_prefix_counts.nlargest(5)
print(top_3_pesticides) #top 5 countrywide

fl_data = dataCSV[dataCSV['Sample ID'].str.startswith('FL')]
pesticide_counts = fl_data.groupby('Pesticide Name')['Sample ID'].count()
top_3_pesticides = pesticide_counts.nlargest(3)
print(top_3_pesticides) #top 3- Florida

def fix_year(year_str):
    year = int(year_str)
    if 24 <= year <= 99:
        return 1900 + year
    else:
        return 2000 + year

for index, row in usda_pdp.iterrows():
    sample_id = row['Sample ID']
    year_str = sample_id[2:4]  # Extract year string
    year = fix_year(year_str)  # Call fix_year to get corrected year
    pesticide_name = row['Pesticide Name']



filtered_data = dataCSV[dataCSV['Pesticide Name'].str.startswith('Metolachlor')] 
filtered_data.sort_values(by=['Concentration'])
print(filtered_data.head(20))

usda_pdp['State'] = usda_pdp['Sample ID'].str[:2]  # Extract first 2 characters for state
usda_pdp['Year'] = usda_pdp['Sample ID'].str[2:4].apply(fix_year)

Thiabendazole_data = usda_pdp[usda_pdp['Pesticide Name'] == 'Thiabendazole'] 
print(Thiabendazole_data) 
Thiabendazole_data[['State', 'Year', 'Concentration']].to_csv('Thiabendazole_data.csv', index=False) 
from google.colab import files

files.download('Thiabendazole_data.csv')

Azoxystrobin_data = usda_pdp[usda_pdp['Pesticide Name'] == 'Azoxystrobin']
fl_Azoxystrobin_data = Azoxystrobin_data[Azoxystrobin_data['Sample ID'].str.startswith('FL')]
print(fl_Azoxystrobin_data)
fl_Azoxystrobin_data[['State', 'Year', 'Concentration']].to_csv('Azoxystrobin_data.csv', index=False)
from google.colab import files
files.download('Azoxystrobin_data.csv')

