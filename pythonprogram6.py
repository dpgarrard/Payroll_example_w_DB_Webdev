
from bottle import route,run,template,request,response,redirect
import sqlite3

@route('/', method = 'GET') #default (home)
def index():
    data = {'title': 'your logged in and ready to go'}
    return template('index', data)  #login form for localhost




@route('/department', method = ['GET','POST'])  #view info by department
def department ():
    if request.method =='GET':
        return template('dept_form')
    else:
        dept = request.forms.get('department')
        con = sqlite3.connect('payroll.db') # connect to database
        cur = con.cursor()  # allow changes to database          
    # SQL statement to obtain certain employee info
        sql = '''SELECT pay_data.emp_id, emp_name, wage, hrs_worked
            FROM employees JOIN pay_data
            WHERE pay_data.emp_id = employees.emp_id AND employees.department = ?'''
        cur.execute(sql, (dept,)) # execute sql with department from form page

        rows = cur.fetchall() #collect all information and assign to rows
        cur.close() #close the connection
        hrs = 0
        wage = 0

        if rows:  # if any information is in variable rows (continue) if not play message

            listed_data = []   #create empty list
            for row in rows:        #cycle through all info in rows and put in row tuple
                eid, name, wage, hrs = row  #unpack row tuple into corresponding variables
                if hrs <= 40:   # evaluate the type of pay REG or OT
                    pay = wage * hrs

                else:
                    ot = (hrs - 40) * 1.5 * wage
                    pay = (wage * 40) + ot  

                emp = (eid, name, wage, hrs, pay) #create new tuple with pay value
                listed_data.append(emp)  #add it to the list
    #setup variable where rows is equal to list of data & department to dept selected by drop down menu from user
            data = {'rows': listed_data, 'department':dept}  
            return template('show_department', data) # send all to template to show it in a table format
        else:
            
            msg = {'msg':'You screwed up and did something wrong, NOW FIX IT!! LOL'}
            return template('message', msg) # if something went wrong
    
   
        
@route('/update_pay', method = ['GET','POST'])  #update hours for pay
def edit_hrs():
    if request.method == 'GET':             #get stuff
        return template('edit_emp_hrs')
    else:
        hrs = request.forms.get('hrs')  #data entered in from forms
        eid = request.forms.get('eid')

        con = sqlite3.connect('payroll.db') # connect to database
        cur = con.cursor()  # allow changes to database
    # statement to update pay data table and set hours
        sql =''' UPDATE pay_data
                SET hrs_worked = ?
                WHERE emp_id = ?'''
        cur.execute(sql, (hrs, eid))
        con.commit() #SAVE CHANGES
    # statement to select certain info for the did it work page (template)
        sql_confirm = ''' SELECT emp_id, emp_name, department FROM employees
                        WHERE emp_id = ?'''
        cur.execute(sql_confirm, (eid, ))  #forgot to make into a tuple
        result = cur.fetchone() #grab results of executed statement

        if result:
            emp_id, emp_name, dept = result  #unpack tuple result into appropriate variables
            data = {'emp_id': emp_id, 'emp_name': emp_name, 'department': dept} #take and put variables associated with key for template

            return template('did_it_work', data) #send it to template

        con.close() #close connection
        

      
        
run(host='0.0.0.0', port=8083)
