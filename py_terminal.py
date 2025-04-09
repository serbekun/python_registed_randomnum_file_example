import os
import sys
import random
import subprocess

x = 0
x_read1 = 0
a = 0

current_directory = os.getcwd()  # updating info about now directory

print("cheking system")  # show all symbols in ("")
print("now directory -", os.getcwd())  # show now directory

#------------------------------------------------#
#        checking change directory system        #
#------------------------------------------------#

try:
    os.chdir("files")
    print("checking directory changing")
    print("now directory -", os.getcwd())

    current_directory = os.getcwd()  # updating info about now directory
    if os.path.basename(current_directory) == "files":
        print("changing directory - OK")
        change_d_s_c = True
    else:
        print("changing directory - ERROR")
        change_d_s_c = False
except FileNotFoundError:
    print("Error: directory 'files' not found!")
    change_d_s_c = False

#------------------------------------------------#
#            checking open file systme           #
#------------------------------------------------#

file_open_file_test_path = "open_file_test.txt" # check exist or file

if os.path.exists(file_open_file_test_path):
    if os.path.isfile(file_open_file_test_path):
        with open("open_file_test.txt", "r") as file: # opening file for test systme
            open_file_test_0 = file.read()  # reading all file and save in variable
        if open_file_test_0 == "test_ok":
            open_file_test_1 = True
            print("open file system - OK")
            with open("x.txt", "r") as file: # X
                x_read1 = file.read()
                x = int(x) + int(x_read1)
        else:
            open_file_test_1 = False
            print("open file system - ERROR")
    else:
        open_file_test_1 = False
        print("file no exist")


if change_d_s_c == True and open_file_test_1 == True:
    print("all system on light - True")
else:
    print("all system on light - False")
    answer_if_sofoff = input("your system have ERROR do you want to continue [y/n]")
    if answer_if_sofoff == "n":
          with open("x.txt", "w") as file:
            file.write(x)
          exit(0)  # stop program     
    
print("")

with open("user_name.txt", "r") as file: #open file for check first user in system
    user_name = file.read() # save content to variable for check her
if user_name == "Ghost":
    user_name = input("type your user name for start registed :")
    with open("user_name.txt", "w") as file: # open file for write
        file.write(user_name)  # write new user name
        passworld = input("write passworld for user :")
        with open("user_passworld.txt", "w") as file: # open file for write
            file.write(passworld) # write new user passworld
            print("start program again")
else:
    with open("user_passworld.txt", "r") as file:
        check_passworld = file.read()
    sign_in_passworld = input("type your passworld :")
    if check_passworld == sign_in_passworld:
        while a < 5:
            ver = "0.0.3"
            first_message = f"welcome {user_name} to Sergey first py project py terminal, now version is {ver}"
            print(first_message)
            answer = "" # clear variable for clear bag
            answer_massage = f"{user_name}:" # making print message
            answer = input(answer_massage) # get answer from user
            if answer == "hash": # show random number code
                x = x + 1
                random_num = random.randint(1, 1000)  # Случайное число от 1 до 1000 (включительно)
                print(random_num)
                continue
            if answer == "show_x": # show int variable X script
                print("x -", int(x))
                continue
            if answer == "change_unap":             
                    user_name = input("type your user name for start registed :")
                    with open("user_name.txt", "w") as file: # open file for write
                        file.write(user_name)  # write new user name
                    passworld = input("write passworld for user :")
                    with open("user_passworld.txt", "w") as file: # open file for write
                        file.write(passworld) # write new user passworld
                    continue
            if answer == "exit": #exit scrip
                save_x = str(x)
                with open("x.txt", "w") as file: # X
                    file.write(save_x)
                exit(0)  # stop program
            if answer == "mun":
                with open("mun.txt", "r") as file:
                    mun = file.read()
                print(mun)
                continue
            else:
                ERROR_massege_1 = f"{answer} command not reconized in py_terminal {ver}"
                print(ERROR_massege_1)
    else:
        print("passworld incorect")       
        save_x = str(x)
        with open("x.txt", "w") as file: # X
            file.write(save_x)
        exit(0)  # stop program
