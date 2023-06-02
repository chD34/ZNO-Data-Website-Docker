DROP TABLE IF EXISTS subject;
DROP TABLE IF EXISTS eo;
DROP TABLE IF EXISTS person;
DROP TABLE IF EXISTS person_subject_eo;


CREATE TABLE IF NOT EXISTS subject(
  subject_name char(100) PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS eo(
  eo_name char(300) PRIMARY KEY,
  eo_type_name char(100),
  eo_reg_name char(50),
  eo_area_name char(50),
  eo_ter_name char(50),
  eo_parent char(300)
);

CREATE TABLE IF NOT EXISTS person(
        out_id                    char(100) PRIMARY KEY,
        birth                     int,
        sex                       char(20),
        region                    char(100),
        area_name                 char(100),
        ter_name                  char(100),
        reg_type_name             char(300),
        ter_type_name             char(100),
        class_prof_name           char(100),
        class_lang_name           char(100),
        eo_name char(300),
  CONSTRAINT fk_person_eo
    FOREIGN KEY(eo_name)
    REFERENCES eo(eo_name)
);



CREATE TABLE IF NOT EXISTS person_subject_eo(
  out_id char(100),
  subject_name char(100),
  eo_name char(300),
  ball decimal(15, 2),
  ball_12 int,
  ball_100 decimal(15, 2),
  status char(50),
  lang char(50),
  dpa_level char(50),
  adapt_scale int,
  pt_name char(300),
  pt_reg char(50),
  pt_area char(50),
  pt_ter char(50),
  year int,
  PRIMARY KEY(out_id, subject_name),
  CONSTRAINT fk_person_subject_eo__subject
    FOREIGN KEY(subject_name)
    REFERENCES subject(subject_name),
  CONSTRAINT fk_person_subject_eo__person
    FOREIGN KEY(out_id)
    REFERENCES person(out_id),
  CONSTRAINT fk_person_subject_eo__eo
    FOREIGN KEY(eo_name)
    REFERENCES eo(eo_name)
);