# The data is in the form of a csv file.
# There are 10 csv files. Storing them in a database would be better.
# Make sure there is no other 'f1.db' in data folder

# Importing libraries
import pandas as pd
import sqlite3

conn = sqlite3.connect("data/f1.db")

# Reading .csv files and storing them as a dataframe
circuits_df = pd.read_csv('data/circuits.csv')
constructors_df = pd.read_csv('data/constructors.csv')
construstors_results_df = pd.read_csv('data/constructor_results.csv')
constructors_standings_df = pd.read_csv('data/constructor_standings.csv')
drivers_df = pd.read_csv('data/drivers.csv')
drivers_standings_df = pd.read_csv('data/driver_standings.csv')
lap_times_df = pd.read_csv('data/lap_times.csv')
pit_stops_df = pd.read_csv('data/pit_stops.csv')
qualifying_df = pd.read_csv('data/qualifying.csv')
races_df = pd.read_csv('data/races.csv')
results_df = pd.read_csv('data/results.csv')
seasons_df = pd.read_csv('data/seasons.csv')

# Inserting these dataframes into f1.db
circuits_df.to_sql("circuits", conn)
constructors_df.to_sql("constructors", conn)
construstors_results_df.to_sql("constructor_results", conn)
constructors_standings_df.to_sql("constructor_standings", conn)
drivers_df.to_sql("drivers", conn)
drivers_standings_df.to_sql("driver_standings", conn)
lap_times_df.to_sql("lap_times", conn)
pit_stops_df.to_sql("pit_stops", conn)
qualifying_df.to_sql("qualifying", conn)
races_df.to_sql("races", conn)
results_df.to_sql("results", conn)
seasons_df.to_sql("seasons", conn)

conn.close()
