# Analysis of Formula 1 history
# Make sure to run load_db.py to generate database

# Importing libraries
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
fig = plt.figure(figsize=(20, 7))

conn = sqlite3.connect('data/f1.db')

# Top 10 circuits which hosted the maximum number of races
cir_max = pd.read_sql(
    'SELECT c.location AS "City",COUNT(r.circuitid) AS "Races Hosted" FROM circuits c,races r WHERE r.circuitid=c.circuitid GROUP BY City ORDER BY "Races Hosted" DESC LIMIT 10;', conn)

plt.bar(data=cir_max, x="City", height="Races Hosted", color='#FF6D00')
plt.ylabel("Races Hosted")
plt.xlabel("City")
plt.title("Cities hosting maximum races")
fig.savefig('imgs/circuits_hosted_max.svg', format='svg', dpi=1200)

# Top 10 circuits that have maximum season opening races
op_circ = pd.read_sql('SELECT r.name AS "Grand Prix Name",c.name AS "Circuit Name",c.location AS "City",c.country AS "Country",COUNT(*) AS "Opening Races Hosted" FROM circuits c,races r WHERE r.circuitid=c.circuitid AND r.round=1 GROUP BY City ORDER BY "Opening Races Hosted" DESC LIMIT 10;', conn)
plt.bar(data=op_circ, x="City", height="Opening Races Hosted", color='#FF6D00')
plt.ylabel("Opening Races Hosted")
plt.xlabel("City")
plt.title("Cities with maximum season opening races")
fig.savefig('imgs/max_op_circs.svg', format='svg', dpi=1200)

# Construstures with most points throughout f1
const = pd.read_sql('SELECT const.name AS "Constructors",const.nationality AS "Nationality",SUM(r.points) AS "Total Points" FROM constructors const,constructor_results r WHERE const.constructorId=r.constructorId GROUP BY Constructors ORDER BY "Total Points" DESC LIMIT 10;', conn)
plt.bar(data=const, x="Constructors", height="Total Points", color='#FF6D00')
plt.ylabel("Total Points")
plt.xlabel("Constructors")
plt.title("Constructors with most points throughout f1")
fig.savefig('imgs/most_points_const.svg', format='svg', dpi=1200)

# Number of races organized per season
ra_season = pd.read_sql(
    'SELECT strftime("%Y","date") AS "Year",COUNT(*) as "Races Held" FROM races GROUP BY Year Having Year>=2000 ORDER BY Year;', conn)
plt.plot(ra_season['Year'], ra_season['Races Held'], color='#FF6D00')
plt.ylabel("Races Held")
plt.xlabel("Year")
fig.savefig('imgs/num_races_per_year.svg', format='svg', dpi=1200)

# Drivers with most GP wins
rawd_top = pd.read_sql('SELECT ("forename" || " " || "surname") AS "Name", COUNT(r.driverId) AS "Races Won" FROM drivers d, results r WHERE r.driverId = d.driverId AND r.position = 1 GROUP BY "Name" ORDER BY "Races Won" DESC LIMIT 10;', conn)
plt.bar(data=rawd_top, x="Name", height="Races Won", color='#FF6D00')
plt.ylabel("Races won")
plt.xlabel("Name")
plt.title("Drivers with most wins throughout f1")
fig.savefig('imgs/most_wins_driv.svg', format='svg', dpi=1200)

conn.close()
