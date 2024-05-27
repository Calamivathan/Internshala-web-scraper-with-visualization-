import pandas as pd
from collections import Counter

# Load the data from Excel
file_path = r"F:\major project\internship_data_analysis.xlsx"
df = pd.read_excel(file_path)  # Update with your file name

# Fill missing values in the 'Location' column with an empty string
df['Location'] = df['Location'].fillna('')

# Group by profile and collect all locations
grouped_df = df.groupby('Profile')['Location'].apply(lambda x: ','.join(map(str, x)))

# Create a dictionary to store the frequency of locations for each profile
profile_locations_counter = {}

# Iterate over each profile
for profile, locations in grouped_df.items():
    locations_counter = Counter()
    # Split locations and filter out "Work from home"
    locations_list = [location.strip() for location in locations.split(',') if location.strip() != 'Work from home']
    locations_counter.update(locations_list)
    profile_locations_counter[profile] = locations_counter

# Create a new column for fixed location in the dataframe
df['Location_fixed'] = ""

# Iterate over each profile and update the location column
for index, row in df.iterrows():
    profile = row['Profile']
    if profile in profile_locations_counter:
        top_locations = profile_locations_counter[profile].most_common(2)
        if top_locations:
            if len(top_locations) > 1:
                if top_locations[0][0] == 'Work from home':
                    df.at[index, 'Location_fixed'] = top_locations[1][0] if top_locations[1][0] != 'Work from home' else 'Work from home only'
                else:
                    df.at[index, 'Location_fixed'] = top_locations[0][0]
            else:
                df.at[index, 'Location_fixed'] = top_locations[0][0]
        else:
            df.at[index, 'Location_fixed'] = 'Work from home'

# Save the updated dataframe to the same Excel file
df.to_excel(file_path, index=False)
