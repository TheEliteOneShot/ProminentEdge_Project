CREATE TABLE IF NOT EXISTS cadfile_upload
(
[ID] INTEGER PRIMARY KEY,
[fileName] TEXT,
[version] TEXT,
[uploaded_dt] DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS cadfile_address
(
[ID] INTEGER PRIMARY KEY, 
[CADFILE_ID] INTEGER,
[address_id] TEXT,
[address_line1] TEXT,
[city] TEXT,
[common_place_name] TEXT,
[cross_street1] TEXT,
[cross_street2] TEXT,
[first_due] TEXT,
[geohash] TEXT,
[latitude] TEXT,
[longitude] TEXT,
[name] TEXT,
[number] TEXT,
[postal_code] TEXT,
[prefix_direction] TEXT,
[response_zone] TEXT,
[state] TEXT,
[suffix_direction] TEXT,
[type] TEXT
);

CREATE TABLE IF NOT EXISTS cadfile_apparatus
(
[ID] INTEGER PRIMARY KEY, 
[CADFILE_ID] INTEGER,
[car_id] TEXT,
[distance] TEXT,
[event_duration] TEXT,
[response_duration] TEXT,
[travel_duration] TEXT,
[turnout_duration] TEXT,
[geohash] TEXT,
[personnel] TEXT,
[shift] TEXT,
[station] TEXT,
[unit_id] TEXT,
[unit_type] TEXT
);

CREATE TABLE IF NOT EXISTS cadfile_unitstatus
(
[ID] INTEGER PRIMARY KEY, 
[APPARATUS_ID] INTEGER,
[type] TEXT,
[geohash] TEXT,
[latitude] TEXT,
[longitude] TEXT,
[timestamp] TEXT
);

CREATE TABLE IF NOT EXISTS cadfile_description
(
[ID] INTEGER PRIMARY KEY, 
[CADFILE_ID] INTEGER,
[comments] TEXT,
[day_of_week] TEXT,
[event_closed] TEXT,
[event_id] TEXT,
[event_opened] TEXT,
[dispatch_duration] TEXT,
[event_duration] TEXT,
[response_time] TEXT,
[first_unit_arrived] TEXT,
[first_unit_dispatched] TEXT,
[first_unit_enroute] TEXT,
[hour_of_day] TEXT,
[incident_number] TEXT,
[loi_search_complete] TEXT,
[subtype] TEXT,
[type] TEXT
);

CREATE TABLE IF NOT EXISTS cadfile_firedepartment
(
[ID] INTEGER PRIMARY KEY, 
[CADFILE_ID] INTEGER,
[fd_id] TEXT,
[firecares_id] TEXT,
[name] TEXT,
[shift] TEXT,
[state] TEXT,
[timezone] TEXT
);