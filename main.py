
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Function 1: Load and clean CSV data
def load_data():

    try:
        df = pd.read_csv("usage.csv")

        # Check required columns
        if "Month" not in df.columns or "Units" not in df.columns:
            print("Error: CSV must contain Month and Units columns.")
            return None

        valid_data = []

        # Check every row
        for index, row in df.iterrows():

            row_number = index + 2
            month = row["Month"]
            units = pd.to_numeric(row["Units"], errors="coerce")

            # Check missing month
            if pd.isna(month) or str(month).strip() == "":
                print(f"Row {row_number} skipped: Month is missing.")
                continue

            # Check invalid or missing units
            if pd.isna(units) or not np.isfinite(units):
                print(f"Row {row_number} skipped: invalid Units '{row['Units']}'.")
                continue

            # Check negative units
            if units < 0:
                print(f"Row {row_number} skipped: Units cannot be negative.")
                continue

            # Store valid data
            valid_data.append({
                "Month": str(month).strip(),
                "Units": float(units)
            })

        clean_df = pd.DataFrame(valid_data)

        print("\nValid rows:", len(clean_df))

        return clean_df

    except FileNotFoundError:
        print("Error: usage.csv file not found.")
        return None

    except Exception as e:
        print("Error:", e)
        return None


# Function 2: Display electricity summary
def show_summary(df):

    if df.empty:
        print("No valid data available.")
        return

    units = df["Units"].to_numpy()

    # Calculate statistics using NumPy
    total = np.sum(units)
    average = np.mean(units)
    highest = np.max(units)
    lowest = np.min(units)
    std_dev = np.std(units)

    # Find highest and lowest months
    highest_month = df[df["Units"] == highest]
    lowest_month = df[df["Units"] == lowest]

    print("\n------ ELECTRICITY SUMMARY ------")

    print("Total:", total, "units")
    print("Average:", f"{average:.2f}")

    for _, row in highest_month.iterrows():
        print("Highest:", row["Month"], f"({row['Units']:g})")

    for _, row in lowest_month.iterrows():
        print("Lowest:", row["Month"], f"({row['Units']:g})")

    print("Std Dev:", f"{std_dev:.2f}")


# Function 3: Find above-average months
def above_average(df):

    if df.empty:
        print("No valid data available.")
        return

    average = np.mean(df["Units"])

    # Boolean filtering
    result = df[df["Units"] > average]

    print("\n------ ABOVE AVERAGE MONTHS ------")
    print(f"Average consumption: {average:.2f}")

    if result.empty:
        print("No months are above average.")
    else:
        for _, row in result.iterrows():
            print(row["Month"], f"({row['Units']:g})")

    # Display bar and line charts
    plt.figure(figsize=(8, 5))
    plt.bar(df["Month"], df["Units"])
    plt.axhline(average, linestyle="--",
                label="Average Consumption")
    plt.title("Monthly Electricity Consumption - Bar Chart")
    plt.xlabel("Month")
    plt.ylabel("Units")
    plt.legend()
    plt.tight_layout()

    plt.figure(figsize=(8, 5))
    plt.plot(df["Month"], df["Units"], marker="o")
    plt.axhline(average, linestyle="--",
                label="Average Consumption")
    plt.title("Monthly Electricity Consumption - Line Chart")
    plt.xlabel("Month")
    plt.ylabel("Units")
    plt.legend()
    plt.tight_layout()

    plt.show()


# Function 4: Main menu
def main():

    print("================================")
    print(" ELECTRICITY CONSUMPTION ANALYZER")
    print("================================")

    # Load CSV file
    df = load_data()

    if df is None:
        return

    if df.empty:
        print("No valid electricity records found.")
        return

    while True:

        print("\n----------- MENU -----------")
        print("1. View Summary")
        print("2. Above Average Months and Charts")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_summary(df)

        elif choice == "2":
            above_average(df)

        elif choice == "3":
            print("Thank you for using the program!")
            break

        else:
            print("Invalid choice! Please try again.")


# Run the program
if __name__ == "__main__":
    main()
