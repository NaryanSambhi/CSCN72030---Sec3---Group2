#Naryan Sambhi

#DBS manager functions


import csv 


def register():
    with open("UserDBS.csv",mode="a", newline="") as f:
        writer = csv.writer(f,delimiter=",")
        
        
        email = input("Please enter email: ")
            
        password = input("Please enter password: ")
        password2 = input("Please re-enter password: ")
        
        if password == password2:   
            #userid = email + "test" + ".pkl"            
            writer.writerow( [email, password])
            print("welcome new user")
            
        else: 
            print("Something went wrong, please try again")
            


def loginUser():
    print("Please enter your credentials")
    email = input("Email: ")
    password = input("Password: ")
    
    with open("UserDBS.csv", mode="r") as f:
        reader = csv.reader(f, delimiter=",")
        for row  in reader:
            if row == [email, password]:
                
                return True
            

    print("Incorrect username or password")
    return False


#register()

#loginUser()


