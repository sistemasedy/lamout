from odoo import fields, models


class LamoutCubage(models.Model):
    _name = "lamout.cubage"
    _description = "Cubicación/destajo por partida y proyecto"
    _order = "date desc, project_id"

    date = fields.Date(required=True, default=fields.Date.context_today)
    project_id = fields.Many2one("project.project", required=True, string="Proyecto")
    partida_id = fields.Many2one(
        "lamout.partida",
        required=True,
        string="Partida",
        domain=[("state", "=", "active")],
    )
    cantidad = fields.Float(required=True, string="Cantidad ejecutada")
    uom_name = fields.Char(
        string="Unidad",
        related="partida_id.uom_name",
        readonly=True,
        store=True,
        help="Heredada de la partida, solo lectura.",
    )
    monto_destajo = fields.Monetary(
        string="Monto destajo (RD$)", currency_field="currency_id"
    )
    currency_id = fields.Many2one(
        "res.currency", default=lambda self: self.env.company.currency_id
    )
    notes = fields.Text()
