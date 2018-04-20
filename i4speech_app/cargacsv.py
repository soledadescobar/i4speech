from .models import Textos, Ocasiones, Autores, Ejes
import csv
import time



class CargaCSV():
    @staticmethod
    def cargacsv(file):
       # f = open(file)
        reader = csv.reader(file, dialect = 'excel')

        for row in reader:
            autor = Autores.objects.get(nombre=row[0])
            ocasioncsv = row[1]
            titulocsv = row[4]
            textocsv= row[5]
            fechacsv = row[3]
            ejecsv =  row[2]

            if Ocasiones.objects.filter(ocasion=ocasioncsv).exists():
                ocasionobj = Ocasiones.objects.get(ocasion=ocasioncsv)
            else:
                ocasionobj = Ocasiones.objects.create(ocasion=ocasioncsv)

            if Ejes.objects.filter(eje=ejecsv).exists():
                ejeobj = Ejes.objects.get(eje=ejecsv)
            else:
                ejeobj = Ejes.objects.create(eje=ejecsv)

            t = Textos.objects.create(idautor=autor,texto=textocsv,titulo=titulocsv,idocasion=ocasionobj, ideje=ejeobj , fecha=fechacsv)
            t.savefromcsv()