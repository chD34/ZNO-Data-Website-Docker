INSERT INTO person_subject_eo(
  out_id,
  subject_name,
  eo_name,
  ball,
  ball_12,
  ball_100,
  status,
  lang,
  dpa_level,
  adapt_scale,
  pt_name,
  pt_reg,
  pt_area,
  pt_ter,
  year)
SELECT out_id, ukr_test, eo_name, ukr_ball, ukr_ball_12, ukr_ball_100, ukr_status, NULL, NULL,
ukr_adapt_scale, ukr_pt_name, ukr_pt_reg, ukr_pt_area, ukr_pt_ter, year FROM public.zno
WHERE ukr_test IS NOT NULL;

INSERT INTO person_subject_eo(
  out_id,
  subject_name,
  eo_name,
  ball,
  ball_12,
  ball_100,
  status,
  lang,
  dpa_level,
  adapt_scale,
  pt_name,
  pt_reg,
  pt_area,
  pt_ter,
  year)
SELECT out_id, uml_test, eo_name, uml_ball, uml_ball_12, uml_ball_100, uml_status, NULL, NULL,
uml_adapt_scale, uml_pt_name, uml_pt_reg, uml_pt_area, uml_pt_ter, year FROM public.zno
WHERE uml_test IS NOT NULL;

INSERT INTO person_subject_eo(
  out_id,
  subject_name,
  eo_name,
  ball,
  ball_12,
  ball_100,
  status,
  lang,
  dpa_level,
  adapt_scale,
  pt_name,
  pt_reg,
  pt_area,
  pt_ter,
  year)
SELECT out_id, hist_test, eo_name, hist_ball, hist_ball_12, hist_ball_100, hist_status, hist_lang, NULL,
NULL, hist_pt_name, hist_pt_reg, hist_pt_area, hist_pt_ter, year FROM public.zno
WHERE hist_test IS NOT NULL;

INSERT INTO person_subject_eo(
  out_id,
  subject_name,
  eo_name,
  ball,
  ball_12,
  ball_100,
  status,
  lang,
  dpa_level,
  adapt_scale,
  pt_name,
  pt_reg,
  pt_area,
  pt_ter,
  year)
SELECT out_id, math_test, eo_name, math_ball, math_ball_12, math_ball_100, math_status, math_lang, NULL,
NULL, math_pt_name, math_pt_reg, math_pt_area, math_pt_ter, year FROM public.zno
WHERE math_test IS NOT NULL;


INSERT INTO person_subject_eo(
  out_id,
  subject_name,
  eo_name,
  ball,
  ball_12,
  ball_100,
  status,
  lang,
  dpa_level,
  adapt_scale,
  pt_name,
  pt_reg,
  pt_area,
  pt_ter,
  year)
SELECT out_id, physics_test, eo_name, physics_ball, physics_ball_12, physics_ball_100, physics_status, physics_lang, NULL,
NULL, physics_pt_name, physics_pt_reg, physics_pt_area, physics_pt_ter, year FROM public.zno
WHERE physics_test IS NOT NULL;


INSERT INTO person_subject_eo(
  out_id,
  subject_name,
  eo_name,
  ball,
  ball_12,
  ball_100,
  status,
  lang,
  dpa_level,
  adapt_scale,
  pt_name,
  pt_reg,
  pt_area,
  pt_ter,
  year)
SELECT out_id, chem_test, eo_name, chem_ball, chem_ball_12, chem_ball_100, chem_status, chem_lang, NULL,
NULL, chem_pt_name, chem_pt_reg, chem_pt_area, chem_pt_ter, year FROM public.zno
WHERE chem_test IS NOT NULL;

INSERT INTO person_subject_eo(
  out_id,
  subject_name,
  eo_name,
  ball,
  ball_12,
  ball_100,
  status,
  lang,
  dpa_level,
  adapt_scale,
  pt_name,
  pt_reg,
  pt_area,
  pt_ter,
  year)
SELECT out_id, bio_test, eo_name, bio_ball, bio_ball_12, bio_ball_100, bio_status, bio_lang, NULL,
NULL, bio_pt_name, bio_pt_reg, bio_pt_area, bio_pt_ter, year FROM public.zno
WHERE bio_test IS NOT NULL;

INSERT INTO person_subject_eo(
  out_id,
  subject_name,
  eo_name,
  ball,
  ball_12,
  ball_100,
  status,
  lang,
  dpa_level,
  adapt_scale,
  pt_name,
  pt_reg,
  pt_area,
  pt_ter,
  year)
SELECT out_id, geo_test, eo_name, geo_ball, geo_ball_12, geo_ball_100, geo_status, geo_lang, NULL,
NULL, geo_pt_name, geo_pt_reg, geo_pt_area, geo_pt_ter, year FROM public.zno
WHERE geo_test IS NOT NULL;

INSERT INTO person_subject_eo(
  out_id,
  subject_name,
  eo_name,
  ball,
  ball_12,
  ball_100,
  status,
  lang,
  dpa_level,
  adapt_scale,
  pt_name,
  pt_reg,
  pt_area,
  pt_ter,
  year)
SELECT out_id, eng_test, eo_name, eng_ball, eng_ball_12, eng_ball_100, eng_status, eng_lang, eng_dpa_level,
NULL, eng_pt_name, eng_pt_reg, eng_pt_area, eng_pt_ter, year FROM public.zno
WHERE eng_test IS NOT NULL;

INSERT INTO person_subject_eo(
  out_id,
  subject_name,
  eo_name,
  ball,
  ball_12,
  ball_100,
  status,
  lang,
  dpa_level,
  adapt_scale,
  pt_name,
  pt_reg,
  pt_area,
  pt_ter,
  year)
SELECT out_id, fra_test, eo_name, fra_ball, fra_ball_12, fra_ball_100, fra_status, fra_lang, fra_dpa_level,
NULL, fra_pt_name, fra_pt_reg, fra_pt_area, fra_pt_ter, year FROM public.zno
WHERE fra_test IS NOT NULL;

INSERT INTO person_subject_eo(
  out_id,
  subject_name,
  eo_name,
  ball,
  ball_12,
  ball_100,
  status,
  lang,
  dpa_level,
  adapt_scale,
  pt_name,
  pt_reg,
  pt_area,
  pt_ter,
  year)
SELECT out_id, deu_test, eo_name, deu_ball, deu_ball_12, deu_ball_100, deu_status, deu_lang, deu_dpa_level,
NULL, deu_pt_name, deu_pt_reg, deu_pt_area, deu_pt_ter, year FROM public.zno
WHERE deu_test IS NOT NULL;

INSERT INTO person_subject_eo(
  out_id,
  subject_name,
  eo_name,
  ball,
  ball_12,
  ball_100,
  status,
  lang,
  dpa_level,
  adapt_scale,
  pt_name,
  pt_reg,
  pt_area,
  pt_ter,
  year)
SELECT out_id, spa_test, eo_name, spa_ball, spa_ball_12, spa_ball_100, spa_status, spa_lang, spa_dpa_level,
NULL, spa_pt_name, spa_pt_reg, spa_pt_area, spa_pt_ter, year FROM public.zno
WHERE spa_test IS NOT NULL;