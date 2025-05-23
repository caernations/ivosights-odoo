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

print("Starting deep cleanup of documentation module references...")

# identify and remove all menu items and actions that reference the old models
cursor.execute("""
DELETE FROM ir_ui_menu WHERE action LIKE '%documentation.project%' OR action LIKE '%documentation.document%';
DELETE FROM ir_act_window WHERE res_model IN ('documentation.project', 'documentation.document');
DELETE FROM ir_act_window_view WHERE view_id IN (SELECT id FROM ir_ui_view WHERE model IN ('documentation.project', 'documentation.document'));
""")
print("Removed menu items and actions")

# Remove views associated with the old models
cursor.execute("""
DELETE FROM ir_ui_view WHERE model IN ('documentation.project', 'documentation.document');
""")
print("Removed views")

# Remove fields that reference the old models
cursor.execute("""
DELETE FROM ir_model_fields WHERE model IN ('documentation.project', 'documentation.document') 
   OR relation IN ('documentation.project', 'documentation.document');
""")
print("Removed model fields")

# Remove model data that references these models
cursor.execute("""
DELETE FROM ir_model_data WHERE model IN ('ir.model', 'ir.model.fields', 'ir.ui.view', 'ir.actions.act_window')
   AND res_id IN (
       SELECT id FROM ir_model WHERE model IN ('documentation.project', 'documentation.document')
       UNION
       SELECT id FROM ir_model_fields WHERE model IN ('documentation.project', 'documentation.document')
       UNION
       SELECT id FROM ir_ui_view WHERE model IN ('documentation.project', 'documentation.document')
       UNION
       SELECT id FROM ir_act_window WHERE res_model IN ('documentation.project', 'documentation.document')
   );
""")
print("Removed model data")

#Remove model constraints and relations
cursor.execute("""
DELETE FROM ir_model_constraint WHERE model IN (
    SELECT id FROM ir_model WHERE model IN ('documentation.project', 'documentation.document')
);
DELETE FROM ir_model_relation WHERE model IN (
    SELECT id FROM ir_model WHERE model IN ('documentation.project', 'documentation.document')
);
""")
print("Removed constraints and relations")

# Delete the models
cursor.execute("""
DELETE FROM ir_model WHERE model IN ('documentation.project', 'documentation.document');
""")
print("Removed models")

cursor.execute("""
DELETE FROM ir_module_module WHERE name = 'documentation';
UPDATE ir_module_module SET state = 'uninstalled' WHERE name = 'project_docs';
""")
print("Updated module state")

print("Database cleanup completed successfully.")
print("Now restart Odoo and install the module again.")


cursor.close()
conn.close()
