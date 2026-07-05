from odoo import _, fields, models
from odoo.exceptions import ValidationError


class AccountMove(models.Model):
    _inherit = "account.move"

    lamout_proveedor_rnc = fields.Char(string="RNC Proveedor")
    lamout_ncf = fields.Char(string="NCF")
    lamout_tipo_comprobante = fields.Selection(
        [("b01", "B01 - Crédito Fiscal"), ("b02", "B02 - Consumo")],
        string="Tipo de Comprobante",
    )
    lamout_categoria_material = fields.Char(
        string="Categoría/Material",
        help="Categoría del material comprado tal como viene del Libro de Compras del "
        "Excel maestro (texto libre por ahora, no catálogo estructurado).",
    )

    def action_post(self):
        for move in self:
            if move.move_type in ("in_invoice", "in_refund"):
                for line in move.invoice_line_ids:
                    account = line.account_id
                    if (
                        account.account_type == "expense_direct_cost"
                        and not line.analytic_distribution
                    ):
                        raise ValidationError(
                            _(
                                "La línea '%s' usa la cuenta de costo directo '%s' y "
                                "debe tener distribución analítica de proyecto antes de "
                                "confirmar la factura (Regla de Oro Contable)."
                            )
                            % (
                                line.name or line.product_id.display_name,
                                account.display_name,
                            )
                        )
        return super().action_post()
