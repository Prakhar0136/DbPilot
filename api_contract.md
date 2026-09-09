# API Documentation

## Base URL
`http://localhost:8000/api`

## POST `/query`
Processes a natural language question, executes the corresponding SQL, and returns the result.

### Request Payload
**Headers:** `Content-Type: application/json`

```json
{
  "question": "Who are our top 5 customers by total spending this year?"
}