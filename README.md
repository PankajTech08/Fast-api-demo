# Python Learning Project

A beginner-friendly Python project with a small FastAPI application.

## Project Structure

```text
python-learning/
├── src/
│   ├── __init__.py
│   ├── main.py              # FastAPI app entry point
│   ├── api/
│   │   ├── __init__.py
│   │   ├── demo.py          # Root, item, and fruit endpoints
│   │   └── users.py         # User endpoint
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py        # Application settings
│   └── models/
│       ├── __init__.py
│       ├── fruit.py         # Fruit response model
│       └── user.py          # User response model
├── tests/
│   └── test_api.py
├── requirements.txt
├── README.md
└── .gitignore
```

The models in this learning example are Pydantic request/response models; no
database is configured.

## Getting Started

### 1. Create and activate a virtual environment

**Windows PowerShell:**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Run the API

From the project root:

```bash
python -m uvicorn src.main:app --reload
```

Open <http://127.0.0.1:8000/docs> to explore the interactive API documentation.

### 4. Run tests

```bash
python -m pytest
```

## Example Endpoints

- `GET /` - welcome message
- `GET /items/{item_id}` - retrieve an item ID and optional query
- `POST /items/?name=book&price=12.5` - create an example item response
- `GET /fruit` - return an example fruit
- `GET /users/{user_id}` - return an example user

## Development

Add API routes under `src/api/`, shared application settings under `src/core/`,
and Pydantic models under `src/models/`.

## License

MIT
