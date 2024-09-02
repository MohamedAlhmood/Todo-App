from functions import get_todos,writeTodos # type: ignore
import time
tim=time.strftime("%m - %d - %y  %H:%M:%S ")
print("It is: ",tim)
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action= user_action.strip()

    if user_action.startswith('add'):
            todo = user_action[4:]
            todos= get_todos()

            todos.append(todo+'\n')


            writeTodos(todos)

    elif user_action.startswith("show"):

                todos = get_todos()
                new_todos = [item.strip('\n') for item in todos]
                for index, item in enumerate(new_todos):
                     row = f"{index+1}-{item}"
                     print(row)
    elif user_action.startswith('edit'):
            try:
                number = int(user_action[5:])
                number-=1
                todos = get_todos()
                newtodo = input("Enter new todo: ")
                todos[number] = newtodo + "\n"
                with open('todos.txt','w') as file:
                    file.writelines(todos)
            except ValueError:
                  print("invalid input")
                  continue

    elif user_action.startswith('complete'):
            try:
                number = int(user_action[9:])
                todos = get_todos()
                index = number-1
                todo_to_remove = todos[index]
                todos.pop(index)
                writeTodos(todos)

                message = f"Todo {todo_to_remove.strip("\n")} has been removed from the list"
                print(message)
            except :
                  print("Item not found")
                  continue
    elif user_action.startswith('exit'):
            break
    else:
          print("command is not valid. ")
print("bye")
