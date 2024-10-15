---
layout: default
---

# Technical scope
- **Scope**: Demonstrate AATP Protocol through an API designed to facilitate the traceability of agricultural products throughout the supply chain.
- **Objectives**: Enable seamless data exchange, verification of credentials, and access to product information, supporting transparency, accountability, and compliance with sustainability and safety standards.

<!-- The technical scope of our project is to demonstrate how the **AATP Protocol** can enhance agricultural traceability. We are doing this by developing an **API** specifically designed to track agricultural products from the point of production to the end consumer.

Our key objectives revolve around enabling seamless **data exchange** across different systems in the supply chain. We want to make sure that **verification of credentials** is straightforward, allowing stakeholders to confirm the origin, safety, and sustainability of agricultural products.

Additionally, we focus on ensuring that product information is easily accessible, which is essential for maintaining **transparency** and **accountability**. These elements are critical for compliance with sustainability and food safety standards. Ultimately, we are creating an open and secure environment for the data flow, one that stakeholders can trust.
-->
---
layout: cover
---

# Functional Requirements

<!-- In this section, we’ll be discussing the **functional requirements** for our AATP system. These requirements describe the essential capabilities the system must have to fulfill its intended purpose, including data exchange, traceability, and the management of unique product identifiers. The focus is on the actions and interactions that enable the complete functionality of the agricultural traceability system.-->

---
layout: default
---

# Single Identifier Management
- Generates and manages unique identifiers (e.g., QR codes) for each product.
- **API Endpoints**:
  - `POST /identifiers`: Create a new identifier for a product.
  - `GET /identifiers/{id}`: Retrieve details associated with a specific identifier.

<!-- An important component of our solution is **Single Identifier Management**. Each agricultural product will have its own **unique identifier**, such as a QR code. This helps in maintaining traceability throughout the entire supply chain.

The unique identifiers are generated and managed through dedicated API endpoints. With the `POST /identifiers` endpoint, we can create a new identifier for a product. This essentially assigns a distinct digital "ID card" to each item in the supply chain.

Meanwhile, the `GET /identifiers/{id}` endpoint allows us to **retrieve detailed information** linked to that specific identifier. For instance, this could include data such as the product’s origin, processing events, or safety credentials. This kind of detailed tracking is crucial for maintaining integrity and transparency.
-->

---
layout: default
---

# Product Passport Creation and Management
- Allows creation and management of a digital product passport, linking to data points such as sustainability credentials and traceability events.
- **API Endpoints**:
  - `POST /product-passport`: Create a new product passport.
  - `GET /product-passport/{id}`: Retrieve product passport details.
  - `PUT /product-passport/{id}`: Update an existing product passport.
  - `DELETE /product-passport/{id}`: Remove a product passport from the system.

<!-- The **Product Passport Creation and Management** module is another core feature of our system. The idea here is to provide each product with a digital passport—a comprehensive document that contains all relevant data points, such as **sustainability credentials** and key traceability events.

We have specific API endpoints for interacting with product passports:
- The `POST /product-passport` endpoint allows the **creation** of a new digital product passport.
- `GET /product-passport/{id}` lets stakeholders **retrieve detailed information** about a product passport—this could be anything from its initial production to specific sustainability credentials.
- `PUT /product-passport/{id}` allows users to **update** information if the product undergoes changes or certifications.
- Lastly, `DELETE /product-passport/{id}` is used when a product passport needs to be **removed** from the system, for instance, if a product is no longer part of the supply chain.

By enabling seamless product passport creation and management, we ensure that there is always reliable, up-to-date information available about every product.
-->

---
layout: default
---

# Independent System Integration
- Enables data exchange between independent systems without direct integration.
- **API Endpoints**:
  - `POST /data-exchange`: Facilitate the exchange of data between independent systems.
  - `GET /data-exchange/status/{id}`: Check the status of ongoing data exchange.

<!-- One of the challenges in the agricultural sector is the existence of multiple, independent systems that must interact without having direct integration. This slide addresses our solution for **Independent System Integration**.

Using our `POST /data-exchange` API endpoint, we facilitate **data exchange** between these systems in a secure and seamless way. Think of it as a bridge—allowing data to flow freely without requiring each system to be tightly coupled with another. This is critical in preserving the integrity of data and allowing flexibility across the supply chain.

We also provide a `GET /data-exchange/status/{id}` endpoint to **check the status** of ongoing data exchanges. This ensures that stakeholders are always informed about the progress of data transfers, giving them confidence in the reliability and responsiveness of the system.
-->

---
layout: cover
---
# Non-Functional Requirements (NFR)


<!-- The **Non-Functional Requirements** (NFR) are just as critical as the functional ones. These are the requirements that describe how the system should operate rather than what it should do.

These requirements ensure the system is **secure**, **performant**, **usable**, **maintainable**, and **compliant** with regulations. They help guide the quality of the overall solution, ensuring that it can effectively meet the needs of all stakeholders in real-world usage.
-->

---
layout: default
---

| **Category**         | **Requirement**                                                                                     |
|----------------------|-----------------------------------------------------------------------------------------------------|
| **Security**         | **NFR1.1 Data Security**: Use encryption for data in transit and at rest.                         |
|                      | **NFR1.2 Authentication**: Use role-based access control (RBAC) for ensuring secure access.        |
| **Performance**      | **NFR2.1 Scalability**: The system must handle an increasing volume of data and users.             |
|                      | **NFR2.2 Latency**: The response time for API requests should be less than 200ms under normal load.|

<!--Here we address the **security** and **performance** aspects of our system.

For **security**, we ensure **data security** by employing **encryption** for both data at rest and data in transit. This guarantees the confidentiality and integrity of data, making sure that unauthorized users cannot intercept or manipulate it.

We also use **role-based access control (RBAC)** to ensure that only authorized personnel can access sensitive information or perform critical operations.

On the **performance** side, we need the system to be **scalable**—capable of handling an increasing number of users and a growing volume of data without a decrease in performance. Additionally, the system's response times must remain quick and efficient, with a **latency** of less than **200ms** for typical API requests.
-->

---
layout: default
---


| **Category**         | **Requirement**                                                                                     |
|----------------------|-----------------------------------------------------------------------------------------------------|
| **Availability**     | **NFR3.1 High Availability**: System should have an uptime of 99.9%.                              |
|                      | **NFR3.2 Fault Tolerance**: Designed to handle failures gracefully with automatic recovery.        |
| **Usability**        | **NFR4.1 Documentation**: Provide comprehensive API documentation.                                 |
|                      | **NFR4.2 User Interface**: The management console shall have a user-friendly interface.           |
|                      | **NFR4.3 Error Handling**: Clear and descriptive error messages for user diagnosis.                |

<!-- For **availability**, our system is designed to ensure **high uptime**—at least **99.9%**—so that users can depend on its reliability. We also ensure **fault tolerance**, meaning that if there is a failure, the system should be able to **recover automatically** with minimal impact on end users.

In terms of **usability**, we focus on providing **comprehensive API documentation**, which is critical for developers who need to interact with our system. A **user-friendly interface** for the management console will make system management easier for non-technical users. Finally, we have clear **error handling**, providing descriptive error messages to help users diagnose and resolve issues efficiently.
-->

---
layout: default
---

| **Category**         | **Requirement**                                                                                     |
|----------------------|-----------------------------------------------------------------------------------------------------|
| **Maintainability**  | **NFR5.1 Modularity**: Modular system components for easy updates.                                 |
|                      | **NFR5.2 Code Quality**: Adhere to coding standards and automated testing.                         |
|                      | **NFR5.3 Versioning**: Support API versioning for backward compatibility.                          |
| **Compliance**       | **NFR6.1 Regulatory Compliance**: Comply with relevant standards such as ISO 22005.               |
|                      | **NFR6.2 Auditability**: Provide comprehensive audit logs.                                         |


<!-- **Maintainability** is key to making sure our system remains relevant and easily adaptable. To do this, we focus on **modularity**, which allows components to be updated or replaced independently without affecting the whole system. We ensure **code quality** by adhering to coding standards and using **automated testing**. Also, **API versioning** helps in maintaining backward compatibility, allowing older versions of APIs to remain functional.

For **compliance**, we are committed to meeting relevant regulatory standards, including **ISO 22005** for food traceability. Additionally, we provide **auditability** by maintaining comprehensive audit logs, which help in tracking all activities within the system and proving compliance during assessments.
-->


---
layout: default
---

| **Category**         | **Requirement**                                                                                     |
|----------------------|-----------------------------------------------------------------------------------------------------|
| **Interoperability** | **NFR7.1 Compatibility**: Compatible with independent systems used by stakeholders.                |
|                      | **NFR7.2 Data Format Support**: Support common data formats like JSON, XML, and CSV.               |

<!-- Finally, let's address **interoperability**. Since the agricultural supply chain consists of various independent systems used by different stakeholders, our system must be **compatible** with these. This allows for seamless integration and data exchange without requiring significant changes to existing infrastructure.

To support this, we ensure that the system can handle **multiple data formats** such as **JSON, XML, and CSV**. This flexibility makes it easier for data to be shared across diverse platforms, promoting smooth communication and integration among all stakeholders involved.
-->