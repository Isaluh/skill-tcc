
"""
agile_evm.py

Gerenciamento de Valor Agregado (GVA/EVM).

Indicadores:
- VP (PV): Valor Planejado
- VA (EV): Valor Agregado
- CR (AC): Custo Real
- IDC (CPI): Índice de Desempenho de Custos
- IDP (SPI): Índice de Desempenho de Prazo
- ENT (EAC): Estimativa no Término

Projeto: Game Economic Engineering
"""

from math import isfinite
from numbers import Real


def calculate_evm(planned_value, earned_value, actual_cost, bac):
    """
    Calcula os indicadores de Gerenciamento de Valor Agregado.

    planned_value: Valor Planejado (VP).
    earned_value: Valor Agregado (VA).
    actual_cost: Custo Real (CR).
    bac: Orçamento no Término.

    Valores monetários devem utilizar a mesma moeda.
    """

    values = [planned_value, earned_value, actual_cost, bac]

    if any(
        isinstance(value, bool) or not isinstance(value, Real)
        for value in values
    ):
        raise TypeError("VP, VA, CR e BAC devem ser valores numéricos.")

    if any(not isfinite(value) for value in values):
        raise ValueError("VP, VA, CR e BAC devem ser valores finitos.")

    if any(value < 0 for value in values):
        raise ValueError("Os valores não podem ser negativos.")

    if bac <= 0:
        raise ValueError("O orçamento no término deve ser positivo.")

    if planned_value > bac or earned_value > bac:
        raise ValueError("VP e VA não devem ultrapassar o orçamento total.")

    if actual_cost == 0:
        raise ValueError("O Custo Real deve ser maior que zero.")

    if planned_value == 0:
        raise ValueError("O Valor Planejado deve ser maior que zero.")

    if earned_value == 0:
        raise ValueError("O Valor Agregado deve ser maior que zero.")

    cpi = earned_value / actual_cost
    spi = earned_value / planned_value

    cv = earned_value - actual_cost
    sv = earned_value - planned_value

    # Estimativa de custo final mantendo a eficiência atual.
    eac = bac / cpi

    # Estimativa de prazo final considerando o desempenho atual.
    estimated_duration_factor = 1 / spi

    return {
        "planned_value": planned_value,
        "earned_value": earned_value,
        "actual_cost": actual_cost,
        "bac": bac,
        "cpi": cpi,
        "spi": spi,
        "cv": cv,
        "sv": sv,
        "eac": eac,
        "estimated_duration_factor": estimated_duration_factor
    }


def print_evm(report):
    """Exibe os indicadores GVA/EVM."""

    print("\n========== GERENCIAMENTO DE VALOR AGREGADO ==========")

    print(f"Valor Planejado (VP): R$ {report['planned_value']:.2f}")
    print(f"Valor Agregado (VA): R$ {report['earned_value']:.2f}")
    print(f"Custo Real (CR): R$ {report['actual_cost']:.2f}")

    print("\n========== INDICADORES ==========")

    print(f"IDC / CPI: {report['cpi']:.2f}")
    print(f"IDP / SPI: {report['spi']:.2f}")

    print(f"Variação de Custo: R$ {report['cv']:.2f}")
    print(f"Variação de Prazo: R$ {report['sv']:.2f}")

    print(f"Orçamento no Término (BAC): R$ {report['bac']:.2f}")
    print(f"Estimativa no Término (EAC): R$ {report['eac']:.2f}")

    print(
        "Fator estimado de duração:",
        f"{report['estimated_duration_factor']:.2f}"
    )

    if report["cpi"] > 1:
        print("\nDesempenho de custos: Favorável.")
    elif report["cpi"] < 1:
        print("\nDesempenho de custos: Desfavorável.")
    else:
        print("\nDesempenho de custos: Dentro do orçamento.")

    if report["spi"] > 1:
        print("Desempenho de prazo: Adiantado.")
    elif report["spi"] < 1:
        print("Desempenho de prazo: Atrasado.")
    else:
        print("Desempenho de prazo: Conforme planejado.")


if __name__ == "__main__":
    print(
        "\nExemplo didático hipotético — "
        "não representa o Ctrl the Witch."
    )

    report = calculate_evm(
        planned_value=24000,
        earned_value=22000,
        actual_cost=23000,
        bac=30000
    )

    print_evm(report)
