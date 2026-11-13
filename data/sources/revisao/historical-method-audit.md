# Auditoria do método histórico

Data da inspeção: 30 de setembro de 2026. Esta auditoria examina os registros disponíveis; não reconstrói decisões de seleção que não foram documentadas. Nenhum procedimento novo descrito abaixo deve ser atribuído retrospectivamente aos autores.

## Fontes inspecionadas

- Manuscrito original preservado em `revisao/main-original.tex`, seção `sec:methodology`, especialmente linhas 741–810.
- Figura original `imgs/methodology/selection-criteria.png`, inspecionada visualmente. O rótulo original era `fig:selection-criteria`.
- Repositório público citado como `https://github.com/rodrigodg1/privacy-survey`, que atualmente redireciona para [blockchain-survey](https://github.com/rodrigodg1/blockchain-survey).
- Snapshot público principal: commit [67acd264f6eeecbc9dda91d3027d1c875295f4ec](https://github.com/rodrigodg1/blockchain-survey/tree/67acd264f6eeecbc9dda91d3027d1c875295f4ec), de 17/11/2023, 15:22:13 UTC.
- Snapshot histórico com seleção parcial: commit [07b9d3cae5c5c03984171fd6bd1b5fb265dbf797](https://github.com/rodrigodg1/blockchain-survey/tree/07b9d3cae5c5c03984171fd6bd1b5fb265dbf797), de 30/05/2023, 18:24:22 UTC.
- Snapshot posterior em que o arquivo de seleção já não aparece: [24d3dd6e274fb6f1cd5dd29677e9bdf2b7a473b5](https://github.com/rodrigodg1/blockchain-survey/tree/24d3dd6e274fb6f1cd5dd29677e9bdf2b7a473b5), de 16/11/2023, 12:15:40 UTC.

As árvores e os metadados de commits foram conferidos pela API pública do GitHub. Os CSVs foram lidos como dados com `csv.DictReader`; o código remoto não foi executado.

## Protocolo recuperável

O texto ativo informa buscas em Google Scholar, Scopus e ACM Digital Library, com palavras no título e sem restrição de ano. A figura contém as mesmas famílias de consultas. Os identificadores abaixo corrigem a repetição de S03/S04/S05 no texto original, sem alterar os predicados.

| ID | Base | Consulta histórica |
|---|---|---|
| S01 | Google Scholar | `allintitle: blockchain data privacy` |
| S02 | Scopus | `TITLE(blockchain) AND TITLE(data) AND TITLE(privacy)` |
| S03 | ACM DL | `[Title: blockchain] AND [Title: data] AND [Title: privacy]` |
| S04 | Google Scholar | `allintitle: blockchain (consent OR permission)` |
| S05 | Scopus | `TITLE(blockchain) AND (TITLE(consent) OR TITLE(permission))` |
| S06 | ACM DL | `[Title: blockchain] AND [[Title: consent] OR [Title: permission]]` |
| S07 | Google Scholar | `allintitle: blockchain (decentralized OR self-sovereign) identity` |
| S08 | Scopus | `TITLE(blockchain) AND TITLE(decentralized OR self-sovereign) AND TITLE(identity)` |
| S09 | ACM DL | `[Title: blockchain] AND [[Title: decentralized] OR [Title: self-sovereign]] AND [Title: identity]` |

O [README publicado](https://github.com/rodrigodg1/blockchain-survey/blob/67acd264f6eeecbc9dda91d3027d1c875295f4ec/README.md) reproduz as consultas Google Scholar/Scopus; não define triagem ou limites de seleção. Também lista aprendizagem federada, fora das três famílias ativas deste survey.

Não foi recuperado um critério explícito de idioma, revisão por pares, tipo de publicação, disponibilidade de texto integral, escore de qualidade, limiar de citações ou número máximo de resultados. O escopo temático do texto ativo é privacidade, consentimento e identidade descentralizada/SSI. Não há exigência documentada de que um estudo implemente simultaneamente as três funções.

## Figura versus arquivos publicados

| Família | Google na figura | Scopus na figura | ACM na figura | Concatenação na figura | “Duplicated Total” | Selecionados |
|---|---:|---:|---:|---:|---:|---:|
| Privacidade | 674 | 394 | 39 | 1107 | 668 | 40 |
| Consentimento | 164 | 88 | 45 | 297 | 159 | 33 |
| Identidade | 209 | 104 | 6 | 319 | 149 | 25 |

Os arquivos do snapshot principal têm contagens diferentes:

| Arquivo | Registros | DOI vazio |
|---|---:|---:|
| `privacy/google.csv` | 674 | 536 |
| `privacy/scopus.csv` | 394 | 12 |
| `privacy/acm.csv` | 21 | 1 |
| `consent/google.csv` | 154 | 132 |
| `consent/scopus.csv` | 88 | 6 |
| `consent/acm.csv` | 45 | 0 |
| `identity/google.csv` | 148 | 123 |
| `identity/scopus.csv` | 104 | 4 |
| `identity/acm.csv` | 6 | 0 |

Os arquivos podem ser inspecionados nas pastas [privacy](https://github.com/rodrigodg1/blockchain-survey/tree/67acd264f6eeecbc9dda91d3027d1c875295f4ec/privacy), [consent](https://github.com/rodrigodg1/blockchain-survey/tree/67acd264f6eeecbc9dda91d3027d1c875295f4ec/consent) e [identity](https://github.com/rodrigodg1/blockchain-survey/tree/67acd264f6eeecbc9dda91d3027d1c875295f4ec/identity).

O [process-papers.py](https://github.com/rodrigodg1/blockchain-survey/blob/67acd264f6eeecbc9dda91d3027d1c875295f4ec/process-papers.py) concatena os arquivos na ordem Google, Scopus, ACM e aplica estas operações:

```python
df = pd.concat([df1, df2,df3])
df = df.drop_duplicates(subset=['DOI'], keep='first')
df = df.drop_duplicates(subset=['Title'], keep='first')
```

A contagem foi reproduzida por uma leitura independente dos CSVs, emulando comparações exatas e equivalência dos DOI ausentes:

| Família | Concatenação dos CSVs | Removidos por DOI | Removidos por título depois do DOI | Registros restantes | Arquivo de saída publicado |
|---|---:|---:|---:|---:|---|
| Privacidade | 1089 | 668 | 10 | 411 | `privacy/privacy_merged_dataset.csv` (411) |
| Consentimento | 287 | 159 | 2 | 126 | `consent/consent_merged_dataset.csv` (126) |
| Identidade | 258 | 149 | 1 | 108 | `identity/fl_merged_dataset.csv` (108) |

Portanto, as caixas “Duplicated Total” coincidem exatamente com o primeiro estágio de exclusão por DOI. Elas não representam registros únicos restantes nem incluem o estágio posterior por título. A divergência entre os totais da figura e os CSVs permanece: não há evidência suficiente para atribuí-la a uma determinada rodada de busca ou corrigir os totais históricos no manuscrito.

Há uma falha na deduplicação publicada: DOI vazio é tratado como um valor repetido. Assim, registros distintos sem DOI podem ser descartados antes da comparação por título. Sob essa implementação, 548 dos 549 registros de privacidade sem DOI, 137 dos 138 de consentimento e 126 dos 127 de identidade são eliminados por ausência compartilhada de identificador. Não são duplicatas bibliográficas comprovadas. A atualização deve comparar DOI normalizado somente quando não vazio e usar título e metadados para registros sem DOI, documentando a correção; não deve reproduzir a falha para alegar fidelidade ao protocolo.

## Datas recuperadas e campos bibliométricos

O campo `QueryDate` é uniforme em cada exportação Google Scholar:

| Arquivo | `QueryDate` registrado | `GSRank` observado | Registros com `Cites = 0` |
|---|---|---|---:|
| `privacy/google.csv` | `2023-11-16 18:25:10` | 1–674 | 218 |
| `consent/google.csv` | `2023-11-17 09:14:23` | 1–154 | 37 |
| `identity/google.csv` | `2023-11-17 09:33:29` | 1–148 | 45 |

Esses campos documentam timestamps das exportações, com fuso não especificado, e posições de resultados. Não estabelecem as datas de toda a seleção, execução nas outras bases, esgotamento de paginação ou uso das citações como filtro. Os arquivos Scopus incluem artigos, trabalhos de conferência, capítulos e reviews; a existência desses registros no conjunto de busca não define os tipos elegíveis na seleção final.

O arquivo `total_works_by_year.csv` apresenta contagens anuais de 2015–2022 e inclui aprendizagem federada. Não é um registro de decisões de inclusão/exclusão e não deve fornecer o denominador da atualização.

## Menção a priorização por citações: somente comentário

Em `revisao/main-original.tex:793`, a frase “We prioritize and select the most highly-cited works in the corresponding publication year” está precedida por `%`. A mesma linha comentada também menciona trabalhos recentes pouco citados escolhidos pela contribuição.

Essa passagem não integra o texto renderizado. Nem o comentário nem os scripts estabelecem limiar, quota anual, top N, ordenação aplicada à seleção, tratamento de empates ou justificativa por candidato. Não autoriza apresentar priorização por citações como procedimento efetivamente executado.

O [privacy/selected-works.csv do commit de maio de 2023](https://github.com/rodrigodg1/blockchain-survey/blob/07b9d3cae5c5c03984171fd6bd1b5fb265dbf797/privacy/selected-works.csv) contém 27 estudos, com ano, caso de uso, técnica, plataforma, disponibilidade de implementação e `Cited by`. Não contém motivo de seleção/exclusão. Os registros estão agrupados cronologicamente; as citações não estão em ordem decrescente, inclusive dentro do ano. Esse arquivo é uma seleção parcial histórica de privacidade, não a seleção final 40/33/25. Nenhum arquivo equivalente foi identificado para as outras duas famílias naquele snapshot.

O [run.py](https://github.com/rodrigodg1/blockchain-survey/blob/67acd264f6eeecbc9dda91d3027d1c875295f4ec/run.py) contém comparação por título e um filtro de ano comentado. Não implementa seleção por citações.

## O que permanece sem documentação

Não foram recuperados: etapas completas de triagem por título/resumo/texto integral; decisões individuais e motivos de exclusão; identidade e número de revisores de seleção; avaliações independentes; resolução de discordâncias; acordo interavaliadores; busca retrospectiva/prospectiva por citações; cobertura completa dos resultados de cada base; ou passagem reproduzível dos conjuntos deduplicados para os 98 estudos.

Uma auditoria independente realizada por outro agente de IA não equivale a triagem humana independente e não permite calcular IRR. A existência do repositório e desta auditoria melhora a inspeção dos dados disponíveis, mas não resolve essas lacunas.

Para a revisão, é possível preservar os predicados documentados, identificar a janela contemporânea como uma decisão da atualização, corrigir deduplicação de DOI ausente e publicar decisões atuais verificáveis. Executar parcialmente Google Scholar não equivale a concluir uma atualização nas três bases originais. Os 98 registros históricos devem permanecer separados da nova seleção.
