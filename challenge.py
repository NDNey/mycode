from datetime import datetime
def main():

    user_name = input("What is your name: ")
    day = datetime.today().strftime('%A')
    
    print(f"Hello, { user_name}! Happy {day}!")

main()
