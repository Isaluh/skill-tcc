
"""
roi.py

Cálculo do Retorno sobre Investimento (ROI).

Projeto: Game Economic Engineering
"""

from math import isfinite


def _validate_number(name, value):
    """Valida se o valor é numérico e finito."""

    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{name} deve ser um número.")

    if not isfinite(value):
        raise ValueError(f"{name} deve ser finito.")


def calculate_roi(investment, total_returns):
    """
    Calcula o Retorno sobre Investimento (ROI).

    investment:
        Valor total investido.

    total_returns:
        Valor total dos retornos obtidos.

    Retorna:
        ROI em percentual.
        Valores positivos indicam retorno acima do investimento.
        Valores negativos indicam prejuízo.
    """

    _validate_number("investment", investment)
    _validate_number("total_returns", total_returns)

    if investment <= 0:
        raise ValueError("O investimento deve ser maior que zero.")

    roi = ((total_returns - investment) / investment) * 100

    return roi


if __name__ == "__main__":
    # Exemplo didático hipotético.
    investimento = 20000.00
    retorno_total = 28000.00

    resultado = calculate_roi(investimento, retorno_total)

    print(
        "========== EXEMPLO DIDÁTICO — ROI "
        "(NÃO REPRESENTA O CTRL THE WITCH) =========="
    )
    print(f"Investimento: R$ {investimento:.2f}")
    print(f"Retorno total: R$ {retorno_total:.2f}")
    print(f"ROI: {resultado:.2f}%")
