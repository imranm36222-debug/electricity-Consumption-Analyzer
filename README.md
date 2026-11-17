# Electricity Consumption Analyzer

A simple console-based Python 3 project that reads monthly electricity
usage from a CSV file, calculates useful statistics, identifies months
with above-average consumption, and displays charts.

## Project Information

-   **Project Number:** PS No. 15
-   **Project Title:** Electricity Consumption Analyzer
-   **Language:** Python 3
-   **Libraries:** Pandas, NumPy, Matplotlib

## Features

-   Reads monthly electricity consumption from `usage.csv`.
-   Checks the CSV for the required `Month` and `Units` columns.
-   Skips rows with missing months, invalid unit values, or negative
    unit values.
-   Calculates:
    -   Total electricity consumption
    -   Average electricity consumption
    -   Highest consumption and month
    -   Lowest consumption and month
    -   Population standard deviation
-   Finds months with consumption above the average.
-   Displays a bar chart and a line chart.
-   Provides a simple menu to view the summary, view above-average
    months and charts, or exit.

## Project Structure

``` text
Electricity_Consumption_Analyzer/
├── main.py
├── usage.csv
├── README.md
└── PROJECT_SUMMARY.md
```

## Requirements

Install Python 3. Then install the required libraries:

``` bash
pip install pandas numpy matplotlib
```

## CSV File Format

Create a file named `usage.csv` in the same folder as `main.py`.

Example:

``` csv
Month,Units
Jan,200
Feb,250
Mar,300
```

The CSV file must contain the column names `Month` and `Units`.

## How to Run

1.  Download or clone this repository.
2.  Open a terminal in the project folder.
3.  Install the required libraries.
4.  Run the program:

``` bash
python main.py
```

## Menu Options

When the program starts, it displays these options:

1.  **View Summary** -- shows total, average, highest, lowest, and
    standard deviation.
2.  **Above Average Months and Charts** -- lists months whose usage is
    greater than the average and displays bar and line charts.
3.  **Exit** -- closes the program.

## Sample Result

For the sample CSV data:

  Month     Units
  ------- -------
  Jan         200
  Feb         250
  Mar         300

The summary is:

``` text
Total: 750 units
Average: 250.00
Highest: Mar (300)
Lowest: Jan (200)
Std Dev: 40.82
```

The above-average result is:

``` text
Mar (300)
```

The standard deviation uses NumPy's default population calculation
(`np.std`).

## Input Validation

The program skips rows when:

-   The month is missing or blank.
-   The units value is missing or is not a valid number.
-   The units value is negative.

A skipped row is reported in the console.

## Test Cases

  -----------------------------------------------------------------------
  Test Case               Input                   Expected Behaviour
  ----------------------- ----------------------- -----------------------
  Normal input            Jan 200, Feb 250, Mar   Total 750, average 250,
                          300                     highest Mar, lowest
                                                  Jan, standard deviation
                                                  about 40.82

  Minimum input           Jan 150                 Total and average 150;
                                                  highest and lowest Jan;
                                                  standard deviation 0

  Invalid input           Jan 200, Feb `abc`, Mar Invalid rows are
                          -30                     skipped; only Jan is
                                                  used

  Above-average scenario  Jan 200, Feb 250, Mar   Mar is listed as above
                          300                     average; bar and line
                                                  charts are displayed
  -----------------------------------------------------------------------

## Author

Add your name, course, college, and other details here if required.

## License

This project is created for educational and academic purposes.
