#!/usr/bin/env python3
"""
Gemma 4 Ethics Auditor - CLI Entry Point
"""
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

import typer
from rich.console import Console
from rich.panel import Panel

from gemma_client import load_client

app = typer.Typer(help="Gemma 4 Ethics Auditor - Pure AI Code Analysis")
console = Console()


@app.command()
def analyze(
    file: str = typer.Argument(None, help="Source file to analyze"),
    dimension: str = typer.Option("bias", "--dimension", "-d",
                                   help="Analysis type: bias, accessibility, security, ethics"),
    stdin: bool = typer.Option(False, "--stdin", help="Read from stdin"),
):
    """Analyze code for ethical concerns using Gemma 4."""
    from pathlib import Path

    # Get code input
    if stdin:
        code = sys.stdin.read()
    elif file:
        file_path = Path(file)
        if not file_path.exists():
            console.print(f"[red]Error: File not found: {file}[/red]")
            raise typer.Exit(1)
        code = file_path.read_text()
    else:
        console.print("[red]Error: Provide a file or use --stdin[/red]")
        raise typer.Exit(1)

    # Load Gemma 4
    console.print("[cyan]Loading Gemma 4...[/cyan]")
    try:
        client = load_client()
    except Exception as e:
        console.print(f"[red]Failed to load model: {e}[/red]")
        raise typer.Exit(1)

    # Analyze
    console.print(f"[cyan]Analyzing for {dimension} concerns...[/cyan]")
    try:
        report = client.analyze_code(code, dimension)
        console.print(Panel(report, title=f"ETHICA - {dimension.upper()} Analysis",
                           border_style="green"))
    except Exception as e:
        console.print(f"[red]Analysis failed: {e}[/red]")
        raise typer.Exit(1)


@app.command()
def test():
    """Test Gemma 4 connection."""
    console.print("[cyan]Testing Gemma 4...[/cyan]")
    try:
        client = load_client()
        response = client.analyze("Say 'Gemma 4 is working' in exactly those words.")
        console.print(Panel(response, title="Gemma 4 Test", border_style="green"))
    except Exception as e:
        console.print(f"[red]Test failed: {e}[/red]")
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
