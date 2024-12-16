# Pet Management System

The Pet Management System is a Flask-based web application that allows users to manage people and their pets through a RESTful API.

This system provides functionality for creating and retrieving person records, as well as listing and deleting pet records. It utilizes a SQLite database for data persistence and follows a modular architecture with clear separation of concerns.

The application is designed with scalability and maintainability in mind, featuring a well-structured codebase that adheres to SOLID principles and employs dependency injection for improved testability and flexibility.

## Repository Structure

```
.
├── ex_pylint.py
├── init
│   └── schema.sql
├── run.py
└── src
    ├── controllers
    ├── errors
    ├── main
    │   ├── composer
    │   ├── routes
    │   └── server
    ├── models
    │   └── sqlite
    │       ├── entities
    │       ├── interfaces
    │       ├── repositories
    │       └── settings
    ├── validators
    └── views
        └── http_types
```

### Key Files:
- `run.py`: Entry point for the application
- `src/main/server/server.py`: Flask application setup and configuration
- `src/controllers/`: Contains controller interfaces and implementations
- `src/models/`: Defines database models and repositories
- `src/views/`: Handles HTTP request processing and response formatting

### Important Integration Points:
- Database Connection: `src/models/sqlite/settings/connection.py`
- API Routes: `src/main/routes/person_routes.py` and `src/main/routes/pets_routes.py`
- Error Handling: `src/errors/error_handler.py`

## Usage Instructions

### Installation

Prerequisites:
- Python 3.7+
- pip (Python package manager)

Steps:
1. Clone the repository:
   ```
   git clone <repository_url>
   cd pet-management-system
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

### Getting Started

1. Initialize the database:
   ```
   sqlite3 pet_management.db < init/schema.sql
   ```

2. Start the application:
   ```
   python run.py
   ```

The server will start running on `http://0.0.0.0:3000`.

### API Endpoints

1. Create a Person:
   ```
   POST /people
   Body: {
     "first_name": "John",
     "last_name": "Doe",
     "age": 30,
     "pet_id": 1
   }
   ```

2. Get a Person:
   ```
   GET /people/<person_id>
   ```

3. List Pets:
   ```
   GET /pets
   ```

4. Delete a Pet:
   ```
   DELETE /pets/<pet_name>
   ```

### Configuration

The application uses a SQLite database by default. To change the database configuration, modify the connection settings in `src/models/sqlite/settings/connection.py`.

### Testing

To run the tests, execute:
```
pytest
```

Note: Some tests are skipped by default due to database interactions. To run all tests, remove the `@pytest.mark.skip` decorators in the test files.

### Troubleshooting

1. Database Connection Issues:
   - Ensure the SQLite database file exists and has the correct permissions.
   - Check the database connection settings in `src/models/sqlite/settings/connection.py`.

2. API Errors:
   - For 400 Bad Request errors, verify the request payload matches the expected format.
   - For 404 Not Found errors, ensure the requested resource (person or pet) exists in the database.

3. Server Start-up Issues:
   - Verify that port 3000 is not in use by another application.
   - Check the console output for any error messages during start-up.

For detailed error logs, enable debug mode by setting the `FLASK_ENV` environment variable to `development`:
```
export FLASK_ENV=development
```

## Data Flow

The Pet Management System follows a typical MVC (Model-View-Controller) architecture for handling requests:

1. The client sends an HTTP request to one of the defined API endpoints.
2. The request is routed to the appropriate view function in `src/views/`.
3. The view function validates the input using validators in `src/validators/`.
4. The validated data is passed to the corresponding controller in `src/controllers/`.
5. The controller interacts with the repository in `src/models/sqlite/repositories/` to perform database operations.
6. The repository executes SQL queries using the SQLAlchemy ORM.
7. The result is passed back through the controller and view.
8. The view formats the response and sends it back to the client.

```
Client -> Route -> View -> Validator -> Controller -> Repository -> Database
        <-       <-      <-           <-           <-            <-
```

Note: Error handling is performed at each step, with custom exceptions being caught and formatted into appropriate HTTP responses.