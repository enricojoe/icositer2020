from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

from poster.models import Poster
from poster.forms import POSTERForm

def create(request):
	akun_form = POSTERForm(request.POST or None)

	if request.method == 'POST':
		if akun_form.is_valid():
			akun_form.save()

		return redirect('poster:list')

	context = {
		"page_title":"Registrasi Perlombaan",
		"akun_form":akun_form,
	}

	return render(request,'poster/form.html',context)

def list(request):
	semua_akun = Poster.objects.all()

	context = {
		'page_title':'Pendaftaran Perlombaan Poster',
		'semua_akun':semua_akun,
	}

	return render(request,'poster/poster.html',context)

import xlwt

def export_poster_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="poster.xls"'
 
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('POSTER')
 
    # Sheet header, first row
    row_num = 1
 
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
 
    columns = ['Nama Ketua', 'Email', 'No Telepon', 'Instansi', 'Prodi Ketua','Nama Anggota','Prodi Anggota','Subtema']
 
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
 
    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
 
    rows = Poster.objects.all().values_list('nama_ketua', 'email', 'no_telepon', 'instansi', 'prodi_ketua','nama_anggota','prodi_anggota','subtema')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
 
    wb.save(response)
    return response