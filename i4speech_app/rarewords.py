#!/usr/bin/env python3

# Legibilidad 2 (beta)
# Averigua la legibilidad de un texto
# Spanish readability calculations
# © 2016 Alejandro Muñoz Fernández

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

import re
from .models import Subtlex
from . import legibilidad

def rare_words(text):
    text =''.join(c if c not in map(str,range(0,10)) else "" for c in text)
    wordlist =  map(lambda x: x.lower(), re.sub("[^\w]", " ", text).split())
    rarewords = []
    for word in wordlist:
        if not Subtlex.objects.filter(palabra=word).exists() and word not in rarewords:
            rarewords.append(word)
    return rarewords

def dificult_words(text):
    text =''.join(c if c not in map(str,range(0,10)) else "" for c in text)
    wordlist =  map(lambda x: x.lower(), re.sub("[^\w]", " ", text).split())
    worddb = Subtlex.objects.filter(palabra__in=wordlist).values('palabra', 'freqpermillion').order_by('freqpermillion')[:30]
    rarewords =  [entry for entry in worddb]
    return rarewords