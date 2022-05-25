import pandas as pd
from django.shortcuts import render, HttpResponse
import json


def index(request):
    df = pd.read_csv('data.csv')

    json_records = df.reset_index().to_json(orient='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}

    return render(request, 'index.html', context)
