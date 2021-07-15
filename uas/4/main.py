class Ternak :
    def __init__(self,namaPeternakan,alamat) :
        self.namaPeternakan=namaPeternakan
        self.alamat=alamat
        self.hewan = {
            1 : {
                "nama" : "Sapi",
                "jumlah" : 100,
                
                
            },
            2 : {
                "nama" : "Kambing",
                "jumlah" : 200,
              
                
            },
            3 : {
                "nama" : "Kerbau",
                "jumlah" : 300,
                
            }
        }

    def tampilkanInformasi(self):
        print("Nama Peternakan : ",self.namaPeternakan)
        print("Alamat Peternakan : ",self.alamat)

    def tampilkanHewanTernak(self) : 
        print(self.hewan[1])
        print(self.hewan[2])
        print(self.hewan[3])


obj = Ternak("Peternakan hewan kurban","pati jawa tengah") 
obj.tampilkanInformasi()
obj.tampilkanHewanTernak()