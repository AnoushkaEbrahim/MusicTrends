import pandas as pd

# Loading the tracks.csv dataset
tracks_df = pd.read_csv('/datasets/tracks.csv')

# Display the first few rows of the dataset
#print(tracks_df.head())
# Get information about the dataset (columns, data types, missing values)
#print(tracks_df.info())
#print(tracks_df.dtypes())

#DATA-CLEANING- tracks.csv-----------------------------------------------------------------------------------------------------------------------
    #MISSING VALUES(name column has 71 missing values)
tracks_df = tracks_df.dropna(subset=['name'])  # Drop rows where 'name' is missing
tracks_df = tracks_df.dropna()  # Drop rows where any column has missing values
missing_values_after = tracks_df.isnull().sum() # Recalculate missing values
#print(missing_values_after)
    #DUPLICATE VALUES
tracks_df = tracks_df.drop_duplicates() #0 duplicate values
duplicates = tracks_df.duplicated() #recalculate missing values
#print(duplicates.sum())
    #FORMATTING AND CONSISTENCY
tracks_df.columns = tracks_df.columns.str.title().str.replace(" ", "_").str.strip() #making lowercase and same format
tracks_df['Artists'] = tracks_df['Artists'].str.lower().str.strip().replace("[","").replace("]","") #formatting data in artists column
#print(tracks_df['Artists'].head())
tracks_df['Name'] = tracks_df['Name'].str.lower().str.strip()
    #Formatting DATEANDTIME
tracks_df['Release_Date'] = tracks_df['Release_Date'].astype(str).str.strip()
def standardize_date(x): 
    if len(x) == 4:
        return f"01-01-{x}"  # If it's just a year, return it as the first day of January of that year
    else:
        return x
tracks_df['Release_Date'] = tracks_df['Release_Date'].apply(standardize_date)
tracks_df['Release_Date'] = pd.to_datetime(tracks_df['Release_Date'], errors='coerce')
#print(tracks_df['Release_Date'].head())
    #checking for OUTLIERS
#using unique method to see if values are within expected range
columns_to_check = ['Danceability', 'Energy', 'Loudness', 'Speechiness', 
                    'Acousticness', 'Instrumentalness', 'Liveness', 'Valence', 'Tempo','Time_Signature','Popularity','Mode','Key']
#for col in columns_to_check:   
    #print(f"Unique values in '{col}':")
    #print(tracks_df[col].unique())
    #print()
tracks_df.to_csv('datasets/cleaned_tracks.csv', index=False)
#print("Cleaned dataset saved as 'cleaned_tracks.csv'")
