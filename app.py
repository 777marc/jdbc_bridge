from flask import Flask, jsonify
from sqlalchemy import create_engine, text
from sqlalchemy.pool import NullPool
import jaydebeapi

app = Flask(__name__)

# DB2 connection configuration
DB2_HOST = 'localhost'
DB2_PORT = '50000'
DB2_DATABASE = 'SAMPLE'
DB2_USER = 'db2user'
DB2_PASSWORD = 'password'
DB2_DRIVER = 'com.ibm.db2.jcc.DB2Driver'
DB2_JAR_PATH = 'path/to/db2jcc4.jar'  # Update with actual path to DB2 JDBC driver

# SSL Configuration
USE_SSL = True
SSL_TRUSTSTORE_PATH = 'path/to/truststore.jks'  # Path to SSL truststore
SSL_TRUSTSTORE_PASSWORD = 'truststore_password'  # Truststore password

# Create custom creator function for SQLAlchemy using JayDeBeApi
def creator():
    # Build JDBC URL with SSL parameters
    jdbc_url = f'jdbc:db2://{DB2_HOST}:{DB2_PORT}/{DB2_DATABASE}'
    
    if USE_SSL:
        jdbc_url += ':sslConnection=true;'
        jdbc_url += f'sslTrustStoreLocation={SSL_TRUSTSTORE_PATH};'
        jdbc_url += f'sslTrustStorePassword={SSL_TRUSTSTORE_PASSWORD};'
    
    conn = jaydebeapi.connect(
        DB2_DRIVER,
        jdbc_url,
        [DB2_USER, DB2_PASSWORD],
        DB2_JAR_PATH
    )
    return conn

# Create SQLAlchemy engine with JayDeBeApi
engine = create_engine(
    'sqlite://',  # Dummy URL - actual connection handled by creator
    creator=creator,
    poolclass=NullPool,
    echo=True
)

@app.route('/db_test', methods=['GET'])
def db_test():
    """Test route to verify DB2 connection using JayDeBeApi and SQLAlchemy"""
    try:
        with engine.connect() as connection:
            # Execute a simple query to test connection
            result = connection.execute(text("SELECT CURRENT TIMESTAMP FROM SYSIBM.SYSDUMMY1"))
            row = result.fetchone()
            
            return jsonify({
                'status': 'success',
                'message': 'Database connection successful',
                'timestamp': str(row[0])
            }), 200
            
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Database connection failed: {str(e)}'
        }), 500

@app.route('/', methods=['GET'])
def home():
    """Home route"""
    return jsonify({
        'message': 'Flask DB2 JDBC Bridge App',
        'routes': {
            '/': 'Home',
            '/db_test': 'Test DB2 connection'
        }
    }), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
