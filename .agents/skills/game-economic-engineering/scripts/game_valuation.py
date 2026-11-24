"""
Indicadores financeiros para avaliação de projetos de jogos digitais.

Os fluxos futuros devem ser valores líquidos por período e não incluem o
investimento inicial, que é recebido separadamente como parâmetro.
"""

from collections.abc import Iterable, Mapping
from math import isfinite
from numbers import Real

from npv_irr import irr as _irr
from npv_irr import npv as _npv
from payback import discounted_payback as _discounted_payback
from payback import simple_payback as _simple_payback
from roi import calculate_roi as _calculate_roi


def _validate_investment_and_flows(initial_investment, future_cash_flows):
    """Valida o investimento inicial e os fluxos líquidos futuros."""
    if isinstance(initial_investment, bool) or not isinstance(
        initial_investment, Real
    ):
        raise TypeError("O investimento inicial deve ser um número.")

    investment = float(initial_investment)
    if not isfinite(investment) or investment <= 0:
        raise ValueError("O investimento inicial deve ser finito e maior que zero.")

    if isinstance(future_cash_flows, (str, bytes, Mapping)):
        raise TypeError("Os fluxos futuros devem ser uma sequência de números.")
    if not isinstance(future_cash_flows, Iterable):
        raise TypeError("Os fluxos futuros devem ser iteráveis.")

    flows = tuple(future_cash_flows)
    if not flows:
        raise ValueError("Informe pelo menos um fluxo de caixa futuro.")

    validated_flows = []
    for period, flow in enumerate(flows, start=1):
        if isinstance(flow, bool) or not isinstance(flow, Real):
            raise TypeError(f"O fluxo do período {period} deve ser um número.")

        flow = float(flow)
        if not isfinite(flow):
            raise ValueError(f"O fluxo do período {period} deve ser finito.")
        validated_flows.append(flow)

    return investment, tuple(validated_flows)


def _validate_tma(tma):
    """Valida a TMA expressa como taxa decimal por período."""
    if isinstance(tma, bool) or not isinstance(tma, Real):
        raise TypeError("A TMA deve ser um número.")

    rate = float(tma)
    if not isfinite(rate) or rate < 0:
        raise ValueError("A TMA deve ser finita e não negativa.")
    return rate


def _cash_flows_with_initial_investment(initial_investment, future_cash_flows):
    """Monta a série de fluxos começando pelo investimento no período zero."""
    investment, flows = _validate_investment_and_flows(
        initial_investment, future_cash_flows
    )
    return investment, flows, (-investment, *flows)


def calculate_npv(initial_investment, future_cash_flows, tma):
    """Calcula o VPL usando a TMA por período e os fluxos líquidos futuros."""
    _, _, cash_flows = _cash_flows_with_initial_investment(
        initial_investment, future_cash_flows
    )
    return _npv(cash_flows, _validate_tma(tma))


def calculate_irr(initial_investment, future_cash_flows):
    """
    Calcula a TIR por período.

    Recusa fluxos com mais de uma mudança de sinal, pois podem resultar em
    múltiplas TIRs e o módulo existente retorna apenas uma raiz encontrada.
    """
    _, _, cash_flows = _cash_flows_with_initial_investment(
        initial_investment, future_cash_flows
    )
    signs = [1 if flow > 0 else -1 for flow in cash_flows if flow != 0]
    sign_changes = sum(
        signs[index] != signs[index - 1]
        for index in range(1, len(signs))
    )
    if sign_changes > 1:
        raise ValueError(
            "Fluxos com múltiplas mudanças de sinal podem ter mais de uma TIR."
        )
    return _irr(cash_flows)


def calculate_simple_payback(initial_investment, future_cash_flows):
    """Calcula o payback simples; retorna None se não recuperar no horizonte."""
    _, _, cash_flows = _cash_flows_with_initial_investment(
        initial_investment, future_cash_flows
    )
    return _simple_payback(cash_flows)


def calculate_discounted_payback(initial_investment, future_cash_flows, tma):
    """Calcula o payback descontado; retorna None se não recuperar no horizonte."""
    _, _, cash_flows = _cash_flows_with_initial_investment(
        initial_investment, future_cash_flows
    )
    return _discounted_payback(cash_flows, _validate_tma(tma))


def calculate_project_roi(initial_investment, future_cash_flows):
    """
    Calcula o ROI sobre o investimento inicial e a soma dos fluxos líquidos.

    O ROI não desconta os fluxos pelo tempo; seu horizonte é o informado
    implicitamente pela quantidade de fluxos futuros.
    """
    investment, flows = _validate_investment_and_flows(
        initial_investment, future_cash_flows
    )
    return _calculate_roi(investment, sum(flows))


def evaluate_game_project(
    initial_investment,
    future_cash_flows,
    tma,
    periodicity,
    data_classification,
):
    """
    Consolida VPL, TIR, paybacks e ROI para um único cenário.

    `future_cash_flows` contém fluxos líquidos futuros, um por período, sem
    incluir o investimento inicial. A TMA deve usar a mesma periodicidade.
    `data_classification` deve ser `real`, `estimado` ou `hipotético`.

    Indicadores que não puderem ser calculados retornam valor None e uma
    justificativa, sem ocultar as demais métricas válidas.
    """
    investment, flows = _validate_investment_and_flows(
        initial_investment, future_cash_flows
    )
    rate = _validate_tma(tma)

    if not isinstance(periodicity, str) or not periodicity.strip():
        raise ValueError("Informe a periodicidade dos fluxos.")
    if not isinstance(data_classification, str) or data_classification not in {
        "real",
        "estimado",
        "hipotético",
    }:
        raise ValueError(
            "A classificação dos dados deve ser real, estimado ou hipotético."
        )

    indicators = {
        "vpl": {
            "value": calculate_npv(investment, flows, rate),
            "status": "calculado",
            "message": None,
        },
        "roi": {
            "value": calculate_project_roi(investment, flows),
            "status": "calculado",
            "message": None,
        },
    }

    try:
        indicators["tir"] = {
            "value": calculate_irr(investment, flows),
            "status": "calculado",
            "message": None,
        }
    except (ValueError, RuntimeError) as error:
        indicators["tir"] = {
            "value": None,
            "status": "não calculável",
            "message": str(error),
        }

    for name, calculation in (
        ("payback_simples", calculate_simple_payback),
        ("payback_descontado", calculate_discounted_payback),
    ):
        try:
            if name == "payback_descontado":
                value = calculation(investment, flows, rate)
            else:
                value = calculation(investment, flows)

            if value is None:
                indicators[name] = {
                    "value": None,
                    "status": "não recuperado no horizonte",
                    "message": (
                        "Os fluxos informados não recuperam o investimento "
                        "no horizonte analisado."
                    ),
                }
            else:
                indicators[name] = {
                    "value": value,
                    "status": "calculado",
                    "message": None,
                }
        except ValueError as error:
            indicators[name] = {
                "value": None,
                "status": "não calculável",
                "message": str(error),
            }

    return {
        "initial_investment": investment,
        "future_cash_flows": flows,
        "tma": rate,
        "periodicity": periodicity.strip(),
        "data_classification": data_classification,
        "indicators": indicators,
    }


def ctrl_the_witch_current_scenario():
    """
    Representa somente a situação econômica atual informada do Ctrl the Witch.

    Não cria projeções nem trata a receita atual zerada como fluxo futuro.
    """
    not_calculable = {
        "value": None,
        "status": "não calculável de forma significativa",
    }

    return {
        "project": "Ctrl the Witch",
        "team_members": {
            "value": 2,
            "classification": "real (informado)",
        },
        "publication": {
            "platform": "itch.io",
            "price": "gratuito",
            "classification": "real (informado)",
        },
        "initial_investment": {
            "value": 10800.00,
            "classification": "estimado",
            "description": (
                "Custo de oportunidade estimado da mão de obra; "
                "não representa necessariamente desembolso financeiro."
            ),
        },
        "current_commercial_revenue": {
            "value": 0.00,
            "classification": "real (informado)",
            "description": "Sem vendas ou doações recebidas até o momento.",
        },
        "additional_costs": {
            "value": None,
            "classification": "não informado",
        },
        "future_cash_flows": None,
        "tma": None,
        "periodicity": None,
        "indicators": {
            "vpl": {
                **not_calculable,
                "message": (
                    "Faltam fluxos líquidos por período, horizonte de análise "
                    "e TMA. Receita atual zero não define fluxos futuros."
                ),
            },
            "tir": {
                **not_calculable,
                "message": (
                    "Não há série de fluxos de caixa por período com entradas "
                    "positivas para determinar uma TIR."
                ),
            },
            "payback_simples": {
                **not_calculable,
                "message": (
                    "Não há fluxos futuros por período para estimar quando "
                    "o investimento seria recuperado."
                ),
            },
            "payback_descontado": {
                **not_calculable,
                "message": (
                    "Além dos fluxos por período, faltam TMA e periodicidade "
                    "compatíveis."
                ),
            },
            "roi": {
                **not_calculable,
                "message": (
                    "A receita informada é zero, mas não há horizonte definido "
                    "nem custos totais e retornos líquidos para apurar ROI."
                ),
            },
        },
    }


def _format_brl(amount):
    """Formata um valor monetário em reais no padrão brasileiro."""
    formatted = f"{amount:,.2f}"
    return formatted.replace(",", "X").replace(".", ",").replace("X", ".")


def print_ctrl_the_witch_current_scenario(scenario):
    """Exibe os dados atuais do jogo e as limitações dos indicadores."""
    print("\n========== CTRL THE WITCH — CENÁRIO ATUAL ==========")
    print(
        f"Integrantes: {scenario['team_members']['value']} "
        f"({scenario['team_members']['classification']})"
    )
    print(
        "Publicação: "
        f"{scenario['publication']['platform']}, "
        f"{scenario['publication']['price']} "
        f"({scenario['publication']['classification']})"
    )
    print(
        "Investimento econômico estimado em mão de obra: "
        f"R$ {_format_brl(scenario['initial_investment']['value'])}"
    )
    print(
        "Receita comercial atual informada: "
        f"R$ {_format_brl(scenario['current_commercial_revenue']['value'])} "
        "(sem vendas nem doações)"
    )
    print("Custos adicionais: não informados; não foram assumidos como zero.")
    print("Fluxos futuros, TMA e horizonte de análise: não informados.")
    print("\nIndicadores:")

    for name, label in (
        ("vpl", "VPL"),
        ("tir", "TIR"),
        ("payback_simples", "Payback simples"),
        ("payback_descontado", "Payback descontado"),
        ("roi", "ROI"),
    ):
        metric = scenario["indicators"][name]
        print(f"- {label}: {metric['status']}. {metric['message']}")

    print(
        "\nA receita atual igual a zero é um dado observado/informado; "
        "não foi projetada para períodos futuros."
    )


def print_valuation_report(report):
    """Exibe os indicadores consolidados e suas unidades."""
    period = report["periodicity"]
    indicators = report["indicators"]

    print("\n========== AVALIAÇÃO FINANCEIRA DO PROJETO ==========")
    print(f"Classificação dos dados: {report['data_classification']}")
    print(f"Periodicidade dos fluxos e da TMA: {period}")
    print(f"Investimento inicial: R$ {_format_brl(report['initial_investment'])}")
    print(f"TMA por período: {report['tma'] * 100:.2f}%")
    print(f"Fluxos líquidos futuros: {report['future_cash_flows']}")

    for name, label in (
        ("vpl", "VPL"),
        ("tir", "TIR"),
        ("payback_simples", "Payback simples"),
        ("payback_descontado", "Payback descontado"),
        ("roi", "ROI"),
    ):
        metric = indicators[name]
        value = metric["value"]

        if value is None:
            print(f"{label}: {metric['status']} — {metric['message']}")
        elif name == "vpl":
            print(f"{label}: R$ {_format_brl(value)}")
        elif name == "tir":
            print(f"{label}: {value * 100:.2f}% por {period}")
        elif name == "roi":
            print(f"{label}: {value:.2f}%")
        else:
            print(f"{label}: {value:.2f} períodos de {period}")


def print_hypothetical_example():
    """Executa separadamente um exemplo didático, sem relação com o jogo."""
    relatorio = evaluate_game_project(
        initial_investment=30000.00,
        future_cash_flows=[8000.00, 10000.00, 14000.00, 16000.00],
        tma=0.12,
        periodicity="ano",
        data_classification="hipotético",
    )
    print("\nEste é um exemplo hipotético e não representa o Ctrl the Witch.")
    print_valuation_report(relatorio)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Indicadores financeiros para projetos de jogos."
    )
    parser.add_argument(
        "--exemplo-hipotetico",
        action="store_true",
        help="Executa a demonstração hipotética, separada dos dados do jogo.",
    )
    arguments = parser.parse_args()

    if arguments.exemplo_hipotetico:
        print_hypothetical_example()
    else:
        print_ctrl_the_witch_current_scenario(
            ctrl_the_witch_current_scenario()
        )