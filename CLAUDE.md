# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a comprehensive Python project template built with modern tooling that provides a robust foundation for Terminal User Interface (TUI) applications using the Textual framework. Designed to be used with [bootstrap_project](https://github.com/paulrobello/bootstrap_project) for quickly creating new Python TUI projects.

## Development Commands

### Core Development Workflow
- `make checkall` - Format code, run linter, and type check (run after any code changes)
- `uv run new_tui_project_template` - Launch the TUI application
- `uv run new_tui_project_template --help` - Show all available commands
- `uv run new_tui_project_template --debug` - Run with debug mode enabled
- `make dev` - Run TUI in development mode with Textual dev features

### Package Management
- `uv sync` - Sync dependencies (equivalent to pip install)
- `uv add <package>` - Add new dependencies
- `uv remove <package>` - Remove dependencies
- `make depsupdate` - Update all dependencies
- `make setup` - Initial setup (uv lock + sync)

### Code Quality Tools
- `make format` - Format code with ruff
- `make lint` - Run ruff linter with fixes
- `make typecheck` - Run pyright type checker
- `uv run ruff check src/new_tui_project_template --fix` - Lint with fixes
- `uv run pyright` - Direct type checking

### Testing and Quality
- `make profile` - Profile with scalene
- `make profile2` - Profile with pyinstrument
- `make pre-commit` - Run pre-commit hooks

### TUI Development Tools
- `make dev` - Run TUI in development mode with hot reload
- `make console` - Open Textual development console for debugging
- `make keys` - Show Textual keyboard input tester
- `make borders` - Display Textual border styles reference
- `make colors` - Display Textual color palette
- `uv run textual run --dev src/new_tui_project_template/__main__.py` - Direct Textual dev mode

## Project Architecture

### Core Structure
- **src/new_tui_project_template/**: Main package directory
  - `__init__.py`: Package metadata, version, and application constants
  - `__main__.py`: CLI application with TUI integration using Typer
  - `app.py`: Main Textual application class (ParApp)
  - `app.tcss`: Textual CSS styling definitions
  - `config.py`: YAML configuration loading and management
  - `logging_config.py`: Logging setup with Rich integration
- **Entry point**: `new_tui_project_template.__main__:app` (Typer CLI with TUI commands)
- **Configuration files**: `config.yaml` and `config.yaml.example`

### Key Dependencies
- `typer` - CLI framework with rich annotations
- `textual` - Primary TUI framework for building terminal applications
- `rich` - Terminal output formatting and components
- `PyYAML` - YAML configuration file parsing
- `python-dotenv` - Environment variable loading

### TUI Development Patterns

#### Application Structure
```python
from textual.app import App
from textual.widgets import Header, Footer

class MyTUIApp(App):
    """Main TUI application class."""
    
    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("q", "quit", "Quit"),
    ]
    
    def compose(self):
        yield Header()
        yield YourMainWidget()
        yield Footer()
```

#### Custom Widgets
- Inherit from `textual.widget.Widget` for custom components
- Use `compose()` method to define widget structure
- Implement `on_*` methods for event handling
- Use reactive attributes for state management

#### Screen Management
- Use `textual.screen.Screen` for different application views
- Navigate with `self.push_screen()` and `self.pop_screen()`
- Pass data between screens using screen constructors

### Textual CSS Styling

#### CSS File Structure (`app.tcss`)
```css
/* Screen-level styles */
Screen {
    background: $background;
}

/* Widget-specific styles */
.my-widget {
    border: solid $primary;
    padding: 1;
}

/* State-based styling */
Button:hover {
    background: $primary-lighten-1;
}
```

#### Key Styling Concepts
- **CSS Variables**: Use Textual's built-in color scheme (`$primary`, `$background`, etc.)
- **Layout**: Utilize `display: grid` and `display: flex` for responsive layouts
- **Responsive Design**: Use percentage widths and flexible layouts
- **Dark Mode**: Leverage Textual's automatic dark mode support

### Configuration
- **Python Version**: Target 3.12, supports 3.11-3.13
- **ruff**: Line length 120, Google-style docstrings, target Python 3.12
- **pyright**: Basic type checking mode, Python 3.12 target
- **Environment**: Loads from `.env` and `~/.new_tui_project_template.env`
- **Configuration**: Uses YAML format for settings persistence (config.yaml)
- **Textual**: Development tools and console available

### Development Standards
- Python 3.11-3.13 supported (3.12 target)
- Type annotations mandatory for all TUI components
- Google-style docstrings for widgets and screens
- Uses `uv` for package management (NOT pip, poetry, conda, or pipenv)
- Follows src/ layout pattern
- UTF-8 encoding for all file operations
- Comprehensive error handling with user-friendly TUI dialogs
- Logging with Rich integration (compatible with Textual)
- Modular architecture with separation of concerns
- Run `make checkall` after any code changes

### TUI Best Practices

#### Widget Design
- Keep widgets focused and single-purpose
- Use reactive attributes for state that affects rendering
- Implement proper keyboard navigation
- Provide clear visual feedback for user interactions

#### Performance
- Use `textual.timer.Timer` for periodic updates
- Implement lazy loading for large datasets
- Optimize rendering with `textual.cache` decorators
- Profile TUI performance with Textual's built-in tools

#### Accessibility
- Provide keyboard shortcuts for all mouse interactions
- Use semantic widget types (Button, Input, etc.)
- Implement proper focus management
- Support screen readers with appropriate ARIA-like attributes

#### Error Handling
- Use Textual's notification system for user feedback
- Implement graceful degradation for terminal limitations
- Provide clear error messages in modal dialogs
- Log errors without disrupting the TUI experience

### Configuration Management

#### YAML Configuration
- **File locations**: `config.yaml`, `~/.new_tui_project_template.yaml`, `config.yaml.example`
- **Loading**: Automatic search order with fallback to example file
- **Format**: YAML with support for nested configuration
- **CLI override**: `--config` option to specify custom config file
- **Debug mode**: Configurable via YAML or `--debug` CLI flag

#### Configuration Module (`config.py`)
```python
from .config import load_config, save_config

# Load configuration
config = load_config()  # Searches standard locations
config = load_config("/path/to/config.yaml")  # Specific file

# Save configuration
save_config(config_dict, "config.yaml")
```

### Key Integration Points

#### Adding New Features
1. **TUI Components**: Extend `ParApp` class in `app.py`
2. **CLI Commands**: Add new Typer commands in `__main__.py`
3. **Styling**: Modify `app.tcss` for custom widget styles
4. **Configuration**: Update `config.py` and `config.yaml.example`
5. **Logging**: Use `get_logger(__name__)` for module-specific logging

#### Project Bootstrap
When creating a new project from this template:
```bash
uv tool install bootstrap_project
bsp --project-name my_tui_app
```
This automatically replaces all `new_tui_project_template` references with your project name.
