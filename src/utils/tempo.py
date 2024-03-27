from datetime import datetime

def obter_informacoes_tempo_atual():
    agora = datetime.now()

    meses = {
        1: "Janeiro",
        2: "Fevereiro",
        3: "Março",
        4: "Abril",
        5: "Maio",
        6: "Junho",
        7: "Julho",
        8: "Agosto",
        9: "Setembro",
        10: "Outubro",
        11: "Novembro",
        12: "Dezembro"
    }

    dias_semana = {
        0: "segunda-feira",
        1: "terça-feira",
        2: "quarta-feira",
        3: "quinta-feira",
        4: "sexta-feira",
        5: "sábado",
        6: "domingo"
    }

    return {
        "hora_minuto": agora.strftime('%H:%M'),
        "dia": agora.day,
        "mes": meses[agora.month],
        "ano": agora.year,
        "dia_semana": dias_semana[agora.weekday()]
    }

