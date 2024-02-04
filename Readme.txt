Basic function to work with sqlite3 with python
- create file .db
- create table with primary unique index in the db file
- create def functions for:
        search by last name with case sensitive and partial search
        insert new row with auto index increment
        update an entry
        remove a row
        print all the table

*************************************************************************

python Sqlite3

import sqlite3

conn = sqlite3.connect (‘employee.db’) 
# this will create an employee.db file if it doesnt exist
# or connect to it if it exist .
# if u put instead ( ‘:memory:’ ) will create the file in the memory

# then we should create a cursor to execute sql comand
# to do so we put conn.cursor() into a variable c :

c = conn.cursor()

# now that we have a cursor, we will create a table named 
# employees inside the employee.db file with 4 columns :
# id as int primary key, first name as text, last as text and pay as integer

c.execute (“”” CREATE TABLE employees (
                       id INTEGER PRIMARY KEY AUTOINCREMENT ,
                       first  text ,
  			last  text ,
			pay integer
			) “”” )

# now we should commit our changes with :

conn.commit()

# then closing back the connection :

conn.close()


# to insert data in the table employees in the file employee.db :

conn = sqlite3.connect (‘employee.db’)
c = conn.cursor()
c.execute(“INSERT INTO employees VALUES (1, ‘corey’ , ‘schafer, , 5000)”)
conn.commit()
conn.close()

# example to insert from variables :
c.execute(“INSERT INTO employees VALUES (?, ? , ?, ,?)” , ( var.id , var.first , var.last , var.pay))
### or : 
c.execute(“INSERT INTO employees VALUES (:id ,:first ,:last, ,:pay)” ,{‘id’:var, ‘first’: var1,’last’:var2…..}


# to select  a row in the employees table :

c.execute(“SELECT * FROM employees WHERE last = ’schafer’”)
print(c.fetchone())
# (1,'corey',schafer',5000)
# to return the search inside a list use fetchall:
print(c.fetchall())
# [(1,'corey','schafer',5000),(2,'sdada','dsfss','gtret')]

# to create table with unique index:

c.execute (""" CREATE TABLE employees (
                       id INTEGER PRIMARY KEY AUTOINCREMENT ,
                       first  text ,
  			last  text ,
			pay integer
			) """ )





def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES(?,?,?,?)”, (emp))


def get_emp_by_name(name):
    name='%'+name.lower()+'%' #transform to lower case and partial search
    c.execute("SELECT * FROM employees  WHERE LOWER(last) LIKE :last"  ,{'last':name })
    return (c.fetchall())

def update_pay(emp,pay):
    print (emp[0])
    print(pay)
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'first': emp[0], 'last': emp[1], 'pay': pay})

def remove_emp(emp):
    print(emp[1])
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first':emp[0],'last':emp[1]})

### to get the next auto id :
c.execute("SELECT COUNT(*) FROM employees ")
row_nmbr=((c.fetchall()))
next_id= ((row_nmbr[(0)])[0])+2
print(next_id)




### inserting using the def function below where next_id is autoindex:
insert_emp([next_id,’chakib','touma',2400])

### updating pay column of emp_1 using def function at the beginning
update_pay(['Houssam','Rassi'], 50000)

### remove employee from database using first and last name in emp
remove_emp(['corey','shafer'])
### select a row in table using name(last name) with def fonction at the beginning
emp=get_emp_by_name("Rassi")
print (emp)


### to print all the employee table :
c.execute("select * from employees")
all_rows = c.fetchall()
for row in all_rows:
    print (row)


conn.commit()
conn.close()

