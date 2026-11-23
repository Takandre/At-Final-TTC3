# Fábrica de Software Agêntica (Continue + 9Router + Gemini)

Este repositório é operado por uma Fábrica de Software Agêntica executada no VS Code por meio da extensão **Continue** (em modo Agent), utilizando o **9Router** com o combo de modelos (base **Gemini**) configurado na VM.

## Como operar no Continue (VS Code)
1. **Use o modo Agent:** garanta que o Continue esteja no modo Agent para ler/escrever arquivos no workspace e executar comandos no terminal.
2. **Referencie o contexto explicitamente:** ao iniciar ou avançar uma etapa, mencione `@AGENTS.md`, o arquivo do subagente correspondente (`@agents/po.md`, `@agents/arquiteto.md`, `@agents/dev.md` ou `@agents/qa.md`) e o `<task-id>` da execução.
3. **Execute uma etapa por vez (ou em sequência explícita):** não pule etapas nem assuma o papel de outro subagente.

## Regras gerais da fábrica
1. **Fonte da verdade em disco:** toda entrada e saída entre subagentes deve ser persistida em `runs/<task-id>/`:
   - PO -> `runs/<task-id>/01-spec.md`
   - Arquiteto -> `runs/<task-id>/02-arquitetura.md`
   - Dev -> `runs/<task-id>/03-implementacao.md` + arquivos do projeto
   - QA -> `runs/<task-id>/04-qa.md`
2. **Reaproveitamento:** sempre que já existirem arquivos, scripts ou artefatos válidos no projeto, reutilize e evolua em vez de recriar do zero.
3. **Notificação obrigatória no Discord:** ao concluir a tarefa, todo subagente deve executar no terminal do workspace o comando abaixo (com `DISCORD_WEBHOOK_URL` disponível no ambiente, por exemplo carregado do `.env`):

python3 scripts/notify_discord.py "<agente>" "<status>" "<task-id>" "<resumo-curto>"

Status válidos: `concluido`, `aprovado`, `reprovado`, `erro`.