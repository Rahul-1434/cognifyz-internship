import os
import uuid
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pandas as pd
import matplotlib
matplotlib.use('Agg')

from django.shortcuts import render
from django.conf import settings

df = sns.load_dataset('iris')

def index(request):
    chart = ''
    subtype = ''
    image_url = ''
    plot_div = ''
    
    if request.method == 'POST':
        chart = request.POST.get('chart')
        subtype = request.POST.get('subtype')

        if chart == 'matplotlib':
            image_url = generate_matplotlib_plot(subtype)
        elif chart == 'seaborn':
            image_url = generate_seaborn_plot(subtype)
        elif chart == 'plotly':
            plot_div = generate_plotly_plot(subtype)

    return render(request, 'index.html', {
        'chart': chart,
        'subtype': subtype,
        'image_url': image_url,
        'plot_div': plot_div
    })


def generate_matplotlib_plot(subtype):
    fig, ax = plt.subplots()
    
    if subtype == 'hist':
        df['sepal_length'].hist(ax=ax)
    elif subtype == 'scatter':
        df.plot(kind='scatter', x='sepal_length', y='sepal_width', ax=ax)
    elif subtype == 'line':
        df.plot(kind='line', y='sepal_length', ax=ax)
    else:
        ax.text(0.5, 0.5, 'Invalid Subtype', ha='center')

    filename = f"{uuid.uuid4()}.png"
    path = os.path.join(settings.BASE_DIR, 'static', 'images', filename)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    plt.savefig(path)
    plt.close()
    return f'/static/images/{filename}'

def generate_seaborn_plot(subtype):
    plt.figure()
    
    if subtype == 'box':
        sns.boxplot(x='species', y='sepal_length', data=df)
    elif subtype == 'violin':
        sns.violinplot(x='species', y='sepal_length', data=df)
    elif subtype == 'heatmap':
        corr = df.corr(numeric_only=True)
        sns.heatmap(corr, annot=True, cmap='coolwarm')
    else:
        plt.text(0.5, 0.5, 'Invalid Subtype', ha='center')

    filename = f"{uuid.uuid4()}.png"
    path = os.path.join(settings.BASE_DIR, 'static', 'images', filename)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    plt.savefig(path)
    plt.close()
    return f'/static/images/{filename}'

def generate_plotly_plot(subtype):
    if subtype == 'scatter':
        fig = px.scatter(df, x='sepal_length', y='sepal_width', color='species')
    elif subtype == 'line':
        fig = px.line(df, x=df.index, y='sepal_length', color='species')
    elif subtype == 'box':
        fig = px.box(df, x='species', y='sepal_length')
    else:
        fig = px.scatter(title='Invalid Subtype')

    return fig.to_html(full_html=False)
