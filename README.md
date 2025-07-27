# New TUI Project Template

## Description
A comprehensive Python project template for building modern Terminal User Interface (TUI) applications. This template provides a robust foundation with multi-command CLI interface, configuration management, logging, and beautiful terminal user interfaces using Textual.

**Note**: This is a template repository designed to be used with [bootstrap_project](https://github.com/paulrobello/bootstrap_project) for quickly creating new Python projects. When used with bootstrap_project, all references to "new_tui_project_template" will be automatically replaced with your chosen project name.

## Features

- **Multi-Command CLI**: Interactive TUI applications with comprehensive command interface
- **Textual Framework**: Build beautiful, responsive terminal user interfaces
- **Configuration Management**: YAML files with layered configuration system
- **Rich Terminal UI**: Beautiful output with Rich library integration
- **Type Safety**: Full type annotations throughout
- **Modern Python**: Built with uv, ruff, pyright, and Python 3.11+

## Technology Stack
- **Python 3.11+** - Modern Python with latest features
- **Typer** - Modern CLI framework with Rich integration
- **Rich** - Beautiful terminal output and formatting
- **Textual** - Build beautiful, responsive TUI applications
- **PyYAML** - YAML configuration file support
- **uv** - Fast Python package management
- **Asyncio** - Asynchronous programming for responsive interfaces


## Using as a Template

The recommended way to use this template is with [bootstrap_project](https://github.com/paulrobello/bootstrap_project):

```bash
# Install bootstrap_project
uv tool install bootstrap_project

# Create a new project from this template
bsp --project-name my_awesome_project

# Create with additional packages
bsp --project-name my_tui_app --packages textual
```

This will:
- Create a new project with your chosen name
- Replace all instances of `new_tui_project_template` with your project name
- Set up git repository
- Install dependencies
- Be ready for development!

## Prerequisites

- Python 3.11 or higher
- [uv](https://docs.astral.sh/uv/) for package management (recommended) or pip

## Quick Start

### 1. Installation

#### From PyPI (when published)
```shell
uv tool install new_tui_project_template
```

#### From Source
```shell
# Clone the repository
git clone https://github.com/paulrobello/new_tui_project_template.git
cd new_tui_project_template

# Install dependencies
uv sync

# Run the application
uv run new_tui_project_template --help
```

### 2. Setup Configuration

```shell
# Copy example configuration file
cp config.yaml.example config.yaml

# Edit config.yaml with your application settings
# Configure debug mode, themes, and other TUI preferences
```

### 3. Basic Usage

```shell
# Start the TUI application
uv run new_tui_project_template

# Start with debug mode enabled
uv run new_tui_project_template --debug

# Use custom configuration file
uv run new_tui_project_template --config /path/to/config.yaml

# View all available commands
uv run new_tui_project_template --help
```

## Configuration

The application uses YAML configuration files for settings management:

### Configuration File Locations

The application searches for configuration files in this order:
1. `config.yaml` (current directory)
2. `~/.new_tui_project_template.yaml` (user home directory)
3. `config.yaml.example` (fallback)

### Configuration Options

```yaml
# Debug mode - enables verbose logging
debug: false

# TODO: Add your custom configuration options here
# Examples:
# theme: "dark"
# refresh_rate: 60
# log_level: "INFO"
# window_title: "My TUI App"
```

### Command Line Options

```shell
# Override debug setting
--debug

# Specify custom config file
--config /path/to/config.yaml

# Show version
--version

# Show help
--help
```

## Development

### Setup Development Environment

```shell
# Clone repository
git clone https://github.com/paulrobello/new_tui_project_template.git
cd new_tui_project_template

# Install dependencies
uv sync

# Run tests and linting
make checkall

# Run the application
uv run new_tui_project_template --help
```

### Common Development Tasks

```shell
# Format, lint, and type check
make checkall

# Individual tools
make format      # Format with ruff
make lint        # Lint with ruff
make typecheck   # Type check with pyright

# Update dependencies
uv sync -U

# Build package
make package
```

### Adding Custom Commands

The template is designed for easy extension:

1. **Add new commands** in `src/new_tui_project_template/__main__.py`
2. **Update help text** and examples

Look for `# TODO` comments for specific extension points.

## What's New

### Version 0.1.0
- **Initial Release**: TUI application template with Textual framework
- **Multi-Command Interface**: CLI and TUI modes
- **Configuration System**: YAML-based configuration management
- **Rich Integration**: Beautiful terminal output and theming

## Template Customization

When creating a new project from this template, you'll want to customize it for your specific needs:

### Key Customization Points

1. **Commands** (`__main__.py`): Add your own CLI and TUI commands
2. **TUI Application** (`app.py`): Customize the main Textual application
3. **Configuration** (`config.py`): Extend YAML configuration handling
4. **Dependencies** (`pyproject.toml`): Add project-specific packages
5. **Styling** (`app.tcss`): Customize TUI appearance with CSS

### Files Automatically Updated

When using bootstrap_project, these files are automatically updated with your project name:
- `pyproject.toml` - Project metadata and dependencies
- `README.md` - Documentation
- `CLAUDE.md` - Development instructions
- `src/new_tui_project_template/*.py` - All Python source files
- `config.yaml` - YAML configuration
- `Makefile` - Build commands
- `.github/workflows/*.yml` - CI/CD workflows

## Contributing

Contributions are welcome! This template is designed to be a starting point for modern TUI applications using the Textual framework.

### How to Contribute

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run `make checkall` to ensure code quality
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Paul Robello - probello@gmail.com
