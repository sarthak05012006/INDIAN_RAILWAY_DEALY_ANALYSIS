# 🚆 Indian Railway Delay Analysis

A Python-based Data Science project that analyzes Indian Railway delays using **NumPy, Pandas, and Matplotlib**. The project explores train arrival and departure delays, compares station performance, identifies delay patterns, and visualizes railway punctuality trends.

## 🎯 Project Objectives

- Analyze train arrival and departure delays.
- Identify stations with higher average arrival delays.
- Compare train-wise delay performance.
- Visualize delay distributions and daily trends.
- Generate statistical summaries and CSV reports.

## 🛠️ Technologies Used

- **Python** — Core programming language
- **NumPy** — Numerical computations and statistical analysis
- **Pandas** — Data cleaning, processing, and aggregation
- **Matplotlib** — Data visualization and graphs

## 📊 Key Features

- Railway dataset exploration and cleaning
- Average, median, and maximum delay calculations
- Train-wise and station-wise performance analysis
- Arrival delay distribution visualization
- Departure versus arrival delay comparison
- Daily delay trend analysis
- CSV report generation

## 📁 Project Structure

```text
Indian-Railway-Delay-Analysis/
├── data/
│   └── train_routes_delays_Sep2024.csv
├── graphs/
├── reports/
├── dashboard_output/
├── analysis.py
├── dashboard.py
└── README.md
```

*Note: `dashboard.py` is an optional interactive terminal-menu tool for exploring analysis results and generating charts.*

## ⚙️ Installation and Setup

**1. Clone the repository**

```bash
git clone YOUR_REPOSITORY_URL
cd Indian-Railway-Delay-Analysis
```

Replace `YOUR_REPOSITORY_URL` with your GitHub repository URL.

**2. Install the required libraries**

```bash
pip install numpy pandas matplotlib
```

**3. Add the dataset**

Place the downloaded CSV file at:

```text
data/train_routes_delays_Sep2024.csv
```

**4. Run the analysis**

```bash
python3 analysis.py
```

**5. Run the optional interactive tool**

```bash
python3 dashboard.py
```

## 📈 Visualizations

The project generates graphs such as:

- Arrival delay distribution
- Top 10 stations by average arrival delay
- Departure delay versus arrival delay
- Top 10 trains by average arrival delay
- Arrival delay severity distribution
- Daily average arrival delay trends

## 📂 Output Reports

The analysis can generate CSV reports containing:

- Summary statistics
- Train-wise delay information
- Station-wise delay information

These reports can be used for further analysis and documentation.

## 📚 Dataset

The project uses a historical Indian Railway delay dataset covering September 2024.

Dataset source: [RSTGCN GitHub Repository](https://github.com/KoyenaChowdhury/RSTGCN)

The analysis reflects only the records available in the dataset and should not be interpreted as a complete representation of all Indian Railway services.

## 🔍 Learning Outcomes

Through this project, I explored:

- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Statistical calculations with NumPy
- Data manipulation using Pandas
- Data visualization using Matplotlib
- Extracting insights from real-world transportation data

## 🚀 Future Improvements

- Analyze delays across multiple months and years
- Investigate the relationship between routes and delays
- Add weather and seasonal information
- Explore machine learning for delay prediction
- Improve performance when processing large datasets

## 👨‍💻 Author

**Sarthak Dewangan**

Interested in Data Science, AI/ML, and real-world data-driven solutions.

---

⭐ If you find this project interesting, consider starring the repository!
