import os
from rich.console import Console
from rich.panel import Panel

console = Console()

pw = console.input("[bold yellow]Tool Şifresi:[/bold yellow] ")

if pw != os.getenv("TOOL_PASS"):
    console.print(Panel("❌ Yetkisiz Erişim", style="red"))
    exit()

console.print(Panel(
    "🛡️ Site Güvenlik Log Aracı\n\n"
    "• IP\n"
    "• Kullanıcı Adı\n"
    "• Şifre\n"
    "• User-Agent\n\n"
    "Loglar anlık ekrana düşer.",
    style="green"
))
