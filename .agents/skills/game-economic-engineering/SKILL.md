
---
name: game-economic-engineering
description: Analisa projetos de jogos digitais, especialmente projetos GameMaker, e aplica Engenharia Econômica para avaliar custos, investimentos, fluxo de caixa, VPL, TIR, Payback, ROI, GVA/EVM, depreciação, tributos, modelos de negócio e viabilidade financeira. Utilize ao analisar arquivos de jogos, estimar seu valor econômico ou elaborar propostas financeiras para projetos de desenvolvimento de jogos.
---

# Game Economic Engineering

## 1. Objetivo

Atuar como especialista em Engenharia Econômica aplicada ao desenvolvimento de jogos digitais.

A Skill auxilia desenvolvedores, líderes técnicos e Product Owners a analisar projetos de jogos, estimar investimentos, calcular indicadores financeiros e avaliar a viabilidade econômica do produto.

O projeto de referência desta Skill é o **Ctrl the Witch**, desenvolvido na engine GameMaker.

## 2. Fluxo de trabalho

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

`references/game-analysis.md`

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

Diferenciar desembolsos financeiros efetivos de custos econômicos estimados.

### Etapa 4 — Modelagem financeira

Consultar:

`references/economic-methods.md`

Construir um fluxo de caixa com:
- Investimento inicial.
- Receitas projetadas.
- Custos operacionais.
- Tributos.
- Investimentos adicionais.
- Fluxos líquidos por período.

Identificar a TMA e sua periodicidade.

Utilizar os scripts disponíveis em `scripts/`:

| Script | Finalidade |
|---|---|
| `cash_flow.py` | Fluxo de caixa |
| `npv_irr.py` | VPL, TIR, VP e VF |
| `payback.py` | Payback simples e descontado |
| `roi.py` | Retorno sobre investimento |
| `agile_evm.py` | Indicadores de valor agregado |

Executar os scripts utilizando os dados fornecidos pelo usuário.

Se os scripts possuírem valores fixos de exemplo, verificar e adaptar esses valores antes de utilizar os resultados como avaliação do TCC.

Nunca apresentar resultados de exemplos como se fossem dados reais do projeto.

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

Apresentar fórmulas, resultados, moeda e periodicidade.

Explicar se os indicadores demonstram atratividade econômica.

### Etapa 6 — Gerenciamento de Valor Agregado

Avaliar o desenvolvimento por sprint ou período.

Levantar:
- Valor Planejado (VP).
- Valor Agregado (VA).
- Custo Real (CR).
- Orçamento no Término (BAC).

Calcular:
- IDC/CPI.
- IDP/SPI.
- Variação de custo.
- Variação de prazo.
- Estimativa no Término (EAC).

Não inventar dados históricos de sprints.

Quando não houver registros, solicitar estimativas e identificá-las como tais.

### Etapa 7 — Avaliação estratégica

Avaliar:
- Potencial de comercialização.
- Modelos de monetização.
- Preço de venda.
- Custos de manutenção.
- Valor percebido pelo jogador.
- Substituição de componentes legados.
- Melhorias necessárias.
- Priorização do backlog.
- Princípio do Bom o Suficiente.

Comparar o custo das funcionalidades com o benefício esperado.

### Etapa 8 — Proposta econômica

Produzir uma recomendação para tomada de decisão contendo:

- Investimento necessário.
- Benefícios esperados.
- Indicadores financeiros.
- Riscos.
- Premissas.
- Modelo de negócio recomendado.
- Alternativas de investimento.
- Conclusão sobre viabilidade.

## 3. Dados conhecidos do Ctrl the Witch

Utilizar os dados abaixo como referência inicial, sem presumir que sejam definitivos.

**Caracterização técnica:**
- Engine: GameMaker.
- Plataforma de distribuição: Windows.
- Total de arquivos: 587.
- Tamanho: 92,89 MB.
- Arquivos GML: 140.
- Linhas GML reportadas: 10.891.
- Objetos: 152 arquivos.
- Scripts: 48 arquivos.
- Salas: 27 arquivos.
- Sprites: 270 arquivos.
- Sons: 22 arquivos.
- Fontes: 44 arquivos.

**Equipe e investimento estimado:**
- Integrantes: 2.
- Período estimado: 90 dias.
- Jornada diária considerada para a equipe: 6 horas.
- Horas totais estimadas: 540.
- Custo de oportunidade: R$ 20,00 por hora por integrante.
- Investimento econômico estimado: R$ 10.800,00.

Esses valores são estimativas retrospectivas e devem ser confirmados pela equipe quando necessário.

## 4. Relatório final

Gerar um relatório em Markdown contendo:

1. Identificação do jogo.
2. Caracterização técnica.
3. Funcionalidades identificadas.
4. Premissas econômicas.
5. Investimento inicial.
6. Custos diretos e indiretos.
7. Fluxo de caixa.
8. VP e VF.
9. VPL.
10. TIR.
11. Payback simples e descontado.
12. ROI.
13. CAC e LTV, quando aplicáveis.
14. Indicadores GVA/EVM.
15. Depreciação e tributos.
16. Modelo de negócio.
17. Priorização de melhorias.
18. Riscos econômicos.
19. Conclusão sobre viabilidade.

Salvar preferencialmente em:

`examples/tcc-valuation-report.md`

## 5. Regras de confiabilidade

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
- Registrar limitações da análise.
- Explicar os resultados em linguagem acessível.

## 6. Divulgação progressiva

Consultar os recursos conforme a necessidade:

- `references/game-analysis.md`: análise técnica de jogos GameMaker.
- `references/economic-methods.md`: fundamentos e fórmulas econômicas.
- `scripts/`: execução dos cálculos financeiros.
- `assets/`: materiais auxiliares, quando disponíveis.

Não carregar todos os recursos desnecessariamente.

Priorizar a análise dos arquivos reais do projeto antes de formular conclusões econômicas.
