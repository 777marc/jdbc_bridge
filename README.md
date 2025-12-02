# Flask DB2 JDBC Bridge App

A Flask application that connects to DB2 database using JayDeBeApi and SQLAlchemy.

## Prerequisites

1. Python 3.8+
2. Java Runtime Environment (JRE) installed
3. DB2 JDBC driver (db2jcc4.jar)

## Installation

1. Install required packages:

```bash
pip install -r requirements.txt
```

2. Download DB2 JDBC driver:

   - Download `db2jcc4.jar` from IBM DB2 JDBC Driver
   - Update the `DB2_JAR_PATH` in `config.py` with the actual path

3. Update database connection settings in `config.py`:
   - DB2_HOST
   - DB2_PORT
   - DB2_DATABASE
   - DB2_USER
   - DB2_PASSWORD

## Usage

Run the Flask application:

```bash
python app.py
```

The app will start on `http://localhost:5000`

## Routes

- `GET /` - Home route with API information
- `GET /db_test` - Test DB2 database connection

## Testing

Test the DB2 connection:

```bash
curl http://localhost:5000/db_test
```

Expected response on success:

```json
{
  "status": "success",
  "message": "Database connection successful",
  "timestamp": "2025-12-02 12:34:56.789"
}
```

## Notes

- JayDeBeApi uses JPype to bridge Python and Java
- The connection uses NullPool to avoid connection pooling issues with JDBC
- Make sure the DB2 JDBC driver path is correctly set
- Ensure Java is installed and accessible in your system PATH
