# import pymysql
# import matplotlib.pyplot as plt
# import seaborn as sns
# import pandas as pd
# import numpy as np
#
#
#
# # Connect to MySQL Server
# connection = pymysql.connect(
#     host="127.0.0.1",
#     user="root",
#     password="1234",
#     database="test"
# )
# cursor = connection.cursor()
#
# # Spatial Analysis: Where are the geographical hotspots for reported crimes?
# cursor.execute("SELECT LAT,LON FROM crime_data;")
# crime_locations = cursor.fetchall()
# crime_df = pd.DataFrame(crime_locations, columns=['Latitude', 'Longitude'])
#
# plt.figure(figsize=(10, 8))
# sns.scatterplot(data=crime_df, x='Longitude', y='Latitude', alpha=0.5)
# plt.title("Geographical Hotspots for Reported Crimes")
# plt.show()
#
# # Victim Demographics: What is the distribution of victim ages in reported crimes?
# cursor.execute("SELECT Vict_Age FROM crime_data WHERE Vict_Age IS NOT NULL;")
# victim_ages = cursor.fetchall()
# victim_ages_df = pd.DataFrame(victim_ages, columns=['VictimAge'])
#
# plt.figure(figsize=(10, 6))
# sns.histplot(data=victim_ages_df, x='VictimAge', kde=True, bins=30)
# plt.title("Distribution of Victim Ages in Reported Crimes")
# plt.xlabel("Victim Age")
# plt.ylabel("Frequency")
# plt.show()
#
# # Is there a significant difference in crime rates between male and female victims?
# cursor.execute("SELECT COUNT(*) FROM crime_data WHERE Vict_Sex='M' OR Vict_Sex='F';")
# total_male_female_victims = cursor.fetchone()[0]
#
# cursor.execute("SELECT COUNT(*) FROM crime_data WHERE Vict_Sex='M';")
# total_male_victims = cursor.fetchone()[0]
#
# cursor.execute("SELECT COUNT(*) FROM crime_data WHERE Vict_Sex='F';")
# total_female_victims = cursor.fetchone()[0]
#
# plt.figure(figsize=(6, 6))
# plt.pie([total_male_victims, total_female_victims], labels=['Male', 'Female'], autopct='%1.1f%%', startangle=90)
# plt.title("Distribution of Male and Female Victims")
# plt.show()
#
# # Location Analysis: Where do most crimes occur based on the "Location" column?
# cursor.execute("SELECT Location, COUNT(*) as CrimeCount FROM crime_data GROUP BY Location ORDER BY CrimeCount DESC LIMIT 10;")
# location_data = cursor.fetchall()
# location_df = pd.DataFrame(location_data, columns=['Location', 'CrimeCount'])
#
# plt.figure(figsize=(12, 6))
# sns.barplot(data=location_df, x='CrimeCount', y='Location', palette='viridis')
# plt.title("Top 10 Locations with the Most Crimes")
# plt.xlabel("Number of Crimes")
# plt.ylabel("Location")
# plt.show()
#
# # Crime Code Analysis: What is the distribution of reported crimes based on Crime Code?
# cursor.execute("SELECT Crm_Cd, COUNT(*) as CrimeCount FROM crime_data GROUP BY Crm_Cd ORDER BY CrimeCount DESC LIMIT 10;")
# crime_code_data = cursor.fetchall()
# crime_code_df = pd.DataFrame(crime_code_data, columns=['CrimeCode', 'CrimeCount'])
#
# plt.figure(figsize=(12, 6))
# sns.barplot(data=crime_code_df, x='CrimeCount', y='CrimeCode', palette='mako')
# # sns.barplot(data=crime_code_df, x='CrimeCount', y='CrimeCode', palette='mako')
# plt.title("Top 10 Crime Codes with the Most Reported Crimes")
# plt.xlabel("Number of Crimes")
# plt.ylabel("Crime Code")
# plt.show()
#
# # Close the MySQL connection
# connection.close()


import pymysql
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Connect to MySQL Server
connection = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="1234",
    database="test"
)
cursor = connection.cursor()

# Spatial Analysis: Where are the geographical hotspots for reported crimes?
cursor.execute("SELECT LAT, LON FROM crime_data;")
crime_locations = cursor.fetchall()
crime_df = pd.DataFrame(crime_locations, columns=['Latitude', 'Longitude'])
print(crime_df)

plt.figure(figsize=(10, 8))
sns.scatterplot(data=crime_df, x='Longitude', y='Latitude', alpha=0.5)
plt.title("Geographical Hotspots for Reported Crimes")
plt.show()

# Victim Demographics: What is the distribution of victim ages in reported crimes?
cursor.execute("SELECT Vict_Age FROM crime_data WHERE Vict_Age IS NOT NULL;")
victim_ages = cursor.fetchall()
victim_ages_df = pd.DataFrame(victim_ages, columns=['VictimAge'])

plt.figure(figsize=(10, 6))
sns.histplot(data=victim_ages_df, x='VictimAge', bins=30)
plt.title("Distribution of Victim Ages in Reported Crimes")
plt.xlabel("Victim Age")
plt.ylabel("Frequency")
plt.show()

# Is there a significant difference in crime rates between male and female victims?
cursor.execute("SELECT COUNT(*) FROM crime_data WHERE Vict_Sex='M' OR Vict_Sex='F';")
total_male_female_victims = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM crime_data WHERE Vict_Sex='M';")
total_male_victims = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM crime_data WHERE Vict_Sex='F';")
total_female_victims = cursor.fetchone()[0]

plt.figure(figsize=(6, 6))
plt.pie([total_male_victims, total_female_victims], labels=['Male', 'Female'], autopct='%1.1f%%', startangle=90)
plt.title("Distribution of Male and Female Victims")
plt.show()

# Location Analysis: Where do most crimes occur based on the "Location" column?
cursor.execute("SELECT Location, COUNT(*) as CrimeCount FROM crime_data GROUP BY Location ORDER BY CrimeCount DESC LIMIT 10;")
location_data = cursor.fetchall()
location_df = pd.DataFrame(location_data, columns=['Location', 'CrimeCount'])

plt.figure(figsize=(12, 6))
sns.barplot(data=location_df, x='CrimeCount', y='Location', palette='viridis', hue='Location', dodge=False)
plt.title("Top 10 Locations with the Most Crimes")
plt.xlabel("Number of Crimes")
plt.ylabel("Location")
plt.show()

# Crime Code Analysis: What is the distribution of reported crimes based on Crime Code?
cursor.execute("SELECT Crm_Cd, COUNT(*) as CrimeCount FROM crime_data GROUP BY Crm_Cd ORDER BY CrimeCount DESC LIMIT 10;")
crime_code_data = cursor.fetchall()
crime_code_df = pd.DataFrame(crime_code_data, columns=['CrimeCode', 'CrimeCount'])

plt.figure(figsize=(12, 6))
sns.barplot(data=crime_code_df, x='CrimeCount', y='CrimeCode', palette='mako', hue='CrimeCode', dodge=False)
plt.title("Top 10 Crime Codes with the Most Reported Crimes")
plt.xlabel("Number of Crimes")
plt.ylabel("Crime Code")
plt.show()

# Close the MySQL connection
connection.close()

