select ai.animal_id, ai.name
from animal_ins as ai, animal_outs as ao
where ai.animal_id = ao.animal_id and date_format(ai.datetime, '%Y-%m-%d %H:%i:%s') > date_format(ao.datetime, '%Y-%m-%d %H:%i:%s')
order by ai.datetime;
