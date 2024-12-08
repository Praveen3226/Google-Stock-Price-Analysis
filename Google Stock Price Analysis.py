#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

# Load the dataset
data = pd.read_csv('google.csv')

# Inspect the data
print(data.head())
print(data.info())





# In[5]:


import matplotlib.pyplot as plt

# Plot prices over time
plt.figure(figsize=(14, 7))
plt.plot(data['Date'], data['Open'], label='Open', alpha=0.7)
plt.plot(data['Date'], data['High'], label='High', alpha=0.7)
plt.plot(data['Date'], data['Low'], label='Low', alpha=0.7)
plt.plot(data['Date'], data['Close'], label='Close', alpha=0.7)
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Price Trends Over Time')
plt.legend()
plt.show()


# In[15]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from CSV
data = pd.read_csv('google.csv')

# Debugging: Print available columns
print("Available columns in the DataFrame:")
print(data.columns)

# Strip spaces in column names
data.columns = data.columns.str.strip()

# Debugging: Print cleaned column names
print("Cleaned columns:")
print(data.columns)

# Check if 'Volume' exists
if 'Volume' not in data.columns:
    raise KeyError("'Volume' column does not exist in the data. Check CSV or computation logic.")

# Set Date as index
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

# Resample data monthly
resampled_data = data['Volume'].resample('M').mean()

# Visualize trends
plt.figure(figsize=(12, 6))
sns.lineplot(x=resampled_data.index, y=resampled_data)
plt.title("Volume Trends Over Time")
plt.xlabel("Time")
plt.ylabel("Volume")
plt.grid(True)
plt.show()


# In[17]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from CSV
data = pd.read_csv('google.csv')

# Debugging: Print available columns
print("Columns in the raw data:")
print(data.columns)

# Strip spaces in column names to ensure no hidden formatting issues
data.columns = data.columns.str.strip()

# Debugging: Check cleaned column names
print("Cleaned column names:")
print(data.columns)

# Ensure 'Date' and 'Volume' exist
if 'Date' not in data.columns:
    raise KeyError("'Date' column does not exist in the data. Check CSV file for errors.")

if 'Volume' not in data.columns:
    raise KeyError("'Volume' column does not exist in the data. Check CSV file for errors.")

# Set Date as index
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

# Visualize trends
plt.figure(figsize=(12, 6))
sns.lineplot(x=data.index, y=data['Volume'])
plt.title("Volume Trends Over Time")
plt.xlabel("Date")
plt.ylabel("Volume")
plt.grid(True)
plt.show()


# In[21]:


import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('google.csv')

# Debugging: Inspect available columns
print("Columns in the DataFrame:")
print(data.columns)

# Strip any accidental spaces in column names
data.columns = data.columns.str.strip()

# Reset index if Date is already set as index
if 'Date' in data.columns:
    data['Date'] = pd.to_datetime(data['Date'])  # Ensure dates are properly formatted
else:
    print("The 'Date' column does not exist. Double-check your input file.")

# Debugging check after cleaning
print("Columns after cleaning:")
print(data.columns)

# Proceed with calculations and plotting
plt.figure(figsize=(14, 7))
plt.plot(data['Date'], data['Close'], label='Close Price', alpha=0.7)
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
data['50_MA'] = data['Close'].rolling(window=50).mean()
data['200_MA'] = data['Close'].rolling(window=200).mean()
plt.title('Close Price Over Time')
plt.grid(True)
plt.show()


# In[ ]:




