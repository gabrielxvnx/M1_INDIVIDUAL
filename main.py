candidatos = [
    ("Gabriel", 5, 10, 8, 8),
    ("Vinicius", 10, 7, 7, 8),
    ("João", 8, 5, 4, 9),
    ("Lucas", 2, 2, 2, 1),
    ("Marcos", 10,10,8,9)
]

selecionados = []

nota_minima_e = int(input("Digite a nota minima em Entrevista:"))
nota_minima_t = int(input("Digite a nota minima em Teste Teórico:"))
nota_minima_p = int(input("Digite a nota minima em Teste Prático:"))
nota_minima_s = int(input("Digite a nota minima em Avaliação Soft Skills:"))

for candidato in candidatos:
    nome, nota_e, nota_t, nota_p, nota_s = candidato
    if nota_e >= nota_minima_e and nota_t >= nota_minima_t and nota_p >= nota_minima_p and nota_s >= nota_minima_s:
        print(candidato)
        selecionados.append(candidato)
if len(selecionados) == 0:
    print("Nenhum candidato atende aos criterios")
