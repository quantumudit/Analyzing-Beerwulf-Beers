# -- Importing Libraries -- #

print('\n')
print('Importing libraries to perform ETL...')

import pandas as pd
import pyfiglet

print('Initiating ETL Process...')
print('\n')

# -- Starting ETL Process --#

etl_title = "BEERWULF BEERS DATA ETL"
ascii_art_title = pyfiglet.figlet_format(etl_title, font='small')
print(ascii_art_title)
print('\n')

# -- Connecting to Dataset -- #

print('Connecting to raw dataset')

scraped_data = pd.read_csv("../01_WEBSCRAPING/beerwulf_beers_scraped_data.csv", index_col=False)

print(f'Shape of scraped dataset: {scraped_data.shape}')
print('\n')

# -- Removing Unnecessary Columns --#

print('Removing unnecessary columns')

keep_columns = ['title','style','container_type','in_stock_status','beer_image_url','beer_details_url','alcohol_percentage','volume_centiliter','price_pounds']
beerwulf_data = scraped_data[keep_columns]

print(f'Shape of dataframe after removal of unnecessary columns: {beerwulf_data.shape}')
print('\n')

# -- Renaming Existing Columns --#

print('Renaming existing columns')

new_column_names = ['Title','Style','Container Type', 'InStock Status', 'Image Link', 'Details Link','Alcohol %','Volume (cl)','Price (£)']
beerwulf_data.columns = new_column_names

print(f'New column names in the dataframe: {list(beerwulf_data.columns)}')
print('\n')

# -- Adding Custom Index Column -- #

print('Adding custom index column to the dataframe')

custom_index_col = pd.RangeIndex(start=1000, stop=1000+len(beerwulf_data), step=1, name='BeerID')

beerwulf_data.index = custom_index_col
beerwulf_data.index = 'B' + beerwulf_data.index.astype('string')

print(f'Is the index column unique: {beerwulf_data.index.is_unique}')
print(f'Snippet of the transformed dataframe:')
print('\n')
print(beerwulf_data.head())
print('\n')

# -- Exporting Data to CSV File --#

print('Exporting the dataframe to CSV file...')

beerwulf_data.to_csv('../03_DATA/beerwulf_beers_data.csv', encoding='utf-8', index_label='BeerID')

print('Data exported to CSV...')
print('ETL Process completed !!!')