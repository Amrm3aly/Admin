admins =["ahmed","ali","maged","maryam","rahma","amr"]
operators=["delete","update","append"]
name= input("please enter your name : ")
if name in admins : 
    print(f"Hello {name.strip().capitalize()} welcome back")
    options=input("Do you ant make any options yes or no? ")
    if options == "yes" :
        chose=input("chose any of these options \t Delete : \t update : \t append : \n")
        if chose == "delete":
            removedname=input("enter the name you want to remove it ")
            admins.remove(removedname)
            print("the name has been removed ")
            print(admins)
        elif chose=="update" :
                theNewName=input("enter the new name :")
                admins[admins.index(name)] =theNewName
                print("the name has been updated ")
                print(admins)
        elif chose == "append":
             newmember=input("Add the new member you want ")
             admins.append(newmember)
             print("Added successfuly ")
             view=input("do you want to see the list ?")
             if view =="yes" :
                  print(admins)
             else :
                    print("your program end")      
        
        else:
            print("Sorry this operation is unavailable now ")        
    else :
        print("thanks for using the program ")
else :
    print("Sorry you don't have an access !! ")
