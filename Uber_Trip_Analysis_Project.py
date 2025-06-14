# Uber Trip Analysis Dashboard - Python Data Science Project
# Detailed, step-by-step analysis and visualization (R project style)
# Author: Aayush Yadav

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import warnings
warnings.filterwarnings('ignore')

plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

print("✅ All essential packages imported successfully!")

colors = ["#CC1011", "#665555", "#05a399", "#cfcaca", "#f5e840", "#0683c9", "#e075b0"]
print("🎨 Color palette set for visualizations.")

df = pd.read_excel('Uber Trip Details.xlsx')  # Update with your actual file path
print(df.head())

df['Date_Time'] = pd.to_datetime(df['Date_Time'])
df['hour'] = df['Date_Time'].dt.hour
df['day'] = df['Date_Time'].dt.day
df['month'] = df['Date_Time'].dt.month_name()
df['year'] = df['Date_Time'].dt.year
df['dayofweek'] = df['Date_Time'].dt.day_name()

# Trips by Hour
hour_data = df.groupby('hour').size().reset_index(name='Total')
plt.figure(figsize=(10,5))
sns.barplot(data=hour_data, x='hour', y='Total', color=colors[0])
plt.title('Trips Every Hour')
plt.show()

# Trips by Day
day_data = df.groupby('day').size().reset_index(name='Total')
plt.figure(figsize=(10,5))
sns.barplot(data=day_data, x='day', y='Total', color=colors[1])
plt.title('Trips Every Day')
plt.show()

# Trips by Month
month_data = df.groupby('month').size().reset_index(name='Total')
plt.figure(figsize=(8,5))
sns.barplot(data=month_data, x='month', y='Total', color=colors[2])
plt.title('Trips by Month')
plt.show()

# Trips by Day of Week
dow_data = df.groupby('dayofweek').size().reset_index(name='Total')
order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
plt.figure(figsize=(8,5))
sns.barplot(data=dow_data, x='dayofweek', y='Total', order=order, color=colors[3])
plt.title('Trips by Day of Week')
plt.show()

# Trips by Base
if 'Base' in df.columns:
    base_data = df.groupby('Base').size().reset_index(name='Total')
    plt.figure(figsize=(8,5))
    sns.barplot(data=base_data, x='Base', y='Total', color=colors[4])
    plt.title('Trips by Base')
    plt.show()

# Vehicle Type Analysis
if 'vehicle_type' in df.columns:
    vehicle_data = df['vehicle_type'].value_counts().reset_index()
    vehicle_data.columns = ['Vehicle Type', 'Total Trips']
    plt.figure(figsize=(7,4))
    sns.barplot(data=vehicle_data, x='Vehicle Type', y='Total Trips', palette=colors)
    plt.title('Trips by Vehicle Type')
    plt.show()

# Payment Type Analysis
if 'payment_type' in df.columns:
    payment_data = df['payment_type'].value_counts().reset_index()
    payment_data.columns = ['Payment Type', 'Total Trips']
    plt.figure(figsize=(7,4))
    sns.barplot(data=payment_data, x='Payment Type', y='Total Trips', palette=colors)
    plt.title('Trips by Payment Type')
    plt.show()

# Top Pickup & Dropoff
if 'pickup_location' in df.columns:
    top_pickup = df['pickup_location'].value_counts().head(10)
    plt.figure(figsize=(8,5))
    sns.barplot(y=top_pickup.index, x=top_pickup.values, color=colors[5])
    plt.title('Top 10 Pickup Locations')
    plt.show()

if 'dropoff_location' in df.columns:
    top_dropoff = df['dropoff_location'].value_counts().head(10)
    plt.figure(figsize=(8,5))
    sns.barplot(y=top_dropoff.index, x=top_dropoff.values, color=colors[6])
    plt.title('Top 10 Dropoff Locations')
    plt.show()

# Trip Distance & Duration
if 'trip_distance' in df.columns:
    plt.figure(figsize=(7,4))
    sns.histplot(df['trip_distance'], bins=40, color=colors[0], kde=True)
    plt.title('Distribution of Trip Distances')
    plt.show()

if 'trip_duration' in df.columns:
    plt.figure(figsize=(7,4))
    sns.histplot(df['trip_duration'], bins=40, color=colors[1], kde=True)
    plt.title('Distribution of Trip Durations')
    plt.show()

# Heatmaps
pivot1 = df.groupby(['day', 'hour']).size().unstack(fill_value=0)
plt.figure(figsize=(12,6))
sns.heatmap(pivot1, cmap='YlOrRd')
plt.title('Heatmap of Trips: Day vs Hour')
plt.show()

pivot2 = df.groupby(['day', 'month']).size().unstack(fill_value=0)
plt.figure(figsize=(12,6))
sns.heatmap(pivot2, cmap='YlOrRd')
plt.title('Heatmap of Trips: Month vs Day')
plt.show()

pivot3 = df.groupby(['dayofweek', 'month']).size().unstack(fill_value=0)
plt.figure(figsize=(10,6))
sns.heatmap(pivot3, cmap='YlOrRd')
plt.title('Heatmap of Trips: Month vs Day of Week')
plt.show()

# Map
if {'Lat', 'Lon'}.issubset(df.columns):
    plt.figure(figsize=(8,8))
    plt.scatter(df['Lon'], df['Lat'], s=1, alpha=0.5)
    plt.title('NYC Map of Uber Rides')
    plt.show()

print("Analysis complete. Visualizations above match the Power BI dashboard and R project insights.")
