from django.shortcuts import render, redirect
from django.views import View
from django.db.models import F, ExpressionWrapper, DecimalField, Sum
from . import models

class ListaTesourosView(View):
    def get(self, request):
        lista_tesouros = models.Tesouro.objects.annotate(
            total = ExpressionWrapper( F('preco') * F('quantidade'),
                                        output_field = DecimalField(max_digits = 10, decimal_places = 2, blank = True )
                    )
        ).all()

        return render(
            request,
            template_name = 'lista_tesouros.html',
            context = dict( lista_tesouros = lista_tesouros, total_geral=lista_tesouros.aggregate(Sum('total'))['total__sum'] )
        )

class SalvarTesouroView(View):
    def get(self, request, tr=None)
        form = forms.TesouroForm()
        if tr:
            form = forms.TesouroForm(instance=models.Tesouro.objects.get(tr=tr))
        return render(request, template_name='salvar_tesouro.html', context=dict(form=form,action=f'/edit/{tr]' if tr else 'new'))


    def post(self, request, tr=None)
        form = forms.TesouroForm(request.POST, request.FILES, instance=models.Tesouro.objects.get(tr=tr) if tr else None)
        if form.is_valid():
            form.save()
            return redirect('list')
        return render(request, template_name='salvar_tesouro.html', context=dict(form=form), action=f'/edit/{tr]' if tr else 'new')

class DeletarTesouroView(view):
    def get(self, request, tr=None):
        models.Tesouro.objects.get(tr=tr).delete()
        return redirect('list')
