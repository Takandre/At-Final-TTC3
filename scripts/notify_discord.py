import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

STATUS_COLORS = {
    "concluido": 0x3B82F6,  # Azul
    "aprovado": 0x22C55E,   # Verde
    "reprovado": 0xEF4444,  # Vermelho
    "erro": 0xF59E0B,       # Âmbar
}


def load_dotenv() -> None:
    env_path = Path(__file__).resolve().parent.parent / ".env"
    if not env_path.is_file():
        return

    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def build_payload(agent: str, status: str, task_id: str, summary: str) -> dict:
    normalized_status = status.strip().lower()
    color = STATUS_COLORS.get(normalized_status, 0x64748B)
    timestamp = datetime.now(timezone.utc).isoformat()

    return {
        "username": "Fábrica de Software Agêntica",
        "embeds": [
            {
                "title": f"[{task_id}] Subagente: {agent.upper()}",
                "description": summary,
                "color": color,
                "fields": [
                    {"name": "Agente", "value": f"`{agent}`", "inline": True},
                    {"name": "Status", "value": f"`{status}`", "inline": True},
                    {"name": "Task ID", "value": f"`{task_id}`", "inline": True},
                ],
                "timestamp": timestamp,
            }
        ],
    }


def main() -> int:
    load_dotenv()

    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL", "").strip()
    if not webhook_url:
        print(
            "Erro: DISCORD_WEBHOOK_URL não definida no ambiente nem no .env.",
            file=sys.stderr,
        )
        return 1

    agent = sys.argv[1] if len(sys.argv) > 1 else "agente"
    status = sys.argv[2] if len(sys.argv) > 2 else "concluido"
    task_id = sys.argv[3] if len(sys.argv) > 3 else "task-01"
    summary = sys.argv[4] if len(sys.argv) > 4 else "Etapa finalizada."

    payload = build_payload(agent, status, task_id, summary)
    body = json.dumps(payload).encode("utf-8")

    request = urllib.request.Request(
        webhook_url,
        data=body,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "AgenticSoftwareFactory/1.0",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            if response.status not in (200, 204):
                print(
                    f"Falha ao enviar webhook para o Discord: HTTP {response.status}",
                    file=sys.stderr,
                )
                return 1
    except urllib.error.URLError as exc:
        print(f"Erro de conexão com o Discord webhook: {exc}", file=sys.stderr)
        return 1

    print(f"Notificação enviada ao Discord: [{task_id}] {agent} ({status})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())