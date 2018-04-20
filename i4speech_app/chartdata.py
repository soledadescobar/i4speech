from .models import Textos, Autores, Escalafh, Escalamu, Escalasp, Escalagu, Escalain, Cr, Fh, Gu, Mu, Sp, Ocasiones, Ejes
import django.utils.encoding
import django.http.request


class ChartData():

    @staticmethod
    def chart_data(indfil, autfil , ocfil , ejefil):
        if 'indice' not in indfil.data == {}:
            data = {'autor': [],'fh':[], 'drilldown':[],'color':[]}
        else:
             data = {'autor': [], 'drilldown':[], 'color':[]}
             if '1' in indfil.data.getlist('indice'): data.update({'cr': []})
             if '2' in indfil.data.getlist('indice'): data.update({'gu': []})
             if '3' in indfil.data.getlist('indice'): data.update({'fh': []})
             if '4' in indfil.data.getlist('indice'): data.update({'mu': []})
             if '5' in indfil.data.getlist('indice'): data.update({'sp': []})
        if  'nombre' not in autfil.data: lista_autores= Autores.objects.all().values('id')
        else: lista_autores= autfil.data.getlist('nombre')
        autores= Autores.objects.filter(pk__in=lista_autores)
        if 'ocasion' not in ocfil.data: lista_ocasiones = Ocasiones.objects.all().values('pk')
        else: lista_ocasiones= ocfil.data.getlist('ocasion')
        if 'eje' not in ejefil.data: lista_ejes = Ejes.objects.all().values('pk')
        else: lista_ejes = ejefil.data.getlist('eje')
        for autor in autores:
            au = django.utils.encoding.force_text(autor.nombre,'utf-8')
            data['autor'].append(au)
            data['drilldown'].append(au)
            if 'cr' in data.keys():
                data['cr'].append(Cr.prom_cr(autor.id,lista_ocasiones, lista_ejes))
                color = '#00bfff'
            if 'gu' in data.keys():
                prom_gu = Gu.prom_gu(autor.id, lista_ocasiones, lista_ejes)
                color = Escalagu.objects.filter( inf__lte=prom_gu, sup__gte=prom_gu ).first().color
                data['gu'].append(prom_gu)
            if 'fh' in data.keys():
                prom_fh= Fh.prom_fh(autor.id, lista_ocasiones, lista_ejes)
                color = Escalafh.objects.filter(inf__lte=prom_fh, sup__gte=prom_fh).first().color
                data['fh'].append(prom_fh)
            if 'mu' in data.keys():
                prom_mu = Mu.prom_mu(autor.id,lista_ocasiones, lista_ejes)
                color = Escalamu.objects.filter(inf__lte=prom_mu, sup__gte=prom_mu).first().color
                data['mu'].append(Mu.prom_mu(autor.id,lista_ocasiones, lista_ejes))
            if 'sp' in data.keys():
                prom_sp = Sp.prom_sp(autor.id, lista_ocasiones, lista_ejes)
                color = Escalasp.objects.filter(inf__lte=prom_sp, sup__gte=prom_sp).first().color
                data['sp'].append(Sp.prom_sp(autor.id, lista_ocasiones, lista_ejes))
            data['color'].append(color)
        return data

    @staticmethod
    def drilldowns(data, indfil, ocfil, ejefil):
        drilldown={'series':[]}
        for autor in data.get('autor'):
            serie = {'id': [], 'name': [], 'type':[], 'data': []}
            serie['id'] = autor
            if 'indice' not in indfil.data == {}:
                serie['name'] = 'FH'
            else:
                if '1' in indfil.data.getlist('indice'):  serie['name'] = 'CR'
                if '2' in indfil.data.getlist('indice'):  serie['name'] = 'GU'
                if '3' in indfil.data.getlist('indice'):  serie['name'] = 'FH'
                if '4' in indfil.data.getlist('indice'):  serie['name'] = 'MU'
                if '5' in indfil.data.getlist('indice'):  serie['name'] = 'SP'
            serie['type']= "column"
            if 'ocasion' not in ocfil.data and 'eje' not in ejefil.data:
                lista_textos = Textos.objects.filter(idautor__nombre=autor).order_by('fecha')
            else:
                if 'ocasion' not in ocfil.data and 'eje' in ejefil.data:
                    lista_textos = Textos.objects.filter(idautor__nombre=autor, ideje__in=ejefil.data.get("eje")).order_by('fecha')
                else:
                    if 'ocasion' in ocfil.data and 'eje' not in ejefil.data:
                        lista_textos = Textos.objects.filter(idautor__nombre=autor, idocasion__in=ocfil.data.getlist("ocasion")).order_by('fecha')
                    else:
                        lista_textos = Textos.objects.filter(idautor__nombre=autor, idocasion__in=ocfil.data.getlist("ocasion"),
                                             ideje__in=ejefil.data.getlist("eje")).order_by('fecha')
            if len(lista_textos) > 0:
                for texto in lista_textos:
                    if 'indice' not in indfil.data == {}:
                        color = Escalafh.objects.filter(inf__lte=texto.fh.resultado, sup__gte=texto.fh.resultado).first().color
                        textodata = {'fecha': texto.fecha.__str__(), 'y': texto.fh.resultado, 'name':texto.titulo, 'color': color}
                    else:
                        if '1' in indfil.data.getlist('indice'):  textodata = {'fecha': texto.fecha.__str__(), 'y': texto.cr.resultado, 'name':texto.titulo, 'color':'#00bfff' }
                        if '2' in indfil.data.getlist('indice'):
                            color = Escalagu.objects.filter(inf__lte=texto.gu.resultado, sup__gte=texto.gu.resultado).first().color
                            textodata = {'fecha': texto.fecha.__str__(), 'y': texto.gu.resultado, 'name':texto.titulo, 'color': color}
                        if '3' in indfil.data.getlist('indice'):
                            color = Escalafh.objects.filter(inf__lte=texto.fh.resultado, sup__gte=texto.fh.resultado).first().color
                            textodata = {'fecha': texto.fecha.__str__(), 'y': texto.fh.resultado, 'name':texto.titulo, 'color': color}
                        if '4' in indfil.data.getlist('indice'):
                            color = Escalamu.objects.filter(inf__lte=texto.mu.resultado, sup__gte=texto.mu.resultado).first().color
                            textodata = {'fecha': texto.fecha.__str__(), 'y': texto.mu.resultado, 'name':texto.titulo, 'color': color}
                        if '5' in indfil.data.getlist('indice'):
                            color = Escalasp.objects.filter(inf__lte=texto.sp.resultado, sup__gte=texto.sp.resultado).first().color
                            textodata = {'fecha': texto.fecha.__str__(), 'y': texto.sp.resultado, 'name':texto.titulo, 'color': color}
                    serie['data'].append(textodata)
                drilldown['series'].append(serie)
        return drilldown