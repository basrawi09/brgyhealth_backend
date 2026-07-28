# Barangay Health Center Management System - Backend

## Technologies Used

- FastAPI
- SQLAlchemy
- MySQL
- JWT Authentication
- Python 3.13+

---

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Create `.env`

Example:

```env
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=localhost
DB_NAME=barangay_health

SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 6. Run the backend

```bash
uvicorn app.main:app --reload
```

Swagger API:

```
http://127.0.0.1:8000/docs
```