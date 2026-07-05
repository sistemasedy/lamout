from odoo import api, fields, models


class LamoutAttendance(models.Model):
    _name = "lamout.attendance"
    _description = "Asistencia diaria de obrero por proyecto"
    _order = "date desc, project_id"

    date = fields.Date(required=True, default=fields.Date.context_today)
    project_id = fields.Many2one("project.project", required=True, string="Proyecto")
    worker_id = fields.Many2one("lamout.worker", required=True, string="Obrero")
    asistencia = fields.Selection(
        [("0", "Ausente (0)"), ("0.5", "Medio día (0.5)"), ("1", "Día completo (1)")],
        required=True,
        default="1",
        string="Asistencia",
    )
    comida = fields.Monetary(
        string="Comida (RD$)",
        currency_field="currency_id",
        help="Precargado desde el catálogo del obrero, editable libremente en este "
        "registro sin afectar el valor sugerido del catálogo.",
    )
    currency_id = fields.Many2one(
        "res.currency", default=lambda self: self.env.company.currency_id
    )
    notes = fields.Text()

    _sql_constraints = [
        (
            "unique_worker_project_date",
            "unique(worker_id, project_id, date)",
            "Ya existe un registro de asistencia para este obrero, proyecto y fecha.",
        )
    ]

    @api.onchange("worker_id")
    def _onchange_worker_id(self):
        for rec in self:
            if rec.worker_id:
                rec.comida = rec.worker_id.comida_sugerida
