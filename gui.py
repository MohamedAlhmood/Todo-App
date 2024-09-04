import functions
import FreeSimpleGUI as sg


label = sg.Text("Type in a todo")
input_box=sg.InputText(tooltip="enter a todo",key='todo')
addButton = sg.Button("add")
listBox = sg.Listbox(values=functions.get_todos(),key='todos',enable_events=True,size =(45,10))
edit_button = sg.Button("edit")
completeButton= sg.Button("complete")
window =sg.Window("My Todo App",layout=[[[label]
                                            ,input_box,addButton],[listBox,edit_button],[completeButton]]
                                            ,font=('Helvetica',20))
while True:
    event,values= window.read()
    print(1,event)
    print(2,values)
    match event:
        case 'add':
            todos=functions.get_todos()
            new_todo=values['todo']+"\n"
            todos.append(new_todo)
            functions.writeTodos(todos)
            window['todos'].update(values=todos)

        case 'edit':
            try:
                todo_to_edit= values['todos'][0]
                newTodo= values['todo']
                todos=functions.get_todos()
                index=todos.index(todo_to_edit)
                todos[index]=newTodo
                functions.writeTodos(todos)
                window['todos'].update(values=todos)
            except:
                continue
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'complete':
            try:
                deleteTodo =values['todos'][0]
                todo = functions.get_todos()
                index = todo.index(deleteTodo)
                del todo[index]
                functions.writeTodos(todo)
                window['todos'].update(values=todo)
            except:
                continue

        case sg.WIN_CLOSED:
            break
window.close()