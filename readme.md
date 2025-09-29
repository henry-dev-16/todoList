# Todo Application - FastAPI + PostgreSQL

A RESTful API for task management built with FastAPI, PostgreSQL, and SQLAlchemy. Features user authentication with JWT tokens and comprehensive task management capabilities.

## 🚀 Features

- **User Authentication**: JWT-based authentication system
- **Task Management**: Create, read, update, and delete tasks
- **Task Status**: Customizable task status with colors
- **User Management**: User registration and profile management
- **Secure Password Handling**: Bcrypt hashing for password security
- **Auto-generated API Documentation**: Interactive API docs via Swagger UI

## 📋 Prerequisites

- Python 3.10+
- PostgreSQL (or Docker for containerized PostgreSQL)
- pip package manager

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd Todo_FastApi_React_SQL
```

### 2. Create a virtual environment

```bash
python3.10 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up PostgreSQL Database

#### Option A: Using Docker (Recommended)

```bash
docker run --name todo-postgres \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -e POSTGRES_DB=todoList \
  -p 5433:5432 \
  -d postgres:latest
```

#### Option B: Local PostgreSQL
- Create a database named `todoList`
- Update connection string in `backend/config/db.py`

### 5. Configure Environment Variables

Create a `.env` file in the backend directory:

```env
DATABASE_URL=postgresql+psycopg2://postgres:mysecretpassword@localhost:5433/todoList
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## 🚀 Running the Application

### Development Server

```bash
cd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Production Server

```bash
uvicorn backend.main:app --host 0.0.0.0 --port 8000
```

## 📚 API Documentation

Once the server is running, you can access:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🔑 API Endpoints

### Authentication
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/login` | User login | No |

### Users
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/user` | Register new user | No |
| GET | `/users/me` | Get current user info | Yes |

### Tasks
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/todos` | Get user's tasks | Yes |
| POST | `/todos` | Create new task | Yes |

## 📁 Project Structure

```
backend/
├── config/
│   └── db.py              # Database configuration
├── models/
│   ├── users.py           # User model
│   └── task.py            # Task and TaskStatus models
├── routes/
│   ├── auth.py            # Authentication endpoints
│   ├── user.py            # User endpoints
│   └── task.py            # Task endpoints
├── schemas/
│   ├── users.py           # Pydantic schemas for users
│   └── task.py            # Pydantic schemas for tasks
├── utils/
│   ├── auth.py            # JWT utilities
│   └── utils.py           # Password hashing utilities
└── main.py                # FastAPI application
```

## 🔐 Authentication Flow

1. **Register**: Create a new user account via `/user` endpoint
2. **Login**: Authenticate with username/password via `/login` endpoint
3. **Token**: Receive JWT token upon successful login
4. **Authorized Requests**: Include token in Authorization header as `Bearer <token>`

### Example Request with Authentication:

```bash
curl -X GET "http://localhost:8000/todos" \
  -H "Authorization: Bearer your-jwt-token-here"
```

## 📊 Database Schema

### Users Table
- `id`: Primary key
- `username`: Unique username
- `email`: Unique email address
- `password`: Hashed password
- `created_at`: Timestamp
- `updated_at`: Timestamp

### Tasks Table
- `id`: Primary key
- `title`: Task title (unique)
- `description`: Task description
- `assigned_to`: Foreign key to Users
- `status_id`: Foreign key to TaskStatus
- `due_date`: Task deadline
- `create_at`: Timestamp
- `update_at`: Timestamp

### Task Status Table
- `id`: Primary key
- `name`: Status name (unique)
- `description`: Status description
- `color`: HEX color for UI
- `create_at`: Timestamp
- `update_at`: Timestamp

## 🧪 Testing

```bash
# Run tests (when implemented)
pytest tests/
```

## 🐛 Common Issues

### Database Connection Error
- Ensure PostgreSQL is running on port 5433
- Check database credentials in `backend/config/db.py`
- Verify database `todoList` exists

### JWT Token Invalid
- Check if token has expired (default: 30 minutes)
- Ensure SECRET_KEY matches between sessions

## 🚧 Roadmap

- [ ] Add React frontend
- [ ] Implement task update and delete endpoints
- [ ] Add task filtering and search
- [ ] Implement task categories
- [ ] Add email notifications
- [ ] Implement task sharing between users
- [ ] Add unit and integration tests
- [ ] Implement rate limiting
- [ ] Add Docker Compose for full stack deployment

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- Your Name - Initial work

## 🙏 Acknowledgments

- FastAPI documentation
- SQLAlchemy documentation
- PostgreSQL community
