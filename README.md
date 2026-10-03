# Merchant Service API

> 🚧 **Status: In Progress — Active Development**

A Python-based merchant payment service inspired by the core backend concepts behind payment platforms such as Paystack and Flutterwave.

This project is being built as a **backend-focused, project-based learning project**. The goal is to understand how merchant systems, payments, transactions, authentication, webhooks, balances, and payment security work together in a real backend application.

---

## 🚧 Current Status

**ACTIVE DEVELOPMENT**

This project is currently being built step-by-step.

Features will be implemented progressively rather than all at once.

> **Current stage:** Project setup

---

## 🎯 Project Goals

The service will eventually allow merchants to:

- Create and manage merchant accounts
- Authenticate securely
- Generate and use API keys
- Create payment requests
- Track customer payments
- View transaction history
- Verify transactions
- Receive payment webhooks
- Manage merchant balances
- Request withdrawals

---

## 🛠️ Planned Technology Stack

- **Python**
- **FastAPI**
- **PostgreSQL**
- **SQLAlchemy**
- **JWT Authentication**
- **REST API**
- **Docker**
- **Postman**
- **Git & GitHub**

The technology stack may evolve as the project develops.

---

## 🗺️ Development Roadmap

### 1. Project Setup
- [ ] Initialize Python project
- [ ] Create virtual environment
- [ ] Install dependencies
- [ ] Create FastAPI application
- [ ] Create `/health` endpoint

### 2. Merchant Registration
- [ ] Create merchant model
- [ ] Create registration endpoint
- [ ] Validate merchant information
- [ ] Hash passwords
- [ ] Save merchant to database

### 3. Authentication
- [ ] Merchant login
- [ ] Password verification
- [ ] JWT generation
- [ ] Protected routes
- [ ] Authentication middleware/dependency

### 4. API Keys
- [ ] Generate merchant API keys
- [ ] Secure API key storage
- [ ] API key authentication
- [ ] Merchant-specific access

### 5. Payments
- [ ] Create payment request
- [ ] Generate payment reference
- [ ] Store payment information
- [ ] Payment status management

### 6. Transactions
- [ ] Create transaction records
- [ ] Pending transactions
- [ ] Successful transactions
- [ ] Failed transactions
- [ ] Transaction history
- [ ] Transaction verification

### 7. Webhooks
- [ ] Create webhook endpoint
- [ ] Receive payment events
- [ ] Verify webhook authenticity
- [ ] Update transaction status
- [ ] Handle duplicate webhook events

### 8. Merchant Balance
- [ ] Calculate merchant balance
- [ ] Record incoming payments
- [ ] Record deductions
- [ ] Create ledger
- [ ] Balance history

### 9. Withdrawals
- [ ] Withdrawal request
- [ ] Withdrawal status
- [ ] Withdrawal records
- [ ] Basic withdrawal validation

### 10. Security
- [ ] Input validation
- [ ] Password hashing
- [ ] JWT security
- [ ] API key security
- [ ] Webhook verification
- [ ] Idempotency
- [ ] Rate limiting
- [ ] Secure error handling

### 11. Testing
- [ ] API testing with Postman
- [ ] Unit tests
- [ ] Authentication tests
- [ ] Payment tests
- [ ] Webhook tests
- [ ] Error handling tests

### 12. Deployment
- [ ] Dockerize application
- [ ] Configure production environment
- [ ] PostgreSQL production setup
- [ ] Deploy API
- [ ] Production testing

---

## 🏗️ Planned Architecture

```text
                    ┌───────────────┐
                    │   Customer    │
                    └───────┬───────┘
                            │
                         Payment
                            │
                            ▼
                    ┌───────────────┐
                    │ Payment Layer │
                    └───────┬───────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   Merchant API      │
                 │      FastAPI        │
                 └──────────┬──────────┘
                            │
             ┌──────────────┼──────────────┐
             │              │              │
             ▼              ▼              ▼
        Merchants       Payments      Transactions
             │              │              │
             └──────────────┼──────────────┘
                            │
                            ▼
                    ┌───────────────┐
                    │  PostgreSQL   │
                    └───────────────┘
```

---

## 📁 Planned Project Structure

```text
merchant-service/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── auth.py
│   │
│   └── routes/
│       ├── merchants.py
│       ├── payments.py
│       └── transactions.py
│
├── tests/
│
├── .env
├── .gitignore
├── requirements.txt
├── Dockerfile
└── README.md
```

> The structure may change as the project grows.

---

## 🔄 Development Philosophy

This project is being developed **incrementally**.

Instead of building everything at once, each feature will be:

```text
Understand
    ↓
Design
    ↓
Implement
    ↓
Test
    ↓
Fix
    ↓
Move to the next feature
```

The focus is not only on getting the API working, but understanding **why each component exists and how the pieces communicate**.

---

## Project Status

🚧 **Status: In Progress — Active Development**

### Completed

- [x] Project initialization with `uv`
- [x] FastAPI application setup
- [x] Environment configuration with Pydantic Settings
- [x] PostgreSQL database setup
- [x] SQLAlchemy database configuration
- [x] Alembic migration setup
- [x] Merchant database model
- [x] Merchant registration endpoint
- [x] Email validation
- [x] Password hashing with Argon2
- [x] Duplicate merchant email protection
- [x] Merchant login endpoint
- [x] Password verification
- [x] JWT access token generation
- [x] JWT secret configuration

### Current API Endpoints

| Method | Endpoint | Purpose | Status |
|---|---|---|---|
| GET | `/health` | Health check | ✅ |
| POST | `/api/merchants/register` | Register merchant | ✅ |
| POST | `/api/auth/login` | Authenticate merchant | ✅ |

### Current Architecture

```text
Client
  │
  ├── POST /api/merchants/register
  │       ↓
  │   Validate merchant data
  │       ↓
  │   Hash password
  │       ↓
  │   PostgreSQL
  │
  └── POST /api/auth/login
          ↓
      Find merchant
          ↓
      Verify password
          ↓
      Generate JWT
          ↓
      Access Token
```

### Security Implemented

- Passwords are never stored in plaintext.
- Passwords are hashed using Argon2.
- Merchant emails are protected by a unique database constraint.
- Login returns a generic error for invalid credentials.
- JWT authentication uses a configurable secret key.
- JWT access tokens have an expiration time.
- JWT signing uses HS256.

### Next Development Step

**JWT-Protected Routes**

The next stage is to build authentication middleware/dependencies that can:

1. Read the JWT from the request.
2. Validate the token signature.
3. Check token expiration.
4. Extract the merchant ID.
5. Load the authenticated merchant.
6. Protect merchant-only endpoints.

After that, we will move into **API key generation and merchant API authentication**.

---

## ⚠️ Disclaimer

This project is primarily a **learning and development project**.

It is not intended to process real customer funds or replace a regulated payment processor without the appropriate security, compliance, licensing, infrastructure, and financial controls.

---

## 📌 Development Status

**🟢 ACTIVE — Currently under development**

This README will be updated as new components are completed.