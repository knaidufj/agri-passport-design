---
theme: default
background: https://cover.sli.dev
title: Agri Passport Presentation
info: |
  ## Slidev Starter Template
  Presentation slides for developers.

  Learn more at [Sli.dev](https://sli.dev)
# apply unocss classes to the current slide
class: text-center
drawings:
  persist: false
# slide transition: https://sli.dev/guide/animations.html#slide-transitions
transition: slide-left
# enable MDC Syntax: https://sli.dev/features/mdc
mdc: true
# take snapshot for each slide in the overview
overviewSnapshots: true
---

## 1. Nature of the Problem and User Requirements

### Problem Overview
- Enhance Australia's agricultural traceability initiatives to improve food security, safety, and agility.
- Design and implement a prototype of an AATP-enabled Agri Food Product Passport.
- Leverage Decentralized Identifiers (DIDs) and Verifiable Credentials.

#### Expanded Overview
- Utilize Decentralized Identity (DI) based W3C verifiable credentials and Decentralized Identifiers.
- Leverage open-source tools for system implementation.
- Demonstrate capabilities to issue and verify product credentials, establish a DI wallet, and create a verifiable data registry (VDR).
- Ensure food security, safety, and agility through a product passport system with conformity credentials and traceability for specific products or batch identifiers.

### User Requirements
- **Stakeholders**: Farmers, distributors, consumers, and regulatory authorities.
- **Requirements**: Develop a decentralized, transparent system for end-to-end traceability of agricultural products.

### Client Information
- **Client 1**: Veritas Digital
  - **Contact Person**: Dr. Tony Lenko, CEO
  - **Address**: 50 Cavill Avenue, GC
  - **Phone Number**: +61 401 294 192
  - **Email**: tony@veritasdigital.io
- **Client 2**: Anonyome Lab
  - **Contact Person**: Dr. Paul Ashley, CTO
  - **Address**: 50 Cavill Avenue, GC
  - **Phone Number**: +61 421 611 853
  - **Email**: pashley@anonyome.com
- **Support**: Veritas Digital and Anonyome Labs will provide materials and advice.
- **Potential Presentation**: Project might be presented at the Internet Identity Workshop (IIW) in Mountain View, California.

### Definitions and Acronyms

#### Definitions
- **Australian Agricultural Traceability Protocol (AATP)**: Enhances food security, safety, and agility in Australia's agricultural sector through traceability.
- **Decentralized Identity (DI)**: Identity management system using DIDs and verifiable credentials for secure, privacy-preserving data sharing.
- **Verifiable Data Registry (VDR)**: Registry used to store and verify product credentials, ensuring data integrity and traceability.
- **W3C Verifiable Credentials**: Standards developed by W3C for issuing and verifying credentials in a decentralized manner.
- **Agri Food Product Passport**: Digital passport including traceability information, sustainability credentials, and conformity certifications for agricultural products.
- **Generative AI**: AI techniques generating data, such as dummy data for credentials.
- **Role-Based Access Control (RBAC)**: Regulates access based on user roles within an organization.
- **ISO 22005**: International standard for traceability in the food and feed chain, ensuring product transparency and safety.
- **JSON, XML, CSV**: Common data formats for data exchange and interoperability.

#### Acronyms
- **AATP**: Australian Agricultural Traceability Protocol
- **DI**: Decentralized Identity
- **VDR**: Verifiable Data Registry
- **W3C**: World Wide Web Consortium
- **ICT**: Information and Communication Technology
- **IIW**: Internet Identity Workshops

### Resources and Facilities
- Prototype built on personal laptops owned by team members.
- Remote servers may be used as needed during prototype development.
- Computer programming labs at Griffith University available if additional resources are required.

---
transition: fade-out
---

## 2. Vision

### Product Vision
- Develop a prototype of the Australian Agricultural Traceability Protocol (AATP)-enabled Agri Food Product Passport.
- Leverage Decentralized Identity (DI) based W3C verifiable credentials and Decentralized Identifiers.
- Enhance food security, safety, and agility in Australia by issuing and verifying credentials, establishing a DI wallet, and creating a verifiable data registry (VDR).
- Ensure comprehensive traceability for agricultural products.

### Agri Passport Description
- **For**: Supply chain participants, government bodies, conformity assessment bodies, academic and research community, buyers of environmental outcomes, agricultural industry bodies, and standards development organizations.
- **Who Need**: A reliable and efficient system for tracking and verifying the origin, safety, and quality of agricultural products.
- **Agri Passport**: A traceability and verification system.
- **That Ensures**: Enhanced transparency, security, and efficiency in the agricultural supply chain, providing verifiable credentials and decentralized identity management.
- **Unlike**: Traditional centralized traceability systems.
- **Our Product Offers**: A decentralized, secure, and privacy-preserving solution using W3C verifiable credentials and decentralized identifiers, ensuring compliance with food safety regulations and increasing consumer trust through enhanced traceability.

### Customers and Benefits
- **Primary Customers**: Agricultural producers, food distributors, and regulatory bodies involved in food safety and traceability.

#### Customer Groups
- **Agricultural Producers**:
  - **Characteristics**: Farmers and agricultural businesses focused on crop and livestock production.
  - **Benefits**: Enhanced traceability, improved safety standards, increased consumer trust, and easier verification of organic and other certifications.
- **Food Distributors**:
  - **Characteristics**: Companies that distribute agricultural products throughout the supply chain.
  - **Benefits**: Enhanced efficiency, greater transparency, and reduced risk of fraud or non-compliance.
- **Regulatory Bodies**:
  - **Characteristics**: Government and other regulatory organizations responsible for ensuring food safety and compliance.
  - **Benefits**: Improved monitoring capabilities, enhanced data accuracy, and streamlined certification processes.

### Benefits of Agri Passport
- **Enhanced Transparency**: Provides all stakeholders in the supply chain with easy access to verifiable product information.
- **Increased Consumer Trust**: By ensuring end-to-end traceability, consumers can be confident in the quality and safety of agricultural products.
- **Compliance**: Supports regulatory compliance with standards such as ISO 22005.

---
transition: fade-out
---

## 3. Software Methodology

### Methodology Used
- **Agile Software Development**: Iterative cycles for development, testing, and feedback.

### Evaluation
- **Strengths**: Flexibility in responding to changes in user requirements; quick adaptation during development.
- **Challenges**: Managing expectations and ensuring synchronization of all team members due to remote collaboration.

---
transition: fade-out
---


## 4. Team Roles and Assignments

### Team Overview
- Members with diverse technical skills, including software engineering, blockchain, and design.

### Assigned Roles
- **Project Lead and System Designer**: Arpita Dhar
  - Responsible for overall system design and overseeing project progress.
  - Ensures timely completion, coordinates with the team, and manages internal communication.

- **API Developer and Student Liaison**: Gaurav Singh
  - Designs and implements the Passport and VDR API for the prototype.
  - Demonstrates functionality through the DI wallet and maintains project documentation.

- **API Security Analyst**: Prathap Reddy K
  - Ensures API security by implementing robust protocols and conducting risk assessments.
  - Protects sensitive data from unauthorized access.

- **Quality Assurance Analyst**: Sheikh Ashik Rahman Elahi
  - Creates comprehensive test plans outlining testing scope, objectives, and resources.
  - Designs and develops test cases based on software requirements, runs unit testing, and executes test cases.
  - Generates reports on test results and overall software quality.

- **User Experience Designer**: Jins Alias
  - Designs intuitive and user-friendly interfaces for user-facing components.
  - Tests for alignment with stakeholder needs and conducts usability testing to refine the user experience.
  - Creates documentation for the user interface, ensuring consistency and accessibility.

- **Database Administrator**: Albin Johny
  - Manages the database to support project requirements.
  - Implements database security protocols and ensures high availability.
  - Performs regular backups and optimization for efficient performance.

### Changes in Roles
- **Role Adjustments**: Roles remained consistent throughout the project; however, adjustments were made based on workload and priorities to ensure effective project progress.

---
transition: fade-out
---

## 5. Requirements

### Scope
- **Scope**: Demonstrate AATP Protocol through an API designed to facilitate the traceability of agricultural products throughout the supply chain.
- **Objectives**: Enable seamless data exchange, verification of credentials, and access to product information, supporting transparency, accountability, and compliance with sustainability and safety standards.

### Key Features
- **Single Identifier Management**:
  - Generates and manages unique identifiers (e.g., barcodes) for each product.
  - **API Endpoints**:
    - `POST /identifiers`: Create a new identifier for a product.
    - `GET /identifiers/{id}`: Retrieve details associated with a specific identifier.

- **Product Passport Creation and Management**:
  - Allows creation and management of a digital product passport, linking to data points such as sustainability credentials and traceability events.
  - **API Endpoints**:
    - `POST /product-passport`: Create a new product passport.
    - `GET /product-passport/{id}`: Retrieve product passport details.
    - `PUT /product-passport/{id}`: Update an existing product passport.
    - `DELETE /product-passport/{id}`: Remove a product passport from the system.

- **Independent System Integration**:
  - Enables data exchange between independent systems without direct integration.
  - **API Endpoints**:
    - `POST /data-exchange`: Facilitate the exchange of data between independent systems.
    - `GET /data-exchange/status/{id}`: Check the status of ongoing data exchange.

### Non-Functional Requirements (NFR)

#### Security
- **NFR1.1 Data Security**: Use encryption for data in transit and at rest.
- **NFR1.2 Authentication**: Use role-based access control (RBAC) for ensuring secure access.

#### Performance
- **NFR2.1 Scalability**: The system must handle an increasing volume of data and users.
- **NFR2.2 Latency**: The response time for API requests should be less than 200ms under normal load.

#### Availability
- **NFR3.1 High Availability**: System should have an uptime of 99.9%.
- **NFR3.2 Fault Tolerance**: Designed to handle failures gracefully with automatic recovery.

#### Usability
- **NFR4.1 Documentation**: Provide comprehensive API documentation.
- **NFR4.2 User Interface**: The management console shall have a user-friendly interface.
- **NFR4.3 Error Handling**: Clear and descriptive error messages for user diagnosis.

#### Maintainability
- **NFR5.1 Modularity**: Modular system components for easy updates.
- **NFR5.2 Code Quality**: Adhere to coding standards and automated testing.
- **NFR5.3 Versioning**: Support API versioning for backward compatibility.

#### Compliance
- **NFR6.1 Regulatory Compliance**: Comply with relevant standards such as ISO 22005.
- **NFR6.2 Auditability**: Provide comprehensive audit logs.

#### Interoperability
- **NFR7.1 Compatibility**: Compatible with independent systems used by stakeholders.
- **NFR7.2 Data Format Support**: Support common data formats like JSON, XML, and CSV.

---
transition: fade-out
---

## 6. Plan

### Initial Planning and Research (Week 4 to 5)
- **Milestone**: Project kick-off and requirements gathering.
- **Deliverable**: Project plan and requirements document.

### Design Phase (Week 6)
- **Milestone**: Completion of system architecture and design specifications.
- **Deliverable**: Design document detailing the DI wallet, VDR, and credential issuance and verification processes.

### Development Phase (Week 7 to 9)
- **Milestone**: Development of core functionalities for DI wallet and VDR.
- **Deliverable**: Prototype of the DI wallet and VDR system.

### Testing Phase (Week 7 to 9)
- **Milestone**: Completion of system testing and debugging.
- **Deliverable**: Test reports and bug fixes documentation.

### Integration and User Testing (Week 9 to 10)
- **Milestone**: Integration with existing systems and user acceptance testing.
- **Deliverable**: User feedback report and final system adjustments.

### Analysis Phase (Week 10 to 12)
- **Milestone**: Review of the AATP prototype.
- **Deliverable**: Evaluation report and recommendations for future improvements.

---
transition: fade-out
---


## 7. Progress and Testing of Requirements

### Requirements Progress
- **Product Passport API**: Implemented to provide traceability information.
- **Blockchain Integration**: Completed using Hyperledger Aries.

### Testing and Scope Changes
- **Testing**: Conducted both unit and integration testing.
- **Scope Change**: Expanded to support third-party traceability tools due to stakeholder feedback.

---
transition: fade-out
---

## 8. Live Demo

### Demo Overview
- **Product Traceability Flow**: Demonstrating the journey of an agricultural product through the supply chain.
- **Integration**: Using APIs and DIDs for secure and transparent communication.

---
transition: fade-out
---

## 9. Lessons Learned

### Team-Level Insights
- Effective communication is crucial, especially across time zones.
- Agile methods helped quickly adapt to changes; managing workload balance remained challenging.

### Individual Reflections
- **Arpita Dhar**: "Leading the project taught me valuable lessons about system design and team coordination."
- **Gaurav Singh**: "Developing the API gave me deep insights into DI and VDR integration."
- **Sheikh Ashik Rahman Elahi**: "Quality assurance processes helped me improve my testing and analysis skills."
- **Jins Alias**: "Designing for transparency pushed me to think beyond traditional UI/UX practices."

---
transition: fade-out
---

## 10. Client Feedback and Incorporation

### Feedback Process
- **Initial Feedback**: Received during week 4; need for easier user onboarding highlighted.
- **Action Taken**: Simplified onboarding by refining the user interface.

### Final Feedback
- **Response**: Client appreciated streamlined API and visual clarity of traceability data.