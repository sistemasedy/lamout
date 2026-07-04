from odoo import fields, models


class Project(models.Model):
    _inherit = "project.project"

    lamout_code = fields.Char(
        string="Código Lamout",
        help="Código corto de 2-3 letras usado en analítica y reportes (ej. VE, YM, BM, VC).",
    )
