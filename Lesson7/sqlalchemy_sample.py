from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, text, and_, ForeignKey
from sqlalchemy.sql import select
engine = create_engine('sqlite:///college.db', echo = True)
meta = MetaData()

students = Table(
    'students', meta,
    Column('id', Integer, primary_key = True ),
    Column('name', String),
    Column('lastname', String)
)

addresses = Table(
    'addresses', meta,
    Column('id', Integer, primary_key = True),
    Column('std_id', Integer, ForeignKey('students.id')),
    Column('postal_add', String),
    Column('email_add', String)
)

conn = engine.connect()
# ins = students.insert().values(name = 'Tuan', lastname='Tran Quoc' )
# ins = students.insert().values(name = 'Khang', lastname='Huynh Thuc' )
# result = conn.execute(ins)

# conn.execute(students.insert(),[
#     {'name': 'Thuy', 'lastname': 'Hoang Dao'},
#     {'name': 'Duan', 'lastname': 'Le'},
#     {'name': 'Bo', 'lastname': 'Trinh Van'},
#     {'name': 'Ngu', 'lastname': 'Dang Van'},
#     {'name': 'Quat', 'lastname': 'Cao Ba'},
# ])

# conn.execute(addresses.insert(),[
#     {'std_id': 1, 'postal_add': 'Demo postal_add1', 'email_add':'demo1@gmail.com'},
#     {'std_id': 2, 'postal_add': 'Demo postal_add2', 'email_add':'demo2@gmail.com'},
#     {'std_id': 3, 'postal_add': 'Demo postal_add3', 'email_add':'demo3@gmail.com'},
#     {'std_id': 4, 'postal_add': 'Demo postal_add4', 'email_add':'demo4@gmail.com'},
#     {'std_id': 7, 'postal_add': 'Demo postal_add7', 'email_add':'demo7@gmail.com'},
# ])


# s = students.select()
# result = conn.execute(s)

# for row in result:
#     print(row)

# s = students.select().where(students.c.id > 6)
# result = conn.execute(s)

# for row in result:
#     print(row)

#txt = text("SELECT * FROM students WHERE students.id = 5 ")
#txt = text("select s.name, s.lastname from students s where s.name between :x and :y")
#result = conn.execute(txt, x = 'K', y='L').fetchall()

# for row in result:
#     print(row)

# s = select([text("* from students")]) \
# .where(
#     and_(
#         text("students.name between :x and :y"),
#         text("students.id > 4")
#     )
# )
# result = conn.execute(s, x = 'A', y = 'L').fetchall()

# for row in result:
#     print(row)


# std = students.alias("st")
# s = select([std]).where(std.c.id > 4)
# result = conn.execute(s).fetchall()

# for row in result:
#     print(row)

#stmt = students.update().where(students.c.lastname =="Trinh Van").values(lastname = "Trinh Van1")
# stmt = students.delete().where(students.c.lastname == "Trinh Van1")
# conn.execute(stmt)
# s = students.select()
# conn.execute(s).fetchall()


# Hiển thị tất cả sinh viên có địa chỉ address
# s = select([students, addresses]).where(students.c.id == addresses.c.std_id)
# result = conn.execute(s)

# for row in result:
#     print(row)

# Thực hiện update 2 table
stmt = students.update(). \
values({
    students.c.name : 'Tuan111',
}).\
where(students.c.id == 1)
result = conn.execute(stmt)

meta.create_all(engine)