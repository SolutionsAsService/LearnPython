import pandas as pd
import matplotlib.pyplot as plt

# Data for RF modules and ranges
data = [
    {"Module": "nRF24L01+ (PCB Antenna)", "Band": "2.4 GHz", "Range_m": 100},
    {"Module": "nRF24L01+ (Wire Dipole)", "Band": "2.4 GHz", "Range_m": 1000},
    {"Module": "RFM69HCW (Whip)", "Band": "868/915 MHz", "Range_m": 500},
    {"Module": "RFM69HCW (Helical)", "Band": "868/915 MHz", "Range_m": 5000},
    {"Module": "LoRa RFM95 (Wire Whip)", "Band": "868/915 MHz", "Range_m": 2000},
    {"Module": "LoRa RFM95 (High-Gain)", "Band": "868/915 MHz", "Range_m": 20000},
    {"Module": "XBee S1 (1 mW)", "Band": "2.4 GHz", "Range_m": 100},
    {"Module": "XBee-Pro S1 (18 dBm)", "Band": "2.4 GHz", "Range_m": 1600},
]

df = pd.DataFrame(data)

# Display the data in a table
import ace_tools as tools; tools.display_dataframe_to_user(name="RF Module Ranges", dataframe=df)

# Plotting the ranges
plt.figure(figsize=(10, 6))
plt.bar(df["Module"], df["Range_m"])
plt.xticks(rotation=45, ha="right")
plt.ylabel("Range (m)")
plt.title("Effective Data-Transmission Ranges of RF Modules with Different Antennas")
plt.tight_layout()
plt.show()
