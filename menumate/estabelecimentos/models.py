from django.db import models

class Estabelecimento(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Mesa(models.Model):
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)
    numero = models.IntegerField()
    ocupada = models.BooleanField(default=False)

    def __str__(self):
        return f"Mesa {self.numero} ({self.estabelecimento})"

    def verificar_ocupacao(self):
        return self.ocupada

class Garcon(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Menu(models.Model):
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class ItemMenu(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nome

class Comanda(models.Model):
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    garcon = models.ForeignKey(Garcon, on_delete=models.CASCADE)
    items = models.ManyToManyField(ItemMenu, through='ItemComanda')
    data_hora_abertura = models.DateTimeField(auto_now_add=True)
    data_hora_fechamento = models.DateTimeField(null=True, blank=True)
    valor_total = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    def __str__(self):
        return f"Comanda {self.id} (Mesa {self.mesa.numero})"

    def adicionar_item(self, item_menu, quantidade=1):
        # Verifica se a comanda está aberta
        if self.data_hora_fechamento is not None:
            raise ValueError('A comanda já foi fechada.')
        # Adiciona o item à comanda
        item_comanda, created = ItemComanda.objects.get_or_create(comanda=self, item_menu=item_menu)
        if not created:
            item_comanda.quantidade += quantidade
            item_comanda.save()
        # Atualiza o valor total da comanda
        self.atualizar_valor_total()

    def remover_item(self, item_menu, quantidade=1):
        # Verifica se a comanda está aberta
        if self.data_hora_fechamento is not None:
            raise ValueError('A comanda já foi fechada.')
        # Remove o item da comanda
        try:
            item_comanda = ItemComanda.objects.get(comanda=self, item_menu=item_menu)
            if item_comanda.quantidade > quantidade:
                item_comanda.quantidade -= quantidade
                item_comanda.save()
            else:
                item_comanda.delete()
        except ItemComanda.DoesNotExist:
            pass
        # Atualiza o valor total da comanda
        self.atualizar_valor_total()

    def atualizar_valor_total(self):
        total = 0
        for item_comanda in self.items.all():
            total += item_comanda.quantidade * item_comanda.item_menu.preco
        self.valor_total = total
        self.save()

class ItemComanda(models.Model):
    comanda = models.ForeignKey(Comanda, on_delete=models.CASCADE)
    item_menu = models.ForeignKey(ItemMenu, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)
