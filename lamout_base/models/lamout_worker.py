from odoo import fields, models


class LamoutWorker(models.Model):
    _name = "lamout.worker"
    _description = "Obrero de Construcciones Lamout"
    _order = "name"

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
    cargo = fields.Char(string="Cargo")
    jornal = fields.Monetary(string="Jornal (RD$)", currency_field="currency_id")
    comida_sugerida = fields.Monetary(
        string="Comida sugerida (RD$)",
        currency_field="currency_id",
        help="Valor por defecto sugerido. Editable libremente en cada registro de "
        "asistencia/nómina — no es un valor forzado.",
    )
    currency_id = fields.Many2one(
        "res.currency", default=lambda self: self.env.company.currency_id
    )
    notes = fields.Text()
