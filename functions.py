
FILE_PATH = 'todos.txt'


def get_todo(filepath=FILE_PATH):

    with open(FILE_PATH) as todofileopenpath:
        opened_file = todofileopenpath.readlines()
    return opened_file

def record_todo(todolist, filepath=FILE_PATH):

    with open(FILE_PATH, 'w') as todowritefilepath:
        todowritefilepath.writelines(todolist)


if __name__ == '__main__':
    print('hello world!')