"""Crie uma tupla para representar as informações de três
palestrantes, cada uma contendo o nome, o tema da
palestra e a instituição à qual estão vinculados.

Exiba na tela as informações do terceiro palestrante,
incluindo nome, tema da palestra e instituição."""

palestrantes = (
    ("Ana Silva", "Inteligência Artificial e o Futuro", "Universidade de São Paulo"),
    ("Carlos Mendes", "Gestão de Projetos Ágeis", "Fundação Getulio Vargas"),
    ("Mariana Rocha", "Desenvolvimento Sustentável", "Universidade Federal do Rio de Janeiro")
)

nome , tema, instituicao = palestrantes[2]
print(f"Nome: {nome}\ntema: {tema}\nInstutuição: {instituicao}")