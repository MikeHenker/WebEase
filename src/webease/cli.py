"""
Webease CLI - Command-line interface for Webease
"""

import click
import webbrowser
import os
from pathlib import Path
from .compiler import WebeaseCompiler


@click.group(invoke_without_command=True)
@click.pass_context
@click.version_option(version='1.0.0')
def cli(ctx):
    """Webease - A beginner-friendly language for creating websites"""
    if ctx.invoked_subcommand is None:
        click.echo("🌐 Webease - Create websites with ease!")
        click.echo("\nUsage: webease <filename.ws>")
        click.echo("\nExamples:")
        click.echo("  webease mypage.ws          # Compile and open in browser")
        click.echo("  webease mypage.ws --save   # Compile and save without opening")
        click.echo("\nFor more help: webease --help")


@cli.command()
@click.argument('filename', type=click.Path(exists=True))
@click.option('--save', is_flag=True, help='Save HTML without opening browser')
@click.option('--output', '-o', default='output', help='Output directory')
def compile(filename, save, output):
    """Compile a .ws file to HTML"""
    run_compiler(filename, save, output)


@click.command()
@click.argument('filename', type=click.Path(exists=True))
@click.option('--save', is_flag=True, help='Save HTML without opening browser')
@click.option('--output', '-o', default='output', help='Output directory')
def main(filename, save, output):
    """Main entry point for webease command"""
    run_compiler(filename, save, output)


def run_compiler(filename, save, output):
    """Run the Webease compiler"""
    compiler = WebeaseCompiler()
    
    click.echo(f"🔨 Compiling {filename}...")
    
    html, error = compiler.compile_file(filename)
    
    if error:
        click.echo(error, err=True)
        return
    
    output_dir = Path(output)
    output_dir.mkdir(exist_ok=True)
    
    input_path = Path(filename)
    output_filename = input_path.stem + '.html'
    output_path = output_dir / output_filename
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    click.echo(f"✅ Successfully compiled to {output_path}")
    
    if not save:
        click.echo(f"🚀 Opening in browser...")
        webbrowser.open(f'file://{output_path.absolute()}')
    else:
        click.echo(f"💾 Saved to {output_path}")


if __name__ == '__main__':
    cli()
