INSERT INTO subject(subject_name)
SELECT ukr_test FROM public.zno WHERE ukr_test IS NOT NULL AND ukr_test='Українська мова' LIMIT 1;

INSERT INTO subject(subject_name)
SELECT uml_test FROM public.zno WHERE uml_test IS NOT NULL LIMIT 1;

INSERT INTO subject(subject_name)
SELECT hist_test FROM public.zno WHERE hist_test IS NOT NULL LIMIT 1;

INSERT INTO subject(subject_name)
SELECT DISTINCT(math_test) FROM public.zno WHERE math_test IS NOT NULL;

INSERT INTO subject(subject_name)
SELECT physics_test FROM public.zno WHERE physics_test IS NOT NULL LIMIT 1;

INSERT INTO subject(subject_name)
SELECT chem_test FROM public.zno WHERE chem_test IS NOT NULL LIMIT 1;

INSERT INTO subject(subject_name)
SELECT bio_test FROM public.zno WHERE bio_test IS NOT NULL LIMIT 1;

INSERT INTO subject(subject_name)
SELECT geo_test FROM public.zno WHERE geo_test IS NOT NULL LIMIT 1;

INSERT INTO subject(subject_name)
SELECT eng_test FROM public.zno WHERE eng_test IS NOT NULL LIMIT 1;

INSERT INTO subject(subject_name)
SELECT fra_test FROM public.zno WHERE fra_test IS NOT NULL LIMIT 1;

INSERT INTO subject(subject_name)
SELECT deu_test FROM public.zno WHERE deu_test IS NOT NULL LIMIT 1;

INSERT INTO subject(subject_name)
SELECT spa_test FROM public.zno WHERE spa_test IS NOT NULL LIMIT 1;