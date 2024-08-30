# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
crimes = pd.read_csv("crimes.csv", parse_dates=["Date Rptd", "DATE OCC"], dtype={"TIME OCC": str})
crimes.head()

# Step 1: Extract Hour from Time of Occurrence

crimes["HOUR OCC"] = crimes["TIME OCC"].str[:2].astype(int)
crimes.head()

# Step 2: Determine Peak Crime Hour

sns.countplot(data=crimes, x="HOUR OCC")
plt.show()

peak_crime_hour = 12

# Step 3: Identify Area with Highest Night Crime Frequency

night_time = crimes[crimes["HOUR OCC"].isin([22, 23, 0, 1, 2, 3])]
peak_night_crime_location = night_time.groupby("AREA NAME", 
                                               as_index=False)["HOUR OCC"].count().sort_values("HOUR OCC",
                                                                                               ascending=False).iloc[0]["AREA NAME"]
print(f"The area with the largest volume of night crime is {peak_night_crime_location}")

# Step 4: Analyze Victim Age Groups

age_bins = [0, 17, 25, 34, 44, 54, 64, np.inf]
age_labels = ["0-17", "18-25", "26-34", "35-44", "45-54", "55-64", "65+"]
crimes["Age Bracket"] = pd.cut(crimes["Vict Age"], bins=age_bins, labels=age_labels)
victim_ages = crimes["Age Bracket"].value_counts()
print(victim_ages)
