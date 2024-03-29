from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.utils import timezone
from .forms import *
from .models import Piloto, Comissario, Aeronave, Passageiro, CompanhiaAerea, Funcionario, Passagem

class HomePageView(View):
    def get(self, request):
        voos = Voo.objects.all()
        return render(request, 'home.html', {'voos': voos})

class PilotoCreateView(View):
    def get(self, request):
        form = PilotoForm()
        return render(request, 'piloto_form.html', {'form': form})

    def post(self, request):
        form = PilotoForm(request.POST)
        if form.is_valid():
            piloto = form.save()
            return redirect('piloto_list')
        return render(request, 'piloto_form.html', {'form': form})

    def put(self, request, piloto_id):
        piloto = get_object_or_404(Piloto, pk=piloto_id)
        form = PilotoForm(request.POST, instance=piloto)
        if form.is_valid():
            form.save()
            return redirect('piloto_list')
        return render(request, 'piloto_form.html', {'form': form})

    def delete(self, request, piloto_id):
        piloto = get_object_or_404(Piloto, pk=piloto_id)
        piloto.delete()
        return redirect('piloto_list')

class ComissarioCreateView(View):
    def get(self, request):
        form = ComissarioForm()
        return render(request, 'comissario_form.html', {'form': form})

    def post(self, request):
        form = ComissarioForm(request.POST)
        if form.is_valid():
            comissario = form.save()
            return redirect('comissario_list')
        return render(request, 'comissario_form.html', {'form': form})

    def put(self, request, comissario_id):
        comissario = get_object_or_404(Comissario, pk=comissario_id)
        form = ComissarioForm(request.POST, instance=comissario)
        if form.is_valid():
            form.save()
            return redirect('comissario_list')
        return render(request, 'comissario_form.html', {'form': form})

    def delete(self, request, comissario_id):
        comissario = get_object_or_404(Comissario, pk=comissario_id)
        comissario.delete()
        return redirect('comissario_list')

class AeronaveCreateView(View):
    def get(self, request):
        form = AeronaveForm()
        return render(request, 'aeronave_form.html', {'form': form})

    def post(self, request):
        form = AeronaveForm(request.POST)
        if form.is_valid():
            aeronave = form.save()
            return redirect('aeronave_list')
        return render(request, 'aeronave_form.html', {'form': form})

    def put(self, request, aeronave_id):
        aeronave = get_object_or_404(Aeronave, pk=aeronave_id)
        form = AeronaveForm(request.POST, instance=aeronave)
        if form.is_valid():
            form.save()
            return redirect('aeronave_list')
        return render(request, 'aeronave_form.html', {'form': form})

    def delete(self, request, aeronave_id):
        aeronave = get_object_or_404(Aeronave, pk=aeronave_id)
        aeronave.delete()
        return redirect('aeronave_list')

class PassageiroCreateView(View):
    def get(self, request):
        form = PassageiroForm()
        return render(request, 'passageiro_form.html', {'form': form})

    def post(self, request):
        form = PassageiroForm(request.POST)
        if form.is_valid():
            passageiro = form.save()
            return redirect('passageiro_list')
        return render(request, 'passageiro_form.html', {'form': form})

    def put(self, request, passageiro_id):
        passageiro = get_object_or_404(Passageiro, pk=passageiro_id)
        form = PassageiroForm(request.POST, instance=passageiro)
        if form.is_valid():
            form.save()
            return redirect('passageiro_list')
        return render(request, 'passageiro_form.html', {'form': form})

    def delete(self, request, passageiro_id):
        passageiro = get_object_or_404(Passageiro, pk=passageiro_id)
        passageiro.delete()
        return redirect('passageiro_list')

class CompanhiaAereaCreateView(View):
    def get(self, request):
        form = CompanhiaAereaForm()
        return render(request, 'companhia_aerea_form.html', {'form': form})

    def post(self, request):
        form = CompanhiaAereaForm(request.POST)
        if form.is_valid():
            companhia_aerea = form.save()
            return redirect('companhia_aerea_list')
        return render(request, 'companhia_aerea_form.html', {'form': form})

    def put(self, request, companhia_id):
        companhia_aerea = get_object_or_404(CompanhiaAerea, pk=companhia_id)
        form = CompanhiaAereaForm(request.POST, instance=companhia_aerea)
        if form.is_valid():
            form.save()
            return redirect('companhia_aerea_list')
        return render(request, 'companhia_aerea_form.html', {'form': form})

    def delete(self, request, companhia_id):
        companhia_aerea = get_object_or_404(CompanhiaAerea, pk=companhia_id)
        companhia_aerea.delete()
        return redirect('companhia_aerea_list')

class FuncionarioCreateView(View):
    def get(self, request):
        form = FuncionarioForm()
        return render(request, 'funcionario_form.html', {'form': form})

    def post(self, request):
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            funcionario = form.save()
            return redirect('funcionario_list')
        return render(request, 'funcionario_form.html', {'form': form})

    def put(self, request, funcionario_id):
        funcionario = get_object_or_404(Funcionario, pk=funcionario_id)
        form = FuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            return redirect('funcionario_list')
        return render(request, 'funcionario_form.html', {'form': form})

    def delete(self, request, funcionario_id):
        funcionario = get_object_or_404(Funcionario, pk=funcionario_id)
        funcionario.delete()
        return redirect('funcionario_list')

class PassagemCreateView(View):
    template_name = 'passagem_form.html'
    
    def get(self, request, voo_id):
        voo = get_object_or_404(Voo, pk=voo_id)
        passagens_disponiveis = Passagem.objects.filter(voos__id=voo.id, disponivel=True)
        form = PassagemForm()
        passagem_selecionada = None
        form_passageiro = None

        if 'passagem' in request.GET:
            passagem_id = request.GET['passagem']
            passagem_selecionada = get_object_or_404(Passagem, id=passagem_id)
            form = PassagemForm(instance=passagem_selecionada)
            form_passageiro = PassageiroForm()  # Criando um formulário de passageiro vazio

        return render(request, self.template_name, {
            'form': form,
            'passagens_disponiveis': passagens_disponiveis,
            'passagem_selecionada': passagem_selecionada,
            'voo': voo,
            'form_passageiro': form_passageiro  # Enviando o formulário de passageiro para o template
        })

    def post(self, request, voo_id):
        voo = get_object_or_404(Voo, pk=voo_id)
        form = PassagemForm(request.POST)
        form_passageiro = PassageiroForm(request.POST)
        passagens_disponiveis = Passagem.objects.filter(voos__id=voo.id, disponivel=True)

        if form_passageiro.is_valid() and form.is_valid():
            passageiro = form_passageiro.save()
            passagem = form.save(commit=False)
            passagem.voo = voo
            passagem.passageiro = passageiro.id
            passagem.data_compra = timezone.now()
            passagem.disponivel = False
            passagem.save()
            return redirect('passagem_list')

        # Se os formulários não forem válidos, renderize o template novamente com os formulários e os dados do voo
        return render(request, self.template_name, {
            'form': form,
            'form_passageiro': form_passageiro,
            'passagens_disponiveis': passagens_disponiveis,
            'voo': voo,
            'errors': form.errors.items() 
        })

class PassagemListView(View):
    def get(self, request):
        passagens = Passagem.objects.all()
        return render(request, 'passagem_list.html', {'passagens': passagens})

class PassagemDetailView(View):
    def get(self, request, passagem_id):
        passagem = get_object_or_404(Passagem, pk=passagem_id)
        return render(request, 'passagem_detail.html', {'passagem': passagem})

    def put(self, request, passagem_id):
        passagem = get_object_or_404(Passagem, pk=passagem_id)
        form = PassagemForm(request.POST, instance=passagem)
        if form.is_valid():
            form.save()
            return redirect('passagem_list')
        return render(request, 'passagem_detail.html', {'form': form, 'passagem': passagem})

    def delete(self, request, passagem_id):
        passagem = get_object_or_404(Passagem, pk=passagem_id)
        passagem.delete()
        return redirect('passagem_list')

class PilotoListView(View):
    def get(self, request):
        pilotos = Piloto.objects.all()
        return render(request, 'piloto_list.html', {'pilotos': pilotos})

class ComissarioListView(View):
    def get(self, request):
        comissarios = Comissario.objects.all()
        return render(request, 'comissario_list.html', {'comissarios': comissarios})

class AeronaveListView(View):
    def get(self, request):
        aeronaves = Aeronave.objects.all()
        return render(request, 'aeronave_list.html', {'aeronaves': aeronaves})

class PassageiroListView(View):
    def get(self, request):
        passageiros = Passageiro.objects.all()
        return render(request, 'passageiro_list.html', {'passageiros': passageiros})

class CompanhiaAereaListView(View):
    def get(self, request):
        companhias_aereas = CompanhiaAerea.objects.all()
        return render(request, 'companhia_aerea_list.html', {'companhias_aereas': companhias_aereas})

class FuncionarioListView(View):
    def get(self, request):
        funcionarios = Funcionario.objects.all()
        return render(request, 'funcionario_list.html', {'funcionarios': funcionarios})

class PassagemListView(View):
    def get(self, request):
        passagens = Passagem.objects.all()
        return render(request, 'passagem_list.html', {'passagens': passagens})

class VooCreateView(View):
    def get(self, request):
        form = VooForm()
        return render(request, 'voo_form.html', {'form': form})

    def post(self, request):
        form = VooForm(request.POST)
        if form.is_valid():
            novo_voo = form.save()

            # Atualizar todas as passagens vinculadas a este voo
            for passagem in novo_voo.passagens.all():
                passagem.origem = novo_voo.origem
                passagem.destino = novo_voo.destino
                passagem.data_viagem = novo_voo.data
                passagem.valor = novo_voo.valor
                passagem.save()

            return redirect('home')
        return render(request, 'voo_form.html', {'form': form})

class VooListView(View):
    def get(self, request):
        voos = Voo.objects.all()
        return render(request, 'home.html', {'voos': voos})