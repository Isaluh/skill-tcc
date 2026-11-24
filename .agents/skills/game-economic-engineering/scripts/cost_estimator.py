"""
Estimativa de custo de desenvolvimento para projetos de jogos e software.

O custo de oportunidade da mão de obra é separado dos desembolsos financeiros
adicionais informados pelo usuário.
"""

from collections.abc import Mapping
from math import isfinite


def _validate_nonnegative_number(name, value, allow_zero=True):
    """Valida um valor numérico finito e não negativo."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{name} deve ser um número.")

    if not isfinite(value) or value < 0 or (not allow_zero and value == 0):
        qualifier = "maior que zero" if not allow_zero else "não negativo"
        raise ValueError(f"{name} deve ser finito e {qualifier}.")


def estimate_development_cost(
    team_members,
    development_days,
    daily_team_hours,
    opportunity_cost_per_hour_per_member,
    additional_disbursements=None,
):
    """
    Estima horas de trabalho, custo de oportunidade e desembolsos informados.

    `daily_team_hours` representa as horas totais trabalhadas pela equipe por
    dia. `additional_disbursements` deve ser um mapeamento de categorias para
    valores monetários efetivamente pagos ou estimados, como licenças e assets.
    Quando não informado, os desembolsos permanecem desconhecidos, não zero.

    Retorna um dicionário com as horas, os custos separados e o subtotal
    econômico conhecido (mão de obra mais desembolsos informados).
    """
    if isinstance(team_members, bool) or not isinstance(team_members, int):
        raise TypeError("team_members deve ser um número inteiro.")
    if team_members <= 0:
        raise ValueError("team_members deve ser maior que zero.")

    if isinstance(development_days, bool) or not isinstance(development_days, int):
        raise TypeError("development_days deve ser um número inteiro.")
    if development_days <= 0:
        raise ValueError("development_days deve ser maior que zero.")

    _validate_nonnegative_number(
        "daily_team_hours", daily_team_hours, allow_zero=False
    )
    _validate_nonnegative_number(
        "opportunity_cost_per_hour_per_member",
        opportunity_cost_per_hour_per_member,
    )

    if additional_disbursements is not None:
        if not isinstance(additional_disbursements, Mapping):
            raise TypeError("additional_disbursements deve ser um mapeamento.")

        for category, amount in additional_disbursements.items():
            if not isinstance(category, str) or not category.strip():
                raise ValueError("As categorias de custos devem ter um nome.")
            _validate_nonnegative_number(
                f"additional_disbursements['{category}']", amount
            )

    total_team_hours = development_days * daily_team_hours
    hours_per_member = total_team_hours / team_members
    labor_opportunity_cost = (
        hours_per_member
        * team_members
        * opportunity_cost_per_hour_per_member
    )

    total_additional_disbursements = (
        sum(additional_disbursements.values())
        if additional_disbursements is not None
        else None
    )
    total_known_economic_cost = labor_opportunity_cost + (
        total_additional_disbursements or 0
    )

    return {
        "team_members": team_members,
        "development_days": development_days,
        "daily_team_hours": daily_team_hours,
        "total_team_hours": total_team_hours,
        "hours_per_member": hours_per_member,
        "opportunity_cost_per_hour_per_member": (
            opportunity_cost_per_hour_per_member
        ),
        "labor_opportunity_cost": labor_opportunity_cost,
        "additional_disbursements": (
            dict(additional_disbursements)
            if additional_disbursements is not None
            else None
        ),
        "total_additional_disbursements": total_additional_disbursements,
        "total_known_economic_cost": total_known_economic_cost,
    }


def _format_brl(amount):
    """Formata um valor monetário em reais no padrão brasileiro."""
    formatted = f"{amount:,.2f}"
    return formatted.replace(",", "X").replace(".", ",").replace("X", ".")


def print_development_cost_estimate(estimate):
    """Exibe a estimativa separando custo econômico e desembolsos."""
    print("\n========== ESTIMATIVA DE CUSTO DE DESENVOLVIMENTO ==========")
    print(f"Integrantes: {estimate['team_members']}")
    print(f"Dias de desenvolvimento: {estimate['development_days']}")
    print(f"Horas diárias da equipe: {estimate['daily_team_hours']:g}")
    print(f"Horas totais da equipe: {estimate['total_team_hours']:g}")
    print(f"Horas estimadas por integrante: {estimate['hours_per_member']:g}")
    print(
        "Custo de oportunidade da mão de obra: "
        f"R$ {_format_brl(estimate['labor_opportunity_cost'])}"
    )

    disbursements = estimate["additional_disbursements"]
    if disbursements is None:
        print("Desembolsos financeiros adicionais: não informados.")
        print("Subtotal adicional considerado: não calculado.")
    else:
        print("Desembolsos financeiros adicionais informados:")
        if disbursements:
            for category, amount in disbursements.items():
                print(f"- {category}: R$ {_format_brl(amount)}")
        else:
            print("- Nenhum.")
        print(
            "Total de desembolsos adicionais: "
            f"R$ {_format_brl(estimate['total_additional_disbursements'])}"
        )

    print(
        "Subtotal econômico conhecido: "
        f"R$ {_format_brl(estimate['total_known_economic_cost'])}"
    )
    if disbursements is None:
        print(
            "(Inclui somente o custo de oportunidade; "
            "custos adicionais não informados.)"
        )


if __name__ == "__main__":
    # Premissas estimadas fornecidas para o Ctrl the Witch.
    estimativa = estimate_development_cost(
        team_members=2,
        development_days=90,
        daily_team_hours=6,
        opportunity_cost_per_hour_per_member=20.00,
        additional_disbursements=None,
    )

    print_development_cost_estimate(estimativa)