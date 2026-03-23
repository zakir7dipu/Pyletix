from core.database.seeder import Seeder
from app.models.User import User
from core.auth.auth_service import Hash

class DatabaseSeeder(Seeder):
    def run(self):
        # Create an admin user
        User.create(
            name="Admin User",
            email="admin@example.com",
            password=Hash.make("password123")
        )
        print("Initial data seeded.")
