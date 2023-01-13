
def welcome():
    print("==============================================================")
    print("Welcome to Lerato's Body Mass Index Calculator")
    print("==============================================================")
    print("These are the available commands: \n --calculate  \n --exit ")

            
def calculate():
   
    height = float(input("Please enter your height in cm: "))
    weight = float(input("Please enter your weight in kg: "))
    height1 = height/100 #converting height from centimeter to meter
    bmi = weight/(height1**2)
    print("%.2f" % bmi)

    if bmi < 18.5:
        print(bmi)
        print("You are under weight")
    elif bmi > 18.5 and bmi < 25:
        print(bmi)
        print("You are a Normal Weight")
    elif bmi > 25 and bmi < 30:
        print(bmi)
        print("You are a over weight ")
    elif bmi > 30 and bmi < 35:
        print(bmi)
        print("You are obese")
    else:
        print(bmi)
        print("You are clinically Obese")
    replay()
def replay():
    replay = input("would you like to calculate again? :") 
    if replay == 'yes':   
        calculate()
    else:
        exit()    

def exit():
    exit_command = input("are you sure? ")
    while exit_command == "yes":
        break
    


def play():
    
    welcome()
    command = input("Please enter the command you would like to do: ")
    if command == "calculate":
        calculate()
    elif command == "exit":
        exit()
    else:
        print("Invalid command")
        command = input("Please enter the command you would like to do: ") 
if __name__ == "__main__":
    play()