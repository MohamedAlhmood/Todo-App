import functions
import FreeSimpleGUI as fs
label = fs.Text("Type in a todo")
input_box=fs.InputText(tooltip="enter a todo")
button = fs.Button("add")
window =fs.Window("My Todo App",layout=[[[label],input_box,button]])
window.read()
window.close()