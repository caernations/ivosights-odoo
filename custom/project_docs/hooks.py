# Delete the hooks in database
def uninstall_hook(cr, registry):
    cr.execute("DELETE FROM ir_model WHERE model IN ('documentation.project', 'documentation.document')")
    cr.execute("DELETE FROM ir_model_fields WHERE model IN ('documentation.project', 'documentation.document')")
    cr.execute("DELETE FROM ir_model_relation WHERE model IN ('documentation.project', 'documentation.document')")
    cr.execute("DELETE FROM ir_model_constraint WHERE model IN ('documentation.project', 'documentation.document')")
    cr.execute("DELETE FROM ir_model_data WHERE model IN ('documentation.project', 'documentation.document')")
