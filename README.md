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

Projetos de jogos combinam esforço de desenvolvimento, ferramentas, conteúdo,
publicação e possíveis receitas. Sem organizar esses dados, é difícil
comparar alternativas, compreender o custo de oportunidade ou avaliar a
viabilidade econômica sem confundir estimativas com valores efetivamente
recebidos ou pagos.

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
│           │   └── roi.py
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
- `tests/`: diretório destinado a testes; atualmente `test_financial.py` não
  contém casos de teste.

Arquivos gerados de cache do Python, como `__pycache__`, não fazem parte da
estrutura-fonte documentada.

## 6. Funcionalidades

### Implementadas nos scripts

- **Estimativa de custos:** horas totais e por integrante, custo de
  oportunidade e desembolsos adicionais informados, separados. Desembolsos
  omitidos permanecem desconhecidos.
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
devem ser tratados apenas como demonstrações.

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

> Estime o custo de desenvolvimento com 2 integrantes, 90 dias, 6 horas
> diárias para a equipe e R$ 20,00 por hora por integrante. Não presuma
> desembolsos adicionais.

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
| `cost_estimator.py` | Estimar esforço, custo de oportunidade e desembolsos adicionais informados. | Integrantes, dias, horas diárias da equipe, custo/hora/integrante e mapa opcional de desembolsos. A execução direta usa os dados estimados do Ctrl the Witch. | Horas totais e por integrante, custo da mão de obra, desembolsos informados ou desconhecidos e subtotal econômico conhecido. |
| `cash_flow.py` | Calcular fluxo líquido e saldo acumulado; exibir o estado atual do Ctrl the Witch sem criar projeções. | Investimento inicial, receitas e custos por período; tributos e CapEx precisam ser informados para concluir o cálculo. | Detalhes e totais por período, ou indicação de fluxo incompleto. O modo padrão mostra limitações do cenário atual; `--exemplo-didatico` executa um exemplo hipotético. |
| `npv_irr.py` | Calcular VP, VF, VPL e TIR. | VP/VF: valor, taxa decimal e períodos. VPL: série começando no período zero e taxa por período. TIR: série com fluxos positivos e negativos. | Valor presente, valor futuro, VPL ou TIR por período. |
| `payback.py` | Calcular Payback simples e descontado. | Série iniciada com investimento negativo; fluxos futuros não negativos; taxa por período para o descontado. | Número de períodos para recuperação ou `None` se não recuperar no horizonte. |
| `roi.py` | Calcular o retorno percentual sobre investimento. | Investimento maior que zero e retorno total. | ROI em percentual. |
| `agile_evm.py` | Calcular indicadores de GVA/EVM. | VP (`planned_value`), VA (`earned_value`), CR (`actual_cost`) e BAC. | IDC/CPI, IDP/SPI, variações de custo e prazo, EAC e fator estimado de duração. |
| `game_valuation.py` | Consolidar indicadores financeiros para um projeto de jogo e representar o cenário atual do Ctrl the Witch. | Investimento, fluxos líquidos futuros, TMA, periodicidade e classificação dos dados nas funções genéricas. | VPL, TIR, Paybacks e ROI, ou justificativa de não cálculo. A execução padrão mostra o cenário atual; `--exemplo-hipotetico` é separado. |

Os módulos importados entre scripts são arquivos locais do próprio diretório.
Não há dependência de pacote externo.

## 10. Aplicação prática: Ctrl the Witch

Os dados abaixo são premissas e informações levantadas para a análise do TCC.
Os valores de esforço e custo são **estimativas retrospectivas**, não
apontamentos de horas auditados.

| Dado | Valor | Classificação/observação |
|---|---:|---|
| Engine | GameMaker | Informação do projeto |
| Plataforma de distribuição identificada | Windows | Caracterização técnica |
| Integrantes | 2 | Informação da equipe |
| Período considerado | 90 dias | Estimado |
| Jornada diária | 6 horas para a equipe | Premissa estimada |
| Horas totais estimadas | 540 horas | 90 dias × 6 horas/dia |
| Horas por integrante, com divisão igual | 270 horas | 540 ÷ 2 |
| Custo de oportunidade | R$ 20,00 por hora por integrante | Premissa estimada |
| Investimento econômico estimado em mão de obra | R$ 10.800,00 | 540 horas × R$ 20,00/hora |

**Investimento econômico** representa o valor do trabalho dedicado ao jogo
em comparação com o uso alternativo desse tempo. Não comprova que a equipe
tenha recebido ou desembolsado R$ 10.800,00. Desembolso financeiro efetivo
com mão de obra, licenças, assets, ferramentas, energia, internet e
equipamentos não foi quantificado no relatório.

O cenário atual também registra publicação gratuita no itch.io e receita
comercial informada de R$ 0,00, sem vendas nem doações. Esse valor atual não
é uma projeção de receitas futuras.

## 11. Demonstração dos resultados

O [relatório de valoração do TCC](.agents/skills/game-economic-engineering/examples/tcc-valuation-report.md)
documenta a caracterização técnica do Ctrl the Witch e a estimativa inicial
de investimento. Entre os números registrados estão:

- 587 arquivos e 92,89 MB no inventário técnico;
- 140 arquivos GML e 10.891 linhas GML reportadas;
- 152 arquivos na pasta de objetos, 48 na pasta de scripts e 27 na pasta de
  salas;
- 270 arquivos de sprites, 22 de sons e 44 de fontes;
- oito salas principais identificadas pelo nome;
- investimento econômico estimado em mão de obra de R$ 10.800,00, conforme as
  premissas da seção anterior.

Os quantitativos descrevem o inventário e não medem, isoladamente,
complexidade, qualidade ou produtividade. O relatório não documenta fluxos
líquidos futuros, TMA, receitas futuras, VPL, TIR, Payback ou ROI calculados
com dados reais do jogo. Portanto, não há base documentada nesse relatório
para apresentar esses indicadores como resultados do Ctrl the Witch.

## 12. Testes e validação

O projeto não declara frameworks de teste nem dependências externas. O
arquivo `tests/test_financial.py` está vazio; portanto, atualmente não há
casos de teste automatizados. O comando padrão de descoberta do `unittest`
funciona, mas executa zero testes:

```powershell
python -m unittest discover -s .agents/skills/game-economic-engineering/tests -v
```

Os scripts podem ser executados diretamente para verificar que iniciam e
produzem suas demonstrações:

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

Essas execuções são verificações de funcionamento e demonstrações, não uma
suíte de testes que valide todas as entradas e casos-limite. Os exemplos de
`npv_irr.py`, `payback.py`, `roi.py` e `agile_evm.py` usam dados hipotéticos;
não interprete sua saída como avaliação real do jogo.

## 13. Conteúdos de Engenharia Econômica

`references/economic-methods.md` e `SKILL.md` documentam a aplicação dos
seguintes conteúdos:

| Conteúdo documentado | Relação com a Skill |
|---|---|
| Processo de decisão e comparação de alternativas | Comparar desenvolver, adquirir, contratar, adiar ou substituir componentes. |
| Valor do dinheiro no tempo e TMA | VP, VF, taxa por período e desconto de fluxos. |
| Custos e fluxo de caixa | Investimento, custo de oportunidade, OpEx, CapEx, tributos e fluxos líquidos. |
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
- O período, as horas e a taxa horária usados no custo de mão de obra são
  premissas estimadas e devem ser confirmados pela equipe.
- O custo de oportunidade não equivale automaticamente a desembolso.
- Custos indiretos, CapEx adicional e tributos não foram levantados; não
  devem ser interpretados como zero.
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

- Integrante 1: ____________________________________  RA: ______________
- Integrante 2: ____________________________________  RA: ______________

**Docente:** Msc. Ujeverson Tavares Sampaio

## 16. Licença

Não foi encontrada uma licença especificada para este repositório. Os termos
de uso, cópia e distribuição ainda precisam ser definidos pelos autores.
