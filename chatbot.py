import sys
from ollama import chat
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

console = Console()

def main():
    welcome = Panel.fit(
        "[bold green]Welcome to your Local Chatbot with Ollama![/bold green]\n"
        "[dim]Press Ctrl+C to terminate.[/dim]",
        border_style="green"
    )
    console.print(welcome)
    
    messages = []
    MODEL = "llama3" 

    while True:
        try:
            user_input = console.input("\n[bold blue]You:[/bold blue] ")
            
            if not user_input.strip():
                continue

            messages.append({'role': 'user', 'content': user_input})

            with console.status("[bold cyan]Ollama is thinking...[/bold cyan]", spinner="dots"):
                response = chat(model=MODEL, messages=messages)
            
            ai_reply = response['message']['content']
            
            messages.append({'role': 'assistant', 'content': ai_reply})

            reply_panel = Panel(
                Markdown(ai_reply), 
                title="[bold magenta]Ollama[/bold magenta]", 
                border_style="magenta"
            )
            console.print(reply_panel)

        except KeyboardInterrupt:
            console.print("\n[bold red]Exiting chat...[/bold red]")
            sys.exit(0)
        except Exception as e:
            console.print(f"\n[bold red]Connection error:[/bold red] Make sure Ollama is running. (Details: {e})")
            sys.exit(1)

if __name__ == "__main__":
    main()