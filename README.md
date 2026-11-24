# Game Economic Engineering

Ferramenta acadêmica de apoio à análise técnica e à Engenharia Econômica de
projetos de jogos digitais. A Skill utiliza diretrizes e scripts Python para
organizar premissas e calcular indicadores financeiros de forma determinística.

> **Escopo:** os resultados dependem dos dados fornecidos pela equipe. Os
> exemplos numéricos dos scripts são didáticos e não representam resultados
> reais do Ctrl the Witch, salvo quando identificados explicitamente como
> informações ou estimativas do projeto.

## 1. Identificação do projeto

| Campo | Informação |
|---|---|
| Projeto | Game Economic Engineering |
| Instituição | Faculdade SENAI FATESG |
| Curso | Bacharelado em Engenharia de Software |
| Disciplina | Engenharia Econômica |
| Docente | Msc. Ujeverson Tavares Sampaio |
| Projeto de TCC analisado | Ctrl the Witch |

## 2. Sobre o projeto

O Game Economic Engineering reúne uma **Agent Skill** especializada e scripts
Python para apoiar esse trabalho. A Skill orienta um agente de Inteligência
Artificial (IA) a examinar os dados do jogo, solicitar informações ausentes,
explicitar premissas e apresentar limitações. Os scripts executam os cálculos
numéricos; o agente deve consultá-los para indicadores determinísticos, em vez
de estimar resultados financeiros por geração de texto.

A ferramenta não substitui registros contábeis, pesquisa de mercado nem a
decisão da equipe. Ela oferece uma estrutura de análise, não uma garantia de
rentabilidade.

## 3. Objetivos

### Objetivo geral

Aplicar conceitos de Engenharia Econômica à análise de jogos digitais,
combinando levantamento técnico assistido por IA com cálculos reproduzíveis
em Python.

### Objetivos específicos

- Organizar dados técnicos e econômicos disponíveis e identificar lacunas.
- Estimar o custo de oportunidade do trabalho e separar desembolsos
  financeiros.
- Modelar fluxos de caixa sem converter dados desconhecidos em zero.
- Calcular indicadores de valor do dinheiro no tempo, retorno e recuperação
  do investimento quando os dados permitirem.
- Apoiar o acompanhamento de desempenho por Gerenciamento de Valor Agregado
  (GVA/EVM).
- Documentar premissas, classificações dos dados e limitações de cada
  análise.
- Apoiar a discussão de alternativas e viabilidade sem declarar conclusões
  que os dados não sustentem.

## 4. Tecnologias utilizadas

| Tecnologia | Uso observado |
|---|---|
| Python | Implementação dos cálculos e exemplos dos scripts financeiros. |
| Biblioteca padrão do Python | Validação e cálculos com módulos como `math`, `numbers` e `collections.abc`. |
| Git | Controle de versão do repositório. |
| GitHub | Hospedagem remota configurada como `origin`: [Isaluh/skill-tcc](https://github.com/Isaluh/skill-tcc). |
| Agent Skills | Formato da Skill, com metadados YAML no `SKILL.md` e recursos auxiliares. |
| Harness compatível com Agent Skills | Necessário para o agente carregar e seguir a Skill. O repositório não declara configuração de um fornecedor ou harness específico. |
| Visual Studio Code | Pode ser usado como editor; o VS Code, por si só, não carrega a Skill sem um agente/harness compatível. |

Os scripts não importam bibliotecas Python de terceiros. Não há arquivo
`requirements.txt` nem outro manifesto de dependências Python no repositório.
Foi verificada a execução com Python 3.11.9.

## 5. Estrutura do repositório

```text
game-economic-engineering/
├── .gitignore
├── .agents/
│   └── skills/
│       └── game-economic-engineering/
│           ├── SKILL.md
│           ├── examples/
│           │   └── tcc-valuation-report.md
│           ├── references/
│           │   ├── economic-methods.md
│           │   └── game_analysis.md
│           ├── scripts/
│           │   ├── agile_evm.py
│           │   ├── cash_flow.py
│           │   ├── cost_estimator.py
│           │   ├── game_valuation.py
│           │   ├── npv_irr.py
│           │   ├── payback.py
│           │   ├── roi.py
│           │   └── sales_model.py
│           └── tests/
│               └── test_financial.py
└── README.md
```

- `.agents/skills/game-economic-engineering/`: Skill e todos os seus
  recursos.
- `SKILL.md`: objetivo, fluxo de análise, dados conhecidos do jogo e regras de
  confiabilidade para o agente.
- `references/economic-methods.md`: conceitos, fórmulas e orientações de
  Engenharia Econômica.
- `references/game_analysis.md`: roteiro de inspeção técnica de projetos
  GameMaker.
- `scripts/`: funções e exemplos executáveis de cálculo.
- `examples/tcc-valuation-report.md`: relatório de caracterização técnica e
  estimativa inicial de investimento do Ctrl the Witch.
- `tests/`: testes de regressão com `unittest`, incluindo cenários financeiros
  atuais e vendas hipotéticas.
- `.gitignore`: impede versionar arquivos de cache do Python.

Arquivos gerados de cache do Python, como `__pycache__`, são ignorados pelo
Git e não fazem parte da estrutura-fonte.

## 6. Funcionalidades

### Implementadas nos scripts

- **Estimativa de custos:** horas totais da equipe e média por integrante
  sob hipótese de divisão igual, custo de oportunidade com taxa da equipe e
  desembolsos adicionais informados, separados. Desembolsos omitidos
  permanecem desconhecidos.
- **Fluxo de caixa:** calcula fluxos líquidos e saldos por período quando os
  dados necessários são fornecidos. A função retorna o fluxo como incompleto
  quando tributos ou CapEx não foram informados. O cenário atual do Ctrl the
  Witch é apresentado sem inventar períodos ou custos.
- **VP e VF:** calcula valor presente e valor futuro com taxa e período.
- **VPL e TIR:** calcula valor presente líquido e taxa interna de retorno.
  Fluxos que podem produzir TIR ambígua são tratados com limitação explícita.
- **Payback simples e descontado:** estima o tempo de recuperação dos fluxos
  informados; `None` representa que não houve recuperação no horizonte
  fornecido.
- **ROI:** calcula retorno percentual para valores de investimento e retorno
  informados.
- **GVA/EVM:** calcula IDC/CPI, IDP/SPI, variações de custo e prazo, EAC e
  fator estimado de duração a partir de VP, VA, CR e BAC.
- **Vendas e ponto de equilíbrio:** simula receita bruta mensal/anual; calcula
  receita líquida somente quando taxas, quantidade de transações e tributos
  são informados; calcula unidades para break-even somente com custo fixo e
  margem de contribuição conhecidos. A receita após esses itens não equivale
  ao lucro total do projeto.
- **Valoração financeira de projetos de jogos:** `game_valuation.py` reúne
  VPL, TIR, paybacks e ROI. Isso é uma avaliação por indicadores financeiros,
  não uma estimativa automática de preço de mercado do jogo.

### Metodologia documentada, mas sem implementação específica completa

`SKILL.md` e `economic-methods.md` orientam análise de viabilidade, modelos
de negócio, depreciação, tributos, CAC/LTV e priorização econômica. Nem todos
esses tópicos têm calculadoras próprias. A análise completa de viabilidade
continua dependendo de dados do projeto, como fluxos líquidos por período,
custos, horizonte e TMA. A demonstração atual do Ctrl the Witch não permite
concluir sua viabilidade financeira.

Os exemplos fixos de EVM, VP/VF, VPL/TIR, Payback e ROI são **hipotéticos** e
devem ser tratados apenas como demonstrações. Os cenários de vendas do TCC
também são hipotéticos, não previsões nem receitas realizadas.

## 7. Instalação e configuração

### Pré-requisitos

- Git.
- Python instalado. A execução foi verificada com Python 3.11.9.
- Um harness/agente que suporte Agent Skills para usar a Skill com IA.
- Visual Studio Code é opcional.

### Clonar e preparar o projeto

```powershell
git clone https://github.com/Isaluh/skill-tcc.git
cd skill-tcc
python --version
```

Um ambiente virtual é opcional, pois os scripts usam apenas a biblioteca
padrão do Python:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Não é necessário executar `pip install`: não há dependências externas
declaradas. Para abrir a pasta no VS Code, com o comando `code` disponível:

```powershell
code .
```

### Localizar e carregar a Skill

A Skill está em:

```text
.agents/skills/game-economic-engineering/
```

O arquivo de entrada é
`.agents/skills/game-economic-engineering/SKILL.md`. Ele contém o nome e a
descrição da Skill em frontmatter YAML, além das instruções. As pastas
`references/`, `scripts/` e `examples/` fornecem os recursos referenciados por
essas instruções.

Abra a raiz do repositório como workspace no harness compatível e habilite ou
atualize a descoberta de Agent Skills. O harness precisa reconhecer a pasta
`.agents/skills/`; a instalação do VS Code isoladamente não carrega a Skill.
Como não há configuração específica de fornecedor no repositório, consulte a
documentação do harness escolhido para ativar a descoberta nesse caminho.

Para validar a descoberta, peça ao agente para descrever a Skill
`game-economic-engineering` e localizar seus scripts. Se ela não for
encontrada, confirme o workspace e a configuração de descoberta de
`.agents/skills/`.

## 8. Como utilizar

Use prompts que deixem claro o escopo, a origem dos dados e se é permitido
alterar arquivos. Exemplos:

> Analise economicamente este projeto GameMaker apenas em modo de leitura.
> Diferencie informações verificadas, informadas, estimadas e desconhecidas.

> Estime o custo retrospectivo com 2 integrantes, 9 meses (aprox. 39 semanas),
> 6 horas diárias para a equipe e R$ 20,00 por hora da equipe. Compare 5, 6 e
> 7 dias por semana. Identifique tudo como cenário estimado, não como horas
> registradas, e não presuma desembolsos adicionais.

> Com estes fluxos líquidos por período e esta TMA, calcule VPL, TIR, Payback
> simples e descontado. Informe a periodicidade e identifique limitações.

> Avalie o desempenho desta sprint com GVA/EVM. Vou fornecer VP, VA, CR e BAC;
> não invente valores ausentes.

> Elabore um relatório de viabilidade econômica com os dados fornecidos.
> Separe fatos, estimativas e hipóteses e não conclua viabilidade se faltarem
> custos, fluxos, horizonte ou TMA.

Para resultados numéricos, o agente deve consultar e executar o script
adequado em `scripts/`. Isso torna os cálculos reproduzíveis; a interpretação
e a conclusão devem continuar condicionadas à qualidade dos dados fornecidos.

## 9. Scripts financeiros

Os caminhos da tabela são relativos a
`.agents/skills/game-economic-engineering/scripts/`.

| Script | Finalidade | Entradas principais | Saídas |
|---|---|---|---|
| `cost_estimator.py` | Estimar esforço, custo de oportunidade e desembolsos adicionais informados. | Integrantes, dias, horas diárias da equipe, custo por hora da equipe e mapa opcional de desembolsos. A execução direta calcula cenários de 39 semanas para 5, 6 e 7 dias/semana. | Horas totais de equipe, média por integrante sob divisão igual, custo da mão de obra e desembolsos informados ou desconhecidos. |
| `cash_flow.py` | Calcular fluxo líquido e saldo acumulado; exibir o estado atual do Ctrl the Witch sem criar projeções. | Investimento inicial, receitas e custos por período; tributos e CapEx precisam ser informados para concluir o cálculo. | Detalhes e totais por período, ou indicação de fluxo incompleto. O modo padrão mostra limitações do cenário atual; `--exemplo-didatico` executa um exemplo hipotético. |
| `npv_irr.py` | Calcular VP, VF, VPL e TIR. | VP/VF: valor, taxa decimal e períodos. VPL: série começando no período zero e taxa por período. TIR: série com fluxos positivos e negativos. | Valor presente, valor futuro, VPL ou TIR por período. |
| `payback.py` | Calcular Payback simples e descontado. | Série iniciada com investimento negativo; fluxos futuros não negativos; taxa por período para o descontado. | Número de períodos para recuperação ou `None` se não recuperar no horizonte. |
| `roi.py` | Calcular o retorno percentual sobre investimento. | Investimento maior que zero e retorno total. | ROI em percentual. |
| `agile_evm.py` | Calcular indicadores de GVA/EVM. | VP (`planned_value`), VA (`earned_value`), CR (`actual_cost`) e BAC. | IDC/CPI, IDP/SPI, variações de custo e prazo, EAC e fator estimado de duração. |
| `game_valuation.py` | Consolidar indicadores financeiros para um projeto de jogo e representar o cenário atual do Ctrl the Witch. | Investimento, fluxos líquidos futuros, TMA, periodicidade e classificação dos dados nas funções genéricas. | VPL, TIR, Paybacks e ROI, ou justificativa de não cálculo. A execução padrão mostra o cenário atual; `--exemplo-hipotetico` é separado. |
| `sales_model.py` | Simular vendas brutas, receita líquida informada e ponto de equilíbrio. | Preço e cópias mensais para cenários; taxas, transações e tributos para receita líquida; custo fixo e margem de contribuição para break-even. | Receita bruta mensal/anual; receita líquida ou lista de dados ausentes; número inteiro de cópias ou justificativa de não cálculo. |

Os módulos importados entre scripts são arquivos locais do próprio diretório.
Não há dependência de pacote externo.

## 10. Aplicação prática: Ctrl the Witch

Os dados abaixo são premissas e informações levantadas para a análise do TCC.
Os valores de esforço e custo são **estimativas retrospectivas**, não
apontamentos de horas auditados.

| Dado | Valor | Classificação/observação |
|---|---:|---|
| Engine | GameMaker | Informação do projeto |
| Alvo de build | Windows | Opção de exportação identificada; não foi encontrado build empacotado |
| Canal de publicação | itch.io | O levantamento anterior dizia que a publicação era gratuita; configuração atual não verificada |
| Integrantes | 2 | Informação da equipe |
| Duração informada | 9 meses, aproximados como 39 semanas | Informação da equipe |
| Dias de trabalho | 6 dias por semana (segunda a sábado) | Informação da equipe |
| Jornada diária | 6 horas para a equipe inteira | Informação da equipe; não é apontamento de horas |
| Custo de oportunidade | R$ 20,00 por hora da equipe de 2 integrantes | Informação da equipe |
| Desembolso financeiro inicial | R$ 0,00 | Informado pela equipe; não equivale a custo total zero |
| Receita comercial atual | R$ 0,00 | Informada; sem vendas nem doações |
| Preço por unidade | R$ 20,00 | Informado pelo usuário |
| Meta comercial | 10 cópias/mês | Hipótese sem validação de mercado |
| Tributo usado na simulação | 10% da receita bruta | Informação da equipe; base aplicada como premissa |

#### Estimativa de custo de oportunidade

| Dias/semana | Dias estimados | Horas da equipe | Custo de oportunidade |
|---:|---:|---:|---:|
| 6 | 234 | 1.404 | R$ 28.080,00 |

Esta é uma estimativa retrospectiva baseada na jornada informada, não em
registros de ponto. O custo é calculado como 1.404 horas da equipe ×
R$ 20,00 por hora da equipe.

**Investimento econômico** representa o valor do trabalho dedicado ao jogo
em comparação com o uso alternativo desse tempo. Não comprova que a equipe
tenha recebido ou desembolsado esse valor. O desembolso financeiro inicial
informado é R$ 0,00. Energia e internet foram usadas, mas seus custos não
foram medidos; isso não significa que todas as categorias custaram zero.

O levantamento anterior informava que a publicação no itch.io era gratuita e
não tinha receita comercial. O usuário informou que o preço do jogo é
R$ 20,00 por unidade; a configuração atual da página não foi verificada. A
meta de 10 cópias/mês é hipotética. As simulações descontam apenas o tributo
informado de 10% da receita bruta:

| Cópias/mês | Cópias/ano | Receita bruta/mês | Tributo/mês | Após tributo/mês | Receita bruta/ano | Tributo/ano | Após tributo/ano |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 2 | 24 | R$ 40,00 | R$ 4,00 | R$ 36,00 | R$ 480,00 | R$ 48,00 | R$ 432,00 |
| 10 | 120 | R$ 200,00 | R$ 20,00 | R$ 180,00 | R$ 2.400,00 | R$ 240,00 | R$ 2.160,00 |
| 25 | 300 | R$ 500,00 | R$ 50,00 | R$ 450,00 | R$ 6.000,00 | R$ 600,00 | R$ 5.400,00 |

Esses cenários não representam vendas realizadas nem previsões. “Após
tributo” não é a receita líquida total: ainda faltam a participação do
itch.io, taxas de processamento, reembolsos, outros custos e a confirmação
do regime e da base tributária. Considerando somente o tributo informado,
seriam necessárias 1.560 cópias a R$ 18,00 após tributo para recuperar os
R$ 28.080,00 estimados de custo de oportunidade. Esse não é o ponto de
equilíbrio completo.

Segundo a [documentação oficial de pagamentos do itch.io](https://itch.io/docs/creators/payments),
consultada em 2026-11-24, o vendedor configura sua participação entre 0% e
100%. Essa participação é diferente do tributo de 10% informado pela equipe.
As taxas do processador variam por serviço e não foram aplicadas à simulação
em reais. A configuração da página do jogo não foi verificada. O regime e a
base tributária também não foram confirmados; os 10% são usados apenas como
premissa de cálculo.

Uma análise estática anterior também registrou riscos em progressão e
salvamento (`fase.id` versus índice de fase e `mana_ganha` não persistido),
diferenças entre alguns preços exibidos e cobrados em melhorias, referência
a um shader SDF ausente e extensão `ext_capslock` usada pelo sistema de
digitação. Esses são achados técnicos, não evidência de falhas confirmadas em
execução nem de faturamento comercial. A mana é economia virtual do jogo.
A leitura de código também identificou sistemas de digitação, inventário,
pedidos/NPCs, minijogos, progressão, menus, configurações, persistência e
áudio; isso não substitui playtests.

## 11. Demonstração dos resultados

O [relatório de valoração do TCC](.agents/skills/game-economic-engineering/examples/tcc-valuation-report.md)
documenta os dados técnicos auditados, as premissas econômicas da equipe,
os cenários de esforço e receita bruta e as limitações dos indicadores.
Entre os dados registrados estão:

- 587 arquivos e 97,40 MB decimais (92,89 MiB) no inventário técnico;
- 140 arquivos GML e 12.966 linhas físicas nesses arquivos;
- 152 arquivos na pasta de objetos, 48 na pasta de scripts e 27 na pasta de
  salas;
- 270 arquivos de sprites, 22 de sons e 44 de fontes;
- oito salas principais identificadas pelo nome;
- estimativa de custo de oportunidade de R$ 28.080,00, baseada na jornada
  informada, sem registros de horas efetivas.

Os quantitativos descrevem o inventário e não medem, isoladamente,
complexidade, qualidade ou produtividade. O histórico de commits não contém
registros que permitam reconstruir esforço ou EVM. O relatório simula vendas
após o tributo informado de 10%, mas não documenta taxas e custos suficientes
para calcular receita líquida, VPL, TIR, Payback, ROI ou ponto de equilíbrio
completo para o Ctrl the Witch.

## 12. Testes e validação

O projeto não declara frameworks de teste nem dependências externas. Os testes
usam somente `unittest`, biblioteca padrão do Python:

```powershell
python -m unittest discover -s .agents/skills/game-economic-engineering/tests -p "test_*.py" -v
```

Os testes cobrem estimativa de custos, fluxo de caixa, VP/VF, VPL/TIR,
Payback, ROI, GVA/EVM, valoração, vendas brutas/líquidas e ponto de
equilíbrio, incluindo entradas inválidas e dados incompletos.

Para validar sintaxe dos scripts:

```powershell
python -m compileall .agents/skills/game-economic-engineering
```

Os scripts com demonstrações podem ser executados:

```powershell
python .agents/skills/game-economic-engineering/scripts/cost_estimator.py
python .agents/skills/game-economic-engineering/scripts/cash_flow.py
python .agents/skills/game-economic-engineering/scripts/cash_flow.py --exemplo-didatico
python .agents/skills/game-economic-engineering/scripts/game_valuation.py
python .agents/skills/game-economic-engineering/scripts/game_valuation.py --exemplo-hipotetico
python .agents/skills/game-economic-engineering/scripts/npv_irr.py
python .agents/skills/game-economic-engineering/scripts/payback.py
python .agents/skills/game-economic-engineering/scripts/roi.py
python .agents/skills/game-economic-engineering/scripts/agile_evm.py
```

`sales_model.py` contém funções importáveis sem demonstração de linha de
comando. As execuções diretas dos demais módulos são exemplos; não interprete
saídas hipotéticas como resultados reais do jogo.

## 13. Conteúdos de Engenharia Econômica

`references/economic-methods.md` e `SKILL.md` documentam a aplicação dos
seguintes conteúdos:

| Conteúdo documentado | Relação com a Skill |
|---|---|
| Processo de decisão e comparação de alternativas | Comparar desenvolver, adquirir, contratar, adiar ou substituir componentes. |
| Valor do dinheiro no tempo e TMA | VP, VF, taxa por período e desconto de fluxos. |
| Custos e fluxo de caixa | Investimento, custo de oportunidade, OpEx, CapEx, tributos e fluxos líquidos. |
| Vendas e ponto de equilíbrio | Simulação de receita bruta; cálculos líquidos e de break-even dependem de custos/taxas informados. |
| Viabilidade econômica | VPL, TIR, Payback simples e descontado e ROI. |
| Depreciação e tributos | Orientação metodológica; não há calculadora específica ou dados tributários do TCC. |
| Métricas de produtos digitais | CAC e LTV quando aplicáveis; dependem de dados de aquisição, receita e clientes. |
| GVA/EVM | VP, VA, CR, BAC, indicadores de prazo e custo e EAC. |
| Proposta econômica e estratégia | Riscos, premissas, modelo de negócio, melhorias e recomendação condicionada aos dados. |
| Princípio do Bom o Suficiente e backlog | Relacionar benefício esperado, esforço, custo, risco e prioridade. |
| Substituição de legado | Comparar manutenção, migração, incompatibilidade e custos futuros. |

**Relação com as 12 aulas:** os arquivos do repositório não contêm a ementa,
o plano de ensino ou os tópicos individuais das 12 aulas. Para não atribuir
conteúdos curriculares sem evidência, a relação acima é por tema e não por
número de aula. A correspondência aula a aula deve ser completada com o
material oficial da disciplina.

## 14. Limitações e premissas

- Os quantitativos técnicos são os registrados no relatório e não substituem
  uma avaliação qualitativa ou revisão independente do jogo.
- A equipe informou 9 meses, 6 horas diárias para o grupo e R$ 20,00/h para
  a equipe; dias trabalhados por semana não foram apontados. Custos de
  oportunidade são apresentados como cenários estimados.
- O custo de oportunidade não equivale automaticamente a desembolso.
- O desembolso inicial informado é R$ 0,00, mas energia e internet não foram
  mensuradas e outros custos indiretos, CapEx e tributos não foram levantados.
- O preço futuro de R$ 20,00 e 10 cópias mensais são premissas de plano; a
  publicação atual continua identificada como gratuita até confirmação de
  mudança.
- Taxas do itch.io e do processador dependem de configuração, país, moeda,
  método de pagamento e transações. A documentação oficial não determina a
  taxa efetiva deste projeto.
- Receita comercial atual informada como zero não permite assumir receita
  futura nula ou positiva.
- VPL, TIR e Payback exigem fluxos por período e periodicidade; VPL e Payback
  descontado também exigem TMA compatível.
- ROI exige investimento, retorno líquido definido e horizonte de análise.
- EVM exige registros de VP, VA, CR e BAC por período. O exemplo do script
  não é histórico do TCC.
- Depreciação, CAC/LTV, modelo de negócio, impostos e valor de mercado
  dependem de dados e análises que não estão completos no relatório.
- A Skill pode orientar a coleta e interpretação; a confiabilidade final
  depende da origem e qualidade dos dados fornecidos.

## 15. Autores e contexto acadêmico

Projeto desenvolvido no contexto do Bacharelado em Engenharia de Software da
Faculdade SENAI FATESG, na disciplina de Engenharia Econômica.

**Integrantes:**

- Integrante 1: Augusto Lobo 
- Integrante 2: Heloira Medeiros

**Docente:** Msc. Ujeverson Tavares Sampaio

