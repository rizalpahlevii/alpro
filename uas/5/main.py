import os


class Node(object):
    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def getData(self):
        return self.data

    def getNext(self):
        return self.nextNode

    def setNext(self, newText):
        self.nextNode = newText


class Belanja(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        newNode = Node(data)
        newNode.setNext(self.head)
        self.head = newNode

    def showData(self):
        os.system('clear')
        print("Daftar Belanja : ")
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.getNext()



    def mainmenu(self,ff="not"):
        pilih = "y"
        while (pilih == "y"):
            
            print("===============================")
            print("|  Menu aplikasi daftar belanja |")
            print("===============================")
            print("1. Insert belanja")
            print("2. Tampilkan daftar belanja")
            print("===============================")
            pilihan = str(input(("Silakan masukan pilihan anda: ")))
            if(pilihan == "1"):
                os.system("clear")
                obj = str(input("Masukan data yang ingin anda tambahkan: "))
                self.insert(obj)
            
            elif(pilihan == "2"):
                self.showData()
                x = input("")
            else:
                pilih = "n"


if __name__ == "__main__":
    l = Belanja()
    l.mainmenu()
