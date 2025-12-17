# 🏥 Healthcare Backend API

A **clean, backend-first healthcare API** built to manage patient admissions, store data safely, and power frontend apps with reliable APIs.

Think of this as the **engine** behind a healthcare system — no UI fluff, just solid backend logic.

---

## ✨ What this project does

* 📋 Handles patient admissions and related data
* 🔐 Keeps healthcare data structured and secure
* 🔄 Exposes a clear API for frontend apps
* 📈 Built to scale and grow into analytics or AI features

---

## 🧠 How it’s built

* **Backend-first** design (business logic lives on the server)
* **GraphQL API** for flexible, predictable data access
* **Strong typing** to avoid bugs early
* Clear separation between data, logic, and API layers

---

## 🛠️ Tech Stack

* 🐍 **Python / Django**
* 🔗 **GraphQL (Graphene)**
* 🗄️ **PostgreSQL**
* 🧱 **Django ORM & migrations**

---

## 📂 Project Structure (simple & clean)

```text
patient_admission/
├── models.py     # database models
├── schema.py     # GraphQL queries & mutations
├── admin.py      # admin visibility
├── tests.py      # (ready for tests)
```

---

## 🧭 What’s coming next

This project is designed to grow by **adding domains**, not by bloating a single app.
Planned extensions include:

```text
appointments/   # scheduling & visit management
surgeons/       # staff & specialist access
billing/        # payments, invoices, insurance
notifications/  # reminders, alerts, follow-ups
auth/           # roles, permissions, access control
```

Each module will follow the same backend pattern:
**models → schema → business rules → database**.

---

## ▶️ Run it locally

```bash
python3 manage.py migrate
python3 manage.py runserver
```

Open GraphQL:

```
http://127.0.0.1:8000/graphql/
```

---

## 🔐 Security & Data Integrity

* No direct database access from clients
* All rules enforced at the API level
* Ready for role-based access control

---

## 🚀 Why this project matters

This repo shows:

* ✅ Real backend architecture
* ✅ PostgreSQL-backed data models
* ✅ Business rules enforced server-side
* ✅ Production-style API design

Perfect for **backend, health-tech, and AI-adjacent roles**.
