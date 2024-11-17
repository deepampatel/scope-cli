import click
from scope.dir_size import display_tree
from scope.port_checker import check_port


@click.group()
def cli():
    """Scope CLI: A versatile tool for developers."""
    pass


@cli.command()
@click.argument("path", type=click.Path(exists=True, file_okay=False), default=".")
def tree(path):
    """Visualize directory sizes in a tree format."""
    display_tree(path)


@cli.command()
@click.argument("port", type=int)
@click.option("--kill", is_flag=True, help="Kill the process using the specified port.")
def port(port, kill):
    """Check if a port is in use and manage processes."""
    check_port(port, kill)


# Dynamically register the LLM command
try:
    from scope.llm_utils import handle_llm_command

    @cli.command()
    @click.argument("query", type=str)
    @click.option("--execute", is_flag=True, help="Execute the suggested command.")
    def llm(query, execute):
        """Use an LLM to assist with CLI commands."""
        handle_llm_command(query, execute)

except ImportError:
    @cli.command()
    @click.argument("query", type=str)
    @click.option("--execute", is_flag=True, help="Execute the suggested command.")
    def llm():
        """LLM functionality is not available. Install optional dependencies with: pip install scope-cli[llm]"""
        print(
            "LLM functionality is unavailable. Install optional dependencies with: pip install scope-cli[llm]"
        )


def main():
    cli()
