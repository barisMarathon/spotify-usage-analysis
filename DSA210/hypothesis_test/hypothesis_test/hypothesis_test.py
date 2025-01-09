import pandas as pd
from scipy import stats
from datetime import datetime, timedelta

# Read the car and spotify data
car_file = "D:\\Downloads\\SQL for DSA\\car.txt"
spotify_file = "D:\\Downloads\\SQL for DSA\\spotify.txt"

car_data = pd.read_csv(car_file, header=None, names=["timestamp"])
spotify_data = pd.read_csv(spotify_file, header=None, names=["timestamp"])

# Convert timestamps to datetime objects
car_data["timestamp"] = pd.to_datetime(car_data["timestamp"])
spotify_data["timestamp"] = pd.to_datetime(spotify_data["timestamp"])

# Define a function to count matches within a 15-minute window
def count_matches(car_times, spotify_times):
    matches = 0
    for car_time in car_times:
        for spotify_time in spotify_times:
            if abs(car_time - spotify_time) <= timedelta(minutes=15):
                matches += 1
                break
    return matches

# Count the number of matches
matches = count_matches(car_data["timestamp"], spotify_data["timestamp"])

# Calculate the z-score
total_car_entries = len(car_data)
observed_proportion = matches / total_car_entries
expected_proportion = 0.75
standard_error = (expected_proportion * (1 - expected_proportion) / total_car_entries) ** 0.5
z_score = (observed_proportion - expected_proportion) / standard_error

# Print the results
print(f"Total car entries: {total_car_entries}")
print(f"Number of matches: {matches}")
print(f"Observed proportion: {observed_proportion:.2f}")
print(f"Expected proportion: {expected_proportion:.2f}")
print(f"Z-score: {z_score:.2f}")

# Test the hypothesis
alpha = 0.05
p_value = stats.norm.sf(z_score)  # one-tailed test
if p_value < alpha:
    print("Reject the null hypothesis: You listen to music 75% or more of the time you are in the car.")
else:
    print("Fail to reject the null hypothesis: You do not listen to music 75% or more of the time you are in the car.")