"""Testes de regressão dos cálculos financeiros da Skill."""

import math
import sys
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path


SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

from agile_evm import calculate_evm
from cash_flow import (
    calculate_cash_flow,
    ctrl_the_witch_current_scenario as cash_flow_current_scenario,
)
from cost_estimator import (
    estimate_development_cost,
    estimate_development_scenarios,
)
from game_valuation import (
    ctrl_the_witch_current_scenario,
    evaluate_game_project,
    print_hypothetical_example,
)
from npv_irr import future_value, irr, npv, present_value
from payback import discounted_payback, simple_payback
from roi import calculate_roi
from sales_model import (
    calculate_break_even_units,
    calculate_net_revenue,
    simulate_sales_scenarios,
)


class CostEstimatorTests(unittest.TestCase):
    def test_calcula_horas_e_custo_de_oportunidade_para_entradas_genericas(self):
        estimate = estimate_development_cost(2, 90, 6, 20)

        self.assertEqual(estimate["total_team_hours"], 540)
        self.assertEqual(estimate["hours_per_member"], 270)
        self.assertEqual(estimate["labor_opportunity_cost"], 10800)
        self.assertIsNone(estimate["total_additional_disbursements"])

    def test_cenarios_retrospectivos_de_nove_meses_por_dias_semanais(self):
        result = estimate_development_scenarios(
            team_members=2,
            calendar_weeks=39,
            workdays_per_week=[5, 6, 7],
            daily_team_hours=6,
            opportunity_cost_per_team_hour=20,
        )

        self.assertEqual(
            [
                (
                    item["estimated_workdays"],
                    item["total_team_hours"],
                    item["labor_opportunity_cost"],
                )
                for item in result["scenarios"]
            ],
            [(195, 1170, 23400), (234, 1404, 28080), (273, 1638, 32760)],
        )
        self.assertTrue(all(
            item["classification"] == "cenário estimado retrospectivo"
            for item in result["scenarios"]
        ))

    def test_rejeita_cenarios_de_esforco_invalidos(self):
        with self.subTest("semanas inválidas"):
            with self.assertRaises(ValueError):
                estimate_development_scenarios(2, 0, [5], 6, 20)
        with self.subTest("dias repetidos"):
            with self.assertRaises(ValueError):
                estimate_development_scenarios(2, 39, [5, 5], 6, 20)
        with self.subTest("mais de sete dias"):
            with self.assertRaises(ValueError):
                estimate_development_scenarios(2, 39, [8], 6, 20)

    def test_calcula_esforco_com_varios_integrantes_e_desembolsos(self):
        estimate = estimate_development_cost(
            team_members=4,
            development_days=2,
            daily_team_hours=10,
            opportunity_cost_per_hour_per_member=15,
            additional_disbursements={"licencas": 100, "assets": 250},
        )

        self.assertEqual(estimate["total_team_hours"], 20)
        self.assertEqual(estimate["hours_per_member"], 5)
        self.assertEqual(estimate["labor_opportunity_cost"], 300)
        self.assertEqual(estimate["total_additional_disbursements"], 350)
        self.assertEqual(estimate["total_known_economic_cost"], 650)

    def test_nao_trata_desembolsos_nao_informados_como_zero(self):
        estimate = estimate_development_cost(1, 2, 5, 10)

        self.assertIsNone(estimate["additional_disbursements"])
        self.assertIsNone(estimate["total_additional_disbursements"])
        self.assertEqual(estimate["total_known_economic_cost"], 100)

    def test_rejeita_parametros_e_desembolsos_invalidos(self):
        with self.subTest("integrantes não inteiros"):
            with self.assertRaises(TypeError):
                estimate_development_cost(2.5, 10, 5, 20)
        with self.subTest("dias não positivos"):
            with self.assertRaises(ValueError):
                estimate_development_cost(2, 0, 5, 20)
        with self.subTest("horas diárias não positivas"):
            with self.assertRaises(ValueError):
                estimate_development_cost(2, 10, 0, 20)
        with self.subTest("custo por hora negativo"):
            with self.assertRaises(ValueError):
                estimate_development_cost(2, 10, 5, -1)
        with self.subTest("desembolso negativo"):
            with self.assertRaises(ValueError):
                estimate_development_cost(2, 10, 5, 20, {"assets": -1})
        with self.subTest("categoria vazia"):
            with self.assertRaises(ValueError):
                estimate_development_cost(2, 10, 5, 20, {" ": 1})
        with self.subTest("mapeamento inválido"):
            with self.assertRaises(TypeError):
                estimate_development_cost(2, 10, 5, 20, [1])
        with self.subTest("valor infinito"):
            with self.assertRaises(ValueError):
                estimate_development_cost(2, 10, 5, math.inf)


class CashFlowTests(unittest.TestCase):
    def test_calcula_fluxos_liquidos_e_saldo_acumulado(self):
        report = calculate_cash_flow(
            initial_investment=1000,
            revenues=[600, 800],
            operating_costs=[100, 150],
            taxes=[50, 70],
            capex=[25, 0],
        )

        self.assertTrue(report["calculated"])
        self.assertEqual(report["cash_flows"], [-1000, 425, 580])
        self.assertEqual(
            [item["accumulated_cash_flow"] for item in report["details"]],
            [-575, 5],
        )
        self.assertEqual(report["total_revenue"], 1400)
        self.assertEqual(report["total_operating_costs"], 250)
        self.assertEqual(report["total_taxes"], 120)
        self.assertEqual(report["total_capex"], 25)
        self.assertEqual(report["final_balance"], 5)

    def test_dados_opcionais_ausentes_deixam_fluxo_incompleto(self):
        args = (100, [150], [20])
        both_missing = calculate_cash_flow(*args)
        taxes_missing = calculate_cash_flow(*args, capex=[0])
        capex_missing = calculate_cash_flow(*args, taxes=[0])

        self.assertFalse(both_missing["calculated"])
        self.assertEqual(both_missing["missing_data"], ["taxes", "capex"])
        self.assertEqual(taxes_missing["missing_data"], ["taxes"])
        self.assertEqual(capex_missing["missing_data"], ["capex"])
        self.assertIsNone(both_missing["taxes"])
        self.assertIsNone(both_missing["capex"])

    def test_rejeita_investimento_e_series_negativas(self):
        valid = dict(
            revenues=[100],
            operating_costs=[10],
            taxes=[0],
            capex=[0],
        )
        with self.subTest("investimento negativo"):
            with self.assertRaises(ValueError):
                calculate_cash_flow(initial_investment=-1, **valid)
        with self.subTest("receita negativa"):
            with self.assertRaises(ValueError):
                calculate_cash_flow(
                    initial_investment=0,
                    **{**valid, "revenues": [-1]},
                )
        with self.subTest("custo negativo"):
            with self.assertRaises(ValueError):
                calculate_cash_flow(
                    initial_investment=0,
                    **{**valid, "operating_costs": [-1]},
                )
        with self.subTest("tributo negativo"):
            with self.assertRaises(ValueError):
                calculate_cash_flow(
                    initial_investment=0,
                    **{**valid, "taxes": [-1]},
                )
        with self.subTest("CapEx negativo"):
            with self.assertRaises(ValueError):
                calculate_cash_flow(
                    initial_investment=0,
                    **{**valid, "capex": [-1]},
                )

    def test_rejeita_periodos_vazios_ou_inconsistentes(self):
        with self.subTest("sem períodos"):
            with self.assertRaises(ValueError):
                calculate_cash_flow(100, [], [], taxes=[], capex=[])
        with self.subTest("comprimentos divergentes"):
            with self.assertRaises(ValueError):
                calculate_cash_flow(100, [100, 200], [10], taxes=[0, 0], capex=[0, 0])
        with self.subTest("tipo de série inválido"):
            with self.assertRaises(TypeError):
                calculate_cash_flow(100, "100", [10], taxes=[0], capex=[0])


class PresentValueAndReturnTests(unittest.TestCase):
    def test_vp_e_vf_usam_taxa_e_periodo(self):
        self.assertAlmostEqual(present_value(121, 0.1, 2), 100)
        self.assertAlmostEqual(future_value(100, 0.1, 2), 121)

    def test_vpl_positivo_negativo_e_zero(self):
        self.assertAlmostEqual(npv([-1000, 700, 600], 0.1), 132.2314049587)
        self.assertAlmostEqual(npv([-1000, 400], 0.1), -636.3636363636)
        self.assertAlmostEqual(npv([-1000, 1100], 0.1), 0)

    def test_tir_conhecida(self):
        self.assertAlmostEqual(irr([-1000, 1100]), 0.1, places=6)

    def test_tir_sem_solucao_ou_com_multiplas_mudancas_de_sinal(self):
        with self.subTest("sem fluxo positivo"):
            with self.assertRaises(ValueError):
                irr([-100, 0])
        with self.subTest("mais de uma TIR possível"):
            with self.assertRaises(ValueError):
                irr([-100, 230, -132])

    def test_rejeita_taxas_e_series_invalidas(self):
        with self.subTest("taxa de VPL menor que o domínio"):
            with self.assertRaises(ValueError):
                npv([-100, 110], -1)
        with self.subTest("taxa não finita"):
            with self.assertRaises(ValueError):
                npv([-100, 110], math.nan)
        with self.subTest("taxa não numérica"):
            with self.assertRaises(TypeError):
                npv([-100, 110], "10%")
        with self.subTest("VP com período negativo"):
            with self.assertRaises(ValueError):
                present_value(100, 0.1, -1)
        with self.subTest("fluxo vazio"):
            with self.assertRaises(ValueError):
                npv([], 0.1)


class PaybackTests(unittest.TestCase):
    def test_payback_simples_com_interpolacao(self):
        self.assertAlmostEqual(simple_payback([-100, 60, 60]), 5 / 3)

    def test_payback_descontado_com_interpolacao(self):
        self.assertAlmostEqual(
            discounted_payback([-100, 60, 60], 0.1),
            23 / 12,
        )

    def test_investimento_nao_recuperado_no_horizonte(self):
        self.assertIsNone(simple_payback([-100, 20, 20]))
        self.assertIsNone(discounted_payback([-100, 20, 20], 0.1))

    def test_rejeita_fluxos_e_taxas_invalidas(self):
        with self.subTest("investimento inicial não negativo"):
            with self.assertRaises(ValueError):
                simple_payback([0, 100])
        with self.subTest("fluxo futuro negativo"):
            with self.assertRaises(ValueError):
                simple_payback([-100, 120, -20])
        with self.subTest("série curta"):
            with self.assertRaises(ValueError):
                simple_payback([-100])
        with self.subTest("taxa descontada inválida"):
            with self.assertRaises(ValueError):
                discounted_payback([-100, 120], -1)


class RoiTests(unittest.TestCase):
    def test_roi_positivo(self):
        self.assertAlmostEqual(calculate_roi(100, 150), 50)

    def test_roi_negativo(self):
        self.assertAlmostEqual(calculate_roi(100, 70), -30)

    def test_roi_igual_a_zero(self):
        self.assertAlmostEqual(calculate_roi(100, 100), 0)

    def test_rejeita_investimento_zero_e_entradas_invalidas(self):
        with self.subTest("investimento zero"):
            with self.assertRaises(ValueError):
                calculate_roi(0, 100)
        with self.subTest("investimento negativo"):
            with self.assertRaises(ValueError):
                calculate_roi(-1, 100)
        with self.subTest("retorno não numérico"):
            with self.assertRaises(TypeError):
                calculate_roi(100, "150")
        with self.subTest("valor não finito"):
            with self.assertRaises(ValueError):
                calculate_roi(100, math.inf)


class EarnedValueTests(unittest.TestCase):
    def test_calcula_cpi_spi_variacoes_e_eac(self):
        result = calculate_evm(
            planned_value=8000,
            earned_value=7000,
            actual_cost=7500,
            bac=10800,
        )

        self.assertAlmostEqual(result["cpi"], 7000 / 7500)
        self.assertAlmostEqual(result["spi"], 7000 / 8000)
        self.assertEqual(result["cv"], -500)
        self.assertEqual(result["sv"], -1000)
        self.assertAlmostEqual(result["eac"], 10800 / (7000 / 7500))
        self.assertAlmostEqual(result["estimated_duration_factor"], 8000 / 7000)

    def test_rejeita_divisores_zero(self):
        for field in ("actual_cost", "planned_value", "earned_value"):
            values = {
                "planned_value": 100,
                "earned_value": 80,
                "actual_cost": 90,
                "bac": 120,
            }
            values[field] = 0
            with self.subTest(field=field):
                with self.assertRaises(ValueError):
                    calculate_evm(**values)

    def test_rejeita_valores_negativos_e_acima_do_orcamento(self):
        with self.subTest("valor negativo"):
            with self.assertRaises(ValueError):
                calculate_evm(100, 80, -1, 120)
        with self.subTest("VP acima do BAC"):
            with self.assertRaises(ValueError):
                calculate_evm(121, 80, 90, 120)
        with self.subTest("BAC zero"):
            with self.assertRaises(ValueError):
                calculate_evm(100, 80, 90, 0)

    def test_rejeita_entradas_nao_finitas_e_nao_numericas(self):
        with self.subTest("VP NaN"):
            with self.assertRaises(ValueError):
                calculate_evm(math.nan, 80, 90, 120)
        with self.subTest("BAC infinito"):
            with self.assertRaises(ValueError):
                calculate_evm(100, 80, 90, math.inf)
        with self.subTest("valor não numérico"):
            with self.assertRaises(TypeError):
                calculate_evm("100", 80, 90, 120)
        with self.subTest("booleano não é valor monetário"):
            with self.assertRaises(TypeError):
                calculate_evm(True, 80, 90, 120)


class GameValuationTests(unittest.TestCase):
    def test_integra_indicadores_com_fluxos_futuros_liquidos(self):
        result = evaluate_game_project(
            initial_investment=100,
            future_cash_flows=[60, 60],
            tma=0.1,
            periodicity="ano",
            data_classification="estimado",
        )
        metrics = result["indicators"]
        expected_irr = (60 + math.sqrt(27600)) / 200 - 1

        self.assertAlmostEqual(metrics["vpl"]["value"], 4.13223140496)
        self.assertAlmostEqual(metrics["tir"]["value"], expected_irr, places=6)
        self.assertAlmostEqual(metrics["payback_simples"]["value"], 5 / 3)
        self.assertAlmostEqual(metrics["payback_descontado"]["value"], 23 / 12)
        self.assertAlmostEqual(metrics["roi"]["value"], 20)
        self.assertEqual(result["periodicity"], "ano")
        self.assertEqual(result["data_classification"], "estimado")

    def test_cenario_atual_nao_inventa_indicadores_sem_fluxos_futuros(self):
        scenario = ctrl_the_witch_current_scenario()

        self.assertIsNone(scenario["future_cash_flows"])
        self.assertIsNone(scenario["tma"])
        self.assertEqual(scenario["current_commercial_revenue"]["value"], 0)
        self.assertEqual(
            scenario["financial_initial_investment"]["value"], 0
        )
        self.assertEqual(
            scenario["economic_investment_scenarios"]["scenarios"][0][
                "labor_opportunity_cost"
            ],
            23400,
        )
        self.assertEqual(
            scenario["future_commercial_plan"]["gross_sales_scenarios"][
                "scenarios"
            ]["meta de 10 cópias/mês"]["gross_revenue_per_year"],
            2400,
        )
        self.assertIsNone(
            scenario["future_commercial_plan"]["gross_sales_scenarios"][
                "scenarios"
            ]["meta de 10 cópias/mês"]["net_revenue_per_year"]
        )
        self.assertIn(
            "tax_amount",
            scenario["future_commercial_plan"]["gross_sales_scenarios"][
                "scenarios"
            ]["meta de 10 cópias/mês"]["net_revenue_missing_inputs"],
        )
        self.assertEqual(
            scenario["future_commercial_plan"]["classification"],
            "plano informado e hipótese, não preço atual nem demanda validada",
        )
        for metric in scenario["indicators"].values():
            self.assertIsNone(metric["value"])
            self.assertEqual(
                metric["status"],
                "não calculável de forma significativa",
            )

    def test_fluxos_ausentes_e_tma_invalida_sao_rejeitados(self):
        with self.subTest("sem fluxos futuros"):
            with self.assertRaises(ValueError):
                evaluate_game_project(100, [], 0.1, "ano", "real")
        with self.subTest("TMA negativa"):
            with self.assertRaises(ValueError):
                evaluate_game_project(100, [120], -0.01, "ano", "estimado")
        with self.subTest("classificação desconhecida"):
            with self.assertRaises(ValueError):
                evaluate_game_project(100, [120], 0.1, "ano", "observado")

    def test_exemplo_hipotetico_permanece_identificado_e_separado(self):
        output = StringIO()
        with redirect_stdout(output):
            print_hypothetical_example()

        self.assertIn("exemplo hipotético", output.getvalue().lower())
        self.assertIn("não representa o Ctrl the Witch", output.getvalue())
        current = ctrl_the_witch_current_scenario()
        self.assertEqual(
            current["current_commercial_revenue"]["classification"],
            "real (informado)",
        )
        self.assertIsNone(current["future_cash_flows"])


class SalesModelTests(unittest.TestCase):
    def test_simula_receita_bruta_mensal_e_anual_sem_taxas(self):
        result = simulate_sales_scenarios(
            unit_price=20,
            monthly_copies_by_scenario={
                "2 cópias/mês": 2,
                "meta": 10,
                "25 cópias/mês": 25,
            },
        )["scenarios"]

        self.assertEqual(
            [
                result[name]["gross_revenue_per_month"]
                for name in ("2 cópias/mês", "meta", "25 cópias/mês")
            ],
            [40, 200, 500],
        )
        self.assertEqual(
            [
                result[name]["gross_revenue_per_year"]
                for name in ("2 cópias/mês", "meta", "25 cópias/mês")
            ],
            [480, 2400, 6000],
        )
        self.assertEqual(result["meta"]["copies_per_year"], 120)

    def test_rejeita_entradas_invalidas_na_simulacao_de_vendas(self):
        with self.subTest("preço negativo"):
            with self.assertRaises(ValueError):
                simulate_sales_scenarios(-1, {"meta": 10})
        with self.subTest("preço não finito"):
            with self.assertRaises(ValueError):
                simulate_sales_scenarios(math.nan, {"meta": 10})
        with self.subTest("cópias fracionárias"):
            with self.assertRaises(ValueError):
                simulate_sales_scenarios(20, {"meta": 1.5})
        with self.subTest("período inválido"):
            with self.assertRaises(ValueError):
                simulate_sales_scenarios(20, {"meta": 10}, 0)
        with self.subTest("cenários vazios"):
            with self.assertRaises(ValueError):
                simulate_sales_scenarios(20, {})

    def test_receita_liquida_permanece_desconhecida_sem_taxas(self):
        result = calculate_net_revenue(gross_revenue=200)

        self.assertIsNone(result["revenue_after_fees_before_taxes"])
        self.assertIsNone(result["net_revenue"])
        self.assertIn("platform_share_rate", result["missing_fee_inputs"])
        self.assertIn("tax_amount", result["missing_net_inputs"])

    def test_receita_liquida_aplica_taxas_e_tributos_explicitamente_informados(self):
        # Valores sintéticos para validar a fórmula; não representam o projeto.
        result = calculate_net_revenue(
            gross_revenue=200,
            platform_share_rate=0.10,
            processor_percentage_rate=0.029,
            processor_fixed_fee_per_transaction=0.30,
            transaction_count=10,
            tax_amount=5,
        )

        self.assertAlmostEqual(result["platform_fee"], 20)
        self.assertAlmostEqual(result["processor_percentage_fee"], 5.8)
        self.assertAlmostEqual(result["processor_fixed_fee"], 3)
        self.assertAlmostEqual(result["revenue_after_fees_before_taxes"], 171.2)
        self.assertAlmostEqual(result["net_revenue"], 166.2)
        self.assertEqual(result["missing_net_inputs"], [])

    def test_receita_apos_taxas_pode_ser_calculada_sem_presumir_tributos(self):
        result = calculate_net_revenue(
            gross_revenue=100,
            platform_share_rate=0,
            processor_percentage_rate=0,
            processor_fixed_fee_per_transaction=0,
        )

        self.assertEqual(result["revenue_after_fees_before_taxes"], 100)
        self.assertIsNone(result["net_revenue"])
        self.assertEqual(result["missing_net_inputs"], ["tax_amount"])

    def test_taxa_fixa_sem_quantidade_de_transacoes_impede_receita_liquida(self):
        result = calculate_net_revenue(
            gross_revenue=100,
            platform_share_rate=0,
            processor_percentage_rate=0,
            processor_fixed_fee_per_transaction=0.25,
        )

        self.assertIsNone(result["revenue_after_fees_before_taxes"])
        self.assertIn("transaction_count", result["missing_fee_inputs"])

    def test_rejeita_taxas_e_contagem_de_transacoes_invalidas(self):
        with self.subTest("participação acima de 100%"):
            with self.assertRaises(ValueError):
                calculate_net_revenue(100, platform_share_rate=1.1)
        with self.subTest("taxa percentual negativa"):
            with self.assertRaises(ValueError):
                calculate_net_revenue(100, processor_percentage_rate=-0.1)
        with self.subTest("transações não inteiras"):
            with self.assertRaises(ValueError):
                calculate_net_revenue(100, transaction_count=1.5)

    def test_calcula_ponto_de_equilibrio_com_arredondamento_para_copias(self):
        result = calculate_break_even_units(1000, 15)
        self.assertTrue(result["calculable"])
        self.assertEqual(result["units"], 67)
        self.assertEqual(calculate_break_even_units(0, 15)["units"], 0)

    def test_ponto_de_equilibrio_nao_assume_margem_ou_custos_desconhecidos(self):
        missing = calculate_break_even_units(None, 15)
        no_margin = calculate_break_even_units(1000, 0)
        negative_margin = calculate_break_even_units(1000, -1)

        self.assertFalse(missing["calculable"])
        self.assertIn("fixed_cost", missing["missing_inputs"])
        self.assertFalse(no_margin["calculable"])
        self.assertFalse(negative_margin["calculable"])
        with self.assertRaises(ValueError):
            calculate_break_even_units(-1, 15)


class CurrentScenarioTests(unittest.TestCase):
    def test_fluxo_de_caixa_separa_desembolso_de_custo_economico(self):
        scenario = cash_flow_current_scenario()

        self.assertEqual(
            scenario["financial_initial_investment"]["amount"], 0
        )
        self.assertEqual(
            [item["labor_opportunity_cost"]
             for item in scenario["labor_investment"]["scenarios"]],
            [23400, 28080, 32760],
        )
        self.assertEqual(scenario["current_commercial_revenue"]["amount"], 0)
        self.assertIsNone(scenario["operating_costs"])
        self.assertIsNone(scenario["taxes"])


if __name__ == "__main__":
    unittest.main()