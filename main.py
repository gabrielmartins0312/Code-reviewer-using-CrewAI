from dotenv import load_dotenv
from crewai import Agent, Task, Crew
import os

# Carrega variáveis do .env
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = os.getenv("OPENAI_MODEL_NAME")

# Agente 1: Estilo e boas práticas
analista_estilo = Agent(
    role="Analista de Estilo e Boas Práticas Laravel",
    goal="Avaliar se o código PHP segue boas práticas de estilo e Clean Code em projetos Laravel.",
    backstory=(
        "Você é um desenvolvedor experiente especializado em Laravel. "
        "Sua tarefa é revisar código PHP escrito para Laravel, analisando clareza, padronização, organização em camadas, nomeação e legibilidade. "
        "Você também sugere quando funções nativas do Laravel poderiam ser usadas em vez de implementações manuais."
    ),
    allow_delegation=False,
    verbose=True
)

# Agente 2: Segurança
analista_seguranca = Agent(
    role="Especialista em Segurança Laravel",
    goal="Identificar falhas de segurança comuns em código PHP Laravel.",
    backstory=(
        "Você é um analista de segurança com foco em Laravel. "
        "Sua missão é encontrar riscos como SQL Injection, XSS, CSRF, falhas de autenticação e exposição de dados."
    ),
    allow_delegation=False,
    verbose=True
)

# Agente 3: Refatoração
refatorador = Agent(
    role="Consultor de Refatoramento Laravel",
    goal="Sugerir melhorias e refatorar código PHP Laravel para torná-lo mais limpo e eficiente.",
    backstory=(
        "Você é especialista em Clean Code e SOLID. "
        "Sua tarefa é identificar duplicações, acoplamentos excessivos e oportunidades de uso de arquitetura Laravel moderna (como Requests, Services e Eloquent)."
    ),
    allow_delegation=False,
    verbose=True
)

# Agente 4: Editor final do relatório
editor_relatorio = Agent(
    role="Editor de Revisão de Código",
    goal="Compilar um relatório claro e profissional com todas as análises.",
    backstory=(
        "Você é responsável por consolidar todas as análises dos agentes em um relatório final bem estruturado, com recomendações práticas para o desenvolvedor. "
        "Certifique-se de incluir a função final corrigida no final do relatório."
    ),
    allow_delegation=False,
    verbose=True
)

# Função principal que executa os agentes com base no código e descrição fornecidos
def rodar_analise(codigo_php: str, descricao: str = "") -> str:
    # Junta a descrição com o código, se existir
    contexto = f"{descricao.strip()}\n\n{codigo_php}" if descricao else codigo_php

    tarefas = [
        Task(
            description=f"Analise de estilo e boas práticas no seguinte código PHP Laravel:\n\n{contexto}",
            expected_output="Lista de problemas de estilo, nomeação, duplicidade e uso incorreto de recursos do Laravel.",
            agent=analista_estilo
        ),
        Task(
            description=f"Análise de segurança no código PHP Laravel abaixo:\n\n{contexto}",
            expected_output="Lista de falhas de segurança encontradas e como corrigi-las.",
            agent=analista_seguranca
        ),
        Task(
            description=(
                f"Analise cuidadosamente o seguinte código PHP Laravel e sugira melhorias. "
                f"Para cada problema identificado, apresente o trecho original, o código refatorado e explique claramente o motivo da sugestão. "
                f"Depois de todas as sugestões, apresente a versão final da função completa com as correções aplicadas:\n\n{contexto}"
            ),
            expected_output=(
                "Lista de sugestões de melhoria com base em Clean Code e Laravel. "
                "Para cada sugestão, deve haver: 1) código original, 2) código melhorado, 3) explicação. "
                "Ao final, inclua a função inteira já com todas as melhorias aplicadas."
            ),
            agent=refatorador
        ),
        Task(
            description="Organize um relatório final claro com os apontamentos anteriores. Certifique-se de incluir a função corrigida sugerida pelo Consultor de Refatoramento no final do relatório.",
            expected_output="Relatório bem estruturado em português, com todas as análises e uma versão final da função corrigida ao fim.",
            agent=editor_relatorio
        )
    ]

    crew = Crew(
        agents=[analista_estilo, analista_seguranca, refatorador, editor_relatorio],
        tasks=tarefas,
        verbose=2
    )

    resultado = crew.kickoff()
    return resultado
