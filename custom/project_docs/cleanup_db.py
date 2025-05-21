import psycopg2

conn = psycopg2.connect(
    dbname="odoo18",
    user="caernations",
    password="1771311979",
    host="localhost"
)
conn.autocommit = True
cursor = conn.cursor()

# Delete old model
cursor.execute("""
DELETE FROM ir_model WHERE model IN ('documentation.project', 'documentation.document');
DELETE FROM ir_model_fields WHERE model IN ('documentation.project', 'documentation.document');
DELETE FROM ir_model_constraint WHERE model IN ('documentation.project', 'documentation.document');
DELETE FROM ir_model_relation WHERE model IN ('documentation.project', 'documentation.document');
""")

print("Database cleanup completed successfully.")

cursor.close()
conn.close()
