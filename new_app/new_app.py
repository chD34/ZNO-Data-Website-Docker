from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import csv
from flask_caching import Cache
from sqlalchemy import text, func, and_, or_
from sqlalchemy.exc import IntegrityError
import redis

conn = psycopg2.connect(dbname='postgres', user='postgres', password='postgres', host='db')

cursor = conn.cursor()

query = '''
SELECT person.region, 
MAX(ball_100) FILTER (WHERE status = 'Зараховано' and year=2019 AND person_subject_eo.subject_name = 'Математика') as max_100_2019,
MAX(ball_100) FILTER (WHERE status = 'Зараховано' and year=2021 AND person_subject_eo.subject_name = 'Математика') as max_100_2021,
MAX(ball) FILTER (WHERE status = 'Зараховано' and year=2019 AND person_subject_eo.subject_name = 'Математика') as max_test_2019,
MAX(ball) FILTER (WHERE status = 'Зараховано' and year=2021 AND person_subject_eo.subject_name = 'Математика') as max_test_2021,
MAX(ball_12) FILTER (WHERE status = 'Зараховано' and year=2019 AND person_subject_eo.subject_name = 'Математика') as max_12_2019,
MAX(ball_12) FILTER (WHERE status = 'Зараховано' and year=2021 AND person_subject_eo.subject_name = 'Математика') as max_12_2021 
FROM person JOIN person_subject_eo ON person_subject_eo.out_id = person.out_id 
GROUP BY person.region
ORDER BY person.region;
'''

cursor.execute(query)

with open('result2.csv', 'w', encoding="utf-8") as f:
    writer = csv.writer(f, lineterminator="\n")
    for row in cursor:
        writer.writerow(row)

cursor.close()
conn.close()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@db:5432/postgres'
db = SQLAlchemy(app)
app.debug = True
app.secret_key = 'my_key'

# Створення об'єкту кешування
cache = Cache(app)
app.config['CACHE_TYPE'] = 'redis'
app.config['CACHE_REDIS_URL'] = 'redis://localhost:6379/0'

class Eo(db.Model):
    __tablename__ = 'eo'
    eo_name = db.Column(db.String(300), primary_key=True)
    eo_type_name = db.Column(db.String(100))
    eo_reg_name = db.Column(db.String(50))
    eo_area_name = db.Column(db.String(50))
    eo_ter_name = db.Column(db.String(50))
    eo_parent = db.Column(db.String(300))


class Person(db.Model):
    __tablename__ = 'person'
    out_id = db.Column(db.String(100), primary_key=True)
    eo_name = db.Column(db.String(300), db.ForeignKey('eo.eo_name'))
    birth = db.Column(db.Integer)
    sex = db.Column(db.String(20))
    region = db.Column(db.String(100))
    area_name = db.Column(db.String(100))
    ter_name = db.Column(db.String(100))
    reg_type_name = db.Column(db.String(300))
    ter_type_name = db.Column(db.String(100))
    class_prof_name = db.Column(db.String(100))
    class_lang_name = db.Column(db.String(100))


class Subject(db.Model):
    __tablename__ = 'subject'
    subject_name = db.Column(db.String(100), primary_key=True)


class PersonSubjectEo(db.Model):
    __tablename__ = 'person_subject_eo'
    out_id = db.Column(db.String(100), db.ForeignKey('person.out_id'), primary_key=True)
    eo_name = db.Column(db.String(300), db.ForeignKey('eo.eo_name'), primary_key=True)
    subject_name = db.Column(db.String(100), db.ForeignKey('subject.subject_name'), primary_key=True)
    status = db.Column(db.Integer)
    ball_100 = db.Column(db.Numeric(15, 2))
    ball_12 = db.Column(db.Integer)
    ball = db.Column(db.Numeric(15, 2))
    adapt_scale = db.Column(db.Integer)
    pt_name = db.Column(db.String(300))
    pt_reg = db.Column(db.String(100))
    pt_area = db.Column(db.String(100))
    pt_ter = db.Column(db.String(100))
    dpa_level = db.Column(db.String(100))
    lang = db.Column(db.String(100))
    year = db.Column(db.Integer)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/person/<int:page>')
def person(page=1):
    eo_values = [row.eo_name for row in Eo.query.all()]
    persons = Person.query.all()
    id_values = [row.out_id for row in Person.query.all()]
    return render_template('person.html', persons=persons, eo_values=eo_values, id_values=id_values)


@app.route('/create', methods=['POST'])
def create():
    out_id = request.form['out_id']
    eo_name = request.form.get('eo_name')
    birth = request.form['birth']
    sex = request.form['sex']
    region = request.form['region']
    area_name = request.form['area_name']
    ter_name = request.form['ter_name']
    reg_type_name = request.form['reg_type_name']
    ter_type_name = request.form['ter_type_name']
    class_prof_name = request.form['class_prof_name']
    class_lang_name = request.form['class_lang_name']
    new_person = Person(out_id=out_id, eo_name=eo_name, birth=birth, sex=sex, region=region, area_name=area_name,
                        ter_name=ter_name, reg_type_name=reg_type_name, ter_type_name=ter_type_name,
                        class_prof_name=class_prof_name, class_lang_name=class_lang_name)
    db.session.add(new_person)
    db.session.commit()
    return redirect(url_for('person', page=1))


@app.route('/update', methods=['POST'])
def update():
    out_id = request.form['out_id']
    person = Person.query.get(out_id)
    person.out_id = request.form['out_id']
    person.eo_name = request.form['eo_name']
    person.birth = request.form['birth']
    person.sex = request.form['sex']
    person.region = request.form['region']
    person.area_name = request.form['area_name']
    person.ter_name = request.form['ter_name']
    person.reg_type_name = request.form['reg_type_name']
    person.ter_type_name = request.form['ter_type_name']
    person.class_prof_name = request.form['class_prof_name']
    person.class_lang_name = request.form['class_lang_name']
    db.session.commit()
    return redirect(url_for('person', page=1))


@app.route('/delete', methods=['POST'])
def delete():
    out_id = request.form['out_id']
    person = Person.query.get(out_id)
    db.session.execute(text("DELETE FROM person_subject_eo WHERE out_id = :out_id"), {"out_id": out_id})
    db.session.delete(person)
    db.session.commit()
    return redirect(url_for('person', page=1))


@app.route('/eo/<int:page>')
def eo(page=2):
    eos = Eo.query.all()
    eo_values = [row.eo_name for row in Eo.query.all()]
    return render_template('eo.html', eos=eos, eo_values=eo_values)


@app.route('/create_eo', methods=['POST'])
def create_eo():
    eo_name = request.form['eo_name']
    eo_type_name = request.form['eo_type_name']
    eo_reg_name = request.form['eo_reg_name']
    eo_area_name = request.form['eo_area_name']
    eo_ter_name = request.form['eo_ter_name']
    eo_parent = request.form['eo_parent']
    new_eo = Eo(eo_name=eo_name, eo_type_name=eo_type_name, eo_reg_name=eo_reg_name, eo_area_name=eo_area_name,
                eo_ter_name=eo_ter_name, eo_parent=eo_parent)
    db.session.add(new_eo)
    db.session.commit()
    return redirect(url_for('eo', page=2))


@app.route('/update_eo', methods=['POST'])
def update_eo():
    eo_name = request.form.get('eo_name')
    eo = Eo.query.get(eo_name)
    eo.eo_name = request.form['eo_name']
    eo.eo_type_name = request.form['eo_type_name']
    eo.eo_reg_name = request.form['eo_reg_name']
    eo.eo_area_name = request.form['eo_area_name']
    eo.eo_ter_name = request.form['eo_ter_name']
    eo.eo_parent = request.form['eo_parent']
    db.session.commit()
    return redirect(url_for('eo', page=2))


@app.route('/delete_eo', methods=['POST'])
def delete_eo():
    eo_name = request.form['eo_name']
    eo = Eo.query.get(eo_name)
    db.session.execute(text("DELETE FROM person_subject_eo WHERE eo_name = :eo_name"), {"eo_name": eo_name})
    db.session.execute(text("DELETE FROM person WHERE eo_name = :eo_name"), {"eo_name": eo_name})
    db.session.delete(eo)
    db.session.commit()
    return redirect(url_for('eo', page=2))


@app.route('/subject/<int:page>')
def subject(page=3):
    subjects = Subject.query.all()
    s = [row.subject_name for row in Subject.query.all()]
    return render_template('subject.html', subjects=subjects, s=s)


@app.route('/create_subject', methods=['POST'])
def create_subject():
    subject_name = request.form['subject_name']
    new_subject = Subject(subject_name=subject_name)
    db.session.add(new_subject)
    db.session.commit()
    return redirect(url_for('subject', page=3))


@app.route('/delete_subject', methods=['POST'])
def delete_subject():
    subject_name = request.form['subject_name']
    subject = Subject.query.get(subject_name)
    db.session.execute(text("DELETE FROM person_subject_eo WHERE subject_name = :subject_name"),
                       {"subject_name": subject_name})
    db.session.delete(subject)
    db.session.commit()
    return redirect(url_for('subject', page=3))


@app.route('/pse/<int:page>')
def pse(page=4):
    ball_100_list = [i for i in range(100, 201)]
    ball_list = [i for i in range(0, 91)]
    id_values = [row.out_id for row in Person.query.all()]
    eo_values = [row.eo_name for row in Eo.query.all()]
    s = [row.subject_name for row in Subject.query.all()]
    pses = PersonSubjectEo.query.all()
    return render_template('person_subject_eo.html', id_values=id_values, s=s, eo_values=eo_values, pses=pses,
                           ball_100_list=ball_100_list, ball_list=ball_list)


@app.route('/create_pse', methods=['POST'])
def create_pse():
    try:
        out_id = request.form['out_id']
        eo_name = request.form['eo_name']
        subject_name = request.form['subject_name']
        status = request.form['status']
        ball_100 = request.form['ball_100']
        ball_12 = request.form['ball_12']
        ball = request.form['ball']
        adapt_scale = request.form['adapt_scale']
        pt_name = request.form['pt_name']
        pt_reg = request.form['pt_reg']
        pt_area = request.form['pt_area']
        pt_ter = request.form['pt_ter']
        dpa_level = request.form['dpa_level']
        lang = request.form['lang']
        year = request.form['year']
        new_pse = PersonSubjectEo(subject_name=subject_name, out_id=out_id, eo_name=eo_name, status=status,
                                  ball_100=ball_100, ball_12=ball_12, ball=ball, adapt_scale=adapt_scale,
                                  pt_name=pt_name,
                                  pt_reg=pt_reg, pt_area=pt_area, pt_ter=pt_ter, dpa_level=dpa_level, lang=lang,
                                  year=year)
        db.session.add(new_pse)
        db.session.commit()
        return redirect(url_for('pse', page=4))
    except IntegrityError:
        db.session.rollback()
        flash('Дані з таким ключем уже існують в таблиці. Якщо потрібно змінити скористайтеся Update')
        return redirect(url_for('pse', page=4))


@app.route('/update_pse', methods=['POST'])
def update_pse():
    out_id = request.form.get('out_id')
    eo_name = request.form.get('eo_name')
    subject_name = request.form.get('subject_name')
    pse = PersonSubjectEo.query.filter_by(out_id=out_id, eo_name=eo_name, subject_name=subject_name).first()
    if pse:
        pse.out_id = request.form['out_id']
        pse.eo_name = request.form['eo_name']
        pse.subject_name = request.form['subject_name']
        pse.status = request.form['status']
        pse.ball_100 = request.form['ball_100']
        pse.ball_12 = request.form['ball_12']
        pse.ball = request.form['ball']
        pse.adapt_scale = request.form['adapt_scale']
        pse.pt_name = request.form['pt_name']
        pse.pt_reg = request.form['pt_reg']
        pse.pt_area = request.form['pt_area']
        pse.pt_ter = request.form['pt_ter']
        pse.dpa_level = request.form['dpa_level']
        pse.lang = request.form['lang']
        pse.year = request.form['year']
        db.session.commit()
    else:
       flash('Дані з таким ключем не існують в таблиці. Якщо потрібно створити скористайтеся Create')
    return redirect(url_for('pse', page=4))


@app.route('/delete_pse', methods=['POST'])
def delete_pse():
    out_id = request.form['out_id']
    eo_name = request.form['eo_name']
    subject_name = request.form['subject_name']
    pse = PersonSubjectEo.query.filter_by(out_id=out_id, eo_name=eo_name, subject_name=subject_name).first()
    if pse:
        db.session.delete(pse)
        db.session.commit()
    else:
        flash('Дані з таким ключем не існують в таблиці. Якщо потрібно створити скористайтеся Create')
    return redirect(url_for('pse', page=4))


@app.route('/requests/<int:page>', methods=['GET', 'POST'])
@cache.cached(timeout=120)  # Кешування на 120 секунд
def requests(page=5):
    year = request.form.get('year')
    subject_name = request.form.get('subject_name')
    subject_names = set([row.subject_name for row in PersonSubjectEo.query.all()])
    max_ball = db.session.query(Person.region, func.max(PersonSubjectEo.ball_100)).join(Person).filter(PersonSubjectEo.year == year, PersonSubjectEo.subject_name == subject_name, PersonSubjectEo.status == 'Зараховано').group_by(Person.region).all()
    return render_template('requests.html', max_ball=max_ball, subject_names=subject_names)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
