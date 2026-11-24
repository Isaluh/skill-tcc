
"""
npv_irr.py

Cálculos de Engenharia Econômica:
- Valor Presente (VP)
- Valor Futuro (VF)
- Valor Presente Líquido (VPL)
- Taxa Interna de Retorno (TIR)

Projeto: Game Economic Engineering
"""

from math import isfinite


def _validate_number(name, value):
    """Valida valores numéricos finitos."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{name} deve ser um número.")

    if not isfinite(value):
        raise ValueError(f"{name} deve ser finito.")


def present_value(future_value, rate, periods):
    """Calcula o valor presente de um valor futuro."""
    _validate_number("future_value", future_value)
    _validate_number("rate", rate)
    _validate_number("periods", periods)

    if rate <= -1:
        raise ValueError("A taxa deve ser maior que -100%.")

    if periods < 0:
        raise ValueError("O período não pode ser negativo.")

    return future_value / ((1 + rate) ** periods)


def future_value(present_value, rate, periods):
    """Calcula o valor futuro de um valor presente."""
    _validate_number("present_value", present_value)
    _validate_number("rate", rate)
    _validate_number("periods", periods)

    if rate <= -1:
        raise ValueError("A taxa deve ser maior que -100%.")

    if periods < 0:
        raise ValueError("O período não pode ser negativo.")

    return present_value * ((1 + rate) ** periods)


def npv(cash_flows, rate):
    """
    Calcula o Valor Presente Líquido.

    cash_flows:
        Sequência de fluxos começando pelo período zero.

    rate:
        Taxa de desconto por período.
    """
    _validate_number("rate", rate)

    if rate <= -1:
        raise ValueError("A taxa deve ser maior que -100%.")

    if isinstance(cash_flows, (str, bytes)):
        raise TypeError("Os fluxos devem ser uma sequência numérica.")

    try:
        flows = tuple(cash_flows)
    except TypeError:
        raise TypeError("Os fluxos devem ser iteráveis.")

    if not flows:
        raise ValueError("Informe os fluxos de caixa.")

    for index, value in enumerate(flows):
        _validate_number(f"cash_flows[{index}]", value)

    return sum(
        value / ((1 + rate) ** period)
        for period, value in enumerate(flows)
    )


def irr(cash_flows, tolerance=1e-7, max_iterations=1000):
    """
    Calcula a Taxa Interna de Retorno pelo método da bisseção.

    Retorna a taxa por período em formato decimal.

    Limitações:
    - Requer fluxos com pelo menos uma entrada e uma saída.
    - Não garante encontrar todas as possíveis raízes.
    - Fluxos com múltiplas mudanças de sinal podem possuir
      múltiplas TIRs.
    """
    if isinstance(max_iterations, bool) or not isinstance(
        max_iterations, int
    ):
        raise TypeError("max_iterations deve ser um número inteiro.")

    if max_iterations <= 0:
        raise ValueError("max_iterations deve ser maior que zero.")

    _validate_number("tolerance", tolerance)

    if tolerance <= 0:
        raise ValueError("tolerance deve ser maior que zero.")

    if isinstance(cash_flows, (str, bytes)):
        raise TypeError("Os fluxos devem ser uma sequência numérica.")

    try:
        flows = tuple(cash_flows)
    except TypeError:
        raise TypeError("Os fluxos devem ser iteráveis.")

    if len(flows) < 2:
        raise ValueError("São necessários pelo menos dois fluxos.")

    for index, value in enumerate(flows):
        _validate_number(f"cash_flows[{index}]", value)

    if not any(value > 0 for value in flows):
        raise ValueError("É necessário pelo menos um fluxo positivo.")

    if not any(value < 0 for value in flows):
        raise ValueError("É necessário pelo menos um fluxo negativo.")

    signs = [1 if value > 0 else -1 for value in flows if value != 0]

    sign_changes = sum(
        signs[index] != signs[index - 1]
        for index in range(1, len(signs))
    )

    if sign_changes > 1:
        raise ValueError(
            "Fluxos com múltiplas mudanças de sinal podem possuir "
            "mais de uma TIR."
        )

    def calculate_npv(rate):
        return npv(flows, rate)

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
    # Exemplo didático hipotético, sem relação com o Ctrl the Witch.
    fluxos = [-10000, 4000, 4000, 4000]
    taxa = 0.10

    print("========== EXEMPLO DIDÁTICO — NPV E IRR ==========")
    print("Valor Presente Líquido:", round(npv(fluxos, taxa), 2))
    print("Taxa Interna de Retorno:", round(irr(fluxos) * 100, 2), "%")
    print(
        "Valor Presente de R$ 1.000:",
        round(present_value(1000, taxa, 2), 2)
    )
    print(
        "Valor Futuro de R$ 1.000:",
        round(future_value(1000, taxa, 2), 2)
    )
