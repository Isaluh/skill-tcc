# Relatório Técnico-Econômico — Ctrl the Witch

## 1. Escopo e critério de evidência

Este relatório consolida a inspeção técnica do projeto GameMaker e os dados
econômicos fornecidos pela equipe. O projeto original foi inspecionado em
modo somente leitura em `C:\Users\heloi\GameMakerProjects\Ctrl The Witch`.
Os dados monetários não foram verificados em registros contábeis.

Classificação utilizada:

- **Verificado:** encontrado diretamente nos arquivos do projeto ou na
  documentação indicada.
- **Informado:** fornecido pela equipe; não significa confirmação contábil.
- **Estimado:** calculado a partir de premissas informadas.
- **Hipotético:** simulação futura, sem evidência de que ocorrerá.
- **Desconhecido:** não medido ou não fornecido; não tratado como zero.

## 2. Síntese executiva

- O jogo foi desenvolvido em GameMaker e a opção de build para Windows está
  declarada. Não foi encontrado build/instalador empacotado nem implementação
  de monetização comercial no código auditado.
- A equipe informa 9 meses de duração, aproximadamente 39 semanas, 6 horas
  diárias para o grupo e custo de oportunidade de R$ 20,00 por hora da equipe.
- Não há registro de dias/horas efetivamente trabalhados. O custo de
  oportunidade é apresentado em três cenários, não como custo realizado.
- O desembolso financeiro inicial informado é R$ 0,00. Energia e internet
  foram utilizadas, mas não mensuradas; custos totais permanecem desconhecidos.
- A receita comercial atual informada é R$ 0,00, sem vendas nem doações. A
  publicação atual foi informada como gratuita.
- A equipe planeja venda única por R$ 20,00 e tem como meta hipotética 10
  cópias/mês. As simulações abaixo são receita bruta, não previsão nem receita
  líquida.
- Não há dados suficientes para calcular receita líquida, VPL, TIR, Payback,
  ROI, ponto de equilíbrio completo ou EVM histórico. Não se conclui
  viabilidade econômica.

## 3. Caracterização técnica auditada

O projeto contém 587 arquivos (excluída a metainformação `.git`), totalizando
97.399.070 bytes: 97,40 MB decimais ou 92,89 MiB. O valor anterior de
“92,89 MB” confundia MiB com MB.

| Recurso | Inventário verificado |
|---|---:|
| Arquivos `.gml` | 140 |
| Linhas físicas nos arquivos `.gml` | 12.966 |
| Arquivos de objetos | 152 (55 `.yy` e 97 `.gml`) |
| Arquivos de scripts | 48 (24 `.yy` e 24 `.gml`) |
| Arquivos de salas | 27 (8 `.yy` e 19 `.gml`) |
| Arquivos de sprites | 270 em 90 recursos |
| Arquivos de sons | 22 (11 `.yy` e 11 assets) |
| Arquivos de fontes | 44 em 6 recursos |

Salas principais identificadas: `rm_ajustes`, `rm_creditos`,
`rm_estatisticas`, `rm_fase`, `rm_fases`, `rm_guia`, `rm_introducao` e
`rm_menu`. A contagem de linhas usa todas as linhas físicas de 140 arquivos;
ela não mede qualidade, complexidade ou esforço.

O `.yyp` identifica GameMaker IDE 2024.14.4.222. A velocidade configurada é
60 FPS. A configuração Windows define o nome `Ctrl The Witch.exe` e indica
Steam desativado; opções de outras plataformas também existem, mas não
comprovam build ou teste nelas. Não foram encontrados
executável/instalador empacotados.

A auditoria de código não encontrou compras dentro do aplicativo, anúncios,
DLC, integração de loja ou faturamento. A mana e as compras de melhorias de
2 a 10 unidades são economia virtual de gameplay, não evidência de receita
comercial.

A leitura estática também identificou sistemas de digitação, inventário,
pedidos/NPCs, minijogos, progressão, menus, configurações, persistência e
áudio. A existência de código comprova implementação estática desses
componentes, não sua qualidade ou funcionamento correto em execução.

Uma inspeção estática anterior também identificou uma possível divergência
entre `fase.id` e o índice zero-based nos scripts
`scr_finalizar_fase.gml`, `scr_load_game.gml` e `scr_save_game.gml`, e que
`mana_ganha` não é persistido. Isso sustenta um risco de progressão/recompensa,
mas não foi validado por execução do jogo. Alguns preços exibidos em
`scr_melhorias.gml` divergem dos valores cobrados no controlador de fase. A
auditoria encontrou ainda uma referência a shader SDF ausente e a extensão
`ext_capslock` declarada e chamada no sistema de digitação, com dependência
nativa de Windows. Essas conclusões são estáticas, não resultado de playtest.

## 4. Premissas de esforço e custo de oportunidade

### Dados fornecidos

| Dado | Valor | Classificação |
|---|---:|---|
| Integrantes | 2 | Informado pela equipe |
| Duração | 9 meses | Informado pela equipe |
| Aproximação do período para os cenários | 39 semanas | Premissa de conversão |
| Jornada diária | 6 horas para a equipe inteira | Informado, sem apontamento |
| Custo de oportunidade | R$ 20,00 por hora da equipe | Informado pela equipe |

O repositório original contém 130 commits entre 2026-01-28 e 2026-11-20.
Esse histórico serve como evidência de atividade no período, mas não registra
horas nem confirma a distribuição semanal de esforço. Nenhuma hipótese de
5, 6 ou 7 dias por semana é apresentada como fato.

### Cenários estimados

Fórmulas: `dias estimados = 39 semanas × dias/semana`; `horas da equipe =
dias estimados × 6 horas/dia`; `custo de oportunidade = horas da equipe ×
R$ 20,00/h`.

| Dias/semana (hipótese) | Dias estimados | Horas da equipe | Custo de oportunidade |
|---:|---:|---:|---:|
| 5 | 195 | 1.170 | R$ 23.400,00 |
| 6 | 234 | 1.404 | R$ 28.080,00 |
| 7 | 273 | 1.638 | R$ 32.760,00 |

Esses valores são **custos econômicos estimados retrospectivamente**, não
desembolsos, salários pagos ou horas auditadas. Não se distribui o custo por
integrante porque não há apontamento individual; qualquer divisão igual
seria outra hipótese.

## 5. Desembolsos e custos

A equipe informa desembolso financeiro inicial de **R$ 0,00**. Isso descreve
o desembolso inicial informado, não o custo total do desenvolvimento ou da
operação. Não foram fornecidos valores pagos individualmente por licença,
assets, ferramentas ou publicação. Energia e internet foram usadas, mas seus
valores não foram mensurados. Equipamentos e demais custos indiretos também
não têm valores levantados.

| Categoria | Situação |
|---|---|
| Mão de obra | Custo de oportunidade estimado na seção 4; sem desembolso informado |
| Desembolso inicial | R$ 0,00, informado pela equipe |
| Licenças, assets, ferramentas e publicação | Nenhum valor adicional informado; não confirmar como custo total zero |
| Energia e internet | Utilizadas, valores desconhecidos |
| CapEx, OpEx e tributos | Não levantados |
| Taxas da plataforma e do processador | Não informadas |

Logo, não se calcula custo total efetivo. As lacunas não são substituídas por
zeros.

## 6. Situação comercial e simulação de vendas

A publicação atual no itch.io foi informada como gratuita, com receita
comercial de R$ 0,00 e sem vendas ou doações. Separadamente, a equipe informa
um plano futuro de **venda única a R$ 20,00 por cópia** e uma meta de
**10 cópias mensais**. Não foi confirmado que o preço atual do produto foi
alterado, e a meta não foi validada por pesquisa de mercado.

Simulação em reais nominais: `receita bruta = preço unitário × cópias`.
A receita anual assume 12 meses com o mesmo volume mensal.

| Cenário hipotético | Cópias/mês | Cópias/ano | Receita bruta/mês | Receita líquida/mês | Receita bruta/ano | Receita líquida/ano |
|---|---:|---:|---:|---|---:|---|
| Baixo volume | 2 | 24 | R$ 40,00 | Não calculável | R$ 480,00 | Não calculável |
| Meta informada | 10 | 120 | R$ 200,00 | Não calculável | R$ 2.400,00 | Não calculável |
| Volume superior | 25 | 300 | R$ 500,00 | Não calculável | R$ 6.000,00 | Não calculável |

Esses valores não representam vendas realizadas, demanda prevista ou receita
líquida. Reembolsos, descontos, conversão cambial, tarifas, tributos e custos
não foram descontados.

### Taxas do itch.io

A documentação oficial de pagamentos do itch.io explica que a participação
de receita (“open revenue sharing”) é configurável pelo vendedor. A página
apresenta 10% como exemplo, não como taxa comprovada deste jogo, e permite
configuração de 0% a 100%. A documentação também descreve taxas de
processadores que variam por serviço, moeda e região; os exemplos em USD não
devem ser aplicados diretamente a uma venda de R$ 20,00. A modalidade de
pagamento também afeta responsabilidades tributárias.

Fonte consultada em 2026-11-24:
[itch.io — Payments](https://itch.io/docs/creators/payments).
Não foi verificada a configuração específica da página do Ctrl the Witch.

Para calcular receita líquida seriam necessários: participação configurada,
taxas percentuais e fixas efetivamente aplicáveis, quantidade de transações
(não necessariamente igual à quantidade de cópias), valores de reembolso e
tributos efetivos. A função `calculate_net_revenue()` mantém a receita
líquida não calculável quando faltam esses dados; não assume taxas nulas.

## 7. Ponto de equilíbrio

Fórmula geral: `unidades = teto(custos fixos / margem de contribuição por
unidade)`, desde que a margem seja positiva. A margem deve descontar custos
variáveis unitários, participação da plataforma, processamento e tributos
aplicáveis. Taxas por transação também exigem uma hipótese ou dado de
transações por cópia.

O ponto de equilíbrio **financeiro total** não é calculável: embora o
desembolso inicial informado seja R$ 0,00, custos operacionais, taxas e
tributos permanecem desconhecidos. O ponto de equilíbrio **econômico exato**
também não é calculável, pois a margem líquida por cópia é desconhecida.

Como referência matemática de limite bruto, dividir os cenários de custo de
oportunidade pela receita bruta de R$ 20,00 resulta em 1.170, 1.404 ou 1.638
cópias, respectivamente. Isso pressupõe apenas para esse limite que cada
cópia gera R$ 20,00 antes de qualquer dedução; não é ponto de equilíbrio
comercial real nem considera taxas, tributos ou outros custos.

## 8. Fluxo de caixa e indicadores

| Métrica | Situação | Dados faltantes/limitação |
|---|---|---|
| Fluxo de caixa atual | Incompleto; não foi montada série por período | Custos, tributos, CapEx, periodicidade e horizonte |
| VP e VF | Não calculados | Fluxos, taxa e número de períodos compatíveis |
| VPL | Não calculável de forma significativa | Fluxos líquidos futuros por período, horizonte e TMA |
| TIR | Não calculável | Série de fluxos líquidos com investimento e retornos |
| Payback simples | Não calculável | Investimento econômico definido e fluxos futuros por período |
| Payback descontado | Não calculável | Fluxos, periodicidade e TMA |
| ROI | Não calculável | Retornos líquidos e horizonte; desembolso zero também não serve como denominador de ROI financeiro |
| Receita líquida | Não calculável | Participação/taxas efetivas, transações e tributos |
| CAC/LTV | Não calculados | Gastos de aquisição, clientes, receita recorrente ou dados de retenção |
| Depreciação | Não calculada | Ativos, custos de aquisição, vida útil e valor residual |

A receita comercial atual informada de R$ 0,00 é um dado de situação, não
uma série de fluxos futuros. Nenhum indicador acima é apresentado como
resultado realizado ou previsão do jogo.

## 9. Sprints e GVA/EVM

A equipe relata que começou sem metodologia formal; sprints foram
introduzidas aproximadamente na metade do período, em geral com duas semanas
e ocasionalmente uma. Tarefas frequentemente ultrapassavam o prazo, e as
sprints eram usadas sobretudo para acompanhamento. Isso é relato qualitativo
da equipe.

A auditoria do projeto original não encontrou quadro de sprint, backlog
datado, estimativas, baseline, apontamento de horas, burndown, valores
planejados/agregados/reais (VP/VA/CR) ou BAC. Os 130 commits ajudam a
identificar cronologia, mas não medem esforço, escopo concluído ou custos.
Portanto, CPI, SPI, CV, SV e EAC históricos não podem ser reconstruídos
confiavelmente. `agile_evm.py` calcula esses indicadores quando entradas
documentadas são fornecidas; seu exemplo fixo é didático, não histórico do
TCC.

## 10. Métodos implementados e limites

Os scripts Python incluem estimativa de esforço, fluxo de caixa, VP/VF,
VPL/TIR, Payback simples/descontado, ROI e GVA/EVM. `sales_model.py` simula
receita bruta, preserva receita líquida como desconhecida quando dados
faltam e calcula ponto de equilíbrio apenas quando custo fixo e margem de
contribuição são fornecidos.

Markup, valor percebido, CAC/LTV, tributação, depreciação, propostas
econômicas, substituição de legado e priorização de backlog são orientações
metodológicas, sem cálculo específico completo nos scripts. Resultados de
teste com dados artificiais não são usados como resultado do jogo.

## 11. Conclusão e pendências

Os dados atuais permitem caracterizar o projeto, estimar três cenários de
custo de oportunidade e simular receita bruta para volumes hipotéticos.
Não permitem afirmar viabilidade comercial ou econômica, estimar receita
líquida nem calcular indicadores de retorno.

Para concluir a avaliação, levantar:

1. Confirmação se o produto continuará gratuito ou se a publicação será
   alterada para venda a R$ 20,00.
2. Configuração de revenue share, processador, moeda, taxas e modo de
   pagamento no itch.io; quantidade real de transações e reembolsos.
3. Tributos e regime aplicáveis, validados por fonte contábil apropriada.
4. Gastos financeiros por categoria, inclusive energia, internet, ativos,
   licenças, assets, ferramentas e publicação; separar valores pagos de
   estimativas.
5. Registros de horas/dias por integrante, se existirem.
6. Horizonte e periodicidade de projeção, TMA justificada e cenários de
   receita sustentados por pesquisa de mercado.
7. Para EVM, backlog/scope baseline, estimativas, progresso aceito,
   custos reais e orçamento por sprint.

Até obter esses dados, manter os cenários claramente identificados como
estimativas ou hipóteses e os indicadores sem base suficiente como
“não calculáveis”.
