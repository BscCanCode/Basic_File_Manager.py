import sys
print("File_Manager_App")
print("What operations would you like to perform?")
print("1.Open_App\n2.Enter_Data\n3.Delete_Data\n4.Recycle_Bin\n5.Exit")
data=[] #here users entered data will be stored!
recycle=[] #here users deleted will be stored,incase if they changed their mind or done bymistake they can restore!"

while True:
    try:
        n=int(input("Enter your choice: "))
        if n==5:
            print("Thank You for using our app,please do visit again!")
            break
        if 0<n<=4:
            if n==1:
                if data:
                    print("This is your entered data!")
                    print("--------------------------------------------------------")
                    print(data)
                else:
                    print("No data to show!") #First to enter something to see the data
            elif n==2:
                a=input("Enter the data:") #data can be in any format that's why no int(input)
                data.append(a)
                print(f"{a} is added successfully to your storage") #no limit to enter data
            elif n==3:
                if data:
                    b=input("Enter the name of the data to get deleted:")
                    if b in data:
                        data.remove(b)
                        print(f"{b} got deleted from the app successfully")
                        d=input("Would you like to enter your deleted data in recycle bin? yes/no:")
                        if d=="yes":
                            recycle.append(b)
                            print("Data is stored in recycle bin successfully!\nNote: This data will be stored in bin but not \"PERMANENTLY\" !")
                        elif d=="no":
                            print("Data is not stored in recycle bin and has been deleted permanently!")
                        else:
                            print("To perform operation yes or no inputs are only accepted,any other input may give an error!")
                        c=input("Would you like to clear all data?\nNOTE:This data will be \"DELETED PERMANENTLY\" and not store in recycle bin\nWould you still like to continue? yes/no:")
                        if c=="yes":
                            data.clear()
                            print("Full data is cleared successfully!")
                            print(data)
                        elif c=="no":
                            print("Your data is safe and has not been deleted!")
                        else:
                            print("To perform any operation on data you should enter your input in yes or no,any other input may give an error!")
                    else:
                        print(f"{b} is not present in the app")
                else:
                    print("Your app is empty,Please enter something to delete!")
            elif n==4:
                if recycle:
                    print("This is your recycle bin")
                    print(recycle)
                    print("Would you like to restore your\n1.All Data\n2.Specific_Data\n3.Exit")
                    m=int(input("Enter your choice between 1-3 : "))
                    if 0<m<=2:
                        if m==3:
                            print("Nothing is restored!")
                            sys.exit()
                        elif m==1:
                            if recycle:
                                data.extend(recycle)
                                recycle.clear()
                                print("Done! all data is restored")
                            else:
                                print("No data is present in bin to be restored!")
                        elif m==2:
                            if recycle:
                                g=input("Enter data to get restored: ")
                                if g in recycle:
                                    data.append(g)
                                    recycle.remove(g)
                                    print(f"{g} has been restored successfully!")
                                else:
                                    print(f"{g} is not present in recycle bin,either it is deleted or was not present in bin")
                            else:
                                print("Nothing is present in the bin to get restored,first enter to get restored")
                    else:
                        print("You are suppose to enter your your choice between 1-3!")
                else:
                    print("Recycle is empty")
        else:
            print("Enter your choice between 1-5 to perform the operations!")
    except ValueError:
        print("Only int values are accepted,strings are not accepted")



                            
                            
                        
                        
                        
                
