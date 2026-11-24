
# Análise Técnica de Jogos GameMaker

## 1. Objetivo

Orientar a análise técnica de jogos desenvolvidos na
engine GameMaker para apoiar a Engenharia Econômica.

## 2. Arquivos do projeto

Identificar e analisar:

- .yyp: arquivo principal do projeto.
- .yy: configurações de recursos.
- .gml: códigos e scripts.
- Sprites: recursos gráficos.
- Objects: entidades e comportamentos.
- Rooms: telas, fases e ambientes.
- Sounds: músicas e efeitos sonoros.
- Fonts: fontes utilizadas.

## 3. Inventário técnico

Registrar:

- Quantidade total de arquivos.
- Tamanho total do projeto.
- Quantidade de scripts GML.
- Quantidade de linhas de código.
- Quantidade de objetos.
- Quantidade de salas.
- Quantidade de sprites.
- Quantidade de sons.
- Dependências e extensões.

## 4. Identificação de funcionalidades

Investigar os códigos para identificar:

- Sistema de movimentação.
- Interface e menus.
- Inventário.
- Interações.
- Personagens e NPCs.
- Progressão de fases.
- Minijogos.
- Sistema de salvamento.
- Áudio.
- Configurações.

Não concluir que uma funcionalidade está completa
apenas pela existência de um arquivo com determinado nome.

## 5. Complexidade técnica

Avaliar qualitativamente:

- Quantidade de componentes.
- Responsabilidades dos objetos.
- Dependências entre sistemas.
- Reutilização de scripts.
- Complexidade dos algoritmos.
- Necessidade de manutenção.

A quantidade de linhas de código não deve ser
utilizada isoladamente como medida de complexidade.

## 6. Auditoria de histórico, monetização e dependências

Ao atualizar o inventário, documentar o método de contagem, se o diretório
`.git` foi excluído, a unidade de tamanho (bytes/MB/MiB) e se a contagem de
linhas inclui linhas em branco e comentários. Não copiar métricas antigas sem
revalidá-las.

Inspecionar opções de exportação e artefatos de build separadamente. A
existência de configuração para uma plataforma não comprova que o jogo foi
compilado, executado ou publicado nela. Procurar executáveis/instaladores
antes de afirmar que há build distribuível.

Pesquisar no código mecanismos comerciais reais (lojas, billing, anúncios,
DLC, compras no aplicativo) e distinguir esses mecanismos da economia interna
de gameplay, como moedas, mana, gorjetas e preços de melhorias. Valores de
moeda virtual não são receita financeira.

Verificar cada extensão ou recurso externo em três níveis:

1. declarado em metadados/configuração;
2. referenciado ou chamado pelo código;
3. disponível e funcional no ambiente/artefato de build.

Referências a recursos ausentes e extensões específicas de plataforma devem
ser descritas com seus arquivos e limitações. Uma análise estática não
comprova o efeito em runtime.

Para avaliar sprints ou GVA/EVM, procurar backlog e datas de baseline,
estimativas, critérios de aceite/progresso, horas/custos reais e BAC. Histórico
de commits isoladamente não fornece VP, VA, CR ou BAC e não permite reconstruir
indicadores de desempenho.

## 7. Relação com custos econômicos

Relacionar os componentes identificados com:

- Esforço de desenvolvimento.
- Horas de manutenção.
- Custos de infraestrutura.
- Custos de ferramentas.
- Necessidade de atualização.
- Possíveis melhorias.

Não converter automaticamente quantidade de arquivos
em valores monetários.

## 8. Confiabilidade

Diferenciar:

- Informações verificadas nos arquivos.
- Inferências baseadas na estrutura.
- Informações fornecidas pela equipe.
- Estimativas econômicas.

Registrar limitações da inspeção técnica.

### Caso auditado: Ctrl the Witch

O inventário revisado do projeto original registra 587 arquivos, 97.399.070
bytes (97,40 MB decimais ou 92,89 MiB), 140 arquivos GML e 12.966 linhas
físicas. As 8 salas principais são recursos sob `rooms/`; os quantitativos
de recursos (incluindo arquivos `.yy` e assets) devem ser distinguidos do
número de recursos GameMaker.

A configuração identifica GameMaker IDE 2024.14.4.222, 60 FPS e opção de
build Windows. Outras opções de plataforma não comprovam execução ou teste.
Não foi encontrado executável/instalador empacotado nem implementação de
monetização comercial. Compras de mana/melhorias são economia virtual.

Uma análise estática anterior identificou:

- inconsistência entre `fase.id` e o índice zero-based no fluxo de
  progressão/salvamento, além de `mana_ganha` não persistido nos scripts
  `scr_finalizar_fase.gml`, `scr_load_game.gml` e `scr_save_game.gml`;
- divergência entre alguns preços exibidos em `scr_melhorias.gml` e valores
  efetivamente cobrados no controlador de fase;
- referência a shader SDF ausente e extensão `ext_capslock` declarada e
  chamada no sistema de digitação, com dependência nativa de Windows.

Esses são resultados de inspeção de código, não de execução/playtest; efeitos
de runtime não foram confirmados. O repositório GameMaker tem 130 commits entre
2026-01-28 e 2026-11-20, mas não contém registros de sprint, horas, baseline
ou dados VP/VA/CR/BAC.
