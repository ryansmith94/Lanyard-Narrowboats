import ryanUi as ui
from datetime import datetime as dt
from sqlite3 import connect as sql


def accessDb(fn):
    def runAccess():
        try:
            conn = sql(DB_LOCATION)
            cursor = conn.cursor()
            cursor.execute("""PRAGMA foreign_keys=ON;""")
            fn(cursor)
        except Exception as ex:
            ex = ex.args[0].replace("constraint ", "").replace(" failed", "")
            if ex in DB_EXCEPTIONS:
                ui.errorMsg(DB_EXCEPTIONS[ex])
            else:
                ui.errorMsg("An unexpected error occurred.")
        finally:
            cursor.close()
            conn.commit()
            conn.close()
    return runAccess


def viewHolidays(win):
    def displayHolidays(cursor):
        holidays = cursor.execute("SELECT date, assigneeId, workHours FROM jobs WHERE status = 'Holiday' ORDER BY date DESC").fetchall()
        ui.displayList(holidays, listBox)

    # Make UI.
    ui.button(win, "Add", lambda: ui.window("Add Holiday", addHoliday))
    ui.button(win, "Refresh", accessDb(displayHolidays))
    listBox = ui.listBox(win, ["Date", "Employee", "Work hours"])
    accessDb(displayHolidays)()


def viewJobs(win):
    def clickSkills():
        jobId = jobIds[int(listBox.curselection()[0])]
        ui.window("Job Skills", lambda win: viewSkills(win, jobId, True))

    def clickCompleted(cursor):
        selected = int(listBox.curselection()[0])
        jobId = jobIds[selected]
        cursor.execute("UPDATE jobs SET status = 'Complete' WHERE jobId = ?", [jobId])
        if status.get() != "Complete":
            jobIds.pop(selected)
            listBox.delete(selected)

    def displayJobs(cursor):
        jobIds.clear()
        jobs = cursor.execute("SELECT jobId, date, assigneeId, customerId, boatId, description FROM jobs WHERE status = ? ORDER BY date DESC", [status.get()]).fetchall()
        jobIds.extend([job[0] for job in jobs])
        ui.displayList(jobs, listBox)

    def reassignJob(cursor):
        jobId = jobIds[int(listBox.curselection()[0])]

        # Remove assignee.
        cursor.execute("UPDATE jobs SET assigneeId = ? WHERE jobId = ?", [None, jobId])

        # Get and add new assignee.
        cursor.execute("UPDATE jobs SET assigneeId = ? WHERE jobId = ?", [getAssignee(cursor, jobId), jobId])

        displayJobs(cursor)

    jobIds = []

    # Make UI.
    ui.button(win, "Add", lambda: ui.window("Add Job", addJob))
    ui.button(win, "Reassign", accessDb(reassignJob))
    ui.button(win, "Skills", clickSkills)
    ui.button(win, "Incompleted", lambda: False)  # Do not implement.
    ui.button(win, "Completed", accessDb(clickCompleted))
    ui.button(win, "Paid", lambda: False)  # Do not implement.
    ui.button(win, "Refresh", accessDb(displayJobs))
    status = ui.dropDown(win, ["Incomplete", "Complete", "Paid"], lambda evt: accessDb(displayJobs)())
    listBox = ui.listBox(win, ["Job Id", "Date", "Assignee", "Customer", "Boat", "Description"], 30)
    accessDb(displayJobs)()


def viewEmployees(win):
    def clickSkills():
        employeeId = employeeIds[int(listBox.curselection()[0])]
        ui.window("Employee Skills", lambda win: viewSkills(win, employeeId, False))

    def addEmployee(cursor):
        cursor.execute("""INSERT INTO employees(name) VALUES(?)""", [name.get()])
        employees = cursor.execute("""SELECT employeeId FROM employees""").fetchall()
        employeeId = employees[len(employees) - 1][0]
        employeeIds.append(employeeId)
        listBox.insert(ui.END, ui.list2String([employeeId, name.get()]))
        name.delete(0, ui.END)

    def removeEmployee(cursor):
        selected = int(listBox.curselection()[0])
        employeeId = employeeIds[selected]
        cursor.execute("UPDATE jobs SET assigneeId = NULL WHERE assigneeId = ?", [employeeId])
        cursor.execute("DELETE FROM skills WHERE id = ? AND job = 0", [employeeId])
        cursor.execute("DELETE FROM employees WHERE employeeId = ?", [employeeId])
        freeJobs = cursor.execute("SELECT jobId FROM jobs WHERE assigneeId IS NULL AND status = 'Incomplete'").fetchall()
        for job in freeJobs:
            cursor.execute("UPDATE jobs SET assigneeId = ? WHERE jobId = ?", [getAssignee(cursor, job[0]), job[0]])
        employeeIds.pop(selected)
        listBox.delete(selected)

    def displayEmployees(cursor):
        employeeIds.clear()
        employees = cursor.execute("SELECT employeeId, name FROM employees""").fetchall()
        employeeIds.extend([employee[0] for employee in employees])
        ui.displayList(employees, listBox)

    employeeIds = []

    # Make UI.
    name = ui.textBox(win, 0, 0)
    ui.button(win, "Add", accessDb(addEmployee))
    ui.button(win, "Remove", accessDb(removeEmployee))
    ui.button(win, "Skills", clickSkills)
    ui.button(win, "Refresh", accessDb(displayEmployees))
    listBox = ui.listBox(win, ["Employee Id", "Name"])
    accessDb(displayEmployees)()


def viewSkills(win, id, isJob):
    def addSkill(cursor):
        table = "job" if isJob == True else "employee"
        results = cursor.execute("SELECT * FROM " + table + "s WHERE " + table + "Id = ?", [id]).fetchall()
        if (len(results) != 0):
            cursor.execute("""INSERT INTO skills(id, skill, job) VALUES(?, ?, ?)""", [id, skill.get(), isJob])
            listBox.insert(ui.END, skill.get())
            skill.delete(0, ui.END)
        else:
            raise Exception("ID no longer exists.")

    def displaySkills(cursor):
        skills = cursor.execute("SELECT skill FROM skills WHERE id = ? AND job = ?""", [id, isJob]).fetchall()
        ui.displayList(skills, listBox)

    # Make UI.
    skill = ui.textBox(win, 0, 0)
    ui.button(win, "Add", accessDb(addSkill))
    listBox = ui.listBox(win, ["Skill name"])
    accessDb(displaySkills)()
    win.title("Employee " + str(id) if (isJob == False) else "Job " + str(id))


def addHoliday(win):
    def submitClick(cursor):
        assert employee.get() != "", "No employee entered."
        assert float(workHours.get()), "No work hours entered."
        cursor.execute("""INSERT INTO jobs(assigneeId, date, workHours, status) VALUES(?, ?, ?, 'Holiday')""", [employee.get(), startDate.get(), workHours.get()])
        win.destroy()

    # Make UI.
    startDate, workHours, employee = ui.form(win, ["Start date", "Work hours", "Employee"], accessDb(submitClick))


def addJob(win):
    def submitClick(cursor):
        assert description.get() != "", "No description entered."
        assert customer.get() != "", "No customer entered."
        assert boat.get() != "", "No boat entered."
        assert float(workHours.get()), "No work hours entered."
        now = dt.now()
        assigneeId = getAssignee(cursor)
        cursor.execute("""INSERT INTO jobs(description, customerId, boatId, workHours, date, status, assigneeId) VALUES(?, ?, ?, ?, ?, 'Incomplete', ?)""", [description.get(), customer.get(), boat.get(), workHours.get(), now.strftime("%Y-%m-%d"), assigneeId])
        win.destroy()

    # Make UI.
    description, customer, boat, workHours = ui.form(win, ["Description", "Customer", "Boat", "Work hours"], accessDb(submitClick))


def viewMenu(win):
    ui.button(win, "Jobs", lambda: ui.window("Jobs", viewJobs))
    ui.button(win, "Employees", lambda: ui.window("Employees", viewEmployees))
    ui.button(win, "Holidays", lambda: ui.window("Holidays", viewHolidays))
    win.grid_columnconfigure(0, minsize=300)


def getAssignee(cursor, jobId=None):
    jobSkills = [skill[0] for skill in cursor.execute("SELECT skill FROM skills WHERE id = ? AND job = 1", [jobId]).fetchall()]
    skills = len(jobSkills)

    queryA = """SELECT id, COUNT(*) AS skills
        FROM skills
        WHERE job = 0 """ + ("" if skills == 0 else " AND skill IN (" + ("?, " * skills)[:-2] + ")") + """
        GROUP BY id
    """
    queryB = """SELECT employeeId, CASE WHEN skills > 0 THEN skills ELSE 0 END AS skills
        FROM employees
        LEFT JOIN (""" + queryA + """)
        ON employees.employeeID = id
        ORDER BY skills DESC
    """
    queryC = """SELECT assigneeId, SUM(workHours) AS workHours
        FROM jobs
        WHERE jobs.status = 'Incomplete' or (jobs.status = "Holiday" and DATE(jobs.date) < DATE('now') and DATE(DATE(jobs.date), '+' || (jobs.workHours / 9) || ' days') > DATE('now')) = 1
        GROUP BY assigneeId
    """
    queryD = """SELECT employeeId, (CASE WHEN workHours > 0 THEN workHours ELSE 0 END) - (b.skills * 4) AS workHours
        FROM (""" + queryB + """) AS b
        LEFT JOIN (""" + queryC + """) AS c
        ON b.employeeId = c.assigneeId
        ORDER BY workHours ASC
    """

    return cursor.execute(queryD, jobSkills).fetchone()[0]

# Start-up code.
DB_LOCATION = "narrowboats.db"

# Acceptable exceptions.
DB_EXCEPTIONS = {}
DB_EXCEPTIONS["limitHours"] = "Invalid number of work hours."
DB_EXCEPTIONS["limitPrice"] = "Invalid price."
DB_EXCEPTIONS["limitStatus"] = "Invalid status."
DB_EXCEPTIONS["formatDate"] = "Invalid date - must be in the format YYYY-MM-DD."
DB_EXCEPTIONS["limitDate"] = "Invalid date - the date must be after the present."
DB_EXCEPTIONS["foreign key"] = "Invalid ID."
DB_EXCEPTIONS["No description entered."] = "No description entered."
DB_EXCEPTIONS["No customer entered."] = "No customer entered."
DB_EXCEPTIONS["No boat entered."] = "No boat entered."
DB_EXCEPTIONS["No work hours entered."] = "No work hours entered."
DB_EXCEPTIONS["No employee entered."] = "No employee entered."
ui.window("Menu", lambda win: viewMenu(win))
