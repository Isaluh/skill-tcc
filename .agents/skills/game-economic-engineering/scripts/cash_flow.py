
"""
cash_flow.py

Modelagem de fluxo de caixa para projetos de software e jogos.

Projeto: Game Economic Engineering
"""


def calculate_cash_flow(
    initial_investment,
    revenues,
    operating_costs,
    taxes=None,
    capex=None
):
    """
    Calcula o fluxo de caixa por período.

    initial_investment: investimento inicial.
    revenues: receitas por período.
    operating_costs: custos operacionais por período.
    taxes: tributos por período.
    capex: investimentos adicionais por período.

    Retorna um dicionário com os resultados.
    """

    if initial_investment < 0:
        raise ValueError("O investimento inicial não pode ser negativo.")

    if not revenues:
        raise ValueError("Informe as receitas.")

    if len(revenues) != len(operating_costs):
        raise ValueError("Receitas e custos devem ter o mesmo tamanho.")

    periods = len(revenues)

    if taxes is None:
        taxes = [0.0] * periods

    if capex is None:
        capex = [0.0] * periods

    if len(taxes) != periods or len(capex) != periods:
        raise ValueError("Todos os dados devem possuir o mesmo número de períodos.")

    if any(value < 0 for value in revenues + operating_costs + taxes + capex):
        raise ValueError("Receitas, custos, tributos e CapEx devem ser não negativos.")

    cash_flows = [-initial_investment]
    accumulated = -initial_investment

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
        "initial_investment": initial_investment,
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
    """
    Descreve os dados atuais informados sem criar fluxos por período.

    O investimento em mão de obra é um custo econômico estimado e não é
    tratado como desembolso financeiro efetivo.
    """
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
        "\nLimitação: não é possível montar um fluxo líquido por período ou "
        "calcular saldo acumulado sem os custos e a periodicidade. "
        "A receita atual zero não foi projetada para períodos futuros, e "
        "custos desconhecidos não foram tratados como zero."
    )


def print_didactic_example():
    """Executa um exemplo hipotético, separado dos dados do Ctrl the Witch."""
    # Valores didáticos; não representam o Ctrl the Witch.
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
