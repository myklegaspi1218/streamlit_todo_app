import streamlit as st
import functions as fn

todos = fn.get_todo('todos.txt')

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + "\n")
    fn.record_todo(todos)   

st.title('My Todo App')
st.subheader('This is my practive todo app.')
st.write('This app should help increase your productivity...')
 
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        fn.record_todo(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder='Enter new Todo', 
              on_change=add_todo, key="new_todo")

st.session_state
