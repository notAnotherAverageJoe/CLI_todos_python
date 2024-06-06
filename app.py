
while True:
    user_action = input("type add, show , edit, complete or exit: ")
    user_action = user_action.lower().strip()
    
    
    match user_action:
        case 'add':
            todo = input("Enter a todo: ") +"\n"
            
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            
            todos.append("You need to: " + (todo))
                
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
                
            
        case 'show' | 'display':
            
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            
            
            for index, items in enumerate(todos):
                items = items.strip().title()
                row = f"{index + 1}-{items}"
                print(row)
                
        case 'edit':
            number = int(input("Number of the TODO to edit: ")) 
            number = number - 1
            
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            
            new_todo = input("Enter new TODO: ")
            todos[number] = ("You need to: " + (new_todo)) + '\n'
            
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
                
        case 'complete':
            number = int(input("Number of the TODO to complete: "))
             
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            todo_to_remove = todos[number -1]
            
            todos.pop(number -1)
             
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
                
                message = f"Todo {todo_to_remove} was removed from the list."
                print(message)
                
             
            
            
        case 'exit':
            print("Goodbye!")
            break
        
        case _: 
            print('Hey, you entered and unkown command')
        
    
    
    
