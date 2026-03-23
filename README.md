# Pyletix MVC Framework

**Pyletix** is a professional, **Laravel-inspired MVC framework** built for Python using **Flet** for the UI and **SQLite** for data persistence. It brings the power of Rapid Application Development (RAD) to the Flet ecosystem, providing developers with an expressive, clean, and batteries-included foundation for building cross-platform applications.

---

## 1. Project Overview
**Pyletix** is designed for developers who love the architectural elegance of Laravel or Django but want to leverage the modern, reactive UI capabilities of Flet. Its philosophy is based on "Developer Happiness":
- **Convention over Configuration**: Sensible defaults that get you started instantly.
- **Architectural Integrity**: A strict MVC pattern that keeps codebases maintainable.
- **Unified Experience**: One language (Python) for both backend logic and frontend UI.

---

## 2. Features Overview
- **MVC Architecture**: Native separation of Models, Views, and Controllers.
- **Dynamic Configuration**: Integrated `.env` management.
- **Custom ORM**: Eloquent-like Active Record with 1:1, 1:N, N:N, and Polymorphic relations.
- **Auth System**: Secure Register/Login, Password Reset, and Email Verification.
- **RBAC**: Powerful Role and Permission-based access control.
- **Advanced Routing**: Path parameters, prefixing, and middleware pipelines.
- **CLI Tool (manage.py)**: Artisan-like commands for scaffolding and migrations.
- **Migration System**: Reliable schema versioning with rollbacks.
- **REST API**: Built-in support for JSON responses and JWT Auth.
- **Storage & Media**: File uploads, validation, and Pillow-based image processing.
- **Email & PDF**: SMTP mailer with templates and ReportLab PDF generation.
- **Notifications**: Flash messages, SnackBars, and Tooltips.
- **Security**: CSRF protection, hashing, and XSS sanitization.
- **Utilities**: Human-readable dates and input validation.

---

## 3. Installation Guide

### Prerequisites
- Python 3.9+
- [Flet CLI](https://flet.dev/docs/guides/python/install-flet/) (`pip install flet`)

### Step-by-Step
1. **Clone the project:**
   ```bash
   git clone https://github.com/zakir7dipu/Pyletix.git
   cd Pyletix
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Setup environment:**
   ```bash
   cp .env.example .env
   ```
4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```
5. **Start Application:**
   ```bash
   python main.py
   ```

---

## 4. Project Structure
```text
app/
  controllers/    # Business logic handlers
  models/         # Database models & relationships
  views/          
    layouts/      # App-wide templates (Main, Auth)
    pages/        # Full-screen view definitions
    components/   # Reusable UI elements (Button, Card, Table)
    partials/     # Structural parts (Header, Sidebar, Footer)
    ui/           # Low-level UI utilities (Loaders, Validation)
  services/       # Theme, Notification, Mail, PDF services
  middlewares/    # Custom application middleware
core/
  auth/           # Auth engines & JWT
  database/       # Schema builder & Migration engine
  orm/            # Active Record core
  router/         # Route matching & Request/Response
  storage/        # File system facade
  utils/          # Date & Validation helpers
routes/
  inside.py       # Main application routes (Dashboard, etc.)
  api.py          # REST API route definitions
migrations/       # Database versioning files
storage/          # Database files & media uploads
manage.py         # Primary developer CLI
main.py           # App entry & Route registry
```

---

## 5. Configuration (.env)
**Pyletix** uses a `.env` file for all environment-specific settings.

**Sample .env:**
```ini
APP_NAME="Pyletix App"
APP_ENV=local
APP_KEY=base64:random_string
DB_CONNECTION=sqlite
DB_DATABASE=storage/database.sqlite

MAIL_HOST=smtp.mailtrap.io
MAIL_PORT=2525
MAIL_USERNAME=null
MAIL_PASSWORD=null
```

---

## 6. CLI Commands Usage

### Scaffolding
- **Create a Module (Model + Controller + Migration):**
  ```bash
  python manage.py make:module Post
  ```
  *Output: Model Post, Controller PostController, and migration created.*

- **Create a Model:**
  ```bash
  python manage.py make:model Category
  ```

### Database Management
- **Run Migrations:**
  ```bash
  python manage.py migrate
  ```
- **Rollback Last Batch:**
  ```bash
  python manage.py migrate:rollback
  ```
- **Run Seeders:**
  ```bash
  python manage.py db:seed
  ```

---

## 7. ORM Usage

### Basic CRUD
```python
# Create
user = User.create(name="John Doe", email="john@example.com")

# Read
user = User.find(1)
all_users = User.all()

# Update
user.update(name="John Smith")

# Delete
user.delete()
```

### Relationships

**One-to-Many:**
```python
# In User.py
def posts(self):
    return self.has_many(Post)

# Usage
user = User.find(1)
user_posts = user.posts 
```

**Many-to-Many:**
```python
# In User.py
def roles(self):
    return self.belongs_to_many(Role)
```

**Polymorphic:**
```python
# In Comment.py
def commentable(self):
    return self.morph_to()
```

---

## 8. Routing & Controllers

### Defining Routes
```python
# routes/inside.py
def register(router):
    router.get("/posts", "PostController@index")
    router.get("/posts/:id", "PostController@show")
    router.post("/posts", "PostController@store")
```

### Controller Example
```python
class PostController(BaseController):
    def index(self, request):
        posts = Post.all()
        return self.render([ft.Text("Posts"), ...])

    def show(self, request):
        post = Post.find(request.param('id'))
        return self.render([ft.Text(post.title)])
```

---

## 9. Authentication System

### Flow
1. **Registration**: `User.create()` with `Hash.make(password)`.
2. **Login**: `Auth.attempt(email, password)` verifies hash and sets session.
3. **Protection**: Use `@requires_auth` on controller methods.

```python
@requires_auth
def profile(self, request):
    user = Auth.user(self.page)
    return self.render([ft.Text(f"Welcome {user.name}")])
```

---

## 10. Role & Permission System

### Assignment
```python
role = Role.where('slug', 'admin').first()
user.roles().attach(role.id)
```

### Protection
```python
@requires_role('admin')
def delete_user(self, request):
    pass
```

---

## 11. REST API Usage

### API Routes
```python
# routes/api.py
def register(router):
    router.prefix("/api/v1")
    router.get("/products", "ProductController@api_index")
```

### JWT Auth
Endpoints are protected via `@requires_jwt`.
```python
@requires_jwt
def api_index(self, request):
    # request.user_id is populated from token
    return self.json(Product.all())
```

---

## 12. File & Image Handling

### Upload & Validation
```python
from core.storage.file_system import FileSystem
from core.utils.validation import Validation

content = request.file('avatar')
if Validation.validate_size(content, max_mb=2):
    FileSystem.put("storage/uploads/avatar.png", content)
```

### Image Processing
```python
from core.image.image_processor import ImageProcessor

ImageProcessor.resize("source.png", "thumb.png", width=128, height=128)
```

---

## 13. Email System

### Sending Emails
```python
from core.mail.mailer import Mailer

Mailer.send(
    to="user@example.com",
    subject="Welcome!",
    body="<h1>Thanks for joining</h1>",
    is_html=True
)
```

---

## 14. PDF Generation

### Example: Invoice
```python
from core.pdf.pdf_generator import PDFGenerator

PDFGenerator.generate(
    path="storage/reports/invoice_1.pdf",
    title="Invoice #001",
    content_lines=["Item 1: $10", "Item 2: $20", "Total: $30"]
)
```

---

## 15. Notifications System

**Pyletix** provides a `NotificationService` for consistent user feedback.

### Usage
```python
from app.services.notification_service import NotificationService

notifications = NotificationService(self.page)

# Show a snackbar toast
notifications.toast("Saved successfully!", bgcolor=ft.colors.GREEN)

# Show a modal alert
notifications.alert("Warning", "This action is irreversible.")

# Show a confirmation dialog
notifications.confirm(
    "Delete Post", 
    "Are you sure?", 
    on_confirm=lambda: print("Confirmed!")
)
```

---

## 16. UI Components
The framework includes a comprehensive library of atomic UI components in `app/views/components`.

### Reusable Elements
- **FlexButton**: A modern, responsive button with built-in loading states.
- **Input**: Styled text fields with icon support and validation hooks.
- **Card**: Elevated container for grouping information.
- **Table**: Dynamic data tables with heading and row support.
- **Modal**: Managed popups for alerts and confirmations.
- **Navbar & Sidebar**: Structural components for main application navigation.

### Structural Sections (Partials)
- **Header**: Top navigation bar with branding and theme toggle.
- **Sidebar**: Mobile-friendly navigation drawer.
- **Footer**: Constant site footer.

### UI Utilities
- **Loader**: Centered activity indicators.
- **Validation**: Helper for displaying inline form errors.

---

## 16. Middleware

### Creating Middleware
```python
def logging_middleware(func):
    def wrapper(self, request, *args, **kwargs):
        print(f"Request to {request.page.route}")
        return func(self, request, *args, **kwargs)
    return wrapper
```

---

## 17. Security
- **Hashing**: Bcrypt for all passwords.
- **XSS**: Automatic sanitization via `bleach` in `Validation.sanitize()`.
- **CSRF**: Token-based validation for state-changing requests.
- **Rate Limiting**: Throttling login attempts after 5 failures.

---

## 18. Example Application
A full `Post` CRUD module is included by default.
1. **Login** to the dashboard.
2. Navigate to `/posts` to see the list.
3. Click **Add** to create a post (requires Auth).
4. The post is saved with your `user_id` automatically via the `PostController`.

---

## 19. Best Practices
- **Thin Controllers**: Move complex business logic to Services.
- **Eager Loading**: Use `.with_('relation')` to avoid N+1 queries.
- **Validation**: Use the `Validation` utility for all user-provided data.
- **Naming**: `UserController` (PascalCase), `user_id` (snake_case).

---

## 20. Troubleshooting
- **Migration Error**: If a migration fails, standard SQLite constraints or schema syntax are usually the cause. Check the generated SQL.
- **Session Lost**: Ensure `page.session` is not manually cleared.
- **Pillow Errors**: Ensure binary dependencies for Image processing are installed on your OS.

---

## 21. Future Improvements
- **WebSocket support** for real-time Flet updates.
- **Docker** support for containerized deployment.
- **Queue System** for background email/PDF jobs.

---

## 22. View Architecture
**Pyletix** implements a structured View system inspired by modern component-based frameworks.

### The Rendering Pipeline
1. **Controller**: Receives the request and calls `self.render(content, layout)`.
2. **Layout**: A base template (e.g., `MainLayout`) that defines the scaffolding (Navbar, Sidebar).
3. **Page**: A specific view (e.g., `DashboardPage`) that is injected into the Layout's content slot.
4. **Components**: The building blocks (Buttons, Inputs) used inside Pages.

### Custom Layout Example
```python
from app.views.layouts.base import BaseLayout

class CustomLayout(BaseLayout):
    def render(self, content):
        return [
            ft.AppBar(title=ft.Text(self.title)),
            ft.Container(content=content, expand=True)
        ]
```

---

## 23. Theme Management System
Pyletix includes a native, persistent Dark/Light mode system managed via `ThemeService`.

### Features
- **Persistence**: User theme preference is saved in the session store.
- **Automatic Scaling**: Standard components use "surface" and "on_surface" tokens to adjust automatically.
- **Toggle**: Integrated button in the `Navbar` for seamless switching.

### Manual Theme Access
```python
from app.services.theme_service import ThemeService

# Toggle theme programmatically
ThemeService.toggle(page)

# Load saved theme (called automatically in main.py)
ThemeService.load(page)
```

---

## 24. License
The **Pyletix** Framework is open-sourced software licensed under the **MIT license**.
