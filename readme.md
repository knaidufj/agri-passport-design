# AATP-Based Agri Passport Design

## Overview

The Australian Agricultural Traceability Protocol (AATP) is a system developed to interact with ACA-PY compatible agents for agricultural traceability. This documentation covers the main components of the AATP system, including the API server, command-line interface, and user interface.

## File Structure

1. `server.py`: Contains functions for checking the status of the service.
2. `aatp-cli.py`: Command-line interface for interacting with the AATP system.
3. `aatp-ui.py`: Flask-based web interface for the AATP system.
4. `config.py`: Configuration file containing API URL and authentication token.
5. `connections.py`: Functions for managing connections and invitations.
6. `credential.py`: Functions for handling credential-related operations.
7. `curl.py`: Utility function for making API calls.
8. `messages.py`: Functions for sending and querying messages.
9. `schema.py`: Functions for creating and retrieving schemas.

## Detailed Documentation

### server.py

This file contains functions for checking the status of the AATP service.

#### Functions:

- `check_status(auth_token=AUTH_TOKEN, url=API_URL)`: Sends a GET request to check if the service is ready.
- `interactive_check_status()`: Interactively checks the status of the service.

### aatp-cli.py

This file implements the command-line interface for the AATP system.

#### Main Components:

- `main()`: The main function that sets up the argument parser and executes the appropriate action based on user input.
- Various subparsers for different actions such as creating schemas, querying connections, sending messages, etc.
- Interactive mode that allows users to choose actions from a menu.

### aatp-ui.py

This file implements a Flask-based web interface for the AATP system.

#### Main Components:

- Flask routes for various actions such as creating schemas, issuing credentials, tracing products, etc.
- Functions to handle form submissions and API interactions.
- Templates for rendering HTML pages.

### config.py

This file contains configuration variables for the AATP system.

- `API_URL`: The URL for the API endpoint.
- `AUTH_TOKEN`: The authentication token for API calls.

### connections.py

This file contains functions for managing connections and invitations.

#### Main Functions:

- `create_invitation(...)`: Creates a connection invitation and generates a QR code.
- `query_active_connections(...)`: Retrieves a list of active connections.
- `interactive_create_invitation()`: Interactively creates a connection invitation.
- `interactive_query_connections()`: Interactively queries active connections.

### credential.py

This file contains functions for handling credential-related operations.

#### Main Functions:

- `get_credential_definition(...)`: Retrieves a credential definition from the API.
- `create_credential_definition(...)`: Creates a new credential definition in the API.
- `issue_credential(...)`: Issues a W3C credential.
- `fetch_credential_records(...)`: Fetches credential records associated with a connection ID.
- `send_proposal(...)`: Sends a credential proposal to a connection.
- Various interactive functions for credential operations.

### curl.py

This file contains a utility function for making API calls.

#### Main Function:

- `send_api_call(url, method="GET", headers=None, data=None)`: Sends an API call using the specified HTTP method and handles the response.

### messages.py

This file contains functions for sending and querying messages.

#### Main Functions:

- `send_message(...)`: Sends a message to a specific connection.
- `query_messages(...)`: Queries messages for a specific connection.
- `interactive_send_message()`: Interactively sends a message to a connection.
- `interactive_query_messages()`: Interactively queries messages for a connection.

### schema.py

This file contains functions for creating and retrieving schemas.

#### Main Functions:

- `create_schema(...)`: Creates a new schema in the API.
- `get_schema(...)`: Retrieves a schema from the API.
- `interactive_create_schema()`: Interactively creates a schema.
- `interactive_get_schema()`: Interactively retrieves a schema.

## Usage

The AATP system can be used through the command-line interface (`aatp-cli.py`) or the web interface (`aatp-ui.py`). Both interfaces provide access to the core functionality of the system, including:

1. Creating and managing schemas
2. Creating and querying credential definitions
3. Issuing credentials
4. Managing connections and invitations
5. Sending and querying messages
6. Tracing products

To use the command-line interface, run `python aatp-cli.py` with the appropriate arguments or in interactive mode. To use the web interface, run the Flask application in `aatp-ui.py` and access it through a web browser.

## Configuration

Before using the AATP system, ensure that the `config.py` file is properly set up with the correct API URL and authentication token.

## Dependencies

The AATP system relies on several Python libraries, including:

- Flask (for the web interface)
- requests (for making API calls)
- qrcode (for generating QR codes)
- argparse (for command-line argument parsing)

Ensure these dependencies are installed before running the AATP system.

## Appendix

### Screen Recording

```
while [ 1 ];do vardate=$(date +%d\-%m\-%Y\_%H.%M.%S); screencapture -t jpg -x ~/Desktop/ScreenRecord/$vardate.jpg; sleep 5; done
```