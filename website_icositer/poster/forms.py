from django import forms

from poster.models import Poster

class POSTERForm(forms.ModelForm):
	class Meta:
		model = Poster
		fields =[
			'nama_ketua',
			'email',
			'no_telepon',
			'instansi',
			'prodi_ketua',
			'nama_anggota',
			'prodi_anggota',
			'subtema',
		]