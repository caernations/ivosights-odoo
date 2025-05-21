#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
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

# Clean up all references to our modules to ensure a fresh install
cursor.execute("""
-- Drop all tables related to our models
DROP TABLE IF EXISTS project_document CASCADE;

-- Delete references in the ir_model table
DELETE FROM ir_model WHERE model IN ('project.document', 'documentation.project', 'documentation.document');

-- Delete references in other tables
DELETE FROM ir_model_fields WHERE model IN ('project.document', 'documentation.project', 'documentation.document');
DELETE FROM ir_model_constraint WHERE model IN ('project.document', 'documentation.project', 'documentation.document');
DELETE FROM ir_model_relation WHERE model IN ('project.document', 'documentation.project', 'documentation.document');

-- Delete actions and menu items
DELETE FROM ir_ui_menu WHERE name = 'Documents' AND parent_id IN (SELECT id FROM ir_ui_menu WHERE name LIKE '%Project%');
DELETE FROM ir_actions WHERE name = 'Documents' AND res_model = 'project.document';
DELETE FROM ir_actions_act_window WHERE name = 'Documents' AND res_model = 'project.document';

-- Delete module reference
DELETE FROM ir_module_module WHERE name IN ('documentation', 'project_docs');
""")

# Show confirmation
print("Database cleanup completed successfully.")

# Close the connection
cursor.close()
conn.close()
