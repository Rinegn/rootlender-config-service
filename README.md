# RootLender Config Service

## Overview

The RootLender Config Service is a lightweight FastAPI microservice that centralizes
environment configuration and feature flags for the RootLender / PeerLink platform.

Its purpose is to eliminate configuration drift, reduce startup failures, and provide
a single source of truth for runtime settings across backend services.

This service is intentionally:
- Read-only
- Stateless
- Database-free

---

## Responsibilities

This service is responsible for:
- Loading and validating required environment variables
- Exposing non-sensitive configuration values
- Managing feature flags used by other services
- Failing fast when configuration is invalid

This service does NOT:
- Handle authentication
- Manage users or loans
- Store secrets
- Persist data

---

## Tech Stack

- Python 3.11+
- FastAPI
- Pydantic v2
- python-dotenv
- Uvicorn

---

## Project Structure

