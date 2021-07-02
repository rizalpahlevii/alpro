class StudentData:
    
    __data = []

    def __init__(self, name= None, nim=None, email=None, studyProgram=None,gender=None):
        self.name = name
        self.nim = nim
        self.email = email
        self.studyProgram = studyProgram
        self.gender = gender
        
    def delete(self,nim):
        for i in range(self.__data.__len__()) :
            if self.__data[i].nim == nim :
                del self.__data[i]
                return True
        return False
                
 
    def create(self, name, nim, email, studyProgram,gender):
        obj = StudentData(name,nim,email,studyProgram,gender)
        self.__data.append(obj)

    def update(self, nimUpdate ,name=None, nim=None, email=None, studyProgram=None,gender=None):
        for i in range(self.__data.__len__()) :
            if self.__data[i].nim == nimUpdate :
                if name != "" : 
                    self.__data[i].name = name 
                if nim != "" : 
                    self.__data[i].nim = nim 
                if email != "" : 
                    self.__data[i].email = email 
                if studyProgram != "" : 
                    self.__data[i].studyProgram = studyProgram 
                if gender != "" : 
                    self.__data[i].gender = gender

                return True
        return False 

    def searchByNim(self,nim) :
        for i in range(self.__data.__len__()) :
            if self.__data[i].nim == nim :
                return True
        return False 

    def displayData(self, title) :
        students = self.__data
        print("\t")
        print(title)
        print("| No\t| Name\t\t | NIM\t\t | Email\t\t | Study Program\t\t |  Gender\t |")
        print("=================================================================================================================================")
        iteration = 1
        for j in students:
            print("| {}\t | {}\t| {}\t\t | {}\t\t | {}\t\t | {}\t |".format(iteration,j.name,j.nim,j.email,j.studyProgram,j.gender))
            iteration +=1
        print("\t")





   
    


