import typer
from rich.console import Console
from rich import print as rprint
from pathlib import Path
from .config import load_config
from .forge import Forge

app = typer.Typer(help="🔨 forge — AI-powered toolkit for open-source maintainers")
console = Console()

@app.command()
def config_init():
    """Initialize or reset configuration"""
    load_config()
    rprint("[green]✅ Configuration initialized successfully![/green]")

@app.command()
def list_prompts():
    """List all available prompts"""
    prompts_dir = Path(__file__).parent / "prompts"
    if not prompts_dir.exists():
        rprint("[red]Prompts folder not found![/red]")
        return
    prompts = [p.stem for p in prompts_dir.glob("*.yaml")]
    rprint("[bold cyan]Available Prompts:[/bold cyan]")
    for p in sorted(prompts):
        rprint(f"  • {p}")

@app.command()
def review_pr(repo: str, pr: int):
    """Review a GitHub Pull Request"""
    forge = Forge()
    rprint(f"[bold]🔍 Reviewing PR #{pr} in {repo}...[/bold]")
    try:
        prompt = forge.load_prompt("pr_review", repo=repo, pr_number=pr)
        rprint("[yellow]Generated prompt (ready to send to LLM):[/yellow]")
        console.print(prompt[:800] + "\n..." if len(prompt) > 800 else prompt)
    except Exception as e:
        rprint(f"[red]Error: {e}[/red]")

@app.command()
def triage_issue(repo: str, issue: int):
    """Triage a GitHub Issue"""
    forge = Forge()
    rprint(f"[bold]📋 Triaging issue #{issue} in {repo}...[/bold]")
    try:
        prompt = forge.load_prompt("issue_triage", repo=repo, issue_number=issue)
        rprint("[yellow]Generated prompt:[/yellow]")
        console.print(prompt[:600] + "\n..." if len(prompt) > 600 else prompt)
    except Exception as e:
        rprint(f"[red]Error: {e}[/red]")

@app.command()
def generate_changelog(repo: str):
    """Generate changelog (placeholder)"""
    rprint(f"[bold]📝 Generating changelog for {repo}...[/bold]")
    rprint("[yellow](Full GitHub integration coming in next update)[/yellow]")

def main():
    app()