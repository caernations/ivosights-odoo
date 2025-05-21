import sys
import psycopg2

conn = psycopg2.connect(
    dbname="odoo18",
    user="caernations",
    password="1771311979",
    host="localhost"
)
conn.autocommit = True
cursor = conn.cursor()

# Clean database
cursor.execute("""
DROP TABLE IF EXISTS project_document CASCADE;

DELETE FROM ir_model WHERE model IN ('project.document', 'documentation.project', 'documentation.document');

DELETE FROM ir_model_fields WHERE model IN ('project.document', 'documentation.project', 'documentation.document');
DELETE FROM ir_model_constraint WHERE model IN ('project.document', 'documentation.project', 'documentation.document');
DELETE FROM ir_model_relation WHERE model IN ('project.document', 'documentation.project', 'documentation.document');

DELETE FROM ir_ui_menu WHERE name = 'Documents' AND parent_id IN (SELECT id FROM ir_ui_menu WHERE name LIKE '%Project%');
DELETE FROM ir_actions WHERE name = 'Documents' AND res_model = 'project.document';
DELETE FROM ir_actions_act_window WHERE name = 'Documents' AND res_model = 'project.document';

DELETE FROM ir_module_module WHERE name IN ('documentation', 'project_docs');
""")

# Show confirmation
print("Database cleanup completed successfully.")

cursor.close()
conn.close()
