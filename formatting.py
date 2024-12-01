import pandas as pd

# Loading the tracks.csv dataset
tracks_df = pd.read_csv(r'C:\GitHub\vsProject\MusicTrends\datasets\tracks.csv')
# Check for blank spaces in the 'release_date' column
blank_space_count = tracks_df['release_date'].apply(lambda x: x.strip() == '' if isinstance(x, str) else False).sum()

# Check for null values in the 'release_date' column
null_count = tracks_df['release_date'].isnull().sum()

# Print the results
print(f"Blank spaces in 'release_date': {blank_space_count}")
print(f"Null values in 'release_date': {null_count}")


def preprocess_release_date(date):
    # Check if the value is a year (e.g., '1955')
    if isinstance(date, str) and date.isdigit() and len(date) == 4:
        return f"{date}-01-01"
    # Check if the value is in the format 'YYYY-MM'
    elif isinstance(date, str) and len(date) == 7 and date.count('-') == 1:
        return f"{date}-01"
    return date  # Return as is for full dates or other valid formats

# Apply preprocessing to the 'release_date' column
tracks_df['release_date'] = tracks_df['release_date'].apply(preprocess_release_date)

# Convert the column to datetime format
tracks_df['release_date'] = pd.to_datetime(tracks_df['release_date'], errors='coerce')

# Check for remaining invalid dates
invalid_dates = tracks_df[tracks_df['release_date'].isna()]

# Display results
print("Conversion complete.")
print(f"Remaining invalid dates (if any): {len(invalid_dates)}")
if not invalid_dates.empty:
    print(invalid_dates)

# Check the data type of the 'release_date' column
release_date_dtype = tracks_df['release_date'].dtype
print(f"The data type of 'release_date' is: {release_date_dtype}")

# Check for missing data
missing_data = tracks_df.isnull().sum()
print(missing_data)

# Display the first few rows of the dataset
#print(tracks_df.head())
# Get information about the dataset (columns, data types, missing values)
#print(tracks_df.info())
#print(tracks_df.dtypes())

#DATA-CLEANING- tracks.csv-----------------------------------------------------------------------------------------------------------------------
    #MISSING VALUES(name column has 71 missing values)
#tracks_df = tracks_df.dropna(subset=['name'])  # Drop rows where 'name' is missing
#tracks_df = tracks_df.dropna()  # Drop rows where any column has missing values
#missing_values_after = tracks_df.isnull().sum() # Recalculate missing values
#print(missing_values_after)
    #DUPLICATE VALUES
#tracks_df = tracks_df.drop_duplicates() #0 duplicate values
#duplicates = tracks_df.duplicated() #recalculate missing values
#print(duplicates.sum())
    #FORMATTING AND CONSISTENCY
#tracks_df.columns = tracks_df.columns.str.title().str.replace(" ", "_").str.strip() #making lowercase and same format
#tracks_df['Artists'] = tracks_df['Artists'].str.lower().str.strip().replace("[","").replace("]","") #formatting data in artists column
#print(tracks_df['Artists'].head())
#tracks_df['Name'] = tracks_df['Name'].str.lower().str.strip()
    
# Convert 'release_date' to datetime format, coercing errors
#tracks_df['Release_Date'] = pd.to_datetime(tracks_df['Release_Date'], errors='coerce')
#missing_data = tracks_df[tracks_df['Release_Date'].isnull()]
#print(missing_data)

#missing_data.to_csv('C:\\DocsSahi\\UE\\Final Projects\\DataAnalytics\\tracksfiltered.csv', index=False)
#print("Saved")

# Check for missing data
#missing_data = tracks_df.isnull()
#print(missing_data)
