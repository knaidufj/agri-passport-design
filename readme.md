# AATP-Based Agri Passport Design

## Overview

The Australian Agricultural Traceability Protocol (AATP) is a system developed to interact with ACA-PY compatible agents for agricultural traceability. This documentation covers the main components of the AATP system, including the API server, command-line interface, and user interface.

## Table of Contents

- [AATP-Based Agri Passport Design](#aatp-based-agri-passport-design)
  - [Overview](#overview)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [File Structure](#file-structure)
  - [Getting Started](#getting-started)
    - [Setting Up a Python Virtual Environment](#setting-up-a-python-virtual-environment)
    - [Dependencies](#dependencies)
  - [Usage](#usage)
  - [Configuration](#configuration)
  - [Testing](#testing)
    - [Running Tests](#running-tests)
    - [Test Files](#test-files)
    - [Writing New Tests](#writing-new-tests)
  - [Developer Manual](#developer-manual)
    - [Project Structure](#project-structure)
    - [Code Style Guidelines](#code-style-guidelines)
    - [Logging and Debugging](#logging-and-debugging)
    - [Extending Functionality](#extending-functionality)
  - [Contributing](#contributing)
  - [License](#license)

## Features

- Creating and managing schemas
- Creating and querying credential definitions
- Issuing credentials
- Managing connections and invitations
- Sending and querying messages
- Tracing agricultural products through ACA-PY compatible agents

## File Structure

- `server.py`: Functions for checking the status of the service.
- `aatp-cli.py`: Backend API for interacting with ACA-PY agents.
- `aatp-ui.py`: Flask-based HTTP server containing frontend API.
- `config.py`: Configuration file with API URL and authentication token.
- `connections.py`: Functions for managing connections and invitations.
- `credential.py`: Functions for handling credential-related operations.
- `curl.py`: Utility function for making API calls.
- `messages.py`: Functions for sending and querying messages.
- `schema.py`: Functions for creating and retrieving schemas.

## Getting Started

### Setting Up a Python Virtual Environment

It's recommended to use a Python virtual environment when working with the AATP system. Follow these steps to set up and activate a virtual environment:

1. Open a terminal and navigate to the project directory.

2. Create a new virtual environment:
   ```
   python -m venv aatp_env
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     aatp_env\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source aatp_env/bin/activate
     ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

5. When you're done working on the project, deactivate the virtual environment:
   ```
   deactivate
   ```

### Dependencies

The AATP system relies on several Python libraries, including:

- `Flask` (for the web interface)
- `requests` (for making API calls)
- `qrcode` (for generating QR codes)
- `argparse` (for command-line argument parsing)

Ensure these dependencies are installed in your virtual environment before running the AATP system.

## Usage

The AATP system can be used through the backend API (`aatp-cli.py`) for interacting with ACA-PY agents or the frontend API (`aatp-ui.py`) which provides a web interface. Both interfaces provide access to the core functionality of the system, including:

1. Creating and managing schemas
2. Creating and querying credential definitions
3. Issuing credentials
4. Managing connections and invitations
5. Sending and querying messages
6. Tracing products

To use the backend API, run:
```
python aatp-cli.py
```
with the appropriate arguments or in interactive mode. To use the frontend API, run the Flask application in `aatp-ui.py` and access it through a web browser.

## Configuration

Before using the AATP system, ensure that the `config.py` file is properly set up with the correct API URL and authentication token.

## Testing

The AATP system includes a comprehensive test suite to ensure the reliability and correctness of its components. The test files are located in the `tests/` directory and cover various aspects of the system. The tests use Python's built-in `unittest` framework.

### Running Tests

To run the tests, follow these steps:

1. Ensure you have activated your Python virtual environment.

2. Navigate to the project root directory.

3. Run the tests using the unittest module:
   ```
   python -m unittest discover tests
   ```

This command will discover and run all test files in the `tests/` directory.

### Test Files

- `test_aatp_cli.py`: Tests for the backend API functionality.
- `test_aatp_ui.py`: Tests for the frontend API functionality.
- `test_credential.py`: Tests for credential-related operations.
- `test_curl.py`: Tests for the API call utility function.
- `test_schema.py`: Tests for schema creation and retrieval.
- `test_connections.py`: Tests for connection and invitation management.

### Writing New Tests

When adding new features or modifying existing ones, make sure to update or add corresponding tests. Follow these guidelines:

1. Create new test files in the `tests/` directory.
2. Name your test classes as `TestClassName(unittest.TestCase)`.
3. Use meaningful names for test methods, prefixed with `test_`.
4. Use `setUp()` and `tearDown()` methods for setup and cleanup operations.
5. Use unittest assertions (e.g., `self.assertEqual()`, `self.assertTrue()`) for verifications.
6. Aim for high test coverage to ensure system reliability.

## Developer Manual

### Project Structure

The AATP project is organized into several key files and directories:

- **Core Components**: The core functionality is implemented in files such as `server.py`, `aatp-cli.py`, `aatp-ui.py`, `connections.py`, `credential.py`, `messages.py`, `schema.py`, and `curl.py`.
- **Configuration**: `config.py` contains essential configuration settings.
- **Tests**: All test-related files are located in the `tests/` directory.

### Code Style Guidelines

To maintain code quality and consistency throughout the AATP system, adhere to the following guidelines:

- Follow PEP 8 for Python code style.
- Use meaningful variable and function names that clearly describe their purpose.
- Include docstrings for all functions and classes.
- Maintain consistent indentation (4 spaces per level).
- Avoid large functions; break them into smaller, reusable components.

### Logging and Debugging

- Use Python's built-in `logging` module for tracking the execution of the code. Logging helps in debugging and provides useful information when running in production.
- Add logging statements at the start and end of functions, and before key actions, to trace the flow of execution.
- Set different logging levels (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`) based on the importance of the message.

Example:
```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Starting the application")
```

### Extending Functionality

The AATP system is designed to be modular and extensible. To extend the system, follow these guidelines:

- **Adding New Features**: When adding a new feature, create a separate Python module if it does not fit into any existing files. Ensure it follows the same code structure and style guidelines.
- **Integrating with ACA-PY**: Use the existing structure in `aatp-cli.py` and `aatp-ui.py` as examples for integrating new commands or routes.
- **Testing**: Always write unit tests for new features. Refer to the `tests/` directory for examples of existing tests.

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```
   git checkout -b feature-name
   ```
3. Make your changes and commit them:
   ```
   git commit -m "Description of feature or fix"
   ```
4. Push your branch to your fork:
   ```
   git push origin feature-name
   ```
5. Submit a pull request to the main repository.

Please ensure your code follows the project's style guide and includes relevant tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

