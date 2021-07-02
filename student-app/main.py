from StudentData import *
 
def main() : 
    obj = StudentData()
    createData(obj)
    menuOption(obj)

    

   


def myInputUpdate(field) : 
    return input("Enter Student {} Update (leave it blank if you don't want to update) : ".format(field))


def createData(obj) : 
    numberOfStudent = int(input("Enter the number of students : "))
    
    no = 1

    for i in range(numberOfStudent) : 

        print("Student Number : " , no)
        name = input("Enter Student Name : ")
        nim = input("Enter Student NIM : ")
        email = input("Enter Student Email : ")
        studyProgram = input("Enter Student Study Program : ")
        gender = input("Enter Student Gender : ")

        obj.create(name,nim,email,studyProgram,gender)
        no +=1


    obj.displayData("Students Data")
    menuOption(obj)

def updateData(obj) :    
    updateId = input("Enter the NIM you want to update : ")
    if obj.searchByNim(updateId) : 
        nameUpdate = myInputUpdate("Name")
        nimUpdate = myInputUpdate("NIM")
        emailUpdate = myInputUpdate("Email")
        studyProgramUpdate = myInputUpdate("Study Program")
        genderUpdate = myInputUpdate("Gender")
        updateReponse = obj.update(updateId,nameUpdate,nimUpdate,emailUpdate,studyProgramUpdate,genderUpdate)
        if updateReponse : 
            print('\x1b[6;30;42m'+"successfully updated data"+ '\x1b[0m')
        else :
            print('\033[91m'+"Failed to update data"+'\033[0m')
    else : 
        print('\033[91m'+"The NIM entered does not match the existing data"+'\033[0m')
    
    obj.displayData("Student data after updating")
    menuOption(obj)


def deleteData(obj) :

    deleteId = input("Enter the NIM you want to delete : ")
    if obj.searchByNim(deleteId) : 
        deleteResponse=obj.delete(deleteId)
        if deleteResponse : 
            print('\x1b[6;30;42m'+"successfully deleted data"+ '\x1b[0m')
        else :
            print('\033[91m'+"Failed to delete data"+'\033[0m')
    else : 
        print('\033[91m'+"The NIM entered does not match the existing data"+'\033[0m')
    
    obj.displayData("Student data after deleting")
    menuOption(obj)

def displayData(obj) :
    obj.displayData("Student data ")
   


def searchData(obj) : 
    searchNim = input("Enter the NIM you want to Search : ")
    search = obj.searchByNim(searchNim)
    if search  : 
        print('\x1b[6;30;42m'+"successfully searched data"+ '\x1b[0m')
        print("| Name\t\t | NIM\t\t | Email\t\t | Study Program\t\t |  Gender\t |")
        print("=================================================================================================================================")
        print("| {}\t| {}\t\t | {}\t\t | {}\t\t | {}\t |".format(search.name,search.nim,search.email,search.studyProgram,search.gender))
            
    else : 
        print('\033[91m'+"The NIM entered does not match the existing data"+'\033[0m')
    
    obj.displayData("Student data after deleting")
    menuOption(obj)


def menuOption(obj) :
    print("\t")
    print("=========================")
    print("Student App Menu") 
    print("A. Update Data")
    print("B. Delete Data")
    print("C. Create Data")
    print("D. Search Data")
    print("E. Display Data")
    print("F. Exit")
    print("=========================")
    print("\t")
    menu = input("Choose Menu : ")
    if menu == "A" : 
        updateData(obj)
    elif menu == "B" : 
        deleteData(obj)
    elif menu == "C" : 
        createData(obj)
    elif menu == "D" : 
        searchData(obj)
    elif menu == "E" : 
        displayData(obj)
    elif menu == "F" : 
        exit()
    else :
        print('\033[91m'+"Menu Not Found"+'\033[0m')
        menuOption(obj)



main()