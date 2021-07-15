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


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        newNode = Node(data)
        newNode.setNext(self.head)
        self.head = newNode

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.getNext()

        return count

    def search(self, data):
        current = self.head
        previous = None
        found = False

        while current and found is False:
            if current.getData() == data:
                found = True
            else:
                previous = current
                current = current.getNext()

        if current is None:
            raise ValueError("Data not in list")

        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def showData(self):
        os.system('clear')
        print("Tampilkan list data : ")
        print("Node -> Next Node")
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data)
            print("    ->")
            print(currentNode.nextNode.data) if hasattr(
                currentNode.nextNode(), "data") else None

            currentNode = currentNode.nextNode()

    def mainmenu(self):
        pilih = "y"
        while (pilih == "y"):
            os.system("clear")
            print("===============================")
            print("|  Menu aplikasi linked list  |")
            print("===============================")
            print("1. Insert data")
            print("2. Delete data")
            print("3. Cari data")
            print("4. Panjang dari linked list")
            print("5. Tampil data")
            print("===============================")
            pilihan = str(input(("Silakan masukan pilihan anda: ")))
            if(pilihan == "1"):
                os.system("clear")
                obj = str(input("Masukan data yang ingin anda tambahkan: "))
                self.insert(obj)
            elif(pilihan == "2"):
                os.system("clear")
                obj = str(input("Masukan data yang ingin anda dihapus: "))
                self.delete(obj)
                x = input("")
            elif(pilihan == "3"):
                os.system("clear")
                obj = str(input("Masukan data yang ingin anda dicari: "))
                status = self.search(obj)
                if status == True:
                    print("Data ditemukan pada list")
                else:
                    print("Data tidak ditemukan")
                x = input("")
            elif(pilihan == "4"):
                os.system("clear")
                print("Panjang dari queue adalah: "+str(self.size()))
                x = input("")
            elif(pilihan == "5"):
                os.system("clear")
                self.showData()
                x = input("")
            else:
                pilih = "n"


if __name__ == "__main__":
    # execute only if run as a script
    l = LinkedList()
    l.mainmenu()
