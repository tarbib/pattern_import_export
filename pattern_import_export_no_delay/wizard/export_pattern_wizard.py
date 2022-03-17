from odoo import models

class ExportPatternWizard(models.Model):
    _inherit = "export.pattern.wizard"

    def run(self):
        return super().with_context(test_queue_job_no_delay=True).run()
