# Requirements

## Scope
The scope of the project is to demonstrate AATP Protocol through an API, which will be designed to facilitate the traceability of agricultural products throughout the supply chain by enabling seamless data exchange, verification of credentials, and access to product information. This API supports transparency, accountability, and compliance with sustainability and safety standards across various agricultural sectors.

## Key Features

### Single Identifier Management
- **Functionality**: The API generates and manages unique identifiers (e.g., barcodes) for each product. These identifiers are the primary keys for accessing associated product data stored in the system.
- **API Endpoints**:
  - `POST /identifiers`: Create a new identifier for a product.
  - `GET /identifiers/{id}`: Retrieve the details associated with a specific identifier.

### Product Passport Creation and Management
- **Functionality**: The API allows for the creation and management of a digital product passport, which includes links to various data points such as sustainability credentials, conformity certifications, and traceability events.
- **API Endpoints**:
  - `POST /product-passport`: Create a new product passport.
  - `GET /identifiers/{id}`: Retrieve the details associated with a specific identifier.
  - `GET /product-passport/{id}`: Retrieve product passport details.
  - `PUT /product-passport/{id}`: Update an existing product passport.
  - `DELETE /product-passport/{id}`: Remove a product passport from the system.

### Independent System Integration
- **Functionality**: 
  - The API enables data exchange between independent systems without requiring direct integration.
  - Allows different stakeholders to use their preferred platforms while still participating in the traceability network.
- **API Endpoints**: 
  - `POST /data-exchange`: Facilitate the exchange of data between independent systems.
  - `GET /data-exchange/status/{id}`: Check the status of an ongoing data exchange.

### Credential Management
- **Functionality**: 
  - The API supports the creation, verification, and management of portable credentials linked to product passports. 
  - These credentials include:
    - ESG sustainability certifications
    - Conformity credentials issued by competent authorities
    - Records of traceability events
- **API Endpoints**:
  - `POST /credentials`: Issue a new credential linked to a product passport.
  - `GET /credentials/{id}`: Retrieve details of a specific credential.
  - `PUT /credentials/{id}`: Update an existing credential.
  - `DELETE /credentials/{id}`: Remove a credential from the system.
  - `POST /credentials/verify`: Verify the authenticity of a credential.

### Data Privacy and Security
- **Functionality**: 
  - The API ensures that all data, particularly rich and confidential business data, is stored securely.
  - Access to sensitive information is controlled and granted only to authorized entities.
- **API Endpoints**:
  - `GET /data-protection/{id}`: Review security settings for a specific data record.
  - `PUT /data-protection/{id}`: Update security settings for a data record.
  - `POST /access-control`: Manage access control lists for different data sets.

### Scalability and Flexibility
- **Functionality**: 
  - The API is designed to scale efficiently across different agricultural sectors and operational sizes.
  - It can be easily integrated into existing systems and adapted to evolving business needs.
- **API Endpoints**: 
  - `GET /scalability-options`: Retrieve recommended configurations for different scales of operation.
  - `PUT /scalability-settings`: Adjust API settings to match operational needs.

## 3.3 Use Cases

### Product Traceability
- **Objective**: Enable end-to-end traceability of agricultural products, ensuring that stakeholders can access complete and accurate information about a product's journey through the supply chain.
- **Example**: A retailer queries the API to retrieve the product passport and associated credentials for a batch of produce to verify its sustainability claims.

### Compliance Verification
- **Objective**: Ensure that products meet regulatory and market requirements by verifying credentials issued by competent authorities.
- **Example**: An EU importer uses the API to verify that an agricultural product complies with EU sustainability and safety standards before finalizing the purchase.

### Decentralized Data Management
- **Objective**: Facilitate data exchange and management across multiple independent systems without requiring centralized integration.
- **Example**: A cattle farm and a grain farm use their own business systems but exchange data through the API to create a combined product passport for a feedlot.

### Security and Compliance
- **Data Encryption**: All data transmitted via the API is encrypted to ensure security and privacy.
- **Access Control**: Role-based access control (RBAC) is implemented to manage permissions for different users and systems.
- **Audit Logging**: The API maintains detailed logs of all transactions and data exchanges for audit purposes.

### Technical Specifications
- **API Protocol**: RESTful API with JSON payloads.
- **Authentication**: OAuth 2.0 for secure access and token management.
- **Rate Limiting**: Configurable rate limits to prevent abuse and ensure fair usage.
- **Versioning**: API versioning to support backward compatibility and smooth transitions during updates.

The further sub-sections outline the detailed requirements necessary for the successful completion and implementation of the Agri Passport project. These functional and non-functional requirements together define the scope and operational parameters of the AATP Protocol API, ensuring that it meets the needs of stakeholders across the agricultural supply chain while adhering to high standards of performance, security, and usability.

## Functional Requirements

### FR1. Single Identifier Management
- **FR1.1 Identifier Generation**: The system shall generate a unique identifier (e.g., barcode) for each product, which serves as the primary key for accessing the associated product data.
- **FR1.2 Retrieve Identifier Details**: The system shall allow users to retrieve the details associated with a specific identifier.
- **FR1.3 Update Identifier Information**: The system shall allow users to update information linked to an existing identifier.
- **FR1.4 Delete Identifier**: The system shall allow users to delete information linked to an existing identifier.

### FR2. Product Passport Creation and Management
- **FR2.1 Create Product Passport**: The system shall allow users to create a digital product passport that includes links to sustainability credentials, conformity certifications, and traceability events.
- **FR2.2 Retrieve Product Passport**: The system shall allow users to retrieve the product passport details using the unique identifier.
- **FR2.3 Update Product Passport**: The system shall allow users to update existing product passports with new or modified information.
- **FR2.4 Delete Product Passport**: The system shall allow users to delete a product passport from the system.

### FR3. Independent System Integration
- **FR3.1 Data Exchange Initiation**: The system shall allow users to initiate data exchanges between independent systems, facilitating the transfer of credentials and traceability data.
- **FR3.2 Monitor Data Exchange**: The system shall provide a mechanism to monitor the status of ongoing data exchanges, including success, failure, and in-progress states.
- **FR3.3 Support for Multiple Systems**: The system shall support data exchanges with multiple independent systems, allowing flexibility in integration.

### FR4. Credential Management
- **FR4.1 Issue Credentials**: The system shall allow the creation and issuance of credentials (e.g., sustainability certifications, conformity credentials) linked to product passports.
- **FR4.2 Retrieve Credential Details**: The system shall allow users to retrieve details of specific credentials using a credential identifier.
- **FR4.3 Update Credentials**: The system shall allow users to update existing credentials.
- **FR4.4 Delete Credentials**: The system shall allow users to delete a credential from the system.
- **FR4.5 Credential Verification**: The system shall provide functionality to verify the authenticity of a credential, ensuring its validity and integrity.

### FR5. Data Privacy and Security
- **FR5.1 Data Encryption**: The system shall encrypt all data during transmission to protect sensitive information.
- **FR5.2 Access Control Management**: The system shall provide role-based access control (RBAC) to manage permissions for different users and systems, ensuring only authorized access.
- **FR5.3 Security Settings Configuration**: The system shall allow users to configure and update security settings for data records.
- **FR5.4 Audit Logging**: The system shall log all transactions and data exchanges for audit purposes, including details such as timestamp, user ID, action performed, and outcome.

### FR6. Scalability and Flexibility
- **FR6.1 Configuration Options for Scale**: The system shall provide configuration options to accommodate different scales of operation, from small farms to large agricultural enterprises.
- **FR6.2 Adjustment of API Settings**: The system shall allow users to adjust API settings to match operational needs, including performance tuning and resource allocation.

### FR7. Compliance and Regulatory Support
- **FR7.1 Compliance Verification**: The system shall support the verification of credentials to ensure products meet regulatory and market requirements.
- **FR7.2 EU Compliance Checks**: The system shall include functionality to perform compliance checks specifically for products destined for the EU market.

### FR8. Advanced System Features
- **FR8.1 User Role Management**: The system shall support the creation and management of user roles, each with specific permissions and access controls.
- **FR8.2 Detailed Reporting and Analytics**: The system shall provide detailed reporting and analytics capabilities to allow users to generate custom reports on traceability data, compliance status, and other key metrics.
- **FR8.3 Enhanced Data Validation**: The system shall implement robust data validation rules to ensure the accuracy and consistency of input data across all modules.

### FR9. Web Application Features
- **FR9.1 Dashboard**: The web application shall include a dashboard displaying key metrics and access to core features. The system shall support the verification of credentials to ensure products meet regulatory and market requirements.
- **FR9.2 Product Passport Management**: The web application shall allow users to create, update, and view product passports.
- **FR9.3 Credential Management**: The web application shall support the issuance, verification, and management of credentials.
- **FR9.4 User Authentication**: The web application shall provide secure login functionality for different user roles.

## Non-Functional Requirements

### NFR1. Performance
- **NFR1.1 Response Time**: The system shall support the verification of credentials to ensure products meet regulatory and market requirements.
- **NFR1.2 Throughput**: The system shall include functionality to perform compliance checks specifically for products destined for the EU market.
- **NFR1.3 Scalability**: The API shall be horizontally scalable to support increasing numbers of users and transactions.

### NFR2. Security
- **NFR2.1 Data Encryption**: All data shall be encrypted in transit using TLS 1.2 or higher, and at rest using AES-256 encryption.
- **NFR2.2 Authentication**: The API shall use OAuth 2.0 for secure access and token management, ensuring that only authenticated users can access the system.
- **NFR2.3 Access Control**: The system shall implement role-based access control (RBAC) to ensure that only authorized users can perform specific actions.
- **NFR2.4 Data Privacy**: The API shall comply with relevant data privacy regulations, such as GDPR, ensuring that personal data is handled appropriately.

### NFR3. Reliability
- **NFR3.1 Availability**: The API shall have an uptime of 99.9% to ensure it is highly available for users.
- **NFR3.2 Fault Tolerance**: The system shall be designed to handle failures gracefully, with automatic recovery and minimal disruption to users.
- **NFR3.3 Data Integrity**: The system shall ensure the integrity of data during transmission, storage, and retrieval, preventing data corruption or loss.

### NFR4. Usability
- **NFR4.1 Documentation**: The API shall be accompanied by comprehensive documentation, including usage examples, API reference, and integration guides.
- **NFR4.2 User Interface**: The management console (if any) shall have a user-friendly interface that allows users to manage identifiers, product passports, credentials, and security settings with ease.
- **NFR4.3 Error Handling**: The system shall provide clear and descriptive error messages to help users diagnose and resolve issues quickly.

### NFR5. Maintainability
- **NFR5.1 Modularity**: The system shall be designed with modular components, allowing for easy updates, bug fixes, and feature enhancements.
- **NFR5.2 Code Quality**: The API shall follow best practices for code quality, including adherence to coding standards, code reviews, and automated testing.
- **NFR5.3 Versioning**: The API shall support versioning to ensure backward compatibility and smooth transitions during updates.

### NFR6. Compliance
- **NFR6.1 Regulatory Compliance**: The API shall comply with relevant international standards and regulations, such as ISO 22005 for traceability in the food and feed chain.
- **NFR6.2 Auditability**: The system shall provide comprehensive audit logs that can be reviewed for compliance verification and incident investigation.

### NFR7. Interoperability
- **NFR7.1 Compatibility**: The API shall be compatible with a wide range of independent systems used by different stakeholders in the agricultural supply chain.
- **NFR7.2 Data Format Support**: The system shall support common data formats such as JSON, XML, and CSV for data exchange.