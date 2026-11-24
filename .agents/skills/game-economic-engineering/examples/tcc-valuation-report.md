# Relatório Técnico-Econômico — Ctrl the Witch

## 1. Escopo e critério de evidência

Este relatório consolida a inspeção técnica do projeto GameMaker e os dados
econômicos registrados no levantamento do projeto. O projeto original foi
inspecionado em modo somente leitura em
`C:\Users\heloi\GameMakerProjects\Ctrl The Witch`.
Os dados monetários não foram verificados em registros contábeis.

Classificação utilizada:

- **Verificado:** encontrado diretamente nos arquivos do projeto ou na
  documentação indicada.
- **Informado:** fornecido pelo usuário/equipe; não significa confirmação
  contábil ou validação independente.
- **Documentado:** registrado no levantamento do projeto; não significa
  confirmação contábil.
- **Estimado:** calculado a partir de premissas documentadas.
- **Hipotético:** simulação futura, sem evidência de que ocorrerá.
- **Desconhecido:** não registrado nem mensurado; não tratado como zero.

## 2. Síntese executiva

- O jogo foi desenvolvido em GameMaker e a opção de build para Windows está
  declarada. Não foi encontrado build/instalador empacotado nem implementação
  de monetização comercial no código auditado.
- A equipe informou que trabalhou por 9 meses, aproximadamente 39 semanas,
  6 horas por dia, de segunda a sábado. A taxa de mão de obra é R$ 20,00 por
  hora para a equipe de 2 integrantes.
- Com essa jornada, estimam-se 234 dias, 1.404 horas da equipe e
  R$ 28.080,00 de custo de oportunidade. Não há apontamento de horas; esse
  valor não representa custo realizado ou salário pago.
- O desembolso financeiro inicial documentado é R$ 0,00. Energia e internet
  foram utilizadas, mas não mensuradas; custos totais permanecem desconhecidos.
- A receita comercial atual documentada é R$ 0,00, sem vendas nem doações. A
  publicação atual consta como gratuita no levantamento.
- O preço informado é R$ 20,00 por unidade e o tributo informado é 10%.
  As simulações mostram receita bruta e valores após esse tributo, mas não
  representam vendas previstas nem a receita líquida total.
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

### Dados fornecidos e premissas

| Dado | Valor | Classificação |
|---|---:|---|
| Integrantes | 2 | Informado pelo usuário |
| Duração | 9 meses | Informado pelo usuário |
| Aproximação do período | 39 semanas | Premissa de conversão |
| Dias de trabalho | 6 dias/semana (segunda a sábado) | Informado pelo usuário |
| Jornada diária | 6 horas para a equipe inteira | Informado pelo usuário |
| Custo de oportunidade | R$ 20,00 por hora da equipe inteira | Confirmado pelo usuário |
| Preço por unidade | R$ 20,00 | Informado pelo usuário |
| Tributo usado na simulação | 10% da receita bruta | Informado pelo usuário; base aplicada como premissa |

O repositório original contém 130 commits entre 2026-01-28 e 2026-11-20.
Esse histórico serve como evidência de atividade no período, mas não registra
horas nem confirma a distribuição semanal de esforço. A jornada semanal e a
taxa horária são informações fornecidas pelo usuário, não apontamentos
auditados.

### Estimativa com a jornada informada

Fórmulas: `dias estimados = 39 semanas × 6 dias/semana`; `horas da equipe =
dias estimados × 6 horas/dia`; `custo de oportunidade = horas da equipe ×
R$ 20,00/h da equipe`.

| Dias/semana | Dias estimados | Horas da equipe | Custo de oportunidade |
|---:|---:|---:|---:|
| 6 | 234 | 1.404 | R$ 28.080,00 |

Esses valores são **custos econômicos estimados retrospectivamente**, não
desembolsos, salários pagos ou horas auditadas. Não se distribui o custo por
integrante porque não há apontamento individual; qualquer divisão igual
seria outra hipótese.

## 5. Desembolsos e custos

O levantamento registra desembolso financeiro inicial de **R$ 0,00**. Isso
descreve o desembolso inicial documentado, não o custo total do desenvolvimento
ou da operação. Não constam valores pagos individualmente por licença, assets,
ferramentas ou publicação. Energia e internet foram utilizadas, mas seus
valores não foram mensurados. Equipamentos e demais custos indiretos também
não têm valores levantados.

| Categoria | Situação |
|---|---|
| Mão de obra | Custo de oportunidade estimado na seção 4; sem desembolso registrado |
| Desembolso inicial | R$ 0,00, documentado no levantamento |
| Licenças, assets, ferramentas e publicação | Nenhum valor adicional documentado; não confirmar como custo total zero |
| Energia e internet | Utilizadas, valores desconhecidos |
| CapEx, OpEx e regime/base tributária | Não levantados; o tributo de 10% é usado apenas na simulação de vendas |
| Taxas da plataforma e do processador | Não registradas |

Logo, não se calcula custo total efetivo. As lacunas não são substituídas por
zeros.

## 6. Situação comercial e simulação de vendas

A publicação atual no itch.io consta como gratuita no levantamento, com
receita comercial de R$ 0,00 e sem vendas ou doações. Separadamente, o plano
comercial registra uma **venda única a R$ 20,00 por cópia** e uma meta de
**10 cópias mensais**. Não foi confirmado que o preço atual do produto foi
alterado, e a meta não foi validada por pesquisa de mercado.

Simulação em reais nominais: `receita bruta = preço unitário × cópias`;
`tributo simulado = receita bruta × 10%`; `após o tributo informado =
receita bruta − tributo simulado`. A receita anual assume 12 meses com o
mesmo volume mensal.

| Cenário hipotético | Cópias/mês | Cópias/ano | Bruta/mês | Tributo 10%/mês | Após tributo/mês | Bruta/ano | Tributo 10%/ano | Após tributo/ano |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Baixo volume | 2 | 24 | R$ 40,00 | R$ 4,00 | R$ 36,00 | R$ 480,00 | R$ 48,00 | R$ 432,00 |
| Meta documental | 10 | 120 | R$ 200,00 | R$ 20,00 | R$ 180,00 | R$ 2.400,00 | R$ 240,00 | R$ 2.160,00 |
| Volume superior | 25 | 300 | R$ 500,00 | R$ 50,00 | R$ 450,00 | R$ 6.000,00 | R$ 600,00 | R$ 5.400,00 |

Esses valores não representam vendas realizadas ou demanda prevista. “Após
tributo” desconta somente os 10% informados, aplicados sobre a receita bruta
para esta simulação; não equivale à receita líquida total nem ao lucro.
Reembolsos, descontos, conversão cambial, taxas da plataforma/processador e
outros custos não foram descontados.

## 7. Ponto de equilíbrio

Fórmula geral: `unidades = teto(custos fixos / margem de contribuição por
unidade)`, desde que a margem seja positiva. A margem deve descontar custos
variáveis unitários, participação da plataforma, processamento e tributos
aplicáveis. Taxas por transação também exigem uma hipótese ou dado de
transações por cópia.

O ponto de equilíbrio **financeiro total** não é calculável: embora o
desembolso inicial documentado seja R$ 0,00, custos operacionais e taxas
permanecem desconhecidos. O ponto de equilíbrio **econômico completo**
também não é calculável, pois a margem líquida por cópia é desconhecida.

Como referência limitada, após descontar somente o tributo informado de 10%,
a contribuição por cópia seria R$ 18,00 (R$ 20,00 − R$ 2,00), antes das
taxas da plataforma/processador e de outros custos. Recuperar o custo de
oportunidade estimado de R$ 28.080,00 exigiria 1.560 cópias nesse cenário.
Esse não é o ponto de equilíbrio comercial completo e não considera custos
adicionais ou taxas desconhecidas.

## 8. Fluxo de caixa e indicadores

| Métrica | Situação | Dados faltantes/limitação |
|---|---|---|
| Fluxo de caixa atual | Incompleto; não foi montada série por período | Custos, tributos efetivos, CapEx, periodicidade e horizonte |
| VP e VF | Não calculados | Fluxos, taxa e número de períodos compatíveis |
| VPL | Não calculável de forma significativa | Fluxos líquidos futuros por período, horizonte e TMA |
| TIR | Não calculável | Série de fluxos líquidos com investimento e retornos |
| Payback simples | Não calculável | Investimento econômico definido e fluxos futuros por período |
| Payback descontado | Não calculável | Fluxos, periodicidade e TMA |
| ROI | Não calculável | Retornos líquidos e horizonte; desembolso zero também não serve como denominador de ROI financeiro |
| Receita líquida | Não calculável | Participação/taxas efetivas, transações e tributos efetivamente aplicáveis |
| Tributo sobre vendas | Simulado a 10% da receita bruta na seção 6 | Regime e base efetivamente aplicáveis não verificados |
| CAC/LTV | Não calculados | Gastos de aquisição, clientes, receita recorrente ou dados de retenção |
| Depreciação | Não calculada | Ativos, custos de aquisição, vida útil e valor residual |

A receita comercial atual documentada de R$ 0,00 é um dado de situação, não
uma série de fluxos futuros. Nenhum indicador acima é apresentado como
resultado realizado ou previsão do jogo.

## 9. Sprints e GVA/EVM

O histórico do desenvolvimento indica início sem metodologia formal; sprints foram
introduzidas aproximadamente na metade do período, em geral com duas semanas
e ocasionalmente uma. Tarefas frequentemente ultrapassavam o prazo, e as
sprints eram usadas sobretudo para acompanhamento. Essas informações constam
como descrição qualitativa do processo documental.

A auditoria do projeto original não encontrou quadro de sprint, backlog
datado, estimativas, baseline, apontamento de horas, burndown, valores
planejados/agregados/reais (VP/VA/CR) ou BAC. Os 130 commits ajudam a
identificar cronologia, mas não medem esforço, escopo concluído ou custos.
Portanto, CPI, SPI, CV, SV e EAC históricos não podem ser reconstruídos
confiavelmente. `agile_evm.py` calcula esses indicadores quando entradas
documentadas são disponibilizadas; seu exemplo fixo é didático, não histórico do
TCC.

## 10. Métodos implementados e limites

Os scripts Python incluem estimativa de esforço, fluxo de caixa, VP/VF,
VPL/TIR, Payback simples/descontado, ROI e GVA/EVM. `sales_model.py` simula
receita bruta, preserva receita líquida como desconhecida quando dados
faltam e calcula ponto de equilíbrio apenas quando custo fixo e margem de
contribuição são disponibilizados.

Markup, valor percebido, CAC/LTV, tributação, depreciação, propostas
econômicas, substituição de legado e priorização de backlog são orientações
metodológicas, sem cálculo específico completo nos scripts. Resultados de
teste com dados artificiais não são usados como resultado do jogo.

## 11. Conclusão e pendências

Os dados atuais permitem caracterizar o projeto, estimar o custo de
oportunidade pela jornada informada e simular receitas brutas e valores após
o tributo informado para volumes hipotéticos. 
