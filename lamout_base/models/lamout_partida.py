from odoo import fields, models


class LamoutPartida(models.Model):
    _name = "lamout.partida"
    _description = "Partida CBS (cubicación/destajo)"
    _order = "capitulo, code"

    code = fields.Char(required=True, string="Código")
    name = fields.Char(required=True, string="Descripción")
    capitulo = fields.Char(string="Capítulo")
    subcapitulo = fields.Char(string="Subcapítulo")
    uom_name = fields.Char(
        string="Unidad",
        help="Unidad de medida tal como viene del Excel maestro (m2, m3, ml, "
        "unidad, etc.) — texto libre, no uom.uom de Odoo, para no forzar "
        "conversión en esta etapa.",
    )
    state = fields.Selection(
        [("active", "Activa"), ("inactive", "Inactiva")],
        default="active",
        string="Estado",
    )
    active = fields.Boolean(default=True)
