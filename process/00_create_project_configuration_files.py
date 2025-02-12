import os.path
import shutil

source_folder = f'./configuration/templates'
dest_folder = f'./configuration'

print("Creating project configuration files, if not already existing in the configuration folder...")
try:
    for folder, subfolders, files in os.walk(source_folder):
        for file in files:
            path_file=os.path.join(folder, file)
            if os.path.exists(f'{dest_folder}/{file}'):
                print(f'\t- {file} exists.')
            else:
                shutil.copy2(path_file, dest_folder)
                print(f'\t- created {file}')
    
    print('''
All required configuration files are present in the configuration folder, and may be customised as required:

config.yml:
    Configuration of overall project
    
regions.yml
    Configuration of regions of interest
    
indicators.yml
    Configuration of indicators
    
osm_destination_definitions.csv
    Configuration of key-value pairs used to identify features of interest using OpenStreetMap data
    
osm_open_space.yml
    Configuration of queries used to derive a dataset of areas of open space using OpenStreetMap data
    
resources.json
    A file which may be used to log details of users processing environments (not currently implemented in code, but may be manually edited by users for their records).
    
''')
except:
    raise
