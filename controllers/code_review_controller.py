from main import rodar_analise

def analisar_com_codigo(codigo: str, descricao: str = "") -> str:
    """
    Recebe um código PHP Laravel e uma descrição opcional.
    Retorna o relatório de análise gerado pelos agentes do CrewAI.
    """
    return rodar_analise(codigo_php=codigo, descricao=descricao)
