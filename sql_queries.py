# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

# fact table
#songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
songplay_table_create = "CREATE TABLE IF NOT EXISTS \
    songplays  (songplay_id int, start_time time, user_id int,\
         level varchar, song_id int, artist_id varchar, session_id varchar,\
              location varchar, user_agent varchar);"

# dimension tables

#user_id, first_name, last_name, gender, level
user_table_create = "CREATE TABLE IF NOT EXISTS \
    users  (user_id int, first_name varchar, last_name varchar,\
         gender varchar, level varchar);"

#song_id, title, artist_id, year, duration
song_table_create = "CREATE TABLE IF NOT EXISTS \
    songs (song_id varchar, title varchar, artist_id varchar, year int, duration numeric);"

#artist_id, name, location, latitude, longitude
artist_table_create = "CREATE TABLE IF NOT EXISTS \
 artists (artist_id varchar, name varchar, location varchar, \
     latitude numeric, longitude numeric);"

#start_time, hour, day, week, month, year, weekday
time_table_create = "CREATE TABLE IF NOT EXISTS time \
    (start_time time, hour varchar, day varchar, week varchar,\
         month varchar, year int, weekday varchar);"

# # INSERT RECORDS

# songplay_table_insert = ("""
# """)

# user_table_insert = ("""
# """)

song_table_insert = "INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s);"

artist_table_insert = "INSERT INTO artists (artist_id, name , location, latitude, longitude) VALUES (%s, %s, %s, %s, %s);"


# time_table_insert = ("""
# """)

# # FIND SONGS

# song_select = ("""
# """)

# QUERY LISTS

# my test
# create_table_queries = [songplay_table_create]
# drop_table_queries = [songplay_table_drop]

create_table_queries = [songplay_table_create, user_table_create,
                        song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop,
                      song_table_drop, artist_table_drop, time_table_drop]
