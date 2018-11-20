from django import forms

class TesouroForm(forms.ModelForm):
	class Meta:
		model = Tesouro
		fields = ['nome', 'quantidade', 'preco', 'img_tesouro']
		labels = {"nome": "Nome", "quantidade": "Quantidade", "preco": "Preco", "img_tesouro": "Imagem"}
