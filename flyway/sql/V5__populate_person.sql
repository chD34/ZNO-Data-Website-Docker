INSERT INTO person
SELECT out_id, birth, sex, region, area_name, ter_name, reg_type_name, ter_type_name,
class_prof_name, class_lang_name, eo_name FROM public.zno ON CONFLICT DO NOTHING;