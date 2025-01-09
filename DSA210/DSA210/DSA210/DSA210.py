import re
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates

def read_sql_file_and_extract_datetimes(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            sql_content = file.read()
            # Regular expression to match datetime values in SQL format
            datetime_values = re.findall(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', sql_content)

            if datetime_values:
                print(f"Extracted Datetime Values from '{file_path}':\n")
                for dt in datetime_values:
                    print(dt)
                
                return datetime_values
            else:
                print(f"No datetime values found in the SQL file '{file_path}'.")
                return []
                
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found!")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def plot_datetime_events(datetime_values_car, datetime_values_spotify):
    # Convert datetime strings to datetime objects
    datetime_objects_car = [datetime.strptime(dt, '%Y-%m-%d %H:%M:%S') for dt in datetime_values_car]
    datetime_objects_spotify = [datetime.strptime(dt, '%Y-%m-%d %H:%M:%S') for dt in datetime_values_spotify]

    # Extracting the date and time components
    dates_car = [dt.date() for dt in datetime_objects_car]
    times_in_seconds_car = [dt.hour * 3600 + dt.minute * 60 + dt.second for dt in datetime_objects_car]

    dates_spotify = [dt.date() for dt in datetime_objects_spotify]
    times_in_seconds_spotify = [dt.hour * 3600 + dt.minute * 60 + dt.second for dt in datetime_objects_spotify]

    # Create figure and three subplots
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(24, 6), sharey=True)

    # Plot for car.sql
    ax1.scatter(dates_car, times_in_seconds_car, color='blue', label='Event times (Car)', alpha=0.7)
    ax1.set_xlim([datetime(2024, 11, 26), datetime(2025, 1, 8)])
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d-%b'))
    ax1.xaxis.set_major_locator(mdates.DayLocator(interval=4))
    ax1.set_ylim([24 * 3600, 0])  # Reverse y-axis
    ax1.set_yticks([i * 3600 for i in range(0, 25, 2)])
    ax1.set_yticklabels([f"{i:02d}:00" for i in range(0, 25, 2)])
    ax1.set_title("SQL Datetime Events (Car)")
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Time of Day (23:59 to 00:00)")
    ax1.grid(True)
    ax1.legend()

    # Plot for spotify.sql
    ax2.scatter(dates_spotify, times_in_seconds_spotify, color='green', label='Event times (Spotify)', alpha=0.7)
    ax2.set_xlim([datetime(2024, 11, 26), datetime(2025, 1, 8)])
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%d-%b'))
    ax2.xaxis.set_major_locator(mdates.DayLocator(interval=4))
    ax2.set_ylim([24 * 3600, 0])  # Reverse y-axis
    ax2.set_title("SQL Datetime Events (Spotify)")
    ax2.set_xlabel("Date")
    ax2.grid(True)
    ax2.legend()

    # Plot for overlay (car.sql + spotify.sql)
    ax3.scatter(dates_car, times_in_seconds_car, color='blue', label='Event times (Car)', alpha=0.5)
    ax3.scatter(dates_spotify, times_in_seconds_spotify, color='green', label='Event times (Spotify)', alpha=0.5)
    ax3.set_xlim([datetime(2024, 11, 26), datetime(2025, 1, 8)])
    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%d-%b'))
    ax3.xaxis.set_major_locator(mdates.DayLocator(interval=4))
    ax3.set_ylim([24 * 3600, 0])  # Reverse y-axis
    ax3.set_title("SQL Datetime Events (Overlay)")
    ax3.set_xlabel("Date")
    ax3.grid(True)
    ax3.legend()

    plt.tight_layout()
    plt.show()

def plot_stacked_bar(car_times, music_times):
    # Convert datetimes to DataFrame for grouping
    car_df = pd.DataFrame({"datetime": car_times})
    music_df = pd.DataFrame({"datetime": music_times})

    # Ensure datetime conversion
    car_df["datetime"] = pd.to_datetime(car_df["datetime"], errors="coerce")
    music_df["datetime"] = pd.to_datetime(music_df["datetime"], errors="coerce")

    # Add "hour" column
    car_df["hour"] = car_df["datetime"].dt.hour
    music_df["hour"] = music_df["datetime"].dt.hour

    # Count occurrences per hour
    car_counts = car_df["hour"].value_counts().sort_index()
    music_counts = music_df["hour"].value_counts().sort_index()

    # Align indexes to ensure both have the same hourly range
    hourly_range = range(0, 24)
    car_counts = car_counts.reindex(hourly_range, fill_value=0)
    music_counts = music_counts.reindex(hourly_range, fill_value=0)

    # Plot stacked bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(hourly_range, car_counts, label="In Car", color='blue', alpha=0.6)
    plt.bar(hourly_range, music_counts, label="Listening to Music", color='green', alpha=0.6, bottom=car_counts)
    
    plt.xlabel("Hour of the Day")
    plt.ylabel("Number of Events")
    plt.title("Comparison of Time Spent in Car vs Music Listening")
    plt.xticks(hourly_range)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Main Menu
def main():
    print("Choose an option:")
    print("1. Plot 3-way graph (Car, Spotify, and Overlay)")
    print("2. Plot stacked bar comparison")

    choice = input("Enter your choice (1 or 2): ")

    # File paths
    file_path_car = "D:\\Downloads\\SQL for DSA\\car.sql"
    file_path_spotify = "D:\\Downloads\\SQL for DSA\\spotify.sql"

    # Read and extract datetimes
    datetime_values_car = read_sql_file_and_extract_datetimes(file_path_car)
    datetime_values_spotify = read_sql_file_and_extract_datetimes(file_path_spotify)

    if choice == "1":
        plot_datetime_events(datetime_values_car, datetime_values_spotify)
    elif choice == "2":
        plot_stacked_bar(datetime_values_car, datetime_values_spotify)
    else:
        print("Invalid choice. Please enter 1 or 2.")

# Run the program
if __name__ == "__main__":
    main()
