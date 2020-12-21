class TesteCovid:
    def __init__(self, tose, febre, coriza, dor_peito, dor_garganta, falta_ar, falta_olfato, falta_apetite, cancaso,
                 gastrintestinais):
        self.tose = tose
        self.febre = febre
        self.coriza = coriza
        self.dor_peito = dor_peito
        self.dor_garganta = dor_garganta
        self.falta_ar = falta_ar
        self.falta_olfato = falta_olfato
        self.falta_apetite = falta_apetite
        self.cancaso = cancaso
        self.gastrintestinais = gastrintestinais

    def alterar_dados(self, tose, febre, coriza, dor_peito, dor_garganta, falta_ar, falta_olfato, falta_apetite, cancaso,
                 gastrintestinais):
        self.tose = tose
        self.febre = febre
        self.coriza = coriza
        self.dor_peito = dor_peito
        self.dor_garganta = dor_garganta
        self.falta_ar = falta_ar
        self.falta_olfato = falta_olfato
        self.falta_apetite = falta_apetite
        self.cancaso = cancaso
        self.gastrintestinais = gastrintestinais
        return

    def imprimir_dados(self):
        print(f' Tose: {self.tose}\n Febre: {self.febre}\n Coriza: {self.coriza}\n Dor no peito: {self.dor_peito}\n Dor '
              f'na garganta: {self.dor_garganta}\n Falta de ar: {self.falta_ar}\n Falta de olfato: {self.falta_olfato}\n '
              f'Falta de apetite: {self.falta_apetite}\n Cançaso: {self.cancaso}\n Problemas gastrintestinais: {self.gastrintestinais}')

    def probabilidade_positivo_negativo(self):
        pass