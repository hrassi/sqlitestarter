import sqlite3

conn = sqlite3.connect('employee.db')
c = conn.cursor()

### create table employees inside the file employee.db(only run one time)
'''
c.execute (""" CREATE TABLE employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT ,
            first  text ,
  			last  text ,
			pay integer
			) """ )
'''

### creating function to insert new employe and delete getbyname :
def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES(?,?,?,?)", (emp))


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



### creating variable emp_1 ...2..3 for employee to add in datafile:
emp_1=('Houssam','Rassi',10000)
emp_2=('jane','doe',9000)
#print(emp_1[0]) #print first position in emp_1

### inserting data in the table employees
#c.execute("INSERT INTO employees VALUES('corey','shafer',5000)")
### inserting in table variable emp_2
#c.execute("INSERT INTO employees VALUES(?,?,?)",(emp_2))


### select row in the table :
#c.execute("SELECT * FROM employees WHERE last = 'Rassi'")


c.execute("SELECT COUNT(*) FROM employees ")
row_nmbr=((c.fetchall()))
next_id= ((row_nmbr[(0)])[0])+2
print(next_id)


### inserting using the def function below:
#insert_emp([next_id,'Rony','abdel samad',9000])

### updating pay column of emp_1 using def function at the beginning
#update_pay(['khara','kaleb'], 27000)

### remove employee from database using first and last name in emp
#remove_emp(['joseph','balawand'])
### select a row in table using name(last name) caseinsensitiv and containing with def fonction at the beginning
emp=get_emp_by_name("la")
print (emp)




conn.commit()





### to print all the employee table :
c.execute("select * from employees")
all_rows = c.fetchall()
for row in all_rows:
    print (row)



#print(c.fetchone())
#print(c.fetchall()) # result in a list

conn.commit()
conn.close()


