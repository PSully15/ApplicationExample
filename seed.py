"""Seed file to make sample data for db"""

from models import Department, Employee, Project, EmployeeProject, db
from app import app


#  Create all tables
db.drop_all()
db.create_all()

# #  Departments
# d1 = Department(
#     dept_code="mktg", 
#     dept_name="Marketing"
# )
# d2 = Department(
#     dept_code="actg", 
#     dept_name="Accounting"
# )
# d3 = Department(
#     dept_code="r&d",
#     dept_name="Research and Development",
#     phone="908-7878"
# )
# d4 = Department(
#     dept_code="sales",
#     dept_name="Sales",
#     phone="225-6912"
# )
# d5 = Department(
#     dept_code="it",
#     dept_name="Information Technology",
#     phone="888-4562"
# )
# d6 = Department(
#     dept_code="freedev",
#     dept_name="Freelance Development",
#     phone="867-5309"
# )

# #  Employees
# river = Employee(
#     name="River Bottom", 
#     state="NY", 
#     dept_code="mktg"
# )
# summer = Employee(
#     name="Summer Winter", 
#     state="OR", 
#     dept_code="mktg"
# )
# joaquin = Employee(
#     name="Joaquin Pheonix", 
#     dept_code="actg"
# )
# octavia = Employee(
#     name="Octavia Spencer",
#     dept_code="r&d"
# )
# larry = Employee(
#     name="Larry David",
#     state="NY",
#     dept_code="r&d"
# )
# kurt = Employee(
#     name="Kurt Cobain",
#     state="WA",
#     dept_code="it"
# )
# rain = Employee(
#     name="Rain Pheonix",
#     dept_code="it"
# )
# freelancer = Employee(
#     name="Freelancer McGee",
#     state="CO"
# )

# db.session.add_all([
#     d1, 
#     d2, 
#     d3, 
#     d4, 
#     d5,
#     d6,
#     river, 
#     summer, 
#     joaquin, 
#     octavia, 
#     larry, 
#     kurt, 
#     rain,
#     freelancer
# ])
# db.session.commit()


EmployeeProject.query.delete()
Employee.query.delete()
Department.query.delete()
Project.query.delete()

#  Add sample employees and departments

#  Departments
df = Department(
    dept_code='fin',
    dept_name='Finance',
    phone='555-1000'
)
dl = Department(
    dept_code='legal',
    dept_name='Legal',
    phone='555-2222'
)
dm = Department(
    dept_code='mktg',
    dept_name='Marketing',
    phone='555-9999'
)

#  Employees
leonard = Employee(
    name='Leonard', 
    dept=dl
)
liz = Employee(
    name='Liz',
    dept=dl
)
maggie = Employee(
    name='Maggie',
    state='DC',
    dept=dm
)
nadine = Employee(
    name='Nadine'
)
mick = Employee(
    name='Mick Jagger'
)
tom = Employee(
    name='Tom Brady',
    dept=dm
)
george = Employee(
    name='George Kittle',
    dept=df
)

db.session.add_all([
    df,
    dl,
    dm,
    leonard,
    liz,
    maggie,
    nadine,
    mick,
    tom,
    george
])
db.session.commit()


#  Projects and Employees Projects
pc = Project(
    proj_code='car',
    proj_name='Design Car',
    assignments=[
        EmployeeProject(
        emp_id=liz.id,
        role='Chair'
    ),
    EmployeeProject(
        emp_id=maggie.id
    )]
)
ps = Project(
    proj_code='server',
    proj_name='Deploy Server',
    assignments=[
        EmployeeProject(
        emp_id=liz.id
    ),
    EmployeeProject(
        emp_id=leonard.id,
        role='Auditor'
    )]
)

db.session.add_all([
    pc,
    ps
])
db.session.commit()
