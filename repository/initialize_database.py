from repository.database import create_data_base_if_not_exists, session_factory
from repository.query import *
from model import Mission
from config.base import Base, engine
import pandas as pd


def load_missions_to_db():
    with session_factory() as session:
        csv_file_path = "C:\\Users\\1\\PycharmProjects\\ww2\\assets\\operations.csv"
        data = pd.read_csv(csv_file_path, low_memory=False)
        data = data.fillna(0)
        for _, row in data.iterrows():
            mission = Mission(
                mission_id=row['Mission ID'],
                mission_date=row['Mission Date'],
                theater_of_operations=row['Theater of Operations'],
                country=row['Country'],
                air_force=row['Air Force'],
                unit_id=row['Unit ID'],
                aircraft_series=row['Aircraft Series'],
                callsign=row['Callsign'],
                mission_type=row['Mission Type'],
                takeoff_base=row['Takeoff Base'],
                takeoff_location=row['Takeoff Location'],
                takeoff_latitude=row['Takeoff Latitude'],
                takeoff_longitude=row['Takeoff Longitude'],
                target_id=row['Target ID'],
                target_country=row['Target Country'],
                target_city=row['Target City'],
                target_type=row['Target Type'],
                target_industry=row['Target Industry'],
                target_priority=row['Target Priority'],
                target_latitude=row['Target Latitude'],
                target_longitude=row['Target Longitude'],
                altitude_hundreds_of_feet=row['Altitude (Hundreds of Feet)'],
                airborne_aircraft=row['Airborne Aircraft'],
                attacking_aircraft=row['Attacking Aircraft'],
                bombing_aircraft=row['Bombing Aircraft'],
                aircraft_returned=row['Aircraft Returned'],
                aircraft_failed=row['Aircraft Failed'],
                aircraft_damaged=row['Aircraft Damaged'],
                aircraft_lost=row['Aircraft Lost'],
                high_explosives=row['High Explosives'],
                high_explosives_type=row['High Explosives Type'],
                high_explosives_weight_pounds=row['High Explosives Weight (Pounds)'],
                high_explosives_weight_tons=row['High Explosives Weight (Tons)'],
                incendiary_devices=row['Incendiary Devices'],
                incendiary_devices_type=row['Incendiary Devices Type'],
                incendiary_devices_weight_pounds=row['Incendiary Devices Weight (Pounds)'],
                incendiary_devices_weight_tons=row['Incendiary Devices Weight (Tons)'],
                fragmentation_devices=row['Fragmentation Devices'],
                fragmentation_devices_type=row['Fragmentation Devices Type'],
                fragmentation_devices_weight_pounds=row['Fragmentation Devices Weight (Pounds)'],
                fragmentation_devices_weight_tons=row['Fragmentation Devices Weight (Tons)'],
                total_weight_pounds=row['Total Weight (Pounds)'],
                total_weight_tons=row['Total Weight (Tons)'],
                time_over_target=row['Time Over Target'],
                bomb_damage_assessment=row['Bomb Damage Assessment'],
                source_id=row['Source ID']
            )
            session.add(mission)
        session.commit()


def create_tabels_if_not_exists():
    Base.metadata.create_all(engine)


def transfer_info_into_normalized_db():
    with session_factory() as session:
        session.execute(normalize_countries_query)
        session.execute(normalize_locations_query)
        session.execute(normalize_types_query)
        session.execute(normalize_targets_query)
        session.commit()


def initialize_db():
    create_data_base_if_not_exists()
    create_tabels_if_not_exists()
    load_missions_to_db()
    transfer_info_into_normalized_db()
