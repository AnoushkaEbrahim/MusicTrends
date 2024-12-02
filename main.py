import pandas as pd

# Loading the tracks.csv dataset
tracks_df = pd.read_csv(r'C:\GitHub\vsProject\MusicTrends\datasets\tracks.csv')

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
def preprocess_release_date(date):
    # Check if the value is a year (e.g., '1955')
    if isinstance(date, str) and date.isdigit() and len(date) == 4:
        return f"{date}-01-01"
    # Check if the value is in the format 'YYYY-MM'
    elif isinstance(date, str) and len(date) == 7 and date.count('-') == 1:
        return f"{date}-01"
    return date  # Return as is for full dates or other valid formats

# Apply preprocessing to the 'release_date' column
tracks_df['Release_Date'] = tracks_df['Release_Date'].apply(preprocess_release_date)

# Convert the column to datetime format
tracks_df['Release_Date'] = pd.to_datetime(tracks_df['Release_Date'], errors='coerce')

# Check for remaining invalid dates
invalid_dates = tracks_df[tracks_df['Release_Date'].isna()]

# Display results
#print("Conversion complete.")
#print(f"Remaining invalid dates (if any): {len(invalid_dates)}")
#if not invalid_dates.empty:
    #print(invalid_dates)

# Check the data type of the 'release_date' column
#release_date_dtype = tracks_df['Release_Date'].dtype
#print(f"The data type of 'release_date' is: {release_date_dtype}")

# Check for missing data
#missing_data = tracks_df.isnull().sum()
#print(missing_data)

    #checking for OUTLIERS
#using unique method to see if values are within expected range
columns_to_check = ['Danceability', 'Energy', 'Loudness', 'Speechiness', 
                    'Acousticness', 'Instrumentalness', 'Liveness', 'Valence', 'Tempo','Time_Signature','Popularity','Mode','Key']
#for col in columns_to_check:   
    #print(f"Unique values in '{col}':")
    #print(tracks_df[col].unique())
    #print()

#creating new column 'Decade'
tracks_df['Decade'] = (tracks_df['Release_Date'].dt.year // 10) * 10

#creating new column 'Duration_Min' (milli second to minute)
tracks_df['Duration_Min'] = tracks_df['Duration_Ms'] / 60000 
#print(tracks_df.dtypes)

#drop columns 'Release_Date' and 'Duration_Ms' since we have 'Decade' and 'Duration_Min' column
tracks_df.drop(columns=['Release_Date', 'Duration_Ms'], inplace=True)
#print(tracks_df.dtypes)

#drop columns which are irrelevant for the analysis 'Artist'
tracks_df.drop(columns=['Artists'], inplace=True)
#print(tracks_df.dtypes)

# Check for missing data
missing_data = tracks_df.isnull().sum()
print(missing_data)


tracks_df.to_csv(r'C:\GitHub\vsProject\MusicTrends\datasets\cleaned_tracks.csv', index=False)
print("Cleaned dataset saved as 'cleaned_tracks.csv'")


