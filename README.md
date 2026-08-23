# DC — Discord Rare Username Hunter

Ferramenta para gerar e verificar nomes curtos para Discord, com foco em identificadores raros de até 3 caracteres.

## Objetivo

O DC combina letras (`a-z`) e números (`0-9`) para procurar combinações curtas e interessantes, priorizando nomes com 1, 2 e 3 caracteres.

Exemplos de padrões:

- `a`
- `7`
- `x9`
- `q2`
- `z7x`
- `0x9`

## Verificação

A ferramenta deve usar somente métodos oficiais/permitidos pelo Discord e respeitar rate limits. Ela não deve tentar contornar CAPTCHA, bloqueios ou limites da plataforma.

Resultados possíveis:

- `available` — aparentemente disponível
- `taken` — já utilizado
- `invalid` — formato não aceito
- `rate_limited` — é necessário aguardar
- `error` — não foi possível determinar

## Prioridade de busca

1. nomes de 1 caractere
2. nomes de 2 caracteres
3. nomes de 3 caracteres
4. combinações alfanuméricas incomuns

O projeto não deve tentar registrar ou tomar posse automaticamente de nenhum nome.
