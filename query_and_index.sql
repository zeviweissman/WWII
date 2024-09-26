select count(*), air_force, target_city from mission
where air_force != '0'
and split_part(mission_date, '-', 1) = '1945'
and target_city != '0'
group by air_force, target_city
ORDER BY count DESC
LIMIT 1;





create index idx_air_force on mission(air_force);
create index idx_mission_date on mission(split_part(mission_date, '-', 1));
create index idx_target_city on mission(target_city);



explain analyze
select count(*), air_force, target_city from mission
where air_force != '0'
and split_part(mission_date, '-', 1) = '1945'
and target_city is not null
group by air_force, target_city
ORDER BY count DESC
LIMIT 1;


drop index if exists idx_air_force;
drop index if exists idx_mission_date;
drop index if exists idx_target_city;






select Count(*) total_times_appeared, target_country, bomb_damage_assessment
from mission
where airborne_aircraft::INTEGER + attacking_aircraft + bombing_aircraft  > 5 
and bomb_damage_assessment != '0'
group by bomb_damage_assessment, target_country
order by total_times_appeared DESC
limit 1;


create index idx_total_aircrafts on mission((airborne_aircraft::INTEGER + attacking_aircraft + bombing_aircraft));
create index idx_bomb_damage_assessment on mission(bomb_damage_assessment);



explain analyze
select Count(*) total_times_appeared, target_country, bomb_damage_assessment
from mission
where airborne_aircraft::INTEGER + attacking_aircraft + bombing_aircraft  > 5 
and bomb_damage_assessment != '0'
group by bomb_damage_assessment, target_country
order by total_times_appeared DESC
limit 1;


drop index if exists idx_total_aircrafts;
drop index if exists idx_bomb_damage_assessment;

