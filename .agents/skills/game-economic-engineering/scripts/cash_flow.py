
"""
cash_flow.py

Modelagem de fluxo de caixa para projetos de software e jogos.

Projeto: Game Economic Engineering
"""

from math import isfinite
from numbers import Real


def _validate_money_series(name, values, periods=None):
    """Valida uma sequência de valores monetários não negativos."""
    if isinstance(values, (str, bytes)) or not isinstance(values, (list, tuple)):
        raise TypeError(f"{name} deve ser uma lista ou tupla.")

    if periods is not None and len(values) != periods:
        raise ValueError(
            f"{name} deve possuir exatamente {periods} períodos."
        )

    for index, value in enumerate(values, start=1):
        if isinstance(value, bool) or not isinstance(value, Real):
            raise TypeError(
                f"{name}, período {index}: informe um número."
            )

        if not isfinite(value) or value < 0:
            raise ValueError(
                f"{name}, período {index}: valor deve ser finito e não negativo."
            )

    return tuple(float(value) for value in values)


def calculate_cash_flow(
    initial_investment,
    revenues,
    operating_costs,
    taxes=None,
    capex=None
):
    """
    Calcula o fluxo de caixa por período.

    Tributos e CapEx não informados permanecem desconhecidos.
    Para assumir ausência desses custos, informe listas com zeros.

    Retorna um dicionário com os resultados e a situação dos dados.
    """

    if isinstance(initial_investment, bool) or not isinstance(
        initial_investment, Real
    ):
        raise TypeError("O investimento inicial deve ser numérico.")

    if not isfinite(initial_investment) or initial_investment < 0:
        raise ValueError(
            "O investimento inicial deve ser finito e não negativo."
        )

    revenues = _validate_money_series("revenues", revenues)
    if not revenues:
        raise ValueError("Informe pelo menos uma receita.")

    periods = len(revenues)

    operating_costs = _validate_money_series(
        "operating_costs", operating_costs, periods
    )

    taxes_informed = taxes is not None
    capex_informed = capex is not None

    if taxes_informed:
        taxes = _validate_money_series("taxes", taxes, periods)

    if capex_informed:
        capex = _validate_money_series("capex", capex, periods)

    if not taxes_informed or not capex_informed:
        return {
            "calculated": False,
            "initial_investment": float(initial_investment),
            "revenues": revenues,
            "operating_costs": operating_costs,
            "taxes": taxes,
            "capex": capex,
            "missing_data": [
                name for name, informed in (
                    ("taxes", taxes_informed),
                    ("capex", capex_informed),
                )
                if not informed
            ],
            "message": (
                "Fluxo incompleto: informe tributos e CapEx, "
                "ou informe listas de zeros quando forem comprovadamente nulos."
            ),
        }

    cash_flows = [-float(initial_investment)]
    accumulated = -float(initial_investment)
    details = []

    for period in range(periods):
        net_flow = (
            revenues[period]
            - operating_costs[period]
            - taxes[period]
            - capex[period]
        )

        accumulated += net_flow
        cash_flows.append(net_flow)

        details.append({
            "period": period + 1,
            "revenue": revenues[period],
            "operating_costs": operating_costs[period],
            "taxes": taxes[period],
            "capex": capex[period],
            "net_cash_flow": net_flow,
            "accumulated_cash_flow": accumulated
        })

    return {
        "calculated": True,
        "initial_investment": float(initial_investment),
        "cash_flows": cash_flows,
        "details": details,
        "total_revenue": sum(revenues),
        "total_operating_costs": sum(operating_costs),
        "total_taxes": sum(taxes),
        "total_capex": sum(capex),
        "final_balance": accumulated
    }


def print_cash_flow(report):
    """Exibe o fluxo de caixa organizado."""

    if not report["calculated"]:
        print("\n========== FLUXO DE CAIXA INCOMPLETO ==========")
        print(report["message"])
        print("Dados não informados:", ", ".join(report["missing_data"]))
        return

    print("\n========== FLUXO DE CAIXA ==========")

    print(f"Investimento inicial: R$ {report['initial_investment']:.2f}")

    for item in report["details"]:
        print(f"\nPeríodo {item['period']}")
        print(f"Receitas: R$ {item['revenue']:.2f}")
        print(f"Custos operacionais: R$ {item['operating_costs']:.2f}")
        print(f"Tributos: R$ {item['taxes']:.2f}")
        print(f"CapEx: R$ {item['capex']:.2f}")
        print(f"Fluxo líquido: R$ {item['net_cash_flow']:.2f}")
        print(f"Saldo acumulado: R$ {item['accumulated_cash_flow']:.2f}")

    print("\nReceita total:", f"R$ {report['total_revenue']:.2f}")
    print("Custos operacionais:", f"R$ {report['total_operating_costs']:.2f}")
    print("Tributos:", f"R$ {report['total_taxes']:.2f}")
    print("CapEx adicional:", f"R$ {report['total_capex']:.2f}")
    print("Saldo final:", f"R$ {report['final_balance']:.2f}")


def ctrl_the_witch_current_scenario():
    """Descreve os dados atuais informados sem criar fluxos por período."""
    return {
        "project": "Ctrl the Witch",
        "publication": {
            "platform": "itch.io",
            "price": "gratuito",
            "classification": "informado",
        },
        "labor_investment": {
            "amount": 10800.00,
            "classification": "estimado",
            "type": "custo econômico de oportunidade",
            "cash_disbursement": None,
        },
        "current_commercial_revenue": {
            "amount": 0.00,
            "classification": "informado",
            "sales": 0.00,
            "donations": 0.00,
        },
        "operating_costs": None,
        "taxes": None,
        "additional_capex": None,
        "periodicity": None,
        "cash_flows": None,
    }


def print_ctrl_the_witch_current_scenario(scenario):
    """Exibe os dados disponíveis e as limitações do fluxo de caixa atual."""
    print("\n========== FLUXO DE CAIXA — CTRL THE WITCH ==========")
    print(
        f"Publicação: {scenario['publication']['platform']} "
        f"{scenario['publication']['price']} "
        f"({scenario['publication']['classification']})."
    )
    print(
        "Investimento econômico estimado em mão de obra: "
        f"R$ {scenario['labor_investment']['amount']:.2f} "
        f"({scenario['labor_investment']['classification']})."
    )
    print(
        "Desembolso financeiro correspondente à mão de obra: "
        "não informado; o valor estimado não é presumido como pagamento."
    )
    print(
        "Receita comercial atual informada: "
        f"R$ {scenario['current_commercial_revenue']['amount']:.2f} "
        "(sem vendas nem doações)."
    )
    print("Custos operacionais: desconhecidos/não levantados.")
    print("Tributos: desconhecidos/não levantados.")
    print("CapEx adicional: desconhecido/não levantado.")
    print("Periodicidade e horizonte dos dados: não informados.")
    print(
        "\nLimitação: não é possível montar um fluxo líquido por período "
        "com os dados disponíveis. A receita atual zero não foi projetada "
        "para períodos futuros, e custos desconhecidos não foram tratados "
        "como zero."
    )


def print_didactic_example():
    """Executa um exemplo hipotético, separado dos dados do jogo."""
    report = calculate_cash_flow(
        initial_investment=10800,
        revenues=[5000, 7000, 9000],
        operating_costs=[1000, 1200, 1500],
        taxes=[500, 700, 900],
        capex=[0, 500, 0]
    )

    print("\nExemplo didático hipotético — não representa o Ctrl the Witch.")
    print_cash_flow(report)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Fluxo de caixa para projetos de jogos."
    )
    parser.add_argument(
        "--exemplo-didatico",
        action="store_true",
        help="Executa um exemplo hipotético, separado dos dados do jogo.",
    )
    arguments = parser.parse_args()

    if arguments.exemplo_didatico:
        print_didactic_example()
    else:
        print_ctrl_the_witch_current_scenario(
            ctrl_the_witch_current_scenario()
        )
