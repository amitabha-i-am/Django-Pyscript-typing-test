from django.shortcuts import render
from .models import Words
from django.shortcuts import render, redirect
import random


def index(request):
    separate_words = []
    text_words = Words.objects.filter(title='Русский')
    letter = ''
    for i in text_words:
        for j in i.text:
            if j != '|':
                letter += j
            else:
                separate_words.append(letter)
                letter = ''
    random.shuffle(separate_words)
    return render(request, 'main/index.html', {'text_words': separate_words, })
