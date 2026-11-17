# Project Summary -- Electricity Consumption Analyzer

**Project Number:** PS No. 15\
**Project Title:** Electricity Consumption Analyzer\
**Programming Language:** Python 3

## Overview

The Electricity Consumption Analyzer is a simple, menu-driven Python
application. It reads monthly electricity consumption records from a CSV
file and analyzes the data using Pandas and NumPy. It also uses
Matplotlib to display electricity consumption through bar and line
charts.

## Main Features

1.  Reads monthly consumption data from `usage.csv`.
2.  Checks for the required `Month` and `Units` columns.
3.  Skips invalid records, including missing months, non-numeric units,
    and negative units.
4.  Calculates total and average electricity consumption.
5.  Finds the months with the highest and lowest consumption.
6.  Calculates population standard deviation using NumPy.
7.  Displays months whose consumption is above the average.
8.  Creates bar and line charts to show monthly electricity usage.

## Libraries Used

-   **Pandas:** Reads the CSV file and organizes the records in a
    DataFrame.
-   **NumPy:** Performs calculations such as sum, mean, maximum,
    minimum, and standard deviation.
-   **Matplotlib:** Creates bar and line charts.

## Input and Output

The program uses a CSV file with two columns: `Month` and `Units`.

For example, with Jan = 200, Feb = 250, and Mar = 300:

-   Total consumption: 750 units
-   Average consumption: 250.00 units
-   Highest consumption: March (300 units)
-   Lowest consumption: January (200 units)
-   Population standard deviation: 40.82 units
-   Above-average month: March

## Conclusion

This project demonstrates basic Python programming, CSV file handling,
data validation, statistical calculations, and data visualization. It
provides a simple way to understand and compare monthly electricity
consumption.
