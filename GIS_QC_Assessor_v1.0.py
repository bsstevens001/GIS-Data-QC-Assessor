#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Imports the pandas library as "pd", numpy as "np", and matplotlib as "plt"
import os
import pandas as pd
import matplotlib.pyplot as plt
from contextlib import redirect_stdout


# In[ ]:


#Reads in a .csv document from a file path. Accepts quotes within file path input
input_file = input("Enter Filepath:").replace('"', '')
pipes_df = pd.read_csv(input_file)


# In[ ]:


#Create variables for each row in column that can be read in later in the script
DIAMETER = 'Diameter'
ASSET_ID = 'Asset_ID'
ASSET_TYPE = 'Asset_Type'
LATITUDE = 'Latitude'
LONGITUDE = 'Longitude'
INSTALL_YEAR = 'Install_Year'
STATUS = 'Status'
MATERIAL = 'Material'


# In[ ]:


#Rename all aliases of each column name to a standardized format
pipes_df = pipes_df.rename(columns={'AssetID': ASSET_ID,
                                    'assetID': ASSET_ID,
                                    'assetid': ASSET_ID,
                                    'ASSETID': ASSET_ID,
                                    'asset_id': ASSET_ID,
                                    'ASSET_ID': ASSET_ID,
                                    'AssetType': ASSET_TYPE,
                                    'assettype': ASSET_TYPE,
                                    'Asset Type': ASSET_TYPE,
                                    'asset type': ASSET_TYPE,
                                    'ASSET_TYPE': ASSET_TYPE,
                                    'ASSET TYPE': ASSET_TYPE,
                                    'latitude': LATITUDE,
                                    'lat': LATITUDE,
                                    'longitude': LONGITUDE,
                                    'long': LONGITUDE,
                                    'lon': LONGITUDE,
                                    'InstallYear': INSTALL_YEAR,
                                    'installyear': INSTALL_YEAR,
                                    'Install Year': INSTALL_YEAR,
                                    'Install_Year': INSTALL_YEAR,
                                    'install_year': INSTALL_YEAR,
                                    'INSTALL_YEAR': INSTALL_YEAR,
                                    'INSTALL YEAR': INSTALL_YEAR,
                                    'Year Installed': INSTALL_YEAR,
                                    'yearinstalled': INSTALL_YEAR,
                                    'ConstructionYear': INSTALL_YEAR,
                                    'diameter': DIAMETER,
                                    'DIAMETER': DIAMETER,
                                    'pipe_size': DIAMETER,
                                    'PIPE_SIZE': DIAMETER,
                                    'PIPE SIZE': DIAMETER,
                                    'pipesize': DIAMETER,
                                    'PIPESIZE': DIAMETER,
                                    'Pipe Size': DIAMETER,
                                    'status': STATUS,
                                    'STATUS': STATUS,
                                    'Pipe Status': STATUS,
                                    'pipe status': STATUS,
                                    'PIPE_STATUS': STATUS,
                                    'pipe_status': STATUS,
                                    'pipestatus': STATUS,
                                    'PIPESTATUS': STATUS,
                                    'material': MATERIAL,
                                    'MATERIAL': MATERIAL
                                   })


# In[ ]:


if DIAMETER in pipes_df.columns:
    print("The tool has detected a diameter column in the dataset. Proceed by entering threshold of min and max pipe diameters")
    min_diameter_input = float(input("Enter Minimum Pipe Diameter(ex./ 0.25in):"))
    max_diameter_input = float(input("Enter Maximum Pipe Diameter(ex./ 8in):"))


# In[ ]:


#Displays data frame (for reference)
pipes_df.head()


# In[ ]:


#Used for visualization further into the code, two variables are created that append values and strings based on if the condition is true or not. Then zipped into a dictionary and visualized on a chart
#Nulls and duplicates assumed to be true by default as they do not take any input column
runnable_count_names = ["Nulls", "Duplicates"]
runnable_counts = []
skipped_checks = []


# In[ ]:


#Function that checks for null cells in table
def total_null(df):
    total_nans = df.isna().sum().to_string() #finds all occurences of null(empty) values and conducts sum of all nulls, converts to string to remove "dtype int64"
    total_nans_sum = df.isna().sum().sum()
    return total_nans, total_nans_sum


# In[ ]:


#Function that checks for duplicate rows in table
def total_duplicates(df):
    total_duplicates = df.duplicated().sum().sum() #finds all duplicate records and conducts sum of all duplicates
    return total_duplicates 


# In[ ]:


#Function that checks for coordinates out of lat and long range if "Latitude" and "Longitude" columns exist
def invalid_coordinates(df):
    invalid_coords = df[
        (df[LATITUDE] > 90) | 
        (df[LATITUDE] < -90) | 
        (df[LONGITUDE] > 180) | 
        (df[LONGITUDE] < -180) | 
        (df[LATITUDE] == 0) | 
        (df[LONGITUDE] == 0)]
    invalid_coords = len(invalid_coords)
    return invalid_coords


# In[ ]:


#Function that checks if any install years are ahead of the current year if the "Install_Year" column exists
def check_year(df):
    invalid_year = df[df[INSTALL_YEAR] > pd.Timestamp.now().year]
    invalid_asset = invalid_year[ASSET_ID]
    invalid_year = len(invalid_year)
    return invalid_year


# In[ ]:


#Function that checks if any pipe diameters are beyond standards if the DIAMETER column exists
def check_diameter(df):
    diameter_rows = df[(df[DIAMETER] > max_diameter_input) | (df[DIAMETER] < min_diameter_input)]
    diameter_rows = len(diameter_rows)
    return diameter_rows


# In[ ]:


#Function that conducts domain validation for pipe status if the "Status" column exists
def check_status(df):
    valid_status = df[df[STATUS] == "Active"]
    valid_status = len(valid_status)
    invalid_status = df[(df[STATUS] != "Active") & (df[STATUS] != "Inactive")] #Invalid status includes broken or unknown statuses
    invalid_status = len(invalid_status)
    inactive = df[df[STATUS] == "Inactive"]
    inactive = len(inactive)
    return valid_status, invalid_status, inactive


# In[ ]:


#Execute null check function and turn them into a list based on their asset_id. Append to runnable counts as the function ran
null_count = total_null(pipes_df)
null_id = pipes_df[pipes_df.isna().any(axis=1).tolist()]
null_id = null_id[ASSET_ID]
runnable_counts.append(null_count[1])


# In[ ]:


duplicate_count = total_duplicates(pipes_df)
duplicate_asset = pipes_df[pipes_df.duplicated().tolist()]
duplicate_asset = duplicate_asset[ASSET_ID]
runnable_counts.append(duplicate_count)


# In[ ]:


#Execute invalid coordinates function then list them based on their asset_id and append the check name and count only if Latitude and Longitude exist in the data frame
if LATITUDE in pipes_df.columns and LONGITUDE in pipes_df.columns:
    coord_count = invalid_coordinates(pipes_df)
    coord_asset = pipes_df[(pipes_df[LATITUDE] > 90) | 
    (pipes_df[LATITUDE] < -90) | 
    (pipes_df[LONGITUDE] > 180) | 
    (pipes_df[LONGITUDE] < -180) | 
    (pipes_df[LATITUDE] == 0) | 
    (pipes_df[LONGITUDE] == 0)]
    coord_asset = coord_asset[ASSET_ID]
    runnable_count_names.append("Coordinates")
    runnable_counts.append(coord_count)
else:
    skipped_checks.append("Coordinates")
    pass


# In[ ]:


if INSTALL_YEAR in pipes_df.columns:
    year_count = check_year(pipes_df)
    invalid_asset = pipes_df[pipes_df[INSTALL_YEAR] > pd.Timestamp.now().year]
    invalid_asset = invalid_asset[ASSET_ID]
    runnable_count_names.append("Installation Years")
    runnable_counts.append(year_count)
else:
    skipped_checks.append("Installation Years")
    pass


# In[ ]:


if DIAMETER in pipes_df.columns:
    diameter_count = check_diameter(pipes_df)
    diameter_asset = pipes_df[(pipes_df[DIAMETER] > max_diameter_input) | (pipes_df[DIAMETER] < min_diameter_input)]
    diameter_asset = diameter_asset[ASSET_ID]
    runnable_count_names.append("Pipe Diameters")
    runnable_counts.append(diameter_count)
else:
    skipped_checks.append("Pipe Diameters")
    pass


# In[ ]:


if STATUS in pipes_df.columns:
    status_count = check_status(pipes_df)
    invalid_stat_id = pipes_df[(pipes_df[STATUS] != "Active") & (pipes_df[STATUS] != "Inactive")]
    invalid_stat_id = invalid_stat_id[ASSET_ID]
    runnable_count_names.append("Service Status")
    runnable_counts.append(len(invalid_stat_id))
else:
    skipped_checks.append("Service Status")
    pass


# In[ ]:


#Creates dictionary "scoring_system" that stores a weighted scoring system for errors based on their severity
#ex./ an invalid location contributes more to the overall score than duplicates causing more invalid locations to reduce the score more
scoring_system = { "Missing Attribute": 25,
                  "Duplicates": 10,
                  "Out of Range": 25,
                  "Invalid Location": 30,
                  "Invalid Status": 10
                 }

#gets the values of each score criteria within the "scoring_system" dictionary
range_value = scoring_system.get("Out of Range")
attribute_value = scoring_system.get("Missing Attribute")
location_value = scoring_system.get("Invalid Location")
duplicates_value = scoring_system.get("Duplicates")
status_value = scoring_system.get("Invalid Status")

#1: Uses a percent error calculation that gets the count of an error, divides it by the length of the table to get percent error, then subtracts it by 1 to get the percent success
#2: Once percent success is calculated, it then multiplies that value by the value of a specific scoring criteria ex./Out of Range to get the decimal (score) that the errors contribute based on the criteria
runnable_scores = [] #an empty list to store all scores that were ran, skip ones that werent
runnable_score_names = [] #an empty list to store all score names that were ran, skip ones that werent
runnable_total_values = [] #an empty list to store all max score values that were ran based on scoring system weight, skip ones that werent
#Missing attribute and duplicates already assumed to be true in table since they do not refer to a column name so both run by default
missing_attributes_score = scoring_system["Missing Attribute"] * (1 - (null_count[1] / (len(pipes_df) * len(pipes_df.columns))))
runnable_scores.append(missing_attributes_score)
runnable_score_names.append("Missing Attribute")
runnable_total_values.append(attribute_value)
duplicates_score = scoring_system["Duplicates"] * (1 - (duplicate_count / len(pipes_df)))
runnable_scores.append(duplicates_score)
runnable_score_names.append("Duplicates")
runnable_total_values.append(duplicates_value)
#Checks to see if various column names exist in the table, if they do the score is ran. Same exact reasoning applies to the count functions
if DIAMETER in pipes_df.columns and INSTALL_YEAR in pipes_df.columns:
    out_of_range_score = scoring_system["Out of Range"] * (1 - ((diameter_count + year_count) / len(pipes_df))) #Else if both cases DIAMETER and "Install_Year" are true, calculare both of them combined since they are both out of range errors
    runnable_scores.append(out_of_range_score)
    runnable_score_names.append("Out of Range")
    runnable_total_values.append(range_value)
elif DIAMETER in pipes_df.columns:
    out_of_range_score = scoring_system["Out of Range"] * (1 - (diameter_count / len(pipes_df))) #If DIAMETER is in the data frame, run the scoring calculation
    runnable_scores.append(out_of_range_score)
    runnable_score_names.append("Out of Range")
    runnable_total_values.append(range_value)
elif INSTALL_YEAR in pipes_df.columns:
    out_of_range_score = scoring_system["Out of Range"] * (1 - (year_count / len(pipes_df))) #Else if "Install_Year" is in the data frame, run the scoring calculation
    runnable_scores.append(out_of_range_score)
    runnable_score_names.append("Out of Range")
    runnable_total_values.append(range_value)
if LATITUDE in pipes_df.columns and LONGITUDE in pipes_df.columns:
    invalid_location_score = scoring_system["Invalid Location"] * (1 - (coord_count / len(pipes_df)))
    runnable_scores.append(invalid_location_score)
    runnable_score_names.append("Invalid Location")
    runnable_total_values.append(location_value)
if STATUS in pipes_df.columns:
    status_score = scoring_system["Invalid Status"] * (1- (status_count[2] / len(pipes_df)))
    runnable_scores.append(status_score)
    runnable_score_names.append("Invalid Status")
    runnable_total_values.append(status_value)

#creates sum of all scores that met column conditions and were executed. Sums the executable scores into a total score
#If table skips a check within the scoring system, convert its score back to a normalized range
if sum(runnable_total_values) != 100:
    total_score = round(((sum(runnable_scores)) / sum(runnable_total_values) * 100), 1)
else:
    total_score = sum(runnable_scores)


# In[ ]:


#creates dictionary of values and keys(strings) for both the runnable counts and runnable scores to be used for visualization in score and count chart
runnable_count_dict = dict(zip(runnable_count_names, runnable_counts))
runnable_score_dict = dict(zip(runnable_score_names, runnable_scores))


# In[ ]:


#outputs the report to the same path of the input dataset
output_folder = os.path.join(os.path.dirname(input_file), "QC_Output")
os.makedirs(output_folder, exist_ok=True)
report_path = os.path.join(output_folder, "QC_Report.txt")
#Outputs all print statements to the report path. Will overwrite after each code execution
with open(report_path, "w", encoding="utf-8") as f:
    with redirect_stdout(f):
        print("Water Utility GIS QC Checker")
        print("==================================")
        #Prints how many null values are contained within each column in dables
        print(f"Null Values by Column: \n{null_count[0]}")
        print(f"Total Count of Null Values: \n{null_count[1]}")
        print("\t Null Values Found in:")
        #For each invalid asset ID in the table, print which asset ID it is
        for null in null_id:
            print(f"\t\t Asset ID {null}")
        print("==================================")
        if DIAMETER in pipes_df.columns:
            print(f"Invalid Pipe Diameters: \n{diameter_count}")
            print("\t Invalid Pipe Diameters Found in:")
            for diameter_id in diameter_asset:
                print(f"\t\t Asset ID {diameter_id}")
        if INSTALL_YEAR in pipes_df.columns:
            print(f"Invalid Installation Years: \n{year_count}")
            print("\t Invalid Installation Year Found in:")
            for invalid_id in invalid_asset:
                print(f"\t\t Asset ID {invalid_id}")
        if LATITUDE in pipes_df.columns and LONGITUDE in pipes_df.columns:
            print(f"Invalid Geographic Coordinates: \n{coord_count}")
            print("\t Invalid Geographic Coordinates Found in:")
            for coord_id in coord_asset:
                print(f"\t\t Asset ID {coord_id}")
        elif LATITUDE not in pipes_df.columns and LONGITUDE not in pipes_df.columns:
            print("ERROR: Latitude and Longitude Field Missing") 
        elif LATITUDE not in pipes_df.columns:
            print("ERROR: Latitude Field Missing")
        elif LONGITUDE not in pipes_df.columns:
            print("ERROR: Longitude Field Missing")
        print(f"Duplicate Records: \n{duplicate_count}")
        print("\t Duplicate Records Found in:")
        for duplicate_id in duplicate_asset:
            print(f"\t\t Asset ID {duplicate_id}")
        if STATUS in pipes_df.columns:
            print("Status Counts:")
            print(f"\t Active Pipes: {status_count[0]}")
            print(f"\t Inactive Pipes: {status_count[2]}")
            print(f"\t Invalid Pipes: {status_count[1]}")
            for invalid in invalid_stat_id:
                print(f"\t\t Asset ID {invalid}")
        print("==================================")
        #Prints score of each criteria out of the value of that criteria
        print(f"Missing Attribute Score: {round(missing_attributes_score, 1)} / {attribute_value}")
        print(f"Duplicates Score: {round(duplicates_score, 1)} / {duplicates_value}")
        if DIAMETER in pipes_df.columns and INSTALL_YEAR in pipes_df.columns:
            print(f"Out of Range Score: {round(out_of_range_score, 1)} / {range_value}")
        elif DIAMETER in pipes_df.columns:
            print(f"Out of Range Score: {round(out_of_range_score, 1)} / {range_value}")
        elif INSTALL_YEAR in pipes_df.columns:
            print(f"Out of Range Score: {round(out_of_range_score, 1)} / {range_value}")
        if LATITUDE in pipes_df.columns and LONGITUDE in pipes_df.columns:
            print(f"Invalid Location Score: {round(invalid_location_score, 1)} / {location_value}")
        if STATUS in pipes_df.columns:
            print(f"Status Score: {round(status_score, 1)} / {status_value}")
        print("==================================")
        print(f"Total Score: {round(total_score, 0)} / 100")

        #Gives a scoring grade based on how high the score is
        if total_score >= 95:
            print("Grade: Excellent Score")
        elif total_score >=85:
            print("Grade: Good Score")
        elif total_score >= 70:
            print("Grade: Fair Score")
        elif total_score >= 50:
            print("Grade: Poor Score")
        else:
            print("Grade: Critical")

        print(f"\n{len(runnable_count_names)} / 6 Checks Executed")
        print("\nChecks Executed:")
        for name in runnable_count_names:
            print(f"\u2705 {name}")
        print("\nChecks Skipped:")
        for skipped in skipped_checks:
            print(f"\u274C {skipped}")
            print(f"\tReason: Column not found")
print("QC Report Successfully Generated")
print(f"Report Saved To: {report_path}")


# In[ ]:


error_chart_path = os.path.join(output_folder, "Error_Counts.png")
fig, ax = plt.subplots(figsize=(8, 8), facecolor='lightgray') #creates a subplot chart, size 8(width), 8(height) and changes background color to light gray
invalid_numbers = runnable_count_dict.values()
invalid_names = runnable_count_dict.keys()
labels = ax.get_xticklabels() #gets the x-axis labels from chart and stores them in "labels" variable
plt.setp(labels, rotation=45, horizontalalignment='right') #arranges the labels to have a 45 degree angle for better visualization
invalid_attributes = ax.bar(invalid_names, invalid_numbers, color='#66BD4D') #creates a bar chart called "invalid_attributes" using "invalid_names" as the x-axis and "invalid_numbers" as the y-axis
#sets the x-axis label and the y-axis label
plt.xlabel('Error Parameters', weight='bold')
plt.ylabel('Error Count', weight='bold')
plt.title('Invalid Attributes Chart', fontsize=15, weight='bold')
#for each bar in the invalid_attributes chart, get its value(height) and put it above the bar
for bar in invalid_attributes:
    height = bar.get_height()
    rounded_height = int(height)
    ax.text(bar.get_x() + bar.get_width() / 2, height, f'{rounded_height}', ha='center', va='bottom', fontstyle='italic')
plt.savefig(error_chart_path, dpi=300, bbox_inches="tight")
print("Error Chart Successfully Generated")
print(f"Chart Saved To: {error_chart_path}")


# In[ ]:


score_chart_path = os.path.join(output_folder, "Score_Chart.png")
fig, ax = plt.subplots(figsize=(8, 8), facecolor='lightgray')
scoring_numbers = runnable_score_dict.values()
scoring_names = runnable_score_dict.keys()
bars_background = ax.bar(scoring_names, runnable_total_values, color='#C1CFDE')
bars = ax.bar(scoring_names, scoring_numbers, color='#003087')
plt.xlabel('Scoring Criteria', weight='bold')
plt.ylabel('Score', weight='bold')
plt.title('Score Chart', fontsize=15, weight='bold')
ax.text(-1, -2, f"Total Score: {round(total_score, 0)} / 100", fontstyle='italic')
for bar, max_score in zip(bars, runnable_total_values):
    height = bar.get_height()
    rounded_height = round(height, 1)
    ax.text(bar.get_x() + bar.get_width() / 2, height, f"{rounded_height} / {max_score}", ha='center', va='bottom', fontstyle='italic')
plt.savefig(score_chart_path, dpi=300, bbox_inches="tight")
print("Score Chart Successfully Generated")
print(f"Chart Saved To: {score_chart_path}")


# In[ ]:




