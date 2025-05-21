from odoo import models, fields, api

class Project(models.Model):
    _inherit = 'project.project'
    
    document_ids = fields.One2many('project.document', 'project_id', string='Documents')

class ProjectTask(models.Model):
    _inherit = 'project.task'
    
    document_ids = fields.One2many('project.document', 'task_id', string='Documents')

class Document(models.Model):
    _name = 'project.document'
    _description = 'Project Document'
    
    _check_company_auto = False
    
    name = fields.Char(string='Document Name', required=True)
    description = fields.Text(string='Description')
    project_id = fields.Many2one('project.project', string='Project', ondelete='cascade', check_company=False)
    task_id = fields.Many2one('project.task', string='Task', ondelete='cascade', check_company=False)
    file = fields.Binary(string='Document File', attachment=True, required=True)
    filename = fields.Char(string='Filename')
    date_uploaded = fields.Datetime(string='Upload Date', default=fields.Datetime.now)
    user_id = fields.Many2one('res.users', string='Uploaded By', default=lambda self: self.env.user)
    company_id = fields.Many2one('res.company', string='Company', required=False, default=False, index=True)
    document_type = fields.Selection([
        ('requirements', 'Requirements'),
        ('design', 'Design Document'),
        ('user_manual', 'User Manual'),
        ('technical', 'Technical Documentation'),
        ('other', 'Other'),
    ], string='Document Type', default='other', required=True)
    notes = fields.Html(string='Notes')
    
    @api.model
    def default_get(self, fields_list):
        res = super(Document, self).default_get(fields_list)
        if 'company_id' in res:
            res.pop('company_id')
        return res
