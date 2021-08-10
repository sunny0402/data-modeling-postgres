## Introduction

    The purpose of this project is help a startup, Sparkify!
    They need to analyze the data collected on songs and user activity via their music streaming app.

    The result will be  an ETL pipeline and Postgres database optimized for queries on song play analysis.

## Database Schema

# Fact Table

- songplays - records in log data associated with song plays
- Columns: songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

# Dimension Tables

- users - users in the app
- Columns: user_id, first_name, last_name, gender, level

- songs - songs in music database
- Columns: song_id, title, artist_id, year, duration

- artists - artists in music database
- Columns: artist_id, name, location, latitude, longitude

- time - timestamps of records in songplays
- Columns: start_time, hour, day, week, month, year, weekday

## Repository Files

- create_tables.py: drops and creates tables
- etl.ipynb: explanation of the ETL process.
- etl.py: reads and processes files from song_data and log_data and loads them into tables
- sql_queries.py: contains all necessary sql queries
- test.ipynb: displays the first few rows of each table

## Local Set Up

pip install psycopg2
pip install pandas

After complete sql_queries.py
py create_tables.py

To run test.ipynb
pip install ipython-sql --user

To manage postgres use TablePlus

On Windows restart can restart PostgreSQL Server 13 if connection not closed.

## TODO

Insert data using the COPY command to bulk insert log files instead of using INSERT on one row at a time
Add data quality checks
Create a dashboard for analytic queries on your new database
