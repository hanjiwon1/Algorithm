/*
중성화
Spayed Female
Neutered Male

중성화 ㄴ
Intact Male
Intact Female
*/

select ai.animal_id, ai.animal_type, ai.name
from (SELECT * from animal_ins where sex_upon_intake LIKE 'Intact%') as ai, animal_outs as ao
where ai.animal_id = ao.animal_id and (ao.sex_upon_outcome LIKE 'Spayed%' or ao.sex_upon_outcome LIKE 'Neutered%')
order by ai.animal_id;