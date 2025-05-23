import psycopg2

conn = psycopg2.connect(
    dbname="odoo18",
    user="caernations",
    password="1771311979",
    host="localhost"
)
conn.autocommit = True
cursor = conn.cursor()

# Find menus
cursor.execute("""
SELECT m.id, m.name, d.name as external_id, m.parent_id
FROM ir_ui_menu m
LEFT JOIN ir_model_data d ON (d.model = 'ir.ui.menu' AND d.res_id = m.id)
WHERE m.name LIKE '%Project%' OR d.name LIKE '%project%'
ORDER BY m.id;
""")

print("Project Menus:")
for menu in cursor.fetchall():
    print(f"ID: {menu[0]}, Name: {menu[1]}, External ID: {menu[2]}, Parent ID: {menu[3]}")

cursor.close()
conn.close()
