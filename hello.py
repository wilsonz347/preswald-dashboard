from preswald import connect, get_df
import os
from preswald import query
from preswald import table, text
from preswald import plotly
import plotly.express as px

connect()  
df = get_df("seattle_weather") 

# Check for dir
print("Working directory:", os.getcwd())

# SQL Query
sql = """
SELECT * FROM seattle_weather 
WHERE precipitation > 5 AND weather IN ('rain', 'snow')"""
filtered_df = query(sql, "seattle_weather")

# UI
text("# Seattle Weather Dashboard")
table(filtered_df, title="Heavy Rain/Snow Days")

# Data Visualization
fig = px.scatter(df, x="temp_max", y="wind", color="weather", size="precipitation",
    title="Max Temperature vs Wind Speed (by Weather Condition)",
    labels={
        "temp_max": "Max Temp (°C)",
        "wind": "Wind Speed (m/s)",
        "precipitation": "Precipitation (mm)",
        "weather": "Condition"
    }
)
plotly(fig)