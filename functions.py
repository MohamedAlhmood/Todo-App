FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """Read a text file and return
       list of to-do items"""
    with open(filepath, 'r') as fileLocal:
        todosLocal = fileLocal.readlines()
    return todosLocal


def writeTodos(todosArg, filepath=FILEPATH):
    """Write the todo items list in a given text file"""
    with open(filepath, 'w') as file:
        file.writelines(todosArg)

