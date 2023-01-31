from tkinter import *
from tkinter import ttk
from Connect import *


window = Tk()
window.config()
# window.wm_attributes("-fullscreen", True)
window.geometry("1800x800")
# window.wm_attributes('-transparentcolor',"black")

# Title
window.title("SQLite")
icon = PhotoImage(file="IMG\\icon1.png")
window.iconphoto(True, icon)

# Background
background = PhotoImage(file="IMG\\background.png")
labelBackground = Label(image=background)
labelBackground.place(x=0, y=0)

Label(text="Student Management", font=("Times New Roman", 30, "bold"),bg="#713859",fg="white").pack(pady=30)

# Quit button
Button(text="Quit", command=window.destroy,
       width=13, height=1).place(x=20, y=100)

# create frame contain widgets
frame = Frame(window)
frame.pack(pady=100)
helloLabel = Label(
    window,
    text="HELLO EVERYONE!\nWelcome to Group 2",
    font=("Times New Roman", 40, "bold"),
    background="#5d3b56",fg="white"
)
helloLabel.pack(pady=50)

# Clear frame
def clearFrame():
    # destroy all widgets from frame
    for widget in frame.winfo_children():
        widget.destroy()


# create tree view to display the results of the query
# columnName : name of column in result table
# dataList : data in result table
def treeview(columnName, dataList):
    helloLabel.destroy()
    table = ttk.Treeview(frame)

    table["columns"] = columnName
    table.column("#0", width=50, stretch=YES, anchor=CENTER)
    table.heading("#0", text="STT")

    for index in range(len(columnName)):
        table.column(columnName[index], width=200, anchor=CENTER)

    for index in range(len(columnName)):
        table.heading(columnName[index], text=columnName[index])

    for index in range(0, len(dataList)):
        table.insert(
            parent="", index="end", iid=index, text=f"{index+1}", values=dataList[index]
        )
    table.grid()


# display table of database
def treeTable(selection):
    clearFrame()
    tableName = selection
    if tableName == "Subject":
        query = querySubject
    elif tableName == "Class":
        query = queryClass
    elif tableName == "Student":
        query = queryStudent
    else:
        query = queryStudentGrade
    columnName = getData(cursor, query)
    dataList = executeQuery(cursor, query)
    createLable(tableName)
    treeview(columnName, dataList)


# display result
def showQuery(selection):
    q = selection
    if q == "5.1":
        exeQuery(query1, queryName[0])

    if q == "5.2":
        exeQuery(query2, queryName[1])

    if q == "5.3":
        exeQuery(query3, queryName[2])

    if q == "5.4":
        exeQuery(query4, queryName[3])

    if q == "5.5":
        exeQuery(query5, queryName[4])

    if q == "5.6":
        exeQuery(query6, queryName[5])

    if q == "5.7":
        exeQuery(query7, queryName[6])

    if q == "5.8":
        exeQuery(query8, queryName[7])

    if q == "5.9":
        exeQuery(query9, queryName[8])

    if q == "5.10":
        exeQuery(query10, queryName[9])


# execute query
def exeQuery(query, name):
    clearFrame()
    columnName = []
    columnName = getData(cursor, query)
    dataList = executeQuery(cursor, query)
    createLable(name)
    treeview(columnName, dataList)


def createLable(name):
    Label(frame, text=name, font=(20)).grid()



# Drop down menu:
selectTable = StringVar()
listQuery = ["5.1", "5.2", "5.3", "5.4",
             "5.5", "5.6", "5.7", "5.8", "5.9", "5.10"]
tableList = ["Subject", "Class", "Student", "StudentGrade"]

selectTable.set("Table Name")
tableMmenu = OptionMenu(
    window,
    selectTable,
    *tableList,
    command=treeTable,
)
tableMmenu.config(width=10, height=1)
tableMmenu.place(x=20, y=50)

selectQuery = StringVar()
selectQuery.set("Query")
queryMenu = OptionMenu(
    window,
    selectQuery,
    *listQuery,
    command=showQuery,
)
queryMenu.config(width=10, height=1)
queryMenu.place(x=150, y=50)



window.mainloop()
connected.close()
