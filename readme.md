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
  - [Project Demo](#project-demo)
    - [Getting a Traction Tenant Agent](#getting-a-traction-tenant-agent)
    - [Getting the API key](#getting-the-api-key)
    - [Schema and Credential definitions for the demo](#schema-and-credential-definitions-for-the-demo)
    - [Demo sequences](#demo-sequences)
      - [Sequence 1: Issue credential to producer, retailer (Pre-registered) and certifying authority (Pre-registered)](#sequence-1-issue-credential-to-producer-retailer-pre-registered-and-certifying-authority-pre-registered)
      - [Sequence 2: Onsite inspection](#sequence-2-onsite-inspection)
      - [Sequence 3: Self-certify a product](#sequence-3-self-certify-a-product)
      - [Sequence 4: Package a product](#sequence-4-package-a-product)
      - [Sequence 5: Transport a product](#sequence-5-transport-a-product)
      - [Sequence 6: Consumer scans QR code to trace a product](#sequence-6-consumer-scans-qr-code-to-trace-a-product)
  - [Models](#models)
    - [Certification Schema](#certification-schema)
    - [Certifying Authority Schema](#certifying-authority-schema)
    - [Consumer Schema](#consumer-schema)
    - [Packaging Schema](#packaging-schema)
    - [Producer Schema](#producer-schema)
    - [Product Schema](#product-schema)
    - [Recall Schema](#recall-schema)
    - [Retailer Schema](#retailer-schema)
    - [Transportation Schema](#transportation-schema)
    - [User Schema](#user-schema)
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

## Project Demo

### Getting a Traction Tenant Agent

To get started with the AATP system, you'll need to set up a traction tenant agent. This is essential for interacting with ACA-PY compatible agents. Follow the steps below, adapted from the [ACA-Py Workshop](https://aca-py.org/latest/demo/ACA-Py-Workshop/#lab-1-getting-a-traction-tenant-agent-and-mobile-wallet):

1. **Access the Traction Console**: Navigate to the Traction Console and sign up for a tenant agent.

2. **Create a Tenant**: Use the provided interface to create a new tenant. This tenant will represent your entity within the AATP system.

3. **Configure the Tenant**: After creating the tenant, note down the configuration details such as `tenant_id`, `agent_endpoint`, and any authentication tokens provided.

4. **Download Mobile Wallet**: You may also need a mobile wallet to interact with your tenant. Download and set up a compatible mobile wallet app (e.g., Trinsic or Lissi). Follow the instructions to link your mobile wallet to the tenant agent.

5. **Test the Connection**: Use the tenant console to generate a connection invitation. Scan this invitation using your mobile wallet to establish a connection. This will verify that your tenant is successfully set up.

These steps will prepare you to begin working with ACA-PY agents for agricultural traceability using the AATP system.

### Getting the API key

To obtain the API key for the AATP system, follow these steps:

1. **Navigate to the API Key Management Section**: Log in to your AATP console and find the API Key Management section in the settings.

2. **Generate a New API Key**: Click on the "Generate API Key" button. This will create a new API key for your account.

3. **Copy the API Key**: Once the key is generated, make sure to copy it immediately. You will not be able to see it again after you navigate away from the page.

4. **Store the API Key Securely**: Store your API key in a secure location, such as a password manager or an environment variable, to prevent unauthorized access.

5. **Use the API Key in Your Application**: When making API calls, include the API key in the request headers for authentication. For example:
   ```python
   import requests

   url = "https://api.example.com/endpoint"
   headers = {
       "Authorization": "Bearer YOUR_API_KEY"
   }
   response = requests.get(url, headers=headers)
   ```

By following these steps, you will be able to successfully generate and use your API key for the AATP system.

### Schema and Credential definitions for the demo

```
Schema IDs: 
- 13ZM7KEfAzLC12q1R1SiTS:2:AATP_UserSchema:1.0
- 13ZM7KEfAzLC12q1R1SiTS:2:AATP_ProducerSchema:1.1
- 13ZM7KEfAzLC12q1R1SiTS:2:AATP_CertifyingAuthoritySchema:1.0
- 13ZM7KEfAzLC12q1R1SiTS:2:AATP_ProductSchema:1.0
- 13ZM7KEfAzLC12q1R1SiTS:2:AATP_RetailerSchema:1.0
- 13ZM7KEfAzLC12q1R1SiTS:2:AATP_ConsumerSchema:1.0
- 13ZM7KEfAzLC12q1R1SiTS:2:AATP_PackagingSchema:1.0
- 13ZM7KEfAzLC12q1R1SiTS:2:AATP_TransportationSchema:1.1
- 13ZM7KEfAzLC12q1R1SiTS:2:AATP_RecallSchema:1.0
- 13ZM7KEfAzLC12q1R1SiTS:2:AATP_CertificationSchema:1.0
```

```
Credential Definition IDs:
- 13ZM7KEfAzLC12q1R1SiTS:3:CL:2308153:User
- 13ZM7KEfAzLC12q1R1SiTS:3:CL:2308155:Producer
- 13ZM7KEfAzLC12q1R1SiTS:3:CL:2308156:CertifyingAuthority
- 13ZM7KEfAzLC12q1R1SiTS:3:CL:2308157:Product
- 13ZM7KEfAzLC12q1R1SiTS:3:CL:2308159:Retailer
- 13ZM7KEfAzLC12q1R1SiTS:3:CL:2308160:Packaging
- 13ZM7KEfAzLC12q1R1SiTS:3:CL:2308438:Transportation
- 13ZM7KEfAzLC12q1R1SiTS:3:CL:2308162:Recall
- 13ZM7KEfAzLC12q1R1SiTS:3:CL:2308158:Consumer
- 13ZM7KEfAzLC12q1R1SiTS:3:CL:2308259:Certification
```

### Demo sequences

#### Sequence 1: Issue credential to producer, retailer (Pre-registered) and certifying authority (Pre-registered)
- Producer downloads Wallet app
- Producer scans QR code to connect to AATP_Tenant
- Producer requests a User credential from AATP_Tenant at 127.0.0.1:5000/new-user (Use connection ID: f5f80243-cce2-4e90-9193-e8c039620e05)
- AATP_Tenant issues a User credential to Producer
- Producer requests a Producer credential from AATP_Tenant at 127.0.0.1:5000/new-producer (Use connection ID: f5f80243-cce2-4e90-9193-e8c039620e05)
- AATP_Tenant issues a Producer credential to Producer
- Producer stores both credentials in Wallet

#### Sequence 2: Onsite inspection
- Producer requests a Certification credential from AATP_Tenant at 127.0.0.1:5000/new-certification (Use connection ID: f5f80243-cce2-4e90-9193-e8c039620e05)
- AATP_Tenant issues a Certification credential to Producer

#### Sequence 3: Self-certify a product
- Producer requests a Product credential from AATP_Tenant at 127.0.0.1:5000/new-product (Use connection ID: f5f80243-cce2-4e90-9193-e8c039620e05)
- AATP_Tenant issues a Product credential to Producer

#### Sequence 4: Package a product
- Producer requests a Packaging credential from AATP_Tenant at 127.0.0.1:5000/new-packaging (Use connection ID: f5f80243-cce2-4e90-9193-e8c039620e05)
- AATP_Tenant issues a Packaging credential to Producer

#### Sequence 5: Transport a product 
- Producer requests a Transportation credential from AATP_Tenant at 127.0.0.1:5000/new-transportation (Use connection ID: f5f80243-cce2-4e90-9193-e8c039620e05)
- AATP_Tenant issues a Transportation credential to Producer

#### Sequence 6: Consumer scans QR code to trace a product
- Consumer scans the QR code on the product
- AATP_UI is invoked at 127.0.0.1:5000/product-trace
- AATP_UI displays the product's journey from production to packaging to transportation to retailer


## Models

### Certification Schema
The **AATP_CertificationSchema** is used to capture certification details for a producer. The schema includes the following attributes:
- `certification_id`: Unique identifier for the certification.
- `producer_id`: Identifier for the producer receiving the certification.
- `certification_date`: Date of certification.
- `certification_authority_id`: Identifier of the certifying authority.
- `certification_status`: Status of the certification (e.g., active, expired).

### Certifying Authority Schema
The **AATP_CertifyingAuthoritySchema** defines information about certifying authorities. The schema includes:
- `authority_id`: Unique identifier for the certifying authority.
- `user_id`: Identifier for the user associated with the authority.
- `authority_type`: Type of the certifying authority.

### Consumer Schema
The **AATP_ConsumerSchema** represents consumer information. The attributes are:
- `consumer_id`: Unique identifier for the consumer.
- `user_id`: Identifier for the user associated with the consumer.

### Packaging Schema
The **AATP_PackagingSchema** captures details about product packaging. Attributes include:
- `packaging_id`: Unique identifier for the packaging.
- `product_id`: Identifier for the product being packaged.
- `packaging_date`: Date when packaging was done.
- `packaging_facility_id`: Identifier for the facility where packaging took place.
- `packaging_conditions`: Conditions under which the product was packaged.
- `batch_number`: Batch number associated with the packaging.

### Producer Schema
The **AATP_ProducerSchema** defines information about the producer. The schema includes:
- `producer_id`: Unique identifier for the producer.
- `user_id`: Identifier for the user associated with the producer.
- `organization_type`: Type of the producer's organization.

### Product Schema
The **AATP_ProductSchema** represents product details. The attributes are:
- `product_id`: Unique identifier for the product.
- `product_name`: Name of the product.
- `producer_id`: Identifier of the producer of the product.
- `production_date`: Date of product production.
- `expiration_date`: Expiration date of the product.

### Recall Schema
The **AATP_RecallSchema** captures information about product recalls. The schema includes:
- `recall_id`: Unique identifier for the recall.
- `recall_reason`: Reason for recalling the product.
- `affected_product_id`: Identifier of the affected product.
- `recall_date`: Date of the recall.
- `issuer_id`: Identifier of the recall issuer.

### Retailer Schema
The **AATP_RetailerSchema** defines information about retailers. Attributes include:
- `retailer_id`: Unique identifier for the retailer.
- `user_id`: Identifier for the user associated with the retailer.
- `store_location`: Location of the retail store.

### Transportation Schema
The **AATP_TransportationSchema** represents transportation details for product shipments. The attributes are:
- `shipment_id`: Unique identifier for the shipment.
- `product_id`: Identifier for the product being transported.
- `origin_location`: Location from which the shipment originated.
- `destination_location`: Destination location for the shipment.
- `shipment_date`: Date of shipment.
- `transport_conditions`: Conditions under which the product is transported.

### User Schema
The **AATP_UserSchema** defines basic user information. Attributes include:
- `user_id`: Unique identifier for the user.
- `name`: Name of the user.
- `email`: Email address of the user.

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

