"""
Configuration file for DB2 connection settings
Update these values according to your DB2 instance
"""

class Config:
    # DB2 Connection Settings
    DB2_HOST = 'localhost'
    DB2_PORT = '50000'
    DB2_DATABASE = 'SAMPLE'
    DB2_USER = 'db2user'
    DB2_PASSWORD = 'password'
    
    # JDBC Driver Settings
    DB2_DRIVER = 'com.ibm.db2.jcc.DB2Driver'
    DB2_JAR_PATH = 'path/to/db2jcc4.jar'  # Update with actual path
    
    # SSL Configuration
    USE_SSL = True
    SSL_TRUSTSTORE_PATH = 'path/to/truststore.jks'  # Path to SSL truststore
    SSL_TRUSTSTORE_PASSWORD = 'truststore_password'  # Truststore password
    
    # Flask Settings
    DEBUG = True
    HOST = '0.0.0.0'
    PORT = 5000
