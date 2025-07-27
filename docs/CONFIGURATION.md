# Configuration Guide

This document explains how to configure the TUI application using YAML configuration files.

## Configuration File Locations

The application searches for configuration files in the following order:

1. `config.yaml` (current working directory)
2. `~/.new_tui_project_template.yaml` (user home directory)
3. `config.yaml.example` (fallback example file)

## Configuration Format

Configuration uses YAML format for easy readability and editing:

```yaml
# Application Settings
debug: false              # Enable debug mode and verbose logging
log_level: "INFO"         # Logging level: DEBUG, INFO, WARNING, ERROR, CRITICAL

# TUI Application Settings  
theme: "dark"             # Application theme: "dark", "light"
title: "My TUI App"       # Window title
refresh_rate: 60          # Screen refresh rate in Hz

# Development Settings
auto_reload: false        # Auto-reload CSS and Python files during development
show_fps: false          # Show FPS counter in development mode
```

## Configuration Options

### Core Settings

- **debug** (boolean): Enable debug mode with verbose logging
- **log_level** (string): Set logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)

### TUI Settings

- **theme** (string): Application theme ("dark" or "light")
- **title** (string): Window title displayed in terminal
- **refresh_rate** (integer): Screen refresh rate in Hz

### Development Settings

- **auto_reload** (boolean): Automatically reload files during development
- **show_fps** (boolean): Display FPS counter for performance monitoring

## Using Configuration in Code

```python
from new_tui_project_template.config import load_config, save_config

# Load configuration
config = load_config()  # Uses default search order
config = load_config("custom_config.yaml")  # Specific file

# Access configuration values
debug_mode = config.get("debug", False)
theme = config.get("theme", "dark")
log_level = config.get("log_level", "INFO")

# Save configuration
config["debug"] = True
save_config(config, "config.yaml")
```

## Command Line Configuration

You can override configuration settings using command line options:

```bash
# Use custom configuration file
new_tui_project_template --config /path/to/config.yaml

# Enable debug mode (overrides config file)
new_tui_project_template --debug

# Combine options
new_tui_project_template --config custom.yaml --debug
```

## Configuration Validation

The application performs basic validation on configuration values:

- Boolean values must be `true` or `false`
- String values are accepted as-is
- Integer values are validated for numeric format
- Missing values use sensible defaults

## Environment Variables

You can also use environment variables for some settings:

- `DEBUG`: Set to "true" to enable debug mode
- `LOG_LEVEL`: Override the log level setting

Environment variables take precedence over configuration file values.

## Best Practices

1. **Start with the example**: Copy `config.yaml.example` to `config.yaml`
2. **Version control**: Add `config.yaml` to `.gitignore` for local settings
3. **Documentation**: Comment your custom configuration options
4. **Validation**: Test configuration changes before deployment
5. **Defaults**: Ensure your application works with minimal configuration

## Troubleshooting

### Configuration Not Loading

1. Check file permissions on configuration files
2. Verify YAML syntax using an online validator
3. Enable debug mode to see configuration loading messages
4. Check that the file path is correct

### Invalid Configuration Values

1. Review the YAML syntax for proper formatting
2. Ensure boolean values use `true`/`false` (lowercase)
3. Check for proper indentation (use spaces, not tabs)
4. Validate string values are properly quoted when needed

### Configuration Ignored

1. Verify the file is in the correct search location
2. Check command line options aren't overriding settings
3. Review application logs for configuration loading messages
4. Ensure the configuration module is properly imported