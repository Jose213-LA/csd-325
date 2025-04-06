import csv
from datetime import datetime
from matplotlib import pyplot as plt
import sys

def plot_temperatures(dates, temperatures, color, label):
    """Function to plot temperatures"""
    fig, ax = plt.subplots()
    ax.plot(dates, temperatures, c=color)
    
    # Format plot.
    plt.title(f"Daily {label} temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

def main():
    filename = 'sitka_weather_2018_simple.csv'

    # Open the weather data file and read it.
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get dates, high and low temperatures from this file.
        dates, highs, lows = [], [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            highs.append(int(row[5]))
            lows.append(int(row[6]))

    # Menu loop
    while True:
        # Display the menu options
        print("\nSelect an option:")
        print("1. View High Temperatures")
        print("2. View Low Temperatures")
        print("3. Exit")

        # Get the user's choice
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            # Plot high temperatures
            plot_temperatures(dates, highs, 'red', 'high')
        elif choice == '2':
            # Plot low temperatures
            plot_temperatures(dates, lows, 'blue', 'low')
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            sys.exit()  # Exit the program
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Run the main function
if __name__ == "__main__":
    main()
