from database import get_db

'''
Returns primary key for a CAD file upload
'''
def insert_cad_file_into_db(fileName, version):

    sql = f'''
    INSERT INTO cadfile_upload 
    (
    fileName,
    version
    ) VALUES 
    ('{fileName}', '{version}') RETURNING ID;
    '''.format(fileName=fileName, version=version)

    db = get_db()
    returned_id = db.execute(sql).fetchone()['id']
    db.commit()
    return returned_id

def insert_cad_address_into_database(
            CADFILE_ID,
            address_id, 
            address_line1, 
            city, 
            common_place_name, 
            cross_street1, 
            cross_street2, 
            first_due, 
            geohash, 
            latitude, 
            longitude, 
            name, 
            number, 
            postal_code, 
            prefix_direction, 
            response_zone, 
            state, 
            suffix_direction, 
            type
        ):

    sql = f'''
    INSERT INTO cadfile_address 
    (
        CADFILE_ID,
        address_id,
        address_line1,
        city,
        common_place_name,
        cross_street1,
        cross_street2,
        first_due,
        geohash,
        latitude,
        longitude,
        name,
        number,
        postal_code,
        prefix_direction,
        response_zone,
        state,
        suffix_direction,
        type
        )
        VALUES (
            '{CADFILE_ID}',
            '{address_id}',
            '{address_line1}',
            '{city}',
            '{common_place_name}',
            '{cross_street1}',
            '{cross_street2}',
            '{first_due}',
            '{geohash}',
            '{latitude}',
            '{longitude}',
            '{name}',
            '{number}',
            '{postal_code}',
            '{prefix_direction}',
            '{response_zone}',
            '{state}',
            '{suffix_direction}',
            '{type}'
        );
    '''.format(
        CADFILE_ID=CADFILE_ID,
        address_id=address_id, 
        address_line1=address_line1, 
        city=city, 
        common_place_name=common_place_name, 
        cross_street1=cross_street1, 
        cross_street2=cross_street2, 
        first_due=first_due, 
        geohash=geohash, 
        latitude=latitude, 
        longitude=longitude, 
        name=name, 
        number=number, 
        postal_code=postal_code, 
        prefix_direction=prefix_direction, 
        response_zone=response_zone, 
        state=state, 
        suffix_direction=suffix_direction, 
        type=type)

    db = get_db()
    db.execute(sql)
    db.commit()
    return True

def insert_cad_firedepartment_into_database(
            CADFILE_ID,
            fd_id,
            firecares_id,
            name,
            shift,
            state,
            timezone
        ):

    sql = f'''
   INSERT INTO cadfile_firedepartment 
   (
        CADFILE_ID,
        fd_id,
        firecares_id,
        name,
        shift,
        state,
        timezone
    )
    VALUES (
        '{CADFILE_ID}',
        '{fd_id}',
        '{firecares_id}',
        '{name}',
        '{shift}',
        '{state}',
        '{timezone}'
    );
    '''.format(
        CADFILE_ID=CADFILE_ID,
        fd_id=fd_id,
        firecares_id=firecares_id,
        name=name,
        shift=shift,
        state=state,
        timezone=timezone)

    db = get_db()
    db.execute(sql)
    db.commit()
    return True


def insert_cad_description_into_db(
            CADFILE_ID,
            comments,
            day_of_week,
            event_closed,
            event_id,
            event_opened,
            dispatch_duration,
            event_duration,
            response_time,
            first_unit_arrived,
            first_unit_dispatched,
            first_unit_enroute,
            hour_of_day,
            incident_number,
            loi_search_complete,
            subtype,
            type
        ):

    sql = f'''
    INSERT INTO cadfile_description 
    (
        CADFILE_ID,
        comments,
        day_of_week,
        event_closed,
        event_id,
        event_opened,
        dispatch_duration,
        event_duration,
        response_time,
        first_unit_arrived,
        first_unit_dispatched,
        first_unit_enroute,
        hour_of_day,
        incident_number,
        loi_search_complete,
        subtype,
        type
    )
    VALUES (
        '{CADFILE_ID}',
        '{comments}',
        '{day_of_week}',
        '{event_closed}',
        '{event_id}',
        '{event_opened}',
        '{dispatch_duration}',
        '{event_duration}',
        '{response_time}',
        '{first_unit_arrived}',
        '{first_unit_dispatched}',
        '{first_unit_enroute}',
        '{hour_of_day}',
        '{incident_number}',
        '{loi_search_complete}',
        '{subtype}',
        '{type}'
    );
    '''.format(
        CADFILE_ID=CADFILE_ID,
        comments=comments,
        day_of_week=day_of_week,
        event_closed=event_closed,
        event_id=event_id,
        event_opened=event_opened,
        dispatch_duration=dispatch_duration,
        event_duration=event_duration,
        response_time=response_time,
        first_unit_arrived=first_unit_arrived,
        first_unit_dispatched=first_unit_dispatched,
        first_unit_enroute=first_unit_enroute,
        hour_of_day=hour_of_day,
        incident_number=incident_number,
        loi_search_complete=loi_search_complete,
        subtype=subtype,
        type=type
    )

    db = get_db()
    db.execute(sql)
    db.commit()
    return True

'''
Returns primary key for a cad apparatus
'''
def insert_cad_apparatus_into_database(
            CADFILE_ID,
            car_id,
            distance,
            event_duration,
            response_duration,
            travel_duration,
            turnout_duration,
            geohash,
            personnel,
            shift,
            station,
            unit_id,
            unit_type
        ):

    sql = f'''
   INSERT INTO cadfile_apparatus 
   (
    CADFILE_ID,
    car_id,
    distance,
    event_duration,
    response_duration,
    travel_duration,
    turnout_duration,
    geohash,
    personnel,
    shift,
    station,
    unit_id,
    unit_type
    )
    VALUES (
        '{CADFILE_ID}',
        '{car_id}',
        '{distance}',
        '{event_duration}',
        '{response_duration}',
        '{travel_duration}',
        '{turnout_duration}',
        '{geohash}',
        '{personnel}',
        '{shift}',
        '{station}',
        '{unit_id}',
        '{unit_type}'
    ) RETURNING ID;
    '''.format(
        CADFILE_ID=CADFILE_ID,
        car_id=car_id,
        distance=distance,
        event_duration=event_duration,
        response_duration=response_duration,
        travel_duration=travel_duration,
        turnout_duration=turnout_duration,
        geohash=geohash,
        personnel=personnel,
        shift=shift,
        station=station,
        unit_id=unit_id,
        unit_type=unit_type,
        )

    db = get_db()
    returned_id = db.execute(sql).fetchone()['id']
    db.commit()
    return returned_id

def insert_cad_unitstatus_into_db(
            APPARATUS_ID,
            type,
            geohash,
            latitude,
            longitude,
            timestamp
        ):

    sql = f'''
    INSERT INTO cadfile_unitstatus (
        APPARATUS_ID,
        type,
        geohash,
        latitude,
        longitude,
        timestamp
    )
    VALUES (
        '{APPARATUS_ID}',
        '{type}',
        '{geohash}',
        '{latitude}',
        '{longitude}',
        '{timestamp}'
    );
    '''.format(
    APPARATUS_ID=APPARATUS_ID,
    type=type,
    geohash=geohash,
    latitude=latitude,
    longitude=longitude,
    timestamp=timestamp
    )

    db = get_db()
    db.execute(sql)
    db.commit()
    return True