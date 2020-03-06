def get_chatbot_response(message):
    if message[:2] != "!!":
        return ''

    bangs, command, args = message.split(' ', 2)
    
    # bangs = !!
    # command = add
    # args = "2 4"
    
    if command == "Hey":
        return "What's up!"
        
    elif command == "add":
        num1, num2 = args.split()
        num1 = int(num1)
        num2 = int(num2)
        return num1 + num2
        
    elif command == "divide":
        num1, num2 = args.split()
        num1 = int(num1)
        num2 = int(num2)
        return num1 / num2
        
    elif command == "say":
        return args
    else:
        return "Oops! I didn't recognize your command :("

if __name__ == "__main__":
    print(get_chatbot_response("!! add 10 5"))
    
# Run this file in the terminal by:
# - cd current directory
# - typing "python functions.py"