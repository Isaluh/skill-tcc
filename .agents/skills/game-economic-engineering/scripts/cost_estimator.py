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
    opportunity_cost_per_team_hour=None,
    additional_disbursements=None,
    *,
    opportunity_cost_per_hour_per_member=None,
):
    """
    Estima horas de trabalho, custo de oportunidade e desembolsos informados.

    `daily_team_hours` representa as horas totais trabalhadas pela equipe por
    dia. `opportunity_cost_per_team_hour` é o custo por hora da equipe inteira.
    O argumento nomeado `opportunity_cost_per_hour_per_member` é mantido por
    compatibilidade e tem o mesmo significado de custo por hora da equipe.
    `additional_disbursements` mapeia categorias para valores pagos ou
    estimados. Quando omitido, os desembolsos permanecem desconhecidos, não
    zero.

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
    if (
        opportunity_cost_per_team_hour is not None
        and opportunity_cost_per_hour_per_member is not None
    ):
        raise ValueError(
            "Informe o custo horário da equipe apenas uma vez."
        )
    if opportunity_cost_per_team_hour is None:
        opportunity_cost_per_team_hour = opportunity_cost_per_hour_per_member
    if opportunity_cost_per_team_hour is None:
        raise TypeError("Informe o custo de oportunidade por hora da equipe.")

    _validate_nonnegative_number(
        "opportunity_cost_per_team_hour", opportunity_cost_per_team_hour
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
        total_team_hours * opportunity_cost_per_team_hour
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
        "opportunity_cost_per_team_hour": opportunity_cost_per_team_hour,
        # Chave preservada para consumidores da interface anterior.
        "opportunity_cost_per_hour_per_member": (
            opportunity_cost_per_team_hour
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


def estimate_development_scenarios(
    team_members,
    calendar_weeks,
    workdays_per_week,
    daily_team_hours,
    opportunity_cost_per_team_hour,
):
    """
    Estima esforço retrospectivo por cenários de dias trabalhados na semana.

    Cada cenário assume a mesma média diária da equipe durante as semanas
    informadas. Os resultados são cenários, não registros de horas efetivas.
    """
    if (
        isinstance(calendar_weeks, bool)
        or not isinstance(calendar_weeks, int)
        or calendar_weeks <= 0
    ):
        raise ValueError("calendar_weeks deve ser um inteiro positivo.")

    if (
        isinstance(workdays_per_week, (str, bytes))
        or not isinstance(workdays_per_week, (list, tuple))
        or not workdays_per_week
    ):
        raise TypeError("workdays_per_week deve ser uma lista ou tupla não vazia.")

    if len(set(workdays_per_week)) != len(workdays_per_week):
        raise ValueError("workdays_per_week não deve conter valores duplicados.")

    scenarios = []
    for days_per_week in workdays_per_week:
        if (
            isinstance(days_per_week, bool)
            or not isinstance(days_per_week, int)
            or not 1 <= days_per_week <= 7
        ):
            raise ValueError("Cada cenário deve conter de 1 a 7 dias por semana.")

        estimated_workdays = calendar_weeks * days_per_week
        estimate = estimate_development_cost(
            team_members=team_members,
            development_days=estimated_workdays,
            daily_team_hours=daily_team_hours,
            opportunity_cost_per_team_hour=opportunity_cost_per_team_hour,
            additional_disbursements=None,
        )
        scenarios.append({
            "workdays_per_week": days_per_week,
            "estimated_workdays": estimated_workdays,
            "total_team_hours": estimate["total_team_hours"],
            "hours_per_member_if_equal": estimate["hours_per_member"],
            "labor_opportunity_cost": estimate["labor_opportunity_cost"],
            "classification": "cenário estimado retrospectivo",
        })

    return {
        "team_members": team_members,
        "calendar_weeks": calendar_weeks,
        "daily_team_hours": daily_team_hours,
        "opportunity_cost_per_team_hour": opportunity_cost_per_team_hour,
        "scenarios": scenarios,
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
    print(
        "Média por integrante se a divisão for igual: "
        f"{estimate['hours_per_member']:g}"
    )
    print(
        "Custo de oportunidade por hora da equipe: "
        f"R$ {_format_brl(estimate['opportunity_cost_per_team_hour'])}"
    )
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
    # Cenários retrospectivos; não são registros de horas efetivamente trabalhadas.
    scenarios = estimate_development_scenarios(
        team_members=2,
        calendar_weeks=39,
        workdays_per_week=[5, 6, 7],
        daily_team_hours=6,
        opportunity_cost_per_team_hour=20.00,
    )

    print("\nCENÁRIOS ESTIMADOS — CTRL THE WITCH")
    print("Nove meses são aproximados como 39 semanas.")
    print("A jornada de 6 horas e a taxa de R$ 20,00 são da equipe inteira.")
    print("Nenhum cenário representa apontamento histórico de horas.")
    for scenario in scenarios["scenarios"]:
        print(
            f"\n{scenario['workdays_per_week']} dias/semana: "
            f"{scenario['estimated_workdays']} dias estimados, "
            f"{scenario['total_team_hours']:g} horas de equipe, "
            f"R$ {_format_brl(scenario['labor_opportunity_cost'])} "
            "de custo de oportunidade."
        )