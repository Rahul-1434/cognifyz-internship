import pandas as pd
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
from fpdf import FPDF
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

def upload_file(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        fs = FileSystemStorage()
        filename = fs.save(csv_file.name, csv_file)
        filepath = fs.path(filename)

        # Process CSV
        df = pd.read_csv(filepath)
        df['Total'] = df['Quantity'] * df['Price']
        summary = df.groupby('Product')['Total'].sum()

        # Plot and save image
        summary.plot(kind='bar', title="Sales by Product")
        plt.tight_layout()
        plot_path = fs.path('plot.png')
        plt.savefig(plot_path)
        plt.close()

        # Generate PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Sales Report", ln=1, align="C")
        for product, total in summary.items():
            pdf.cell(200, 10, txt=f"{product}: {total:.2f}", ln=1)
        pdf.image(plot_path, x=10, y=None, w=180)
        pdf_file_path = fs.path('report.pdf')
        pdf.output(pdf_file_path)

        return render(request, 'reports/success.html', {'pdf_url': fs.url('report.pdf')})

    return render(request, 'reports/upload.html')