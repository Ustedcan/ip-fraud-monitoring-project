import pandas as pd
import folium
import geoip2.database

# Process excel file
def process_excel(path: str) -> pd.DataFrame:
    try:
        df = pd.read_excel(path, header=0)

        if df.empty:
            print(f"The file is empty. Check if you paste the IPs information correctly!")
            return
        
        ip_df = df.value_counts(['IP', 'Status']).reset_index(name='count')
        #ip_column = df.iloc[:, 0]
        return ip_df
    
    except FileNotFoundError:
        print(f"Error: The File was not found. Please check if file exists.")

# Create the map
def create_map():
    map = folium.Map(location=[20, 20], zoom_start=2)
    return map

# To read de IPs database
def database_reader(path: str):
    reader = geoip2.database.Reader(path)
    return reader
