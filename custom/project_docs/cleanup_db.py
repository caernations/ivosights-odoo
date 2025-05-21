#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname="odoo18",
    user="caernations",
    password="1771311979",
    host="localhost"
)
conn.autocommit = True
cursor = conn.cursor()

# Delete old model references that might be causing conflicts
cursor.execute("""
DELETE FROM ir_model WHERE model IN ('documentation.project', 'documentation.document');
DELETE FROM ir_model_fields WHERE model IN ('documentation.project', 'documentation.document');
DELETE FROM ir_model_constraint WHERE model IN ('documentation.project', 'documentation.document');
DELETE FROM ir_model_relation WHERE model IN ('documentation.project', 'documentation.document');
""")

# Show confirmation
print("Database cleanup completed successfully.")

# Close the connection
cursor.close()
conn.close()
