import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('data.csv')

# Filter the data based on the given conditions
filtered_data = data[(data['LocationAbbr'] == 'US') & 
                     (data['Age'].isin(['40-64 years', '65-84 years', '85 years and older'])) & 
                     (data['Gender'].isin(['Female', 'Male'])) &
                     (data['RiskFactor'] == 'All participants')]

# Show unique values for 'RaceEthnicity'
unique_race_ethnicity = filtered_data['RaceEthnicity'].unique()
for i, value in enumerate(unique_race_ethnicity):
    print(f"{i}: {value}")

# Ask the user to select a 'RaceEthnicity' value by number
selected_number = int(input("Select a 'RaceEthnicity' value by number: "))
selected_race_ethnicity = unique_race_ethnicity[selected_number]

# Filter the data based on the selected 'RaceEthnicity'
filtered_data = filtered_data[filtered_data['RaceEthnicity'] == selected_race_ethnicity]

# Sort data by 'YearStart'
filtered_data = filtered_data.sort_values(by='YearStart')

# Plot the data
plt.figure(figsize=(12, 6))

linestyles = ['-', '--', '-.', ':']
widths = [1, 2]

# Create a list of unique combinations of linestyles and widths
line_styles = [(ls, w) for ls in linestyles for w in widths]

for i, (age, gender) in enumerate(filtered_data.groupby(['Age', 'Gender'])):
    age_group, gender_group = age
    linestyle, width = line_styles[i % len(line_styles)]
    plt.plot(gender['YearStart'], gender['Data_Value'], label=f'{age_group} - {gender_group}', linestyle=linestyle, linewidth=width, color='black')

# Rotate xticks and set tight layout
plt.xticks(rotation=90)

# Place the legend outside the plot
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

# Set the title and Y-axis label
plt.title(f'Data for {selected_race_ethnicity}')
plt.ylabel('Percent')

# Save the figure as a PNG file
plt.tight_layout()
plt.savefig(f'{selected_race_ethnicity}.png')

# Show the plot
plt.show()

