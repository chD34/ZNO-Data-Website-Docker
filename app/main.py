import time
import psycopg2
import csv

conn = psycopg2.connect(dbname='postgres', user='postgres', password='postgres', host='db')
cursor = conn.cursor()

csv_zno_2019 = 'Odata2019File.csv'
csv_zno_2021 = 'Odata2021File.csv'

query1 = ''' INSERT INTO zno(out_id, birth, sex, region, area_name, ter_name, reg_type_name, ter_type_name,
        class_prof_name, class_lang_name, eo_name, eo_type_name, eo_reg_name, eo_area_name, eo_ter_name, 
        eo_parent, ukr_test, ukr_status, ukr_ball_100, ukr_ball_12, ukr_ball, ukr_adapt_scale, 
        ukr_pt_name, ukr_pt_reg, ukr_pt_area, ukr_pt_ter, hist_test, hist_lang, 
        hist_status, hist_ball_100, hist_ball_12, hist_ball, hist_pt_name, hist_pt_reg, hist_pt_area, 
        hist_pt_ter, math_test, math_lang, math_status, math_ball_100, math_ball_12, math_ball, math_pt_name, 
        math_pt_reg, math_pt_area, math_pt_ter, physics_test, physics_lang,physics_status, physics_ball_100, 
        physics_ball_12, physics_ball, physics_pt_name, physics_pt_reg, physics_pt_area, physics_pt_ter, 
        chem_test, chem_lang, chem_status, chem_ball_100, chem_ball_12, chem_ball, chem_pt_name, chem_pt_reg, 
        chem_pt_area, chem_pt_ter, bio_test, bio_lang, bio_status, bio_ball_100, bio_ball_12, bio_ball, 
        bio_pt_name, bio_pt_reg, bio_pt_area, bio_pt_ter, geo_test, geo_lang, geo_status, geo_ball_100, 
        geo_ball_12, geo_ball, geo_pt_name, geo_pt_reg, geo_pt_area, geo_pt_ter, eng_test, eng_status, 
        eng_ball_100, eng_ball_12, eng_dpa_level, eng_ball, eng_pt_name, eng_pt_reg, eng_pt_area, eng_pt_ter, fra_test, 
        fra_status, fra_ball_100, fra_ball_12, fra_dpa_level, fra_ball, fra_pt_name, fra_pt_reg, fra_pt_area, 
        fra_pt_ter, deu_test, deu_status, deu_ball_100, deu_ball_12, deu_dpa_level, deu_ball, deu_pt_name, 
        deu_pt_reg, deu_pt_area, deu_pt_ter, spa_test, spa_status, spa_ball_100, spa_ball_12, spa_dpa_level, 
        spa_ball, spa_pt_name, spa_pt_reg, spa_pt_area, spa_pt_ter, year) VALUES (%s, %s, %s, %s, %s, %s, 
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 2019)
'''

query2 = ''' INSERT INTO zno (out_id, birth, sex, region, area_name, ter_name, reg_type_name, ter_type_name,
        class_prof_name, class_lang_name, eo_name, eo_type_name, eo_reg_name, eo_area_name, eo_ter_name, 
        eo_parent, uml_test, uml_status, uml_ball_100, uml_ball_12, uml_ball, uml_adapt_scale, uml_pt_name, 
        uml_pt_reg, uml_pt_area, uml_pt_ter, ukr_test, ukr_sub_test, ukr_status, ukr_ball_100, ukr_ball_12, 
        ukr_ball, ukr_adapt_scale, ukr_pt_name, ukr_pt_reg, ukr_pt_area, ukr_pt_ter, 
        hist_test, hist_lang, hist_status, hist_ball_100, hist_ball_12, hist_ball, hist_pt_name, hist_pt_reg, 
        hist_pt_area, hist_pt_ter, math_test, math_lang, math_status, math_ball_100, math_ball_12, math_dpa_level, 
        math_ball, math_pt_name, math_pt_reg, math_pt_area, math_pt_ter, physics_test, physics_lang, physics_status, 
        physics_ball_100, physics_ball_12, physics_ball, physics_pt_name, physics_pt_reg, physics_pt_area, 
        physics_pt_ter, chem_test, chem_lang, chem_status, chem_ball_100, chem_ball_12, chem_ball, chem_pt_name, 
        chem_pt_reg, chem_pt_area, chem_pt_ter, bio_test, bio_lang, bio_status, bio_ball_100, bio_ball_12, bio_ball, 
        bio_pt_name, bio_pt_reg, bio_pt_area, bio_pt_ter, geo_test, geo_lang, geo_status, geo_ball_100, 
        geo_ball_12, geo_ball, geo_pt_name, geo_pt_reg, geo_pt_area, geo_pt_ter, eng_test, eng_status, 
        eng_ball_100, eng_ball_12, eng_dpa_level, eng_ball, eng_pt_name, eng_pt_reg, eng_pt_area, eng_pt_ter, fra_test, 
        fra_status, fra_ball_100, fra_ball_12, fra_dpa_level, fra_ball, fra_pt_name, fra_pt_reg, fra_pt_area, 
        fra_pt_ter, deu_test, deu_status, deu_ball_100, deu_ball_12, deu_dpa_level, deu_ball, deu_pt_name, 
        deu_pt_reg, deu_pt_area, deu_pt_ter, spa_test, spa_status, spa_ball_100, spa_ball_12, spa_dpa_level, 
        spa_ball, spa_pt_name, spa_pt_reg, spa_pt_area, spa_pt_ter, year) VALUES (%s, %s, %s, %s, %s, %s, 
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
        %s, %s, %s, %s, %s, %s, %s, 2021)
'''

query3 = """SELECT region, 
            MAX(math_ball_100) FILTER (WHERE math_status = 'Зараховано' and year=2019) as max_100_2019,
            MAX(math_ball_100) FILTER (WHERE math_status = 'Зараховано' and year=2021) as max_100_2021,
            MAX(math_ball) FILTER (WHERE math_status = 'Зараховано' and year=2019) as max_test_2019,
            MAX(math_ball) FILTER (WHERE math_status = 'Зараховано' and year=2021) as max_test_2021,
            MAX(math_ball_12) FILTER (WHERE math_status = 'Зараховано' and year=2019) as max_12_2019,
            MAX(math_ball_12) FILTER (WHERE math_status = 'Зараховано' and year=2021) as max_12_2021
            FROM zno
            GROUP BY region 
            ORDER BY region;"""

cursor.execute(
    """ CREATE TABLE IF NOT EXISTS zno(
        out_id                    char(100),
        birth                     int,
        sex                       char(20),
        region                    char(100),
        area_name                 char(100),
        ter_name                  char(100),
        reg_type_name             char(300),
        ter_type_name             char(100),
        class_prof_name           char(100),
        class_lang_name           char(100),
        eo_name                   char(300),
        eo_type_name              char(100),
        eo_reg_name               char(50),
        eo_area_name              char(50),
        eo_ter_name               char(50),
        eo_parent                 char(300),
        ukr_test                  char(50),
        ukr_sub_test              char(50),
        ukr_status                char(30),
        ukr_ball_100              decimal(15, 2),
        ukr_ball_12               int,
        ukr_ball                  decimal(15, 2),
        ukr_adapt_scale           int,
        ukr_pt_name               char(300),
        ukr_pt_reg                char(50),
        ukr_pt_area               char(50),
        ukr_pt_ter                char(50),
        uml_test                  char(50),
        uml_status                char(50),
        uml_ball_100              decimal(15, 2),
        uml_ball_12               int,
        uml_ball                  decimal(15, 2),
        uml_adapt_scale           int,
        uml_pt_name               char(300),
        uml_pt_reg                char(50),
        uml_pt_area               char(50),
        uml_pt_ter                char(50),
        hist_test                 char(50),
        hist_lang                 char(50),
        hist_status               char(50),
        hist_ball_100             decimal(15, 2),
        hist_ball_12              int,
        hist_ball                 decimal(15, 2),
        hist_pt_name              char(250),
        hist_pt_reg               char(50),
        hist_pt_area              char(50),
        hist_pt_ter               char(50),
        math_test                 char(50),
        math_lang                 char(50),
        math_status               char(50),
        math_ball_100             decimal(15, 2),
        math_ball_12              int,
        math_dpa_level            char(50),
        math_ball                 decimal(15, 2),
        math_pt_name              char(250),
        math_pt_reg               char(50),
        math_pt_area              char(50),
        math_pt_ter               char(50),
        physics_test              char(50),
        physics_lang              char(50),
        physics_status            char(50),
        physics_ball_100          decimal(15, 2),
        physics_ball_12           int,
        physics_ball              decimal(15, 2),
        physics_pt_name           char(300),
        physics_pt_reg            char(50),
        physics_pt_area           char(50),
        physics_pt_ter            char(50),
        chem_test                 char(50),
        chem_lang                 char(50),
        chem_status               char(50),
        chem_ball_100             decimal(15, 2),
        chem_ball_12              int,
        chem_ball                 decimal(15, 2),
        chem_pt_name              char(250),
        chem_pt_reg               char(50),
        chem_pt_area              char(50),
        chem_pt_ter               char(50),
        bio_test                  char(50),
        bio_lang                  char(50),
        bio_status                char(50),
        bio_ball_100              decimal(15, 2),
        bio_ball_12               int,
        bio_ball                  decimal(15, 2),
        bio_pt_name               char(250),
        bio_pt_reg                char(50),
        bio_pt_area               char(50),
        bio_pt_ter                char(50),
        geo_test                  char(50),
        geo_lang                  char(50),
        geo_status                char(50),
        geo_ball_100              decimal(15, 2),
        geo_ball_12               int,
        geo_ball                  decimal(15, 2),
        geo_pt_name               char(250),
        geo_pt_reg                char(50),
        geo_pt_area               char(50),
        geo_pt_ter                char(50),
        eng_test                  char(50),
        eng_lang                  char(50),
        eng_status                char(50),
        eng_ball_100              decimal(15, 2),
        eng_ball_12               int,
        eng_dpa_level             char(50),
        eng_ball                  decimal(15, 2),
        eng_pt_name               char(250),
        eng_pt_reg                char(50),
        eng_pt_area               char(50),
        eng_pt_ter                char(50),
        fra_test                  char(50),
        fra_lang                  char(50),
        fra_status                char(50),
        fra_ball_100              decimal(15, 2),
        fra_ball_12               int,
        fra_dpa_level             char(50),
        fra_ball                  decimal(15, 2),
        fra_pt_name               char(250),
        fra_pt_reg                char(50),
        fra_pt_area               char(50),
        fra_pt_ter                char(50),
        deu_test                  char(50),
        deu_lang                  char(50),
        deu_status                char(50),
        deu_ball_100              decimal(15, 2),
        deu_ball_12               int,
        deu_dpa_level             char(50),
        deu_ball                  decimal(15, 2),
        deu_pt_name               char(250),
        deu_pt_reg                char(50),
        deu_pt_area               char(50),
        deu_pt_ter                char(50),
        spa_test                  char(50),
        spa_lang                  char(50),
        spa_status                char(50),
        spa_ball_100              decimal(15, 2),
        spa_ball_12               int,
        spa_dpa_level             char(50),
        spa_ball                  decimal(15, 2),
        spa_pt_name               char(250),
        spa_pt_reg                char(50),
        spa_pt_area               char(50),
        spa_pt_ter                char(50),
        year                      int
    );"""
)
conn.commit()
cursor.close()

start_time = time.time()

with open(csv_zno_2019, 'r', encoding="cp1251", errors='ignore') as inf:
    reader1 = list(csv.reader(inf, delimiter=';'))
    row_num1 = len(reader1)
    print('Number of rows 2019: ', row_num1)


start_idx = 1
end_idx = 400

while start_idx < 1000:
    list1 = reader1[start_idx:end_idx+1]
    try:
        try:
            conn = psycopg2.connect(dbname='postgres', user='postgres', password='postgres', host='db')
        except psycopg2.Error as err:
            raise Exception(err)

        cur = conn.cursor()

        for row in list1:
            for i in range(len(row)):
                if i == 0:
                    continue

            for i in range(len(row)):
                if row[i] == 'null':
                    row[i] = None

            for i in range(len(row)):
                if row[i] is not None:
                    row[i] = row[i].replace(',', '.')
            cur.execute(query1, row)
        conn.commit()
        cur.close()

    except Exception as e:
        print('Error ', e)
        time.sleep(10)
        continue

    print(end_idx, "rows loaded to db")
    start_idx += 400
    end_idx += 400
    list1.clear()
reader1.clear()
print('DATA FROM FILE 2019 LOADED TO DB')

with open(csv_zno_2021, 'r', encoding="utf-8", errors='ignore') as inf:
    reader2 = list(csv.reader(inf, delimiter=';'))
    row_num2 = len(reader2)
    print('Number of rows 2021: ', row_num2)

start_idx = 1
end_idx = 400

while start_idx < 1000:
    list1 = reader2[start_idx:end_idx+1]
    try:
        try:
            conn = psycopg2.connect(dbname='postgres', user='postgres', password='postgres', host='db')
        except psycopg2.Error as err:
            raise Exception(err)

        cur = conn.cursor()

        for row in list1:
            for i in range(len(row)):
                if i == 0:
                    continue

            for i in range(len(row)):
                if row[i] == 'null':
                    row[i] = None

            for i in range(len(row)):
                if row[i] is not None:
                    row[i] = row[i].replace(',', '.')

            if row[47] is not None:
                values = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                        row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19],
                        row[20], row[21], row[22], row[23], row[24], row[25], row[26], row[27], row[28], row[29],
                        row[30], row[31], row[32], row[33], row[34], row[35], row[36], row[37], row[38], row[39],
                        row[40], row[41], row[42], row[43], row[44], row[45], row[46], row[47], row[48], row[49],
                        row[50], row[51], row[52], row[53], row[54], row[55], row[56], row[57], row[67], row[68],
                        row[69], row[70], row[71], row[72], row[73], row[74], row[75], row[76], row[77], row[78],
                        row[79], row[80], row[81], row[82], row[83], row[84], row[85], row[86], row[87], row[88],
                        row[89], row[90], row[91], row[92], row[93], row[94], row[95], row[96], row[97], row[98],
                        row[99], row[100], row[101], row[102], row[103], row[104], row[105], row[106], row[107],
                        row[108], row[109], row[110], row[111], row[112], row[113], row[114], row[115], row[116],
                        row[117], row[118], row[119], row[120], row[121], row[122], row[123], row[124], row[125],
                        row[126], row[127], row[128], row[129], row[130], row[131], row[132], row[133], row[134],
                        row[135], row[136], row[137], row[138], row[139],
                        row[140], row[141], row[142], row[143], row[144], row[145], row[146]]
            else:
                values = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                        row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19],
                        row[20], row[21], row[22], row[23], row[24], row[25], row[26], row[27], row[28], row[29],
                        row[30], row[31], row[32], row[33], row[34], row[35], row[36], row[37], row[38], row[39],
                        row[40], row[41], row[42], row[43], row[44], row[45], row[46], row[58], row[59], row[60],
                        None, row[61], None, row[62], row[63], row[64], row[65], row[66], row[67], row[68],
                        row[69], row[70], row[71], row[72], row[73], row[74], row[75], row[76], row[77], row[78],
                        row[79], row[80], row[81], row[82], row[83], row[84], row[85], row[86], row[87], row[88],
                        row[89], row[90], row[91], row[92], row[93], row[94], row[95], row[96], row[97], row[98],
                        row[99], row[100], row[101], row[102], row[103], row[104], row[105], row[106], row[107],
                        row[108], row[109], row[110], row[111], row[112], row[113], row[114], row[115], row[116],
                        row[117], row[118], row[119], row[120], row[121], row[122], row[123], row[124], row[125],
                        row[126], row[127], row[128], row[129], row[130], row[131], row[132], row[133], row[134],
                        row[135], row[136], row[137], row[138], row[139],
                        row[140], row[141], row[142], row[143], row[144], row[145], row[146]]
            cur.execute(query2, values)
        conn.commit()
        cur.close()

    except Exception as e:
        print('Error ', e)
        time.sleep(10)
        continue

    print(end_idx, "rows loaded to db")
    start_idx += 400
    end_idx += 400
    list1.clear()

reader2.clear()
print('DATA FROM FILE 2021 LOADED TO DB')

with conn:
    cur = conn.cursor()
    with open('result.csv', 'w', encoding='utf-8') as outfile:
        cur.execute(query3)
        fields = [x[0] for x in cur.description]
        writer = csv.writer(outfile)
        writer.writerow(fields)
        for row in cur:
            writer.writerow([str(x) for x in row])
    cur.close()
print('Result file is ready')


s = f" time --- {(time.time() - start_time)/60} minutes ---"
f = open('time.txt', 'w')
f.write(s)
f.close()

conn.close()
