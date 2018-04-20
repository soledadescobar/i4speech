
from .models import Fh, Cr, Mu, Gu, Sp


class ChartData(object):

    @classmethod
    def get_avg_by_indice(cls, indice):

        if indice == 'cr': d = Cr.prom_cr()
        data = {'dates': [], 'values': []}
        for avg in data:
            data['dates'].append(avg['record_date'].strftime('%m/%d'))
            data['values'].append(avg['avg_value'])


        return d