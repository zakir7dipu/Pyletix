# Zak Flet MVC Framework

Zak Flet is a professional, Laravel-inspired MVC framework for Python, built on top of the **Flet** UI toolkit and **SQLite**. It brings the elegant developer experience of modern PHP frameworks to the Python ecosystem, enabling the rapid creation of scalable desktop, web, and mobile applications.

## 🚀 Overview

The framework follows the **Model-View-Controller** pattern and provides a robust suite of tools for database management, authentication, security, and media processing. Its philosophy is to minimize boilerplate while maximizing developer productivity and code maintainability.

---

## ✨ Features

### 🏛️ Core Architecture
- **MVC Pattern**: Strict separation of concerns for clean, modular code.
- **Dynamic Configuration**: Full `.env` support for environment-specific settings.
- **Advanced Routing**: Regex-based path matching, HTTP-like verbs (`GET`, `POST`), and middleware support.

### 💾 Data & ORM
- **Eloquent-like ORM**: Active Record implementation with advanced relationships:
  - One-to-One, One-to-Many
  - Many-to-Many (Pivot tables)
  - Polymorphic relations
- **Eager & Lazy Loading**: Optimised data fetching to prevent N+1 query problems.
- **Soft Deletes**: Transparently handle deleted records without removing data.
- **Migration System**: Expressive schema builder with `up()` and `down()` support and rollbacks.

### 🔐 Security & Auth
- **Strong Authentication**: Secure login/register with `bcrypt` hashing and session persistence.
- **RBAC (Role-Based Access Control)**: Granular permissions and roles with custom middleware and decorators.
- **Security Suite**: Built-in CSRF protection, input sanitization (`Bleach`), and Rate Limiting.
- **REST API**: Standardized JSON responses and **JWT-based** API authentication.

### 🛠️ Services & Utilities
- **CLI (manage.py)**: A powerful command-runner for scaffolding and database maintenance.
- **File & Image Processing**: Safe storage management and `Pillow`-powered image transformations.
- **Email & PDF**: Integrated SMTP mailer and professional PDF generation (`ReportLab`).
- **Notification System**: Built-in service for Toasts, Alerts, and Confirmation dialogs.
- **Date Utilities**: Human-readable time formatting powered by `Arrow`.

---

## 📥 Installation

### 1. Prerequisites
- Python 3.9 or higher
- [Flet CLI](https://flet.dev/docs/guides/python/install-flet/) installed (`pip install flet`)

### 2. Setup
```bash
# Clone the repository
git clone https://github.com/your-repo/zak-flet-framework.git
cd zak-flet-framework

# Install dependencies
pip install -r requirements.txt
# Core dependencies include: flet, bcrypt, PyJWT, Pillow, reportlab, arrow, bleach

# Setup environment
cp .env.example .env
```

### 3. Initialize Database
```bash
python manage.py migrate
python manage.py db:seed
```

---

## 🏃 Build & Launch

### Development Mode
Run the application directly with Python:
```bash
python main.py
```
Or use the Flet hot-reload runner:
```bash
flet run main.py
```

### Building for Production
The framework supports cross-platform builds via the Flet CLI:
```bash
# Build for Windows
flet build windows

# Build for Android (APK)
flet build apk

# Build for Web
flet build web
```

### Production Configuration
1. Update `.env`:
   - `APP_DEBUG=false`
   - `APP_ENV=production`
   - `DB_DATABASE=storage/database.sqlite`
2. **Deployment**: For Web, the application can be hosted as a static site or behind a Python server (Uvicorn/Gunicorn) to handle the backend logic.

---

## 📂 Project Structure

```text
app/
  controllers/    # Business logic
  models/         # Database models & relationships
  views/          # UI components & layouts
  services/       # External integrations (Mail, PDF)
  database/seeds/ # Sample data seeders
core/
  auth/           # Security & JWT logic
  database/       # Schema builder & ORM core
  router/         # Navigation & Request/Response logic
  storage/        # File system utilities
  utils/          # Date & Validation helpers
storage/          # Database files & logs
migrations/       # Database schema scripts
manage.py         # Framework CLI tool
main.py           # Application entry point
.env              # Configuration variables
```

---

## ⌨️ CLI Commands Usage

Generate components rapidly using the `manage.py` tool:

| Command | Usage | Description |
| :--- | :--- | :--- |
| `make:model` | `python manage.py make:model [Name]` | Create a new ORM model. |
| `make:controller` | `python manage.py make:controller [Name]` | Create a new BaseController. |
| `make:migration` | `python manage.py make:migration [Name]` | Create a new schema script. |
| `make:module` | `python manage.py make:module [Name]` | Generate Model, Controller, and Migration in one go. |
| `migrate` | `python manage.py migrate` | Run all pending migrations. |
| `migrate:rollback` | `python manage.py migrate:rollback` | Undo the last migration batch. |
| `db:seed` | `python manage.py db:seed` | Run the DatabaseSeeder. |

---

## 🗄️ ORM & Migration Usage

### Defining a Model
```python
from core.orm.model import BaseModel

class Post(BaseModel):
    table = 'posts'

    def user(self):
        from .User import User
        return self.belongs_to(User)
```

### Schema Builder
```python
def up():
    Schema.create('posts', lambda table: (
        table.id(),
        table.integer('user_id'),
        table.string('title'),
        table.timestamps()
    ))
```

---

## 🌐 REST API Usage

Enable JSON responses and prefix-based routing:

```python
# main.py
router.prefix("/api/v1")
router.get("/users", "UserResourceController@index")

# Controller
class UserResourceController(ResourceController):
    model = User
    
    @requires_jwt
    def index(self, request):
        return super().index(request)
```

---

## 🛡️ Security
- **Bcrypt**: All passwords are automatically hashed using salt.
- **XSS Protection**: Inputs can be sanitized via `Validation.sanitize()`.
- **JWT**: Secure token-based access for stateless API endpoints.
- **RBAC**: Protect routes using `@requires_role("admin")`.

---

## 💡 Best Practices
- **Naming**: Use `PascalCase` for Models/Controllers and `snake_case` for database fields/methods.
- **Controllers**: Keep them thin; move complex logic into Service classes under `app/services`.
- **Validation**: Always sanitize user input before database entry using `Validation.sanitize()`.

## 🔧 Troubleshooting
- **Database Locked**: Ensure no other process is holding a write-lock on `storage/database.sqlite`.
- **ImportErrors**: Ensure you are running from the project root and that `PYTHONPATH` includes the current directory.
- **Flet UI Not Updating**: Remember to call `page.update()` after modifying controls (already handled by most framework Response methods).

## 🚀 Future Improvements
- **JWT Refresh Tokens**: For long-lived API sessions.
- **WebSocket Integration**: Real-time push notifications.
- **Docker Support**: Containerized deployment for easy scaling.

## 📄 License
This framework is open-sourced software licensed under the **MIT license**.
