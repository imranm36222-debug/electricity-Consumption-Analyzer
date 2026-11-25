# Electricity Consumption Analyzer

A simple console-based Python 3 project that reads monthly electricity usage from a CSV file, calculates useful statistics, finds months with above-average consumption, and displays charts.

## Project Information

- **Project Number:** PS No. 15
- **Project Title:** Electricity Consumption Analyzer
- **Language:** Python 3
- **Libraries:** Pandas, NumPy, Matplotlib

## Features

- Reads monthly electricity consumption from `usage.csv` (with or without a `Month,Units` header row).
- Skips rows with a missing month, an invalid unit value, or a negative unit value, and reports each skipped row.
- Calculates total, average, highest, lowest and population standard deviation.
- Finds months with consumption above the average.
- Displays a bar chart and a line chart with an average line.
- Provides a simple menu: view summary, view above-average months and charts, or exit.

## Project Structure

```text
Electricity_Consumption_Analyzer/
├── Main.py
├── usage.csv
├── Readme.md
└── Summary.md
```

## Requirements

Install Python 3, then install the required libraries:

```bash
pip install pandas numpy matplotlib
```

## CSV File Format

Keep a file named `usage.csv` in the same folder as `Main.py`.

```csv
Month,Units
Jan,200
Feb,250
Mar,300
```

## How to Run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Install the required libraries.
4. Run the program:

```bash
python Main.py
```

## Menu Options

1. **View Summary** - shows total, average, highest, lowest and standard deviation.
2. **Above Average Months and Charts** - lists months above the average and displays bar and line charts.
3. **Exit** - closes the program.

## Sample Result

For Jan = 200, Feb = 250, Mar = 300:

```text
Total: 750 units | Average: 250.00
Highest: Mar (300) | Lowest: Jan (200)
Std Dev: 40.82
```

Above-average result:

```text
Months above average (250.00): Mar (300)
Bar chart 'Monthly Consumption' displayed
```

The standard deviation uses NumPy's default population calculation (`np.std`).

## Input Validation

A row is skipped when:

- The month is missing or blank.
- The units value is missing or not a valid number.
- The units value is negative.

## Test Cases

| Test Case | Input | Expected Output |
|---|---|---|
| Normal input | Jan 200, Feb 250, Mar 300 | Total 750, average 250.00, highest Mar (300), lowest Jan (200), std dev 40.82 |
| Minimum input | Jan 150 | Total 150, average 150.00, highest and lowest Jan (150), std dev 0.00 |
| Invalid input | Jan 200, Feb abc, Mar -30 | Row 2 and Row 3 skipped; valid rows: 1, total 200 |
| Above-average scenario | Jan 200, Feb 250, Mar 300 | Mar (300) above average 250.00; charts displayed |

## License

This project is created for educational and academic purposes.
