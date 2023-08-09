from decouple import config


class EnvironmentSettings:
    def __init__(self):
        self.environment = self.get_environment()
        self.database_settings = self.load_database_settings()
        self.secret_key = self.load_secret_key()
        self.debug = self.load_debug_settings()

    def get_environment(self):
        return config("ENVIRONMENT", default="development")

    def is_production(self):
        if self.environment == "production":
            return True

    def is_development(self):
        if self.environment == "development":
            return True

    def load_database_settings(self):
        if self.is_production():
            return {
                "host": config("PROD_DB_HOST"),
                "username": config("PROD_DB_USERNAME"),
                "password": config("PROD_DB_PASSWORD"),
                "database": config("PROD_DB_NAME"),
                "port": config("PROD_DB_PORT"),
            }
        elif self.is_development():
            return {
                "host": config("DEV_DB_HOST"),
                "username": config("DEV_DB_USERNAME"),
                "password": config("DEV_DB_PASSWORD"),
                "database": config("DEV_DB_NAME"),
                "port": config("DEV_DB_PORT"),
            }
        else:
            raise ValueError("Unknown environment.")

    def load_secret_key(self):
        if self.is_production():
            return config("SECRET_KEY_PROD")
        elif self.is_development():
            return config("SECRET_KEY_DEV")

    def load_debug_settings(self):
        if self.is_production():
            return config("DEBUG_PROD")
        elif self.is_development():
            return config("DEBUG_DEV")


# Usage
# """settings = EnvironmentSettings()

# if settings.is_production():
#     print("Running in production mode.")
#     print("Database settings:", settings.database_settings)
#     print("Hosts settings:", settings.hosts_settings)
#     print("Django settings:", settings.django_settings)
# elif settings.is_development():
#     print("Running in development mode.")
#     print("Database settings:", settings.database_settings)
#     print("Hosts settings:", settings.hosts_settings)
#     print("Django settings:", settings.django_settings)
# else:
#     print("Unknown environment.")"""
