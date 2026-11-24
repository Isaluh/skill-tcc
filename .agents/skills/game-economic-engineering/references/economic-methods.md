
# Métodos de Engenharia Econômica Aplicados a Jogos

## 1. Processo de decisão econômica

A Engenharia Econômica auxilia na escolha entre
alternativas considerando custos, benefícios, riscos
e restrições financeiras.

Em projetos de jogos, comparar alternativas como:

- Desenvolver uma funcionalidade.
- Comprar um asset pronto.
- Utilizar uma ferramenta gratuita.
- Contratar um profissional.
- Adiar uma melhoria.
- Manter ou substituir uma tecnologia.

A escolha deve considerar o custo total e o benefício
esperado durante o ciclo de vida do jogo.

## 2. Valor do Dinheiro no Tempo (TVM)

O dinheiro possui valores diferentes dependendo
do momento em que é recebido ou investido.

### Valor Presente (VP)

VP = VF / (1 + i)^n

Onde:
- VF = Valor Futuro.
- i = taxa por período.
- n = quantidade de períodos.

### Valor Futuro (VF)

VF = VP * (1 + i)^n

### Taxa Mínima de Atratividade (TMA)

Representa o retorno mínimo esperado para aceitar
um investimento.

A TMA deve ser informada ou justificada por uma
premissa explícita.

## 3. Fluxo de Caixa

Registrar as entradas e saídas financeiras por período.

### Fluxo líquido

Fluxo Líquido = Receitas - Custos - Tributos - CapEx

### Saldo acumulado

Saldo Acumulado = Saldo Anterior + Fluxo Líquido

Separar:

- Investimento inicial.
- Receitas.
- Custos operacionais (OpEx).
- Investimentos adicionais (CapEx).
- Tributos.

## 4. Custos, preço e valor em TI

### Custos diretos

- Horas de programação.
- Design e desenvolvimento artístico.
- Testes.
- Produção de conteúdo.

### Custos indiretos

- Energia.
- Internet.
- Equipamentos.
- Licenças.
- Infraestrutura.

### Custo de oportunidade

Representa o valor da melhor alternativa sacrificada.

### Markup

Preço de venda = Custo / (1 - percentual de margem)

Diferenciar custo de desenvolvimento, preço de venda
e valor percebido pelo jogador.

## 5. Viabilidade econômica

### Valor Presente Líquido (VPL)

VPL = -I0 + Σ [FCt / (1 + i)^t]

Onde:
- I0 = investimento inicial.
- FCt = fluxo de caixa no período.
- i = TMA.
- t = período.

Interpretação:
- VPL > 0: investimento economicamente atrativo.
- VPL = 0: retorno equivalente à TMA.
- VPL < 0: investimento não alcança a TMA.

### Taxa Interna de Retorno (TIR)

É a taxa que torna o VPL igual a zero.

Comparação:
- TIR > TMA: atrativo.
- TIR = TMA: indiferente.
- TIR < TMA: não atrativo.

Registrar limitações quando existirem múltiplas
mudanças de sinal no fluxo de caixa.

### Payback simples

Tempo necessário para recuperar o investimento
sem considerar o valor do dinheiro no tempo.

### Payback descontado

Tempo necessário para recuperar o investimento
considerando os fluxos descontados pela TMA.

### ROI

ROI = [(Retorno - Investimento) / Investimento] * 100

Identificar claramente o que está sendo considerado
como retorno e qual o período analisado.

## 6. Depreciação e tributos

Ativos de TI podem sofrer depreciação ao longo
de sua vida útil.

### Depreciação linear

Depreciação anual = (Custo do ativo - Valor residual) / Vida útil

Avaliar possíveis ativos:

- Computadores.
- Equipamentos.
- Servidores.
- Outros bens utilizados no desenvolvimento.

Tributos devem considerar o regime tributário e
a legislação aplicável.

Não inventar alíquotas ou presumir enquadramento
tributário da equipe.

## 7. Métricas de produtos digitais

### CAC

CAC = Investimento em aquisição / Número de clientes adquiridos

### LTV

LTV = Receita média por cliente * Tempo de relacionamento

Quando aplicável, considerar margem de contribuição
e custos variáveis no cálculo do LTV.

Para jogos, adaptar as métricas ao modelo de negócio.

## 8. Gerenciamento de Valor Agregado (GVA/EVM)

### Indicadores básicos

- VP: Valor Planejado.
- VA: Valor Agregado.
- CR: Custo Real.
- BAC: Orçamento no Término.

### Índice de Desempenho de Custos (IDC/CPI)

IDC = VA / CR

### Índice de Desempenho de Prazo (IDP/SPI)

IDP = VA / VP

### Variação de custo

VC = VA - CR

### Variação de prazo

VPr = VA - VP

### Estimativa no Término (EAC)

EAC = BAC / IDC

Essa fórmula pressupõe que o desempenho de custos
observado continuará no restante do projeto.

Interpretar:
- IDC < 1: custo desfavorável.
- IDC > 1: custo favorável.
- IDP < 1: atraso.
- IDP > 1: adiantamento.

## 9. Propostas econômicas de software

Uma proposta econômica deve conter:

- Objetivo do projeto.
- Problema que o software resolve.
- Investimento necessário.
- Benefícios esperados.
- Fluxo de caixa.
- Indicadores financeiros.
- Riscos.
- Premissas.
- Recomendação.

Apresentar resultados de forma transparente.

## 10. Estratégia e princípio Bom o Suficiente

O princípio Bom o Suficiente consiste em equilibrar
qualidade, custo, prazo e valor entregue.

Em jogos, avaliar se uma melhoria realmente agrega
valor suficiente para justificar seu custo.

Evitar investimentos excessivos em funcionalidades
com baixo impacto para o jogador.

## 11. Substituição de componentes legados

Comparar:

- Custo de manutenção da tecnologia atual.
- Custo de substituição.
- Custo de migração.
- Riscos de incompatibilidade.
- Benefícios futuros.
- Vida útil esperada.

Considerar custos futuros e não apenas o investimento
inicial de substituição.

## 12. Priorização econômica do backlog

Avaliar funcionalidades considerando:

- Valor percebido pelo jogador.
- Custo de desenvolvimento.
- Esforço estimado.
- Risco.
- Impacto na experiência.

Uma métrica simples de priorização:

Prioridade = Valor estimado / Esforço estimado

Essa métrica é auxiliar e não substitui uma avaliação
qualitativa de riscos e dependências.

## 13. Regras de interpretação

- Não inventar dados financeiros.
- Informar moeda e periodicidade.
- Explicitar a TMA.
- Diferenciar valores reais e estimados.
- Utilizar cálculos determinísticos.
- Informar limitações dos indicadores.
- Não confundir receita com lucro.
- Não confundir saldo positivo com VPL positivo.
- Não declarar viabilidade sem analisar os indicadores
  e as premissas.
