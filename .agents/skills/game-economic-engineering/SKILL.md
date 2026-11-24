---
name: game-economic-engineering
description: Analisa projetos de jogos digitais, especialmente GameMaker, aplicando Engenharia Econômica. Use para inspecionar arquivos de jogos, estimar custos, simular vendas, calcular receita líquida e ponto de equilíbrio, modelar fluxos de caixa, calcular VP, VF, VPL, TIR, Payback, ROI ou GVA/EVM, comparar alternativas e preparar avaliações ou propostas econômicas. Distingue cálculos disponíveis de análises metodológicas e solicita dados ausentes.
compatibility: Requer um harness compatível com Agent Skills que descubra .agents/skills/ e um interpretador Python 3 para executar os scripts; os cálculos usam apenas a biblioteca padrão.
---

# Game Economic Engineering

## 1. Objetivo

Atuar como especialista em Engenharia Econômica aplicada ao desenvolvimento de jogos digitais.

A Skill auxilia desenvolvedores, líderes técnicos e Product Owners a analisar projetos de jogos, estimar investimentos, calcular indicadores financeiros e avaliar a viabilidade econômica do produto.

O projeto de referência desta Skill é o **Ctrl the Witch**, desenvolvido na engine GameMaker.

## 2. Instruções operacionais

- Por padrão, analise os arquivos em modo somente leitura. Crie ou altere arquivos apenas quando o usuário solicitar.
- Trabalhe com os arquivos fornecidos ou disponíveis no workspace autorizado. Não presuma que o projeto do jogo esteja no mesmo diretório da Skill.
- Registre a origem de cada dado como: verificado em arquivo, informado pelo usuário/equipe, estimado, hipotético ou desconhecido.
- Não converta dados desconhecidos em zero e não misture exemplos hipotéticos com resultados reais ou estimados.
- Use os scripts Python para cálculos determinísticos. Não calcule os mesmos indicadores por estimativa textual.
- Informe moeda, periodicidade e premissas. Quando faltar dado necessário, explique a limitação e solicite-o; não fabrique um resultado.
- Preserve os erros e avisos dos scripts. Corrija entradas inválidas ou reporte o motivo; não esconda erros nem substitua valores inválidos por valores padrão.

## 3. Fluxo de trabalho

Seguir as etapas na ordem apresentada.

### Etapa 1 — Identificação do projeto

Levantar:
- Nome do jogo.
- Gênero.
- Engine utilizada.
- Linguagens e tecnologias.
- Plataformas de distribuição.
- Quantidade de integrantes.
- Tempo de desenvolvimento.
- Situação atual do produto.
- Objetivo da análise econômica.

Utilizar informações dos arquivos e dados fornecidos pela equipe.

Solicitar informações que não estejam disponíveis.

### Etapa 2 — Análise dos arquivos do jogo

Quando uma pasta ou arquivos do projeto forem disponibilizados:

1. Identificar a estrutura de diretórios.
2. Localizar o arquivo principal da engine.
3. Examinar arquivos de configuração.
4. Analisar objetos e seus eventos.
5. Examinar scripts e códigos-fonte.
6. Identificar salas, sprites, sons e fontes.
7. Investigar funcionalidades implementadas.
8. Identificar dependências e extensões.
9. Registrar limitações da análise.

Para projetos GameMaker, consultar:

[Análise Técnica de Jogos GameMaker](references/game_analysis.md)

Priorizar arquivos `.yyp`, `.yy` e `.gml`.

Não considerar que a existência de um arquivo comprova que uma funcionalidade está concluída.

Não utilizar apenas a quantidade de arquivos ou linhas de código como medida de complexidade.

### Etapa 3 — Levantamento econômico

Identificar e classificar:

**Custos diretos**
- Horas de programação.
- Desenvolvimento artístico.
- Design.
- Testes.
- Produção de conteúdo.

**Custos indiretos**
- Energia.
- Internet.
- Equipamentos.
- Licenças.
- Infraestrutura.

Também identificar:
- Custo de oportunidade.
- CapEx.
- OpEx.
- Custos de manutenção.
- Custos de publicação.
- Tributos.
- Custos de aquisição de jogadores.
- Taxas de plataforma e processamento de pagamentos.

Diferenciar desembolsos financeiros efetivos de custos econômicos estimados.
Ao comparar alternativas econômicas, explicitar custos, benefícios, riscos, restrições e horizonte de cada opção. Markup, preço e valor percebido são conceitos de análise: não inferir preço de venda ou disposição a pagar sem dados.

### Etapa 4 — Modelagem financeira

Consultar [Métodos de Engenharia Econômica Aplicados a Jogos](references/economic-methods.md) conforme o tema.

Antes de calcular, construir ou solicitar dados compatíveis para um fluxo de caixa com:
- Investimento inicial.
- Receitas observadas ou projetadas, claramente classificadas.
- Custos operacionais.
- Tributos.
- Investimentos adicionais.
- Fluxos líquidos por período.

Identificar a TMA e a periodicidade dos fluxos. A taxa e os fluxos devem usar a mesma periodicidade. Não anualizar ou converter taxas sem explicitar e justificar a conversão.

Os scripts ficam em `scripts/`, relativo à raiz desta Skill. Para executar exemplos a partir da raiz do repositório, use `python .agents/skills/game-economic-engineering/scripts/<arquivo>.py`. Exemplos de execução:

```text
python .agents/skills/game-economic-engineering/scripts/cost_estimator.py
python .agents/skills/game-economic-engineering/scripts/cash_flow.py
python .agents/skills/game-economic-engineering/scripts/cash_flow.py --exemplo-didatico
python .agents/skills/game-economic-engineering/scripts/game_valuation.py
python .agents/skills/game-economic-engineering/scripts/game_valuation.py --exemplo-hipotetico
```

Somente `cash_flow.py` e `game_valuation.py` têm opções de linha de comando para escolher um exemplo; as demais execuções diretas usam entradas fixas. Não trate essas saídas como entrada do usuário. Os scripts não oferecem CLI genérica para informar valores. Para um cálculo personalizado, importe e invoque a função indicada com os valores fornecidos, usando um comando Python inline ou um script chamador sem alterar os módulos financeiros.

`sales_model.py` fornece funções importáveis, sem execução de demonstração por linha de comando. Use `simulate_sales_scenarios()` para receita bruta hipotética; ela não desconta taxas, tributos ou custos. Use `calculate_net_revenue()` somente com taxas, quantidade de transações e montante de tributos efetivamente informados. `None` mantém o resultado correspondente como não calculável. A receita após os itens modelados não é lucro do projeto e não inclui custos fixos, reembolsos, descontos ou conversão cambial. Use `calculate_break_even_units()` apenas com custo fixo e margem de contribuição unitária conhecidos; margem nula ou negativa não permite recuperação por vendas.

Modelo de chamada personalizada a partir da raiz do repositório (substitua os marcadores somente por valores fornecidos ou explicitamente classificados como estimativas):

```python
import sys
sys.path.insert(0, ".agents/skills/game-economic-engineering/scripts")
from game_valuation import evaluate_game_project

resultado = evaluate_game_project(
    initial_investment=INVESTIMENTO_INFORMADO,
    future_cash_flows=FLUXOS_LIQUIDOS_INFORMADOS,
    tma=TMA_DECIMAL_POR_PERIODO,
    periodicity="PERIODICIDADE_INFORMADA",
    data_classification=CLASSIFICACAO,
)
print(resultado)
```

Este é um modelo, não um bloco para executar sem preencher. `CLASSIFICACAO` deve ser substituída por `"real"`, `"estimado"` ou `"hipotético"` conforme a origem dos dados. A função aplica uma classificação ao cenário inteiro; se houver dados de classes diferentes, discrimine a origem de cada entrada na análise e não rotule o conjunto como exclusivamente real. Se não houver fluxos futuros, TMA ou periodicidade suficientes, não substitua os marcadores por zero: solicite os dados ou use o cenário atual específico, que identifica os indicadores como não calculáveis.

| Script | Finalidade |
|---|---|
| `cost_estimator.py` | `estimate_development_cost(team_members, development_days, daily_team_hours, opportunity_cost_per_team_hour, additional_disbursements=None)` e `estimate_development_scenarios(...)`. A taxa é por hora da equipe inteira, não por integrante. Integrantes/dias são inteiros positivos; horas diárias são finitas e positivas; taxa e adicionais são finitos e não negativos. `None` mantém desembolsos adicionais desconhecidos. O antigo argumento nomeado `opportunity_cost_per_hour_per_member` permanece como alias de compatibilidade, com o mesmo significado de taxa horária da equipe. A execução direta mostra cenários de 39 semanas e não aponta horas reais. |
| `cash_flow.py` | `calculate_cash_flow(initial_investment, revenues, operating_costs, taxes=None, capex=None)`. Investimento não negativo; receitas, custos, tributos e CapEx são listas/tuplas finitas não negativas e de mesmo tamanho por período; informe ao menos um período. Se `taxes` ou `capex` for `None`, retorna `calculated=False` e informa o dado ausente. Passe zeros somente quando sua ausência estiver confirmada. O modo padrão descreve o cenário atual sem criar série futura; `--exemplo-didatico` executa dados hipotéticos. |
| `npv_irr.py` | `present_value(future_value, rate, periods)`, `future_value(present_value, rate, periods)`, `npv(cash_flows, rate)` e `irr(cash_flows)`. Valores devem ser finitos; taxa > -100%; períodos de VP/VF não negativos. VPL recebe fluxo não vazio começando no período zero, com taxa decimal por período. A TIR requer pelo menos um fluxo positivo e um negativo, recusa mais de uma mudança de sinal e usa busca por bisseção com intervalo limitado; pode não encontrar uma raiz ou retornar uma única solução em casos que mereçam análise adicional. |
| `payback.py` | `simple_payback(cash_flows)` e `discounted_payback(cash_flows, rate)`. A série começa com investimento negativo e exige pelo menos um fluxo futuro; fluxos futuros negativos não são aceitos. A taxa descontada deve ser finita e > -100%. Retorna `None` se não recuperar no horizonte. |
| `roi.py` | `calculate_roi(investment, total_returns)`. Entradas finitas; investimento positivo. O retorno é o valor total definido para o cálculo. Retorna percentual e não desconta o tempo; documente o que compõe o retorno e seu horizonte. |
| `agile_evm.py` | `calculate_evm(planned_value, earned_value, actual_cost, bac)`. Retorna CPI, SPI, CV, SV, EAC e fator estimado de duração. Os valores devem ser numéricos, finitos e positivos; VP e VA não podem superar BAC. Divisores nulos são rejeitados. |
| `game_valuation.py` | `evaluate_game_project(initial_investment, future_cash_flows, tma, periodicity, data_classification)`. Recebe fluxos líquidos futuros sem o investimento inicial, TMA decimal por período (finita e não negativa), periodicidade e classificação (`real`, `estimado` ou `hipotético`). Consolida VPL, TIR, Paybacks e ROI. TIR pode ser não calculável ou ambígua; Payback exige fluxos futuros não negativos e pode não recuperar no horizonte. O cenário atual do Ctrl the Witch mantém separados o desembolso inicial informado, cenários de custo de oportunidade e vendas brutas hipotéticas; `--exemplo-hipotetico` é apenas didático. |
| `sales_model.py` | `simulate_sales_scenarios(unit_price, monthly_copies_by_scenario, months_per_year=12)`, `calculate_net_revenue(...)` e `calculate_break_even_units(fixed_cost, contribution_margin_per_unit)`. Simula cópias e receita bruta, calcula receita líquida somente quando taxas/transações/tributos necessários forem conhecidos, e estima unidades de equilíbrio somente com margem conhecida. Não atribui taxas ou custos desconhecidos como zero. |

`cash_flow.py` não recebe unidade/periodicidade: documente a unidade dos períodos externamente. `irr()` retorna taxa decimal por período. Os módulos importados por outros scripts estão no mesmo diretório. Não há dependências Python de terceiros. Ao executar com entradas personalizadas, preserve as mensagens de erro e os estados não calculáveis retornados; não interprete saída hipotética como avaliação do jogo.

Para estimar vendas, os cenários informados para o Ctrl the Witch usam preço planejado de R$ 20,00 e 2, 10 ou 25 cópias por mês. Os resultados são receita bruta hipotética. A taxa de participação do itch.io, os encargos do processador, a quantidade de transações e os tributos do projeto não foram informados. A documentação oficial do itch.io explica que a participação é configurável; não use o exemplo de 10% nem exemplos de taxas de processadores como configuração comprovada do jogo. Consulte a referência econômica antes de interpretar valores líquidos.

### Etapa 5 — Indicadores financeiros

Calcular e interpretar:

- Valor Presente (VP).
- Valor Futuro (VF).
- Valor Presente Líquido (VPL).
- Taxa Interna de Retorno (TIR).
- Payback simples.
- Payback descontado.
- ROI.
- CAC e LTV, quando aplicáveis.
- Receita bruta/líquida e ponto de equilíbrio, quando houver premissas suficientes.

VP/VF, VPL, TIR, Payback e ROI têm funções de cálculo nos scripts indicados. CAC e LTV são orientações metodológicas nos arquivos atuais; não há script específico para eles. Apresentar fórmulas, resultados, moeda, classificação dos dados e periodicidade.

Explicar se os indicadores demonstram atratividade econômica somente quando houver dados suficientes. TIR ou Payback que não puderem ser calculados devem aparecer como não calculáveis, com justificativa. Um indicador calculado não substitui a interpretação de riscos e premissas.

### Etapa 6 — Gerenciamento de Valor Agregado

Avaliar o desenvolvimento por sprint ou período.

Levantar:
- Valor Planejado (VP).
- Valor Agregado (VA).
- Custo Real (CR).
- Orçamento no Término (BAC).

Calcular:
- IDC/CPI (VA ÷ CR).
- IDP/SPI (VA ÷ VP).
- Variação de custo.
- Variação de prazo.
- Estimativa no Término (EAC = BAC ÷ CPI, conforme a hipótese de manutenção do desempenho de custos).

`agile_evm.py` calcula esses indicadores a partir de VP, VA, CR e BAC, mas não lê nem armazena histórico de sprint. Não inventar dados históricos.

Quando não houver registros, solicitar estimativas e identificá-las como tais. A auditoria do projeto original encontrou 130 commits entre 2026-01-28 e 2026-11-20, mas nenhum quadro de sprints, baseline, apontamento de horas ou valores VP/VA/CR/BAC. O histórico de commits não permite reconstruir EVM. O relato da equipe sobre sprints é contexto qualitativo, não substitui esses dados.

### Etapa 7 — Avaliação estratégica

Avaliar:
- Alternativas econômicas (desenvolver, adquirir, contratar, adiar, manter ou substituir).
- Potencial de comercialização.
- Modelos de monetização.
- Markup, preço de venda e valor percebido pelo jogador, somente com premissas e evidências explicitadas.
- Custos de manutenção.
- Substituição de componentes legados.
- Melhorias necessárias.
- Priorização do backlog.
- Princípio do Bom o Suficiente.

Comparar custo, benefício esperado, riscos, dependências e restrições. A prioridade `valor estimado / esforço estimado`, descrita na referência, é apenas um apoio metodológico; não existe calculadora de backlog nos scripts.

### Etapa 8 — Proposta econômica

Produzir uma recomendação para tomada de decisão contendo:

- Investimento necessário.
- Benefícios esperados.
- Indicadores financeiros.
- Riscos.
- Premissas.
- Modelo de negócio recomendado, quando houver evidência suficiente.
- Alternativas de investimento.
- Conclusão sobre viabilidade ou declaração explícita de que os dados são insuficientes.

## 4. Conteúdos acadêmicos e nível de implementação

| Conteúdo | Implementação nos arquivos atuais |
|---|---|
| Processo de decisão e alternativas econômicas | Orientação metodológica em `references/economic-methods.md`; sem comparador automatizado. |
| Valor do dinheiro no tempo, TMA, VP e VF | VP/VF têm funções em `npv_irr.py`; a TMA é entrada para VPL, Payback descontado e `game_valuation.py`. A escolha/justificativa da TMA é metodológica. |
| CapEx e OpEx | Categorias documentadas; `cash_flow.py` aceita custos operacionais, tributos e CapEx por período, mas não estima esses valores. |
| Custos diretos, indiretos e custo de oportunidade | Orientados na referência; `cost_estimator.py` calcula custo de oportunidade e agrega desembolsos adicionais informados, sem estimar categorias desconhecidas. |
| Markup e valor percebido | Orientação metodológica; sem calculadora ou pesquisa de disposição a pagar. |
| VPL, TIR e Payback simples/descontado | Funções de cálculo em `npv_irr.py`, `payback.py` e agregação em `game_valuation.py`, sujeitas às limitações das funções. |
| ROI | Implementado em `roi.py` e `game_valuation.py`; o significado do retorno e o horizonte precisam ser definidos. |
| Simulação de vendas e receita líquida | Receita bruta por cenário implementada em `sales_model.py`; receita líquida depende de taxas, transações e tributos informados. |
| Ponto de equilíbrio | Função de unidades em `sales_model.py`; requer custo fixo total e margem de contribuição por unidade. |
| CAC e LTV | Fórmulas e orientação em `economic-methods.md`; sem funções de cálculo específicas nos scripts atuais. |
| Depreciação e tributos | Métodos explicados na referência; sem calculadora de depreciação, apuração tributária ou alíquotas. Tributos são apenas uma entrada de fluxo de caixa. |
| Propostas econômicas | Estrutura de relatório orientada pela Skill; sem gerador automatizado de proposta. |
| GVA/EVM, CPI, SPI e EAC | Indicadores implementados em `agile_evm.py`; dependem de VP, VA, CR e BAC fornecidos. |
| Substituição de componentes legados | Comparação qualitativa orientada na referência; sem modelo quantitativo dedicado. |
| Princípio do Bom o Suficiente | Orientação de decisão qualitativa; sem indicador automatizado. |
| Priorização econômica de backlog | Fórmula auxiliar descrita na referência; sem ferramenta/script de priorização. |

## 5. Dados conhecidos do Ctrl the Witch

Utilizar os dados abaixo como referência inicial, sem presumir que sejam definitivos.

**Caracterização técnica verificada no projeto original:**
- 587 arquivos, total de 97.399.070 bytes (97,40 MB decimais ou 92,89 MiB).
- 140 arquivos GML e 12.966 linhas físicas nesses arquivos.
- 152 arquivos de objetos (55 `.yy` e 97 `.gml`); 48 arquivos de scripts; 27 arquivos de salas.
- 270 arquivos de sprites distribuídos por 90 recursos; 22 arquivos de sons; 44 arquivos de fontes.
- Oito salas principais; GameMaker IDE 2024.14.4.222; opção de build para Windows.
- O histórico de 130 commits cobre 2026-01-28 a 2026-11-20, mas não contém registros de esforço ou EVM.

**Dados econômicos informados e cenários:**
- Equipe de 2 pessoas; duração informada de 9 meses (aproximada como 39 semanas).
- Jornada média informada: 6 horas por dia para a equipe inteira; taxa de oportunidade: R$ 20,00 por hora da equipe.
- Cenários estimados para 5, 6 e 7 dias por semana: respectivamente 1.170/1.404/1.638 horas e R$ 23.400,00/R$ 28.080,00/R$ 32.760,00 de custo de oportunidade. Não são horas apontadas.
- Desembolso inicial informado pela equipe: R$ 0,00. Isso não significa custo total zero; energia e internet foram usadas, mas não mensuradas, e outros custos adicionais não foram informados.
- Receita comercial atual informada: R$ 0,00, sem vendas nem doações; a publicação atual foi informada como gratuita.
- Plano futuro informado: venda única planejada por R$ 20,00, com meta de 10 cópias/mês. Simulações de 2, 10 e 25 cópias/mês são hipotéticas, sem validação de mercado.
- Taxas da plataforma/processamento, tributos, fluxos líquidos, TMA e horizonte de avaliação permanecem desconhecidos. Não há base para VPL, TIR, Payback, ROI ou fluxo líquido atual.

O preço futuro planejado não substitui a informação de que a publicação atual é gratuita. A mudança comercial e a configuração de pagamento ainda precisam ser confirmadas.

## 6. Relatório final

Gerar um relatório em Markdown contendo:

1. Identificação do jogo.
2. Caracterização técnica.
3. Funcionalidades identificadas.
4. Premissas econômicas.
5. Investimento inicial.
6. Custos diretos e indiretos.
7. Fluxo de caixa.
8. Vendas brutas e líquidas, taxas e ponto de equilíbrio, se houver dados.
9. VP e VF.
10. VPL.
11. TIR.
12. Payback simples e descontado.
13. ROI.
14. CAC e LTV, quando aplicáveis.
15. Indicadores GVA/EVM.
16. Depreciação e tributos.
17. Modelo de negócio.
18. Priorização de melhorias.
19. Riscos econômicos.
20. Conclusão sobre viabilidade.

Salvar em Markdown no caminho solicitado pelo usuário. Se não houver caminho definido, sugerir:

`examples/tcc-valuation-report.md`

Para itens sem dados ou sem implementação, registrar “não informado”, “não calculável” ou “orientação metodológica”, conforme aplicável. Não preencher lacunas com zero. O relatório existente é uma caracterização técnica e estimativa inicial, não contém uma avaliação completa de viabilidade.

## 7. Regras de confiabilidade

- Não inventar dados ausentes.
- Diferenciar informações reais, estimadas e hipotéticas.
- Informar moeda e periodicidade.
- Identificar a origem das informações.
- Não confundir receita com lucro.
- Não confundir saldo positivo com VPL positivo.
- Não confundir investimento econômico com desembolso financeiro.
- Não confundir valor de desenvolvimento com valor de mercado.
- Não declarar viabilidade positiva sem evidências.
- Utilizar cálculos determinísticos em Python.
- Verificar se o script correspondente realmente cobre a métrica antes de afirmar que ela foi calculada.
- Informar entradas, limitações, erros e estados não calculáveis.
- Registrar limitações da análise.
- Explicar os resultados em linguagem acessível.

## 8. Divulgação progressiva

Consultar os recursos conforme a necessidade:

- [`references/game_analysis.md`](references/game_analysis.md): análise técnica de jogos GameMaker; consultar ao inspecionar um projeto.
- [`references/economic-methods.md`](references/economic-methods.md): fundamentos e fórmulas econômicas; consultar ao modelar custos, fluxos ou indicadores.
- `scripts/`: funções e exemplos executáveis; consultar o script específico antes de calcular.
- [`examples/tcc-valuation-report.md`](examples/tcc-valuation-report.md): dados técnicos e estimativa de investimento já documentados para o TCC.

Não carregar todos os recursos desnecessariamente. Os caminhos são relativos à raiz desta Skill e os nomes acima correspondem aos arquivos existentes.

Priorizar a análise dos arquivos reais do projeto antes de formular conclusões econômicas.
