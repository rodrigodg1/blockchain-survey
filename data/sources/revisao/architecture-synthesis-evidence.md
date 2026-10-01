# Enquadramento arquitetural e síntese do survey

Data: 1 de outubro de 2026. Revisão aplicada a `main.tex`, preservando o título, as quatro RQs do survey, as RQs da tese, os estudos selecionados e as tabelas de resultados existentes. O snapshot anterior está em `main-before-architecture-synthesis.tex`.

## O que foi aplicado

- Abstract e introdução: contribuição expressa como mapeamento de requisitos, pontos de controle e evidências para examinar controle do usuário. Governança delimita atores, políticas e fronteiras de confiança; não substitui o problema arquitetural.
- Related Work: comparação explícita com o survey publicado de QoE, com uma linha adicional na tabela. A distinção é a unidade e o produto da análise, não apenas a abrangência multidomínio. Reconhece-se que o survey anterior já discute governança, identidade e credenciais como direções futuras.
- Método: explicitação de que os requisitos são derivados das comparações qualitativas, sem nova extração uniforme ou taxonomia validada.
- Síntese transversal: separação entre permissão para invocar um serviço, computação sobre entradas protegidas e liberação de resultados. Avaliação pública de ciphertexts não é confundida com acesso ao resultado decriptado.
- Findings: nova subseção `sec:architectural-requirements` e quadro `tab:architecture-requirements`, com cinco fronteiras: identidade/autoridade, permissão/liberação, confidencialidade/correção, evidência/privacidade da auditoria e retirada/status de credenciais. Cada linha liga fontes existentes a requisitos e perguntas de avaliação.
- Direções de avaliação: testar separadamente identidade válida com permissão retirada, liberação não autorizada e resultado incorreto sob permissão válida. São propostas, não resultados adicionados.
- Conclusão: contribuição arquitetural delimitada ao mapeamento analítico e às evidências necessárias para avaliar as relações.

O artigo permanece independente da tese: não contém RQs da tese, resultados do Artigo 3 ou uma alegação de ter executado Design Science Research. Não foram removidos estudos para aproximá-lo artificialmente de QoE; nenhuma nova classificação foi atribuída aos 106 estudos.

## Fontes e alcance

A única referência bibliográfica adicionada é contextual:

- Garcia, Ramachandran, Rothenberg, Krishnamachari e Ueyama. *A Survey of Privacy-Preserving Mechanisms on Quality of Experience in Next-Generation Networks*. Computer Networks 275 (2026), 111899. DOI: [10.1016/j.comnet.2025.111899](https://doi.org/10.1016/j.comnet.2025.111899). Chave `GarciaComNet2026`. Metadados conferidos no registro oficial ScienceDirect recuperado por busca; a abertura direta retornou 403. A comparação de conteúdo usa o manuscrito local em `phd-thesis/publications/article_2_elsevier_comnet/main.tex`, especialmente Contributions, Architectural Approaches e User-Centric Privacy and Trust. O ano é 2026; o ano dentro do DOI não o substitui.

O contraste técnico sobre avaliação pública usa a referência já existente `homenc`: Craig Gentry, *A Fully Homomorphic Encryption Scheme*, Stanford, 2009. A seção 2.1, página impressa 27 (página 37 do PDF), define Evaluate com chave pública, circuito e ciphertexts. A seção 1.8, página 21, distingue avaliação no servidor e recuperação do resultado pelo detentor da chave. O [PDF primário](https://crypto.stanford.edu/craig/craig-thesis.pdf) foi acessado via HTTP após o leitor web falhar. Não se acrescentou esse trabalho ao conjunto de aplicações.

| Fronteira do quadro novo | Fontes já analisadas | Limite preservado |
|---|---|---|
| Identidade / autoridade | Zeydan; arquitetura conceitual de Phuyal | Autenticação não estabelece permissão nem privacidade das inferências |
| Permissão / liberação | Can; SecureConsent; delegação PRE/ABE de Gao | Registro ou token não demonstra controle de todo uso posterior |
| Confidencialidade / correção | Agregação homomórfica em smart grid; Gentry; Zerocash | Relações verificadas e dados ocultos têm definições e pressupostos próprios |
| Evidência / privacidade da auditoria | Can; BADIMAC; AnonCreds | Log íntegro não demonstra completude de eventos; divulgação seletiva não elimina todos os metadados |
| Retirada / status | SecureConsent; Phuyal; Bitstring Status List | Bloqueio futuro, revogação de credencial e remoção de cópias são resultados distintos |

A revisão não demonstra primazia do enquadramento nem ausência de sobreposição com outros surveys. Os comparadores Nguyen, Phuyal, Mazzocca e Sandyawan continuam explicitamente reconhecidos. A contribuição adicional está na síntese entre mecanismos, pontos de aplicação e evidência; citar um domínio adicional ou usar a palavra governança não seria suficiente.

## Ligação à RQ2 da tese, sem alteração das perguntas

A RQ2 da tese é preservada:

> How can the proposed architecture enable end-user control at a granular level — allowing them to specify which authorized entities can perform FHE computations on their encrypted QoE data — ensuring both data privacy and the utility of this data for authorized analytical purposes?

O survey contribui à dimensão analítica dessa pergunta: fornece critérios para especificar quem decide, quais dados/operações/destinatários são abrangidos e onde a decisão produz efeito. A resposta completa continua dependendo dos mecanismos, pressupostos e avaliações dos Artigos 1 e 3. O survey não fornece novas medições de utilidade de QoE, custo de FHE ou eficácia operacional dos controles e não confirma experimentalmente H-RQ2.

Na síntese da tese, a descrição de controle deve reconciliar a ACL do Artigo 1 com a avaliação pública e a política de liberação do Artigo 3. Permissão para invocar o serviço, possibilidade de calcular sobre ciphertexts públicos e autorização de decriptação/liberação não são equivalentes. Essa interpretação precisa não exige alterar a redação histórica da RQ2, mas impede apresentar como plenamente demonstrada uma proibição geral de toda computação não autorizada.

A contribuição a RQ1 é a interpretação de evidência auditável e seus limites de privacidade; a contribuição a RQ3 é distinguir histórico de alegações de evidência de correção. As garantias computacionais continuam atribuídas aos artigos que as analisam.

## Papel na DSR da tese

A metodologia DSR pertence à tese. O survey fornece conhecimento e requisitos para sua síntese integradora; não constitui, por esse vínculo, uma execução autônoma do ciclo DSR.

| Etapa da tese | Papel do survey | O que não se pode inferir |
|---|---|---|
| Identificação e refinamento do problema | Distinguir confidencialidade, autoridade, controle de acesso e accountability | Que todo cenário QoE requer blockchain ou FHE |
| Definição dos objetivos/requisitos | Explicitar objeto da permissão, ator, ponto de aplicação e evidência esperada | Que esses requisitos foram derivados prospectivamente antes dos artigos já publicados |
| Projeto e desenvolvimento | Permitir examinar as responsabilidades das ACLs, verificadores e serviços de liberação | Que o survey implementa a arquitetura ou determina uma escolha criptográfica única |
| Demonstração e avaliação | Fornecer perguntas para interpretar resultados existentes e planejar testes ainda necessários | Que a síntese bibliográfica substitui testes ou valida propriedades não avaliadas |
| Comunicação e integração | Relacionar fundamentos, duas iterações arquiteturais e limites remanescentes | Que um artigo adicional é automaticamente indispensável à tese |

A ordem expositiva pode ser survey QoE → survey de governança → Artigo 1 → Artigo 3 → síntese. Trata-se de organização lógica, sem reescrever a cronologia. A aplicação retrospectiva dos requisitos aos artigos técnicos deve ser declarada como tal. A inclusão é justificável pela contribuição analítica que acrescenta; não foi demonstrado que seja necessária para responder às RQs da coletânea existente.

## Elementos para o texto integrador, fora do survey

Proposta de formulação em inglês:

> The governance survey supports the interpretation of granular user control in RQ2 by relating decision authority to policy scope, enforcement points, and assessment evidence. Within the thesis's Design Science Research process, it contributes to the knowledge base and the articulation of architectural requirements. Its application to the two architectural studies is an integrative analysis: the first study implements application-level access control, while the second distinguishes public encrypted evaluation, computation verification, and owner-authorized output release. These distinctions qualify the scope of user control without changing the research questions or replacing the technical evidence reported by those studies.

O texto integrador ainda precisa aplicar a matriz aos artigos, identificar responsabilidades do doutorando e separar componentes entregues de oportunidades futuras. SSI/DID/VC não devem aparecer como implementados na arquitetura apenas porque constam do survey. Auditoria computacional também não deve ser apresentada como certificação regulatória, veracidade da medição ou garantia de toda finalidade posterior.

## Preservação e verificação

`architecture-synthesis-preservation-before.json` registra fingerprints anteriores das extrações, do dataset e dos arquivos que contêm as RQs da tese. `architecture-synthesis-validation.json` registra a comparação após a revisão. As tabelas existentes de estudos e plataformas e as quatro perguntas do survey são comparadas diretamente ao snapshot anterior. A tabela de Related Work recebe a nova referência contextual; a tabela de requisitos é uma nova síntese, não uma alteração dos resultados extraídos.

A compilação e as referências são conferidas por `export_and_validate.py`; o pacote é atualizado por `build_updated_dataset.py` e verificado por `validate_updated_dataset.py`. Essa atualização reflete mudanças de fonte e bibliografia contextual nos manifestos, preservando o CSV de 106 estudos. A inspeção visual do PDF é registrada separadamente e não constitui validação científica.
