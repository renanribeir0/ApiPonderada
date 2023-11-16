class Animal:
    def __init__(self, nome, especie, felicidade=50):
        self.nome = nome
        self.especie = especie
        self.felicidade = felicidade
        self.alimento = False
    
    def alimentar(self):
        if self.alimento:
            self.felicidade += 10
            return f'{self.nome} está alimentado e feliz'
        else:
            return f'{self.nome} está com fome'
    
    def receber_visita(self):
        return self.felicidade * 0.1 
    
    def definir_felicidade(self, nivel):
        self.felicidade = nivel

class Recinto:
    def __init__(self, especie, animais=None):
        self.especie = especie
        if animais is None:
            self.animais = []
        else:
            self.animais = animais

    def adicionar_animal(self, animal):
        if animal.especie == self.especie:
            self.animais.append(animal)
            return f'{animal.nome} adicionado ao recinto de {self.especie}'
        else:
            return f'{animal.nome} não é da espécie deste recinto!'

    def alimentar_animais(self):
        for animal in self.animais:
            animal.alimento = True

    def calcular_felicidade_media(self):
        if not self.animais:
            return 0
        else:
            total_felicidade = sum(animal.felicidade for animal in self.animais)
            return total_felicidade / len(self.animais)

class Zoo:
    def __init__(self):
        self.recintos = []

    def criar_recinto(self, especie):
        novo_recinto = Recinto(especie)
        self.recintos.append(novo_recinto)
        return f'Recinto de {especie} criado'

    def adicionar_animal(self, animal, especie_recinto):
        for recinto in self.recintos:
            if recinto.especie == especie_recinto:
                return recinto.adicionar_animal(animal)
        return f'Recinto de {especie_recinto} não encontrado'

    def alimentar_recintos(self):
        for recinto in self.recintos:
            recinto.alimentar_animais()

    def receber_visitas(self):
        total_visitas = 0
        for recinto in self.recintos:
            felicidade_media = recinto.calcular_felicidade_media()
            total_visitas += felicidade_media * 10  
        return f'O zoológico recebeu {total_visitas} visitantes'


def main():
    zoológico = Zoo()

    vaca = Animal('zezé', 'vaca')
    gato = Animal('bichano', 'gato', 70)

    zoológico.criar_recinto('vaca')
    zoológico.criar_recinto('gato')

    print(zoológico.adicionar_animal(vaca, 'vaca'))
    print(zoológico.adicionar_animal(gato, 'gato'))

    zoológico.alimentar_recintos()

    print(zoológico.receber_visitas())

    print(vaca.alimentar())
    print(gato.alimentar())


if __name__ == "__main__":
    main()