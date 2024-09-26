from sqlalchemy import text


normalize_countries_query = text("""
                                insert into country (country)
                                select distinct target_country
                                FROM mission
                                where target_country is not NULL
                                on conflict (country) do nothing;
                                """)


normalize_locations_query = text("""
                                insert into location (city, country_id, lat, lon)
                                select distinct
                                m.target_city,
                                c.id,
                                m.target_latitude::decimal,
                                m.target_longitude::decimal
                                from mission m
                                join country c on m.target_country = c.country
                                where m.target_city is not null
                                on conflict (city) do nothing;
                                """)

normalize_types_query = text("""
                                insert into type (type)
                                select distinct target_type
                                from mission
                                where target_type is not null
                                on conflict (type) do nothing;
                                select * from type
                                """)


normalize_targets_query = text("""
                        INSERT INTO target (priority, location_id, type_id)
                        SELECT DISTINCT
                        m.target_priority,
                        l.id,
                        t.id
                        FROM mission m
                        JOIN location l ON m.target_city = l.city
                        LEFT JOIN type t ON m.target_type = t.type
                        ON CONFLICT (priority, location_id, type_id) DO NOTHING;
                        """)


