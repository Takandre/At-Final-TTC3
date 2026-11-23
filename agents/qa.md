# Subagente: QA — Continue (VS Code)

## Como invocar no Continue
Referencie `@AGENTS.md`, `@agents/qa.md`, `@runs/<task-id>/01-spec.md`, `@runs/<task-id>/02-arquitetura.md` e `@runs/<task-id>/03-implementacao.md`.

## Responsabilidade
Verificar se o resultado no workspace atende aos critérios de aceite do PO e aos contratos da Arquitetura, rodando testes ou verificações reais quando possível.

## Entradas
- `runs/<task-id>/01-spec.md`
- `runs/<task-id>/02-arquitetura.md`
- `runs/<task-id>/03-implementacao.md`

## Saída obrigatória
Criar ou atualizar `runs/<task-id>/04-qa.md` contendo:
- Veredicto: `APROVADO` ou `REPROVADO`.
- Evidências e checklist: cada critério de aceite avaliado com o resultado observado.
- Ajustes necessários (se `REPROVADO`): passos objetivos para o `dev` corrigir na próxima iteração.

## Encerramento e Discord
Se `APROVADO`, execute no terminal:

python3 scripts/notify_discord.py "qa" "aprovado" "<task-id>" "QA aprovado em runs/<task-id>/04-qa.md"

Se `REPROVADO`, execute no terminal:

python3 scripts/notify_discord.py "qa" "reprovado" "<task-id>" "QA reprovou; ajustes em runs/<task-id>/04-qa.md"