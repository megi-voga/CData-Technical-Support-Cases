# 🛠️ CData Technical Support Assessment

### Python Solutions for Real-World IPWorks Support Scenarios

This repository contains the technical solutions developed as part of a **CData Technical Support assessment**, covering four practical support scenarios using **Python** and **CData IPWorks technologies**.

The assessment focused not only on producing working implementations, but also on approaching each case from a technical support perspective: understanding the reported problem, investigating the relevant technology, implementing and validating a solution, and documenting the outcome clearly for the customer.

---

## 🎯 Assessment Overview

The repository covers four independent technical support cases involving:

* TCP client/server communication
* ZIP archive processing
* Secure SFTP connections and host-key verification
* REST API requests and JSON data extraction

Each case contains its own implementation and documentation so that it can be reviewed and executed independently.

---

## 📡 Case 1 — TCP Client/Server Communication

The first case focuses on establishing communication between a **TCP client and TCP server**.

The implementation demonstrates the fundamental workflow required for socket-based communication, including establishing the connection and exchanging data between two endpoints.

### Concepts Demonstrated

* TCP/IP communication
* Client/server architecture
* Network connections
* Data transmission
* Python-based implementation

---

## 📦 Case 2 — Extracting a Single File from a ZIP Archive

The second support scenario addresses **selective file extraction from a ZIP archive**.

Instead of treating the archive as a single extraction operation, the solution demonstrates how a specific file can be identified and extracted when only one archive entry is required.

### Concepts Demonstrated

* ZIP archive handling
* Archive entry selection
* File extraction
* File-system operations
* Python scripting

---

## 🔐 Case 3 — SFTP Host Key Verification

The third case focuses on **secure SFTP connectivity** and, specifically, **SSH host-key verification**.

Host-key verification is an important part of establishing trusted SSH/SFTP connections because it allows the client to verify the identity of the remote server before proceeding with the connection.

The implementation demonstrates the required verification workflow within an SFTP support scenario.

### Concepts Demonstrated

* SFTP
* SSH security
* Host-key verification
* Secure remote connections
* Connection validation

---

## 🌐 Case 4 — Reading Product Titles from a JSON API

The fourth case works with data returned by a **JSON-based API**.

The implementation retrieves the API response, processes the returned JSON structure, and extracts the required **product title information**.

### Concepts Demonstrated

* HTTP/API communication
* JSON parsing
* Structured data processing
* Response handling
* Data extraction

---

## 📁 Repository Structure

The repository is organized around the four independent support cases:

```text
cdata-technical-support-assessment/
│
├── case-1-tcp-client-server/
│   ├── source code
│   ├── README
│   └── validation screenshots
│
├── case-2-zip-extraction/
│   ├── source code
│   ├── README
│   └── validation screenshots
│
├── case-3-sftp-host-key/
│   ├── source code
│   ├── README
│   └── validation screenshots
│
├── case-4-json-api/
│   ├── source code
│   ├── README
│   └── validation screenshots
│
└── README.md
```

Each case includes:

* Python source code
* Execution instructions
* Validation evidence
* Case-specific README documentation

---

## 🧰 Technical Skills Demonstrated

**Programming**

* Python

**Networking**

* TCP/IP
* Client/server communication
* SFTP
* SSH

**Security**

* SSH host-key verification
* Secure connection validation

**Data & APIs**

* HTTP/API interaction
* JSON parsing
* Structured data extraction

**File Processing**

* ZIP archives
* Selective file extraction

**Technical Support**

* Problem investigation
* Technical troubleshooting
* Solution validation
* Technical documentation
* Customer-oriented communication

---

## 📝 Technical Support Documentation

In addition to the source code contained in this repository, the original assessment included a separate technical report documenting:

* analysis of each support request
* research and investigation process
* proposed technical solution
* implementation approach
* validation of the solution
* recommended customer response

This repository focuses primarily on the **technical implementations and reproducible evidence** for each case.

---

## 💡 What This Assessment Demonstrates

The four cases cover different areas of software support and integration engineering, requiring the ability to move between **networking, security, file processing, and API/data handling**.

More importantly, the assessment demonstrates the complete technical-support workflow:

**Problem Analysis → Investigation → Implementation → Testing → Validation → Documentation → Customer Response**

This combination of technical problem-solving and clear communication is essential when supporting developers integrating software components into real-world applications.

---

## 👩‍💻 Author

**Megi Voga**

AI & Machine Learning • Software Development • Technical Support

GitHub: `@megi-voga`
