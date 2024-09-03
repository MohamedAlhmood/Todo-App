import functions
import FreeSimpleGUI as sg


label = sg.Text("Type in a todo")
input_box=sg.InputText(tooltip="enter a todo",key='todo')
button = sg.Button("add")
window =sg.Window("My Todo App",layout=[[[label]
                                            ,input_box,button]]
                                            ,font=('Helvetica',20))
while True:
    event,values= window.read()
    match event:
        case 'add':
            todos=functions.get_todos()
            new_todo=values['todo']+"\n"
            todos.append(new_todo)
            functions.writeTodos(todos)
        case sg.WIN_CLOSED:
            break
window.close()