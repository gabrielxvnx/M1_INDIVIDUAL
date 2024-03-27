candidatos = [
    ("Gabriel", "e5_t10_p8_s8"),
    ("Vinicius", "e10_t7_p7_s8"),
    ("João", "e8_t5_p4_s9"),
    ("Lucas", "e2_t2_p2_s1"),
    ("Marcos", "e10_t10_p8_s9")
]

def selecionar_candidatos(candidatos, nota_minima_e, nota_minima_t, nota_minima_p, nota_minima_s):
    selecionados = []
    for candidato in candidatos:
        nome, notas = candidato
        nota_e, nota_t, nota_p, nota_s = [int(nota[1:]) for nota in notas.split('_')]
        
        if nota_e >= nota_minima_e and nota_t >= nota_minima_t and nota_p >= nota_minima_p and nota_s >= nota_minima_s:
            selecionados.append((nome, nota_e, nota_t, nota_p, nota_s))
    
    return selecionados

nota_minima_e = int(input("Digite a nota minima em Entrevista: "))
nota_minima_t = int(input("Digite a nota minima em Teste Teórico: "))
nota_minima_p = int(input("Digite a nota minima em Teste Prático: "))
nota_minima_s = int(input("Digite a nota minima em Avaliação Soft Skills: "))

selecionados = selecionar_candidatos(candidatos, nota_minima_e, nota_minima_t, nota_minima_p, nota_minima_s)

if selecionados:
    for candidato in selecionados:
        print(f"Nome: {candidato[0]}, Notas: {candidato[1]}, {candidato[2]}, {candidato[3]} e {candidato[4]}")
else:
    print("Nenhum candidato atende aos critérios")
