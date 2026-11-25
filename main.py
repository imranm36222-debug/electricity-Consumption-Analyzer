import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "usage.csv")


# Function 1: Load and clean CSV data
def load_data():
    try:
        # header=None so files with OR without a header row both work
        raw = pd.read_csv(csv_path, header=None, names=["Month", "Units"],
                          skip_blank_lines=True, dtype=str)

        # Drop header row if present
        if len(raw) > 0 and str(raw.iloc[0]["Month"]).strip().lower() == "month":
            raw = raw.iloc[1:].reset_index(drop=True)

        valid_data = []

        for index, row in raw.iterrows():
            row_number = index + 1  # data row number (Jan = Row 1)
            month = row["Month"]
            units = pd.to_numeric(row["Units"], errors="coerce")

            if pd.isna(month) or str(month).strip() == "":
                print(f"Row {row_number} skipped: Month is missing.")
                continue

            if pd.isna(units) or not np.isfinite(units):
                print(f"Row {row_number} skipped: invalid Units '{row['Units']}'.")
                continue

            if units < 0:
                print(f"Row {row_number} skipped: Units cannot be negative.")
                continue

            valid_data.append({"Month": str(month).strip(), "Units": float(units)})

        clean_df = pd.DataFrame(valid_data, columns=["Month", "Units"])

        total = clean_df["Units"].sum()
        print(f"Valid rows: {len(clean_df)} | Total: {total:g} units")

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

    total = np.sum(units)
    average = np.mean(units)
    std_dev = np.std(units)  # population std dev -> 40.82 for 200/250/300

    highest_row = df.loc[df["Units"].idxmax()]
    lowest_row = df.loc[df["Units"].idxmin()]

    print("\n------ ELECTRICITY SUMMARY ------")
    print(f"Total: {total:g} units | Average: {average:.2f}")
    print(f"Highest: {highest_row['Month']} ({highest_row['Units']:g}) | "
          f"Lowest: {lowest_row['Month']} ({lowest_row['Units']:g})")
    print(f"Std Dev: {std_dev:.2f}")


# Function 3: Find above-average months + charts
def above_average(df):
    if df.empty:
        print("No valid data available.")
        return

    average = np.mean(df["Units"])
    result = df[df["Units"] > average]

    print("\n------ ABOVE AVERAGE MONTHS ------")
    if result.empty:
        print(f"Months above average ({average:.2f}): None")
    else:
        items = ", ".join(f"{r['Month']} ({r['Units']:g})" for _, r in result.iterrows())
        print(f"Months above average ({average:.2f}): {items}")

    print("Bar chart 'Monthly Consumption' displayed")

    plt.figure(figsize=(8, 5))
    plt.bar(df["Month"], df["Units"])
    plt.axhline(average, linestyle="--", label="Average Consumption")
    plt.title("Monthly Consumption")
    plt.xlabel("Month")
    plt.ylabel("Units")
    plt.legend()
    plt.tight_layout()

    plt.figure(figsize=(8, 5))
    plt.plot(df["Month"], df["Units"], marker="o")
    plt.axhline(average, linestyle="--", label="Average Consumption")
    plt.title("Monthly Consumption - Line Chart")
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


if __name__ == "__main__":
    main()
