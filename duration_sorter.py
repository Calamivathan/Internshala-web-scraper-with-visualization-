import pandas as pd
from collections import Counter

# Load the data from Excel
file_path = r"F:\major project\internship_data_analysis.xlsx"
df = pd.read_excel(file_path)  # Update with your file name

# Fill missing values in the 'Skills Required' column with an empty string
df['Duration'] = df['Duration'].fillna('')

# Group by profile and collect all skills
grouped_df = df.groupby('Profile')['Duration'].apply(lambda x: ','.join(map(str, x)))

# Create a dictionary to store the frequency of skills for each profile
profile_skills_counter = {}

# Iterate over each profile
for profile, skills in grouped_df.items():
    skills_counter = Counter()
    skills_list = skills.split(',')
    skills_counter.update(skills_list)
    profile_skills_counter[profile] = skills_counter

# Create a new column for top skills in the dataframe
df['duration_fixed'] = ""

# Iterate over each profile and update the top skills column
for index, row in df.iterrows():
    profile = row['Profile']
    if profile in profile_skills_counter:
        top_skills = profile_skills_counter[profile].most_common(1)
        top_skills_str = ', '.join([skill for skill, frequency in top_skills])
        df.at[index, 'duration_fixed'] = top_skills_str

# Save the updated dataframe to the same Excel file
df.to_excel(file_path, index=False)
