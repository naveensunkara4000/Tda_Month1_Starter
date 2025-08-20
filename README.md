# TDA Data Science Internship — Month 1 Starter (Python Basics & Data Manipulation)

 This repository scaffolds your Month 1 tasks (Weeks 1–4). It includes example datasets, starter scripts, and a clear checklist for each week.

> **How to use this**
> 1. Create a **new GitHub repo** (e.g., `tda-ds-month1`).
> 2. Download this ZIP, extract it, and initialize Git (`git init`), then commit and push.
> 3. Complete each week's tasks inside the respective folder.
> 4. Export your **weekly summary** using the template in `SUMMARY_TEMPLATE.md`.
> 5. Submit your **GitHub repo link** (and screenshots if needed) using your cohort's submission process (Google Form / Classroom).

## Environment Setup
```bash
# 1) Install Python 3.10+
# 2) Create and activate a virtual environment
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

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

## Submission Checklist (Monthly)
- [ ] Push code for all weeks to GitHub (public repo or grant access).
- [ ] Ensure `README.md` explains how to run each script.
- [ ] Include your `SUMMARY_TEMPLATE.md` filled for each week.
- [ ] (Optional) Export plots from `week4/visualization.py` to PNG and add to repo.
- [ ] Submit your repo link via your cohort's **Google Form** or **Classroom** by the 10th.

