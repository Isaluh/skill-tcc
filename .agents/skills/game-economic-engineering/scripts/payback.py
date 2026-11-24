
"""
payback.py

Cálculos de Payback Simples e Descontado.

Projeto: Game Economic Engineering
"""

from math import isfinite
from npv_irr import present_value


def _validate_cash_flows(cash_flows):
    """Valida a sequência de fluxos de caixa."""

    if isinstance(cash_flows, (str, bytes)):
        raise TypeError("Os fluxos devem ser uma sequência numérica.")

    try:
        flows = tuple(cash_flows)
    except TypeError:
        raise TypeError("Os fluxos devem ser iteráveis.")

    if len(flows) < 2:
        raise ValueError("Informe o investimento e pelo menos um fluxo.")

    for index, value in enumerate(flows):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError(
                f"O fluxo da posição {index} deve ser um número."
            )

        if not isfinite(value):
            raise ValueError(
                f"O fluxo da posição {index} deve ser finito."
            )

    if flows[0] >= 0:
        raise ValueError("O fluxo inicial deve ser negativo.")

    if any(value < 0 for value in flows[1:]):
        raise ValueError(
            "Este método exige fluxos futuros não negativos."
        )

    return flows


def simple_payback(cash_flows):
    """
    Calcula o período de recuperação simples.

    cash_flows:
        Sequência começando pelo investimento inicial (período zero).

    Retorna:
        Número de períodos para recuperar o investimento.
        Retorna None se não houver recuperação.
    """

    flows = _validate_cash_flows(cash_flows)

    accumulated = flows[0]

    for period, flow in enumerate(flows[1:], start=1):
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
        Taxa de desconto decimal por período.

    Retorna:
        Número de períodos para recuperar o investimento
        considerando o valor do dinheiro no tempo.

        Retorna None se não houver recuperação.
    """

    flows = _validate_cash_flows(cash_flows)

    if isinstance(rate, bool) or not isinstance(rate, (int, float)):
        raise TypeError("A taxa deve ser um número.")

    if not isfinite(rate) or rate <= -1:
        raise ValueError("A taxa deve ser finita e maior que -100%.")

    accumulated = flows[0]

    for period, flow in enumerate(flows[1:], start=1):
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
    # Exemplo didático hipotético.
    investment = [-10000, 4000, 4000, 4000]
    rate = 0.10

    simple = simple_payback(investment)
    discounted = discounted_payback(investment, rate)

    print("========== EXEMPLO DIDÁTICO — PAYBACK ==========")
    print("Payback Simples:", simple, "períodos")
    print("Payback Descontado:", discounted, "períodos")

    if simple is None:
        print("O investimento não foi recuperado pelo método simples.")

    if discounted is None:
        print("O investimento não foi recuperado pelo método descontado.")
