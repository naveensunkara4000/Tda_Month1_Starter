# TDA Data Science Internship — Month 1 Starter (Python Basics & Data Manipulation)

This repository scaffolds your Month 1 tasks (Weeks 1–4). It includes example datasets, starter scripts, and a clear checklist for each week.

## Environment Setup
```bash
# 1) Install Python 3.10+
# 2) Create and activate a virtual environment
python -m venv .venv
# Windows
.venv\Scripts\activate

# 3) Install dependencies
pip install -r requirements.txt
```

## Repository Structure
```
tda_month1_starter/
├── data/
│   ├── data_raw.csv          
│   ├── sales.csv             
│   └── temperatures.csv      
├── week1/
│   ├── temp_converter.py
│   ├── calculator.py
│   └── avg_temperature.py
├── week2/
│   ├── data_structures.py
│   └── data_cleaning.py
├── week3/
│   ├── numpy_basics.py
│   ├── pandas_manipulation.py
│   └── aggregate_dataset.py
├── week4/
│   └── visualization.py
├── SUMMARY_TEMPLATE.md
├── requirements.txt
└── .gitignore
```

## Week 1 – Python Basics

**Objectives**:
- Learn basic Python syntax: variables, data types, if/else, loops, input/output.
- Build simple CLI scripts and a small data processing client mini-project.
  
**Files you will Create**:
 -  `calculator.py` → Build a simple calculator for +, -, *, /.
 -  `temp_converter.py` → Convert Celsius ↔ Fahrenheit.
 -  `avg_temperature.py` → Load `temperatures.csv` and compute average.

 Run with:
```bash
python week1/calculator.py
python week1/temp_converter.py
python week1/avg_temperature.py
```

## Week 2 – Data Structures & Cleaning
 **Objectives**:
  -  Master lists, tuples, dictionaries, sets, functions, lambda, recursion, and list comprehensions.
  -  Perform basic data cleaning using Pandas.
  
  **Files you will use/create:**
   -  `data_structures.py` → Practice with lists, sets, dicts.
   -  `data_cleaning.py` → Clean missing values in `sales.csv`.
   -  `data/data_raw.csv` → messy dataset — sample provided`.

  **Step-by-step**
  1. Inspect `data/data_raw.csv` in a text editor to see whitespace, duplicates, and missing values.
  2. Run the practice script:
```bash
python week2/data_structures.py
````
  3. Run the cleaning pipeline
```bash  
python week2/data_cleaning.py
```
  4. Open `data/cleaned.csv` and manually verify:
   - Leading/trailing spaces removed
   - Duplicate rows removed
   - Missing numeric values filled with median
   - Rows without `id` removed
  5. Fill `WEEK2_SUMMARY.md` with:
   - Cleaning steps you applied
   - Data before vs after (rows count)
   - Any tricky problems (e.g., wrong datatypes) and how you fixed them

## Week 3 – NumPy & Pandas (Manipulation and Aggregation)

  **Objectives**: Use NumPy for vectorized operations and Pandas for tabular data manipulation and grouping.
  
  **Files you will use/create**: 
    -`week3/numpy_basics.py`
    -`week3/pandas_manipulation.py`
    -`week3/aggregate_dataset.py`
    -`data/sales.csv`(sample sales data included)
    
- **Step-by-step**:
  1. Run the NumPy demo:
    `python week3/numpy_basics.py`
  2. Inspect `data/sales.csv`. Run the pandas manipulation script:
     `python week3/pandas_manipulation.py`
  3. Run aggregation to create per-day aggregates:
     `python week3/aggregate_dataset.py`
  4. Open `data/daily_aggregates.csv` to confirm the aggregated results are saved.
  5. Fill` WEEK3_SUMMARY.md` with:
    - Key pandas operations used (groupby, agg, reset_index)
    - Sample queries you ran and their outputs


## Week 4 – Visualization
 **Objectives**: 
   Create clear visualizations (histogram, scatter, boxplot, heatmap) and export them as PNGs for submission.

 **Files you will use/create**: 
   - `week4/visualization.py` (creates 4 PNG files)

**Step-by-step**:
  1. Run the visualization script (it saves PNG files):
```bash
python week4/visualization.py
```
  2. Confirm the following files are created in project root:
 ```bash
- week4_revenue_hist.png
- week4_units_vs_revenue_scatter.png
- week4_revenue_box_by_category.png
- week4_corr_heatmap.png
 ```
  3. Inspect each plot:
   - Histogram: distribution of revenue
   - Scatter: relationship units vs revenue
   - Boxplot: revenue distribution by category
   - Heatmap: correlation matrix
  4. Save a short interpretation paragraph in WEEK4_SUMMARY.md describing insights from the plots


## Git Quick Commands
```bash
 git add
 git commit -m "weekX: summary"
 git remote add origin https://github.com/<your-username>/<repo-name>.git
 git branch -M main
 git push -u origin main
```
