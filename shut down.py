def shutdown(action):
    if action.lower() == "yes":
        print("System is shutting down...")
    elif action.lower() == "no":
        print("Shutdown canceled.")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

user_input = input("Do you want to shut down the system? (yes/no): ")
shutdown(user_input)
