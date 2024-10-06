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
print(top_3_pesticides)
