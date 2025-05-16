import pandas as pd
import matplotlib.pyplot as plt

# ==========================
#  SECTION: Import & Read Data
# ==========================
# Import Data
try:
    df = pd.read_csv("WWTP_Data.csv")
except FileNotFoundError:
    print("Data not found. Exit program.")
    exit()
# Basic info
print(f"\n[Data Info]")
df.info()

# ==========================
#  SECTION: Prepare Data
# ==========================
# Key groups
trt_df = df[["Ammonia", "Biological Oxygen Demand", "Chemical Oxygen Demand", "Total Nitrogen"]]
opt_df = df[["Average Outflow", "Average Inflow", "Energy Consumption"]]
env_df = df[["Average Temperature", "Average Humidity", "Total Rainfall"]]
# Missing values check
print("\nMissing Values")
print(f"Treatment: {trt_df.isna().sum().sum()}")
print(f"Operational: {opt_df.isna().sum().sum()}")
print(f"Environmental: {env_df.isna().sum().sum()}")

# ==========================
#  SECTION: Analyze & Visualize Data
# ==========================
# --- Treatment Performance ---
print("\n[Treatment Performance Summary]")
print(trt_df.describe().loc[["mean", "50%", "std"]].round(2))
# Visualization
trt_df.plot(title="Treatment Pollutants Over Time")
plt.xlabel("Time")
plt.ylabel("Level")
plt.grid(True)
plt.tight_layout()
plt.show()
# --- Operational Metrics ---
print("\n[Operational Metrics Summary]")
print(opt_df.describe().loc[["mean", "50%", "std"]].round(2))
# Visualization
opt_df[["Average Inflow", "Average Outflow"]].plot(title="Inflow vs Outflow")
plt.ylabel("Flow")
plt.tight_layout()
plt.show()
# --- Environmental Factors ---
print("\n[Environmental Factors Summary]")
print(env_df.describe().loc[["mean", "50%", "std"]].round(2))
# Visualization
env_df.plot(title="Environmental Trends")
plt.xlabel("Time")
plt.ylabel("Value")
plt.tight_layout()
plt.show()

# Terminology:
# - Ammonia: Toxic nitrogen from waste/fertilizer
# - BOD: Oxygen needed to break down wastes (organic)
# - COD: Oxygen needed to oxidize pollutants (organic/chemical)
# - TN: Total nitrogen in all forms