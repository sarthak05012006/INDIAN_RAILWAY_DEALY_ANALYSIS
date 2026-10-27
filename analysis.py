
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Load dataset
df = pd.read_csv("data/train_routes_delays_Sep2024.csv")

# Create folder for graphs
os.makedirs("graphs", exist_ok=True)

print("\n===== DATA CLEANING =====")

# Convert delay columns to numeric
df["arr_delay"] = pd.to_numeric(df["arr_delay"], errors="coerce")
df["dep_delay"] = pd.to_numeric(df["dep_delay"], errors="coerce")

# Remove rows with invalid delay values
df = df.dropna(subset=["arr_delay", "dep_delay"])

print("Rows after cleaning:", len(df))

# Basic statistics
print("\n===== DELAY STATISTICS =====")
print("Average arrival delay:", round(np.mean(df["arr_delay"]), 2), "minutes")
print("Median arrival delay:", round(np.median(df["arr_delay"]), 2), "minutes")
print("Maximum arrival delay:", round(np.max(df["arr_delay"]), 2), "minutes")
print("Average departure delay:", round(np.mean(df["dep_delay"]), 2), "minutes")

# Arrival delay categories
on_time = (df["arr_delay"] <= 5).sum()
moderate = ((df["arr_delay"] > 5) & (df["arr_delay"] <= 15)).sum()
high = (df["arr_delay"] > 15).sum()

print("\n===== ARRIVAL DELAY CATEGORIES =====")
print("On time (0-5 min late, including early arrivals):", on_time)
print("Moderate delay (6-15 min):", moderate)
print("High delay (over 15 min):", high)

# Station analysis
station_delay = (
    df.groupby("station")["arr_delay"]
    .agg(["mean", "count"])
    .rename(columns={"mean": "avg_delay", "count": "observations"})
)

# Avoid ranking stations with very few observations
station_delay = station_delay[station_delay["observations"] >= 100]
top10 = station_delay.nlargest(10, "avg_delay")

print("\n===== TOP 10 STATIONS BY AVERAGE ARRIVAL DELAY =====")
print(top10.round(2))

# Graph 1: Arrival delay distribution
plt.figure(figsize=(10, 5))
plt.hist(df["arr_delay"], bins=40)
plt.title("Distribution of Train Arrival Delays")
plt.xlabel("Arrival delay (minutes)")
plt.ylabel("Number of station observations")
plt.tight_layout()
plt.savefig("graphs/arrival_delay_distribution.png")
plt.close()

# Graph 2: Top 10 stations
plt.figure(figsize=(10, 6))
top10["avg_delay"].sort_values().plot(kind="barh")
plt.title("Top 10 Stations by Average Arrival Delay")
plt.xlabel("Average arrival delay (minutes)")
plt.ylabel("Station code")
plt.tight_layout()
plt.savefig("graphs/top_10_stations.png")
plt.close()

# Graph 3: Arrival vs departure delays
plt.figure(figsize=(8, 6))
plt.scatter(
    df["dep_delay"],
    df["arr_delay"],
    alpha=0.15,
    s=5
)
plt.title("Departure Delay vs Arrival Delay")
plt.xlabel("Departure delay (minutes)")
plt.ylabel("Arrival delay (minutes)")
plt.tight_layout()
plt.savefig("graphs/arrival_vs_departure.png")
plt.close()

print("\nAnalysis complete!")
print("Check the graphs folder for your three graphs.")


# ==========================================
# STEP 6: ADVANCED RAILWAY ANALYSIS
# ==========================================

print("\n===== TRAIN-WISE PERFORMANCE =====")

# Average arrival delay for each train
train_stats = df.groupby("train").agg(
    avg_arrival_delay=("arr_delay", "mean"),
    avg_departure_delay=("dep_delay", "mean"),
    station_records=("station", "count")
)

# Consider only trains with at least 100 station records
reliable_sample = train_stats[
    train_stats["station_records"] >= 100
]

print("\n10 trains with the highest average arrival delay:")
print(
    reliable_sample
    .sort_values("avg_arrival_delay", ascending=False)
    .head(10)
    .round(2)
)

print("\n10 trains with the lowest average arrival delay:")
print(
    reliable_sample
    .sort_values("avg_arrival_delay")
    .head(10)
    .round(2)
)

# ==========================================
# DELAY SEVERITY ANALYSIS
# ==========================================

print("\n===== DELAY SEVERITY =====")

delay_percentages = pd.Series({
    "On time / early (<= 0 min)": (df["arr_delay"] <= 0).mean() * 100,
    "1-5 minutes": (
        (df["arr_delay"] > 0) &
        (df["arr_delay"] <= 5)
    ).mean() * 100,
    "6-15 minutes": (
        (df["arr_delay"] > 5) &
        (df["arr_delay"] <= 15)
    ).mean() * 100,
    "16-60 minutes": (
        (df["arr_delay"] > 15) &
        (df["arr_delay"] <= 60)
    ).mean() * 100,
    "Over 60 minutes": (df["arr_delay"] > 60).mean() * 100
})

print(delay_percentages.round(2))

# Plot train performance
top_trains = (
    reliable_sample
    .nlargest(10, "avg_arrival_delay")["avg_arrival_delay"]
    .sort_values()
)

plt.figure(figsize=(10, 6))
top_trains.plot(kind="barh")
plt.title("10 Most Delayed Trains by Average Arrival Delay")
plt.xlabel("Average arrival delay (minutes)")
plt.ylabel("Train number")
plt.tight_layout()
plt.savefig("graphs/top_10_trains.png")
plt.close()

# Plot delay severity
plt.figure(figsize=(9, 5))
delay_percentages.plot(kind="bar")
plt.title("Distribution of Arrival Delay Categories")
plt.xlabel("Delay category")
plt.ylabel("Percentage of observations")
plt.xticks(rotation=25, ha="right")
plt.tight_layout()
plt.savefig("graphs/delay_severity.png")
plt.close()

print("\nAdvanced analysis completed!")
print("New graphs saved in the graphs folder.")


# ==========================================
# STEP 8: EXPORT PROJECT RESULTS
# ==========================================

import os

os.makedirs("reports", exist_ok=True)

# 1. Export station rankings
station_report = (
    df.groupby("station")
    .agg(
        avg_arrival_delay=("arr_delay", "mean"),
        avg_departure_delay=("dep_delay", "mean"),
        records=("train", "count")
    )
    .reset_index()
)

station_report = station_report[
    station_report["records"] >= 100
].sort_values("avg_arrival_delay", ascending=False)

station_report.to_csv(
    "reports/station_delay_report.csv", index=False
)

# 2. Export train rankings
train_report = (
    df.groupby("train")
    .agg(
        avg_arrival_delay=("arr_delay", "mean"),
        avg_departure_delay=("dep_delay", "mean"),
        station_records=("station", "count")
    )
    .reset_index()
)

train_report = train_report[
    train_report["station_records"] >= 100
].sort_values("avg_arrival_delay", ascending=False)

train_report.to_csv(
    "reports/train_delay_report.csv", index=False
)

# 3. Export summary statistics
summary = pd.DataFrame({
    "Metric": [
        "Total station records",
        "Unique trains",
        "Unique stations",
        "Average arrival delay (minutes)",
        "Median arrival delay (minutes)",
        "Maximum arrival delay (minutes)",
        "Average departure delay (minutes)"
    ],
    "Value": [
        len(df),
        df["train"].nunique(),
        df["station"].nunique(),
        round(df["arr_delay"].mean(), 2),
        round(df["arr_delay"].median(), 2),
        round(df["arr_delay"].max(), 2),
        round(df["dep_delay"].mean(), 2)
    ]
})

summary.to_csv("reports/project_summary.csv", index=False)

print("\n===== PROJECT REPORTS EXPORTED =====")
print("reports/station_delay_report.csv")
print("reports/train_delay_report.csv")
print("reports/project_summary.csv")
print("\nYour project analysis is complete!")

