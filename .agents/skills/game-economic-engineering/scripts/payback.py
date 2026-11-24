
"""
payback.py

Cálculos de Payback Simples e Descontado.

Projeto: Game Economic Engineering
"""

from npv_irr import present_value


def simple_payback(cash_flows):
    """
    Calcula o período de recuperação simples.

    cash_flows:
        Lista começando pelo investimento inicial (período zero).

    Retorna:
        Número de períodos para recuperar o investimento.
        Retorna None se não houver recuperação.
    """

    if len(cash_flows) < 2:
        raise ValueError("Informe o investimento e pelo menos um fluxo.")

    if cash_flows[0] >= 0:
        raise ValueError("O fluxo inicial deve ser negativo.")

    if any(value < 0 for value in cash_flows[1:]):
        raise ValueError("Este método exige fluxos futuros não negativos.")

    accumulated = cash_flows[0]

    for period, flow in enumerate(cash_flows[1:], start=1):
        previous = accumulated
        accumulated += flow

        if accumulated >= 0:
            if flow == 0:
                return float(period)

            fraction = -previous / flow
            return (period - 1) + fraction

    return None


def discounted_payback(cash_flows, rate):
    """
    Calcula o Payback Descontado.

    rate:
        Taxa de desconto por período.

    Retorna:
        Número de períodos para recuperar o investimento
        considerando o valor do dinheiro no tempo.

        Retorna None se não houver recuperação.
    """

    if len(cash_flows) < 2:
        raise ValueError("Informe o investimento e pelo menos um fluxo.")

    if cash_flows[0] >= 0:
        raise ValueError("O fluxo inicial deve ser negativo.")

    if rate <= -1:
        raise ValueError("A taxa deve ser maior que -100%.")

    if any(value < 0 for value in cash_flows[1:]):
        raise ValueError("Este método exige fluxos futuros não negativos.")

    accumulated = cash_flows[0]

    for period, flow in enumerate(cash_flows[1:], start=1):
        discounted_flow = present_value(flow, rate, period)

        previous = accumulated
        accumulated += discounted_flow

        if accumulated >= 0:
            if discounted_flow == 0:
                return float(period)

            fraction = -previous / discounted_flow
            return (period - 1) + fraction

    return None


if __name__ == "__main__":
    investment = [-10000, 4000, 4000, 4000]
    rate = 0.10

    simple = simple_payback(investment)
    discounted = discounted_payback(investment, rate)

    print("Payback Simples:", simple, "períodos")
    print("Payback Descontado:", discounted, "períodos")

    if simple is None:
        print("O investimento não foi recuperado pelo método simples.")

    if discounted is None:
        print("O investimento não foi recuperado pelo método descontado.")
