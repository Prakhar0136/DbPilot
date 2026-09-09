# Product Requirements Document (PRD)

## 1. Problem Statement

Non-technical users and domain experts often require data insights from relational databases but lack the SQL knowledge needed to retrieve them efficiently.

## 2. Proposed Solution (MVP)

DBPilot is an internal tool that allows users to ask natural-language questions about a PostgreSQL database. It safely translates the question into SQL, executes the query, and returns formatted results alongside a human-readable explanation.

## 3. Scope Definition

### In Scope for MVP

- PostgreSQL support only.
- Read-only `SELECT` operations.
- Natural-language-to-SQL translation.
- Automated error correction using a single LLM retry.
- Result presentation using data tables and text explanations.

### Out of Scope

- Modifying database state (`INSERT`, `UPDATE`, `DELETE`, `DROP`, etc.).
- User authentication / RBAC.
- Cross-database joins or support for other database engines.
- Vector databases / RAG document retrieval.
- Data export (CSV/Excel).

## 4. Functional Requirements

- **FR1:** The system shall accept natural-language text inputs from the user.
- **FR2:** The system shall retrieve the live schema of the connected PostgreSQL database before generating a query.
- **FR3:** The system shall use an LLM to generate PostgreSQL-compliant SQL.
- **FR4:** The system shall validate generated SQL and block destructive or non-`SELECT` operations before execution.
- **FR5:** The system shall execute valid SQL queries against the PostgreSQL database.
- **FR6:** The system shall return a maximum of 100 rows to the user interface.
- **FR7:** The system shall provide a natural-language summary of the returned dataset.
- **FR8:** If PostgreSQL returns a syntax or schema error, the system shall provide the error to the LLM and allow a maximum of one retry before returning an error to the user.

## 5. Non-Functional Requirements

- **NFR1 — Security:** The application shall only execute validated `SELECT` queries. The database connection should also use a PostgreSQL role with read-only permissions.
- **NFR2 — Performance:** SQL execution shall timeout after 5 seconds to prevent runaway queries.
- **NFR3 — Resource Safety:** Result payloads shall be capped at 100 rows to prevent excessive memory usage and UI performance issues.
- **NFR4 — Resilience:** LLM failures, API timeouts, database errors, and invalid generated SQL shall be handled gracefully and returned as standardized JSON errors without crashing the server.