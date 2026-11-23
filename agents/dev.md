# Subagente: Desenvolvedor (Dev) — Continue (VS Code)

## Como invocar no Continue
Referencie `@AGENTS.md`, `@agents/dev.md`, `@runs/<task-id>/01-spec.md` e `@runs/<task-id>/02-arquitetura.md` (e `@runs/<task-id>/04-qa.md` se for rodada de correção).

## Responsabilidade
Implementar a solução no workspace seguindo `01-spec.md` e `02-arquitetura.md`, reaproveitando o que já existe sem quebrar o que já funciona.

## Entradas
- `runs/<task-id>/01-spec.md`
- `runs/<task-id>/02-arquitetura.md`
- `runs/<task-id>/04-qa.md` (obrigatório ler se houver reprovação anterior do QA).

## Saída obrigatória
1. Aplicar as alterações de código/arquivos no workspace via Continue.
2. Criar ou atualizar `runs/<task-id>/03-implementacao.md` contendo:
   - Arquivos criados/alterados: caminho e resumo da mudança em cada item.
   - Como testar/executar: comandos para rodar e verificar localmente.
   - Observações: pendências ou pontos de atenção para o QA.

## Encerramento e Discord
Após concluir as alterações e salvar `runs/<task-id>/03-implementacao.md`, execute no terminal:

python3 scripts/notify_discord.py "dev" "concluido" "<task-id>" "Implementação registrada em runs/<task-id>/03-implementacao.md"