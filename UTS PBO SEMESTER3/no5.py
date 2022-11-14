class waktu:

    def __init__ (self,jam,menit,detik)
        self.jam = jam
        self.menit = menit
        self.detik = detik

    def info(self):
        if self.jam >= 24 or self.menit 60 or self.detik 60:
            print("wrong value")
        else :
            print (self.jam,':',self.menit,':',self.detik)
waktu = waktu (int(input("masukan jam: ")), int(input("masukan menit:")), int(input("masukan detik: ")))
waktu.info()