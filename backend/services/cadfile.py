from database import insert_cad_file_into_db, insert_cad_address_into_database, insert_cad_apparatus_into_database, insert_cad_unitstatus_into_db, insert_cad_description_into_db, insert_cad_firedepartment_into_database


def upload_cad_file(cad_file_data):

    # Every CAD File Sent from the client
    for file in cad_file_data:
        CADFILE_ID = insert_cad_file_into_db(file['filename'], file['version'])

        cadfile_address = file['address']
        cadfile_description = file['description']
        cadfile_firedepartment = file['fire_department']

        # Address
        insert_cad_address_into_database(
            CADFILE_ID=CADFILE_ID,
            address_id=cadfile_address.get('address_id', ''),
            address_line1=cadfile_address.get('address_line1', ''),
            city=cadfile_address.get('city', ''),
            common_place_name=cadfile_address.get('common_place_name', ''),
            cross_street1=cadfile_address.get('cross_street1', ''),
            cross_street2=cadfile_address.get('cross_street2', ''),
            first_due=cadfile_address.get('first_due', ''),
            geohash=cadfile_address.get('geohash', ''),
            latitude=cadfile_address.get('latitude', ''),
            longitude=cadfile_address.get('longitude', ''),
            name=cadfile_address.get('name', ''),
            number=cadfile_address.get('number', ''),
            postal_code=cadfile_address.get('postal_code', ''),
            prefix_direction=cadfile_address.get('prefix_direction', ''),
            response_zone=cadfile_address.get('response_zone', ''),
            state=cadfile_address.get('state', ''),
            suffix_direction=cadfile_address.get('suffix_direction', ''),
            type=cadfile_address.get('type', '')
        )

        # Description
        insert_cad_description_into_db(
            CADFILE_ID=CADFILE_ID,
            comments=cadfile_description.get('comments', ''),
            day_of_week=cadfile_description.get('day_of_week', ''),
            event_closed=cadfile_description.get('event_closed', ''),
            event_id=cadfile_description.get('event_id', ''),
            event_opened=cadfile_description.get('event_opened', ''),
            dispatch_duration=cadfile_description.get(
                'extended_data', {}).get('dispatch_duration', ''),
            event_duration=cadfile_description.get(
                'extended_data', {}).get('event_duration', ''),
            response_time=cadfile_description.get(
                'extended_data', {}).get('response_time', ''),
            first_unit_arrived=cadfile_description.get(
                'first_unit_arrived', ''),
            first_unit_dispatched=cadfile_description.get(
                'first_unit_dispatched', ''),
            first_unit_enroute=cadfile_description.get(
                'first_unit_enroute', ''),
            hour_of_day=cadfile_description.get('hour_of_day', ''),
            incident_number=cadfile_description.get('incident_number', ''),
            loi_search_complete=cadfile_description.get(
                'loi_search_complete', ''),
            subtype=cadfile_description.get('subtype', ''),
            type=cadfile_description.get('type', ''),
        )

        # Fire Department
        insert_cad_firedepartment_into_database(
            CADFILE_ID=CADFILE_ID,
            fd_id=cadfile_firedepartment.get('fd_id', ''),
            firecares_id=cadfile_firedepartment.get('firecares_id', ''),
            name=cadfile_firedepartment.get('name', ''),
            shift=cadfile_firedepartment.get('shift', ''),
            state=cadfile_firedepartment.get('state', ''),
            timezone=cadfile_firedepartment.get('timezone', '')
        )

        # All Apparatuses
        for apparatus in file['apparatus']:
            APPARATUS_ID = insert_cad_apparatus_into_database(
                CADFILE_ID=CADFILE_ID,
                car_id=apparatus.get('car_id', ''),
                distance=apparatus.get('distance', ''),
                event_duration=apparatus.get(
                    'extended_data', {}).get('event_duration', ''),
                response_duration=apparatus.get(
                    'extended_data', {}).get('response_duration', ''),
                travel_duration=apparatus.get(
                    'extended_data', {}).get('travel_duration', ''),
                turnout_duration=apparatus.get(
                    'extended_data', {}).get('turnout_duration', ''),
                geohash=apparatus.get('geohash', ''),
                personnel=apparatus.get('personnel', ''),
                shift=apparatus.get('shift', ''),
                station=apparatus.get('station', ''),
                unit_id=apparatus.get('unit_id', ''),
                unit_type=apparatus.get('unit_type', '')
            )

            # All Unit Statuses
            for key, value in enumerate(apparatus['unit_status']):
                insert_cad_unitstatus_into_db(
                    APPARATUS_ID=APPARATUS_ID,
                    type=value,
                    geohash=apparatus['unit_status'][value].get('geohash', ''),
                    latitude=apparatus['unit_status'][value].get(
                        'latitude', ''),
                    longitude=apparatus['unit_status'][value].get(
                        'longitude', ''),
                    timestamp=apparatus['unit_status'][value].get(
                        'timestamp', '')
                )
