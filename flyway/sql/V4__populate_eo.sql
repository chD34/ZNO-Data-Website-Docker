INSERT INTO eo SELECT eo_name, eo_type_name, eo_reg_name, eo_area_name, eo_ter_name, eo_parent
FROM zno WHERE eo_name IS NOT NULL ON CONFLICT DO NOTHING;
