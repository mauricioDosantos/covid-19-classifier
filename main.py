from modelos import TesteCovid
import csv
from sklearn.neural_network import MLPClassifier
from sklearn.svm import OneClassSVM


# variáveis de escopo global
dados = []  # ficará todos os dados do arquivos
base_treino = []  # ficará os dados do treinamento
base_teste = []  # ficará os dados do teste
resposta = []  # respostas aos dados de treinamento
resposta_teste = []  # respostas aos dados de teste


IA = MLPClassifier(verbose=False, max_iter=1000, tol=0.000010)  # iniciando a instância do classificador

def inicializar_var_com_csv():
    ficheiro = open('dados-pi-tratados.csv', newline='', encoding='utf-8')
    reader = csv.reader(ficheiro)  # leitura do arquivo
    for linha in reader:
        dados.append(linha)


# Nesta função o padrão das variáveis é 0, pois onde não trocar por 1 continua com 0, para assim ter uma lista completa.
def selecao(lista):
    assim = 0
    cori = 0
    disp = 0
    dist_g = 0
    dist_o = 0
    outros = 0
    tosse = 0
    febre = 0
    dor_g = 0
    dor_c = 0
    for string in lista:

        if 'Assintomático' in string:
            assim = 1
        elif 'Coriza' in string:
            cori = 1
        elif 'Dispineia' in string:
            disp = 1
        elif 'Distúrbuios Gustativos' in string:
            dist_g = 1
        elif 'Distúrbuios Olfativos' in string:
            dist_o = 1
        elif 'Dor de Cabeça' in string:
            dor_c = 1
        elif 'Dor de Garganta' in string:
            dor_g = 1
        elif 'Febre' in string:
            febre = 1
        elif 'Outros' in string:
            outros = 1
        elif 'Tosse' in string:
            tosse = 1

        if 'Positivo' in string:
            resp = 1
        elif 'Negativo' in string:
            resp = 0

    base = [assim, cori, disp, dist_g, dist_o, dor_c, dor_g, febre, outros, tosse]
    return base, resp


def separar_dados_para_treinamento():
    cont = 0

    for lista in dados:
        cont += 1
        if cont <= 256600:   # esta condição quer saber o ponto exato para parar de adicionar valores para o treinamento
            base, resp = selecao(lista)
            base_treino.append(base)
            resposta.append(resp)

        else:  # após a condição do if ser alcançada, sempre cairá aqui.
            baseT, respT = selecao(lista)
            base_teste.append(baseT)
            resposta_teste.append(respT)

    print('Fim da coleta')


def treinarIa():  # treinamento do algoritimo
    IA.fit(base_treino, resposta)


def testeIa():
    errou = 0
    acertou = 0
    print(len(base_teste))
    for index, lista in enumerate(base_teste):
        resultado = IA.predict([lista])
        # Na separação dos dados a as entradas foram gravadas na mesma ordem das respostas,
        # portanto a entrada está na mesma posição que a resposta
        if resultado != resposta_teste[index]:   # checa o resultado se corresponde a saída esperada.
            errou += 1
        else:
            acertou += 1
    print(f'Quantidade de erros {errou}\nQuantidade de acertos {acertou}')


def checarOutliers():  # aprendizado não supervisionado de teste
    cont = 0
    len(base_treino)  # 246776
    len(base_teste)  # os -1 foram de 40138
    clf = OneClassSVM(gamma='auto').fit(base_treino)
    print('Passou do treino')
    result = clf.predict(base_treino)
    print('Passou da predição')
    for value in result:
        if value == -1:
            cont += 1
    print('A quantidade de -1 é ', cont)


inicializar_var_com_csv()
separar_dados_para_treinamento()
treinarIa()
testeIa()