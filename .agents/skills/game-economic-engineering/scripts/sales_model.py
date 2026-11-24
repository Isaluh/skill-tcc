"""Simulação de vendas, receita líquida e ponto de equilíbrio."""

from collections.abc import Mapping
from math import ceil, isfinite
from numbers import Real


def _validate_nonnegative_money(name, value):
    """Valida um valor monetário finito e não negativo."""
    if isinstance(value, bool) or not isinstance(value, Real):
        raise TypeError(f"{name} deve ser numérico.")
    if not isfinite(value) or value < 0:
        raise ValueError(f"{name} deve ser finito e não negativo.")
    return float(value)


def _validate_optional_rate(name, value):
    """Valida uma taxa opcional entre zero e um, mantendo None como desconhecido."""
    if value is None:
        return None
    rate = _validate_nonnegative_money(name, value)
    if rate > 1:
        raise ValueError(f"{name} deve estar entre zero e um.")
    return rate


def simulate_sales_scenarios(
    unit_price,
    monthly_copies_by_scenario,
    months_per_year=12,
):
    """
    Calcula cópias e receita bruta mensal/anual para cenários hipotéticos.

    Não desconta taxas, tributos, custos ou reembolsos. A quantidade de meses
    anuais é um parâmetro, permitindo explicitar o horizonte da simulação.
    """
    price = _validate_nonnegative_money("unit_price", unit_price)

    if (
        isinstance(months_per_year, bool)
        or not isinstance(months_per_year, int)
        or months_per_year <= 0
    ):
        raise ValueError("months_per_year deve ser um inteiro positivo.")

    if not isinstance(monthly_copies_by_scenario, Mapping):
        raise TypeError(
            "monthly_copies_by_scenario deve ser um mapeamento."
        )
    if not monthly_copies_by_scenario:
        raise ValueError("Informe pelo menos um cenário de vendas.")

    scenarios = {}
    for name, monthly_copies in monthly_copies_by_scenario.items():
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Cada cenário deve ter um nome.")
        if (
            isinstance(monthly_copies, bool)
            or not isinstance(monthly_copies, int)
            or monthly_copies < 0
        ):
            raise ValueError(
                f"A quantidade mensal de cópias em '{name}' "
                "deve ser um inteiro não negativo."
            )

        annual_copies = monthly_copies * months_per_year
        scenarios[name] = {
            "copies_per_month": monthly_copies,
            "copies_per_year": annual_copies,
            "gross_revenue_per_month": price * monthly_copies,
            "gross_revenue_per_year": price * annual_copies,
        }

    return {
        "unit_price": price,
        "months_per_year": months_per_year,
        "scenarios": scenarios,
    }


def calculate_net_revenue(
    gross_revenue,
    platform_share_rate=None,
    processor_percentage_rate=None,
    processor_fixed_fee_per_transaction=None,
    transaction_count=None,
    tax_amount=None,
):
    """
    Calcula receita após taxas conhecidas, sem supor taxas ou tributos.

    As taxas percentuais são aplicadas sobre a receita bruta. A taxa fixa do
    processador depende da quantidade informada de transações. `tax_amount`
    deve ser o valor total de tributos efetivamente informado para o período;
    a função não escolhe alíquotas nem base tributária.

    Retorna `None` para receita líquida sempre que faltar algum dado necessário.
    A receita após taxas, mas antes de tributos, pode ser calculada mesmo que
    `tax_amount` permaneça desconhecido. O resultado não é lucro do projeto:
    não inclui custos fixos, reembolsos, descontos, conversão cambial,
    chargebacks ou outros custos não fornecidos.
    """
    gross = _validate_nonnegative_money("gross_revenue", gross_revenue)
    platform_rate = _validate_optional_rate(
        "platform_share_rate", platform_share_rate
    )
    processor_rate = _validate_optional_rate(
        "processor_percentage_rate", processor_percentage_rate
    )

    if processor_fixed_fee_per_transaction is None:
        fixed_fee = None
    else:
        fixed_fee = _validate_nonnegative_money(
            "processor_fixed_fee_per_transaction",
            processor_fixed_fee_per_transaction,
        )

    if transaction_count is not None and (
        isinstance(transaction_count, bool)
        or not isinstance(transaction_count, int)
        or transaction_count < 0
    ):
        raise ValueError("transaction_count deve ser um inteiro não negativo.")

    taxes = (
        None
        if tax_amount is None
        else _validate_nonnegative_money("tax_amount", tax_amount)
    )

    platform_fee = (
        None if platform_rate is None else gross * platform_rate
    )
    processor_percentage_fee = (
        None if processor_rate is None else gross * processor_rate
    )

    missing_fee_inputs = []
    if platform_rate is None:
        missing_fee_inputs.append("platform_share_rate")
    if processor_rate is None:
        missing_fee_inputs.append("processor_percentage_rate")
    if fixed_fee is None:
        missing_fee_inputs.append("processor_fixed_fee_per_transaction")
        processor_fixed_fee = None
    elif fixed_fee == 0:
        processor_fixed_fee = 0.0
    elif transaction_count is None:
        missing_fee_inputs.append("transaction_count")
        processor_fixed_fee = None
    else:
        processor_fixed_fee = fixed_fee * transaction_count

    revenue_after_fees = None
    if not missing_fee_inputs:
        revenue_after_fees = (
            gross
            - platform_fee
            - processor_percentage_fee
            - processor_fixed_fee
        )

    missing_net_inputs = list(missing_fee_inputs)
    if taxes is None:
        missing_net_inputs.append("tax_amount")
    net_revenue = (
        None
        if revenue_after_fees is None or taxes is None
        else revenue_after_fees - taxes
    )

    return {
        "gross_revenue": gross,
        "platform_fee": platform_fee,
        "processor_percentage_fee": processor_percentage_fee,
        "processor_fixed_fee": processor_fixed_fee,
        "revenue_after_fees_before_taxes": revenue_after_fees,
        "tax_amount": taxes,
        "net_revenue": net_revenue,
        "missing_fee_inputs": missing_fee_inputs,
        "missing_net_inputs": missing_net_inputs,
    }


def calculate_break_even_units(fixed_cost, contribution_margin_per_unit):
    """
    Calcula cópias inteiras para recuperar custo fixo com margem conhecida.

    Se um dos dados estiver ausente, retorna resultado não calculável. Margem
    unitária nula ou negativa não permite atingir o ponto de equilíbrio por
    aumento de vendas.
    """
    missing_inputs = []
    if fixed_cost is None:
        missing_inputs.append("fixed_cost")
    if contribution_margin_per_unit is None:
        missing_inputs.append("contribution_margin_per_unit")
    if missing_inputs:
        return {
            "calculable": False,
            "units": None,
            "missing_inputs": missing_inputs,
            "message": "Faltam dados para calcular o ponto de equilíbrio.",
        }

    fixed = _validate_nonnegative_money("fixed_cost", fixed_cost)
    if isinstance(contribution_margin_per_unit, bool) or not isinstance(
        contribution_margin_per_unit, Real
    ):
        raise TypeError("contribution_margin_per_unit deve ser numérico.")
    if not isfinite(contribution_margin_per_unit):
        raise ValueError("contribution_margin_per_unit deve ser finito.")
    margin = float(contribution_margin_per_unit)
    if margin <= 0:
        return {
            "calculable": False,
            "units": None,
            "missing_inputs": [],
            "message": (
                "Margem de contribuição nula ou negativa: "
                "não há recuperação por vendas."
            ),
        }

    units = fixed / margin
    if not isfinite(units):
        raise OverflowError("O ponto de equilíbrio excede a faixa numérica.")

    return {
        "calculable": True,
        "units": ceil(units),
        "missing_inputs": [],
        "message": None,
    }
