
"""
npv_irr.py

Cálculos de Engenharia Econômica:
- Valor Presente (VP)
- Valor Futuro (VF)
- Valor Presente Líquido (VPL)
- Taxa Interna de Retorno (TIR)

Projeto: Game Economic Engineering
"""

def present_value(future_value, rate, periods):
    """Calcula o valor presente de um valor futuro."""
    if rate <= -1:
        raise ValueError("A taxa deve ser maior que -100%.")

    if periods < 0:
        raise ValueError("O período não pode ser negativo.")

    return future_value / ((1 + rate) ** periods)


def future_value(present_value, rate, periods):
    """Calcula o valor futuro de um valor presente."""
    if rate <= -1:
        raise ValueError("A taxa deve ser maior que -100%.")

    if periods < 0:
        raise ValueError("O período não pode ser negativo.")

    return present_value * ((1 + rate) ** periods)


def npv(cash_flows, rate):
    """
    Calcula o Valor Presente Líquido.

    cash_flows:
        Lista de fluxos começando pelo período zero.

    rate:
        Taxa de desconto por período.
    """
    if not cash_flows:
        raise ValueError("Informe os fluxos de caixa.")

    if rate <= -1:
        raise ValueError("A taxa deve ser maior que -100%.")

    return sum(
        value / ((1 + rate) ** period)
        for period, value in enumerate(cash_flows)
    )


def irr(cash_flows, tolerance=1e-7, max_iterations=1000):
    """
    Calcula a Taxa Interna de Retorno pelo método da bisseção.

    Retorna a taxa por período em formato decimal.

    Limitação:
    - Requer fluxos convencionais ou uma raiz que possa
      ser encontrada no intervalo pesquisado.
    - Fluxos com múltiplas mudanças de sinal podem possuir
      mais de uma TIR.
    """
    if len(cash_flows) < 2:
        raise ValueError("São necessários pelo menos dois fluxos.")

    if not any(value > 0 for value in cash_flows):
        raise ValueError("É necessário pelo menos um fluxo positivo.")

    if not any(value < 0 for value in cash_flows):
        raise ValueError("É necessário pelo menos um fluxo negativo.")

    def calculate_npv(rate):
        return npv(cash_flows, rate)

    low = -0.999999
    high = 1.0

    low_value = calculate_npv(low)
    high_value = calculate_npv(high)

    while low_value * high_value > 0 and high < 1_000_000:
        high *= 2
        high_value = calculate_npv(high)

    if low_value * high_value > 0:
        raise ValueError(
            "Não foi possível encontrar uma TIR no intervalo pesquisado."
        )

    for _ in range(max_iterations):
        middle = (low + high) / 2
        middle_value = calculate_npv(middle)

        if abs(middle_value) < tolerance:
            return middle

        if abs(high - low) < tolerance:
            return middle

        if low_value * middle_value < 0:
            high = middle
            high_value = middle_value
        else:
            low = middle
            low_value = middle_value

    raise RuntimeError("O cálculo da TIR não convergiu.")


if __name__ == "__main__":
    fluxos = [-10000, 4000, 4000, 4000]
    taxa = 0.10

    print("Valor Presente Líquido:", round(npv(fluxos, taxa), 2))
    print("Taxa Interna de Retorno:", round(irr(fluxos) * 100, 2), "%")
    print("Valor Presente de R$ 1.000:", round(
        present_value(1000, taxa, 2), 2
    ))
    print("Valor Futuro de R$ 1.000:", round(
        future_value(1000, taxa, 2), 2
    ))
