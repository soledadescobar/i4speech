# -*- coding: utf-8 -*-
from . import legibilidad
from .models import Escalagu, Escalain, Escalasp, Escalamu, Escalafh
class Analizador():

    @staticmethod
    def analizatexto(texto):
        resultado = {'cr': [],'fh':[], 'gu':[],'mu':[], 'sp': [], 'in':[]}
        resultado['cr'].append(legibilidad.crawford(texto))
        resultado['cr'].append('#669999')

        resfh = legibilidad.fernandez_huerta(texto)
        if resfh > 0 and resfh <= 100:
            resultado['fh'].append(resfh)
            filaescala = Escalafh.objects.filter(inf__lte=resfh, sup__gte=resfh).first()
            resultado['fh'].append(filaescala.resultado)
            resultado['fh'].append(filaescala.color)
            resultado['fh'].append(filaescala.grado_escolar)

        resgu = legibilidad.gutierrez(texto)
        resultado['gu'].append(resgu)
        filaescala = Escalagu.objects.filter(inf__lte=resgu, sup__gte=resgu).first()
        resultado['gu'].append(filaescala.resultado)
        resultado['gu'].append(filaescala.color)

        resmu = legibilidad.mu(texto)
        resultado['mu'].append(resmu)
        filaescala = Escalamu.objects.filter(inf__lte=resmu, sup__gte=resmu).first()
        resultado['mu'].append(filaescala.resultado)
        resultado['mu'].append(filaescala.color)

        ressp = legibilidad.szigriszt_pazos(texto)
        resultado['sp'].append(ressp)
        filaescala = Escalasp.objects.filter(inf__lte=ressp, sup__gte=ressp).first()
        resultado['sp'].append(filaescala.resultado)
        resultado['sp'].append(filaescala.color)
        resultado['sp'].append(filaescala.tipopublicacion)
        resultado['sp'].append(filaescala.estudios)

        resin = ressp
        resultado['in'].append(resin)
        filaescala = Escalain.objects.filter(inf__lte=resin, sup__gte=resin).first()
        resultado['in'].append(filaescala.resultado)
        resultado['in'].append(filaescala.color)
        return resultado