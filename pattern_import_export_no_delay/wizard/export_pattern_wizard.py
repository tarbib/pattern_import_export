from odoo import models

class ExportPatternWizard(models.Model):
    _inherit = "export.pattern.wizard"

    def run(self):
        self = self.with_context(test_queue_job_no_delay=True)
        return super(ExportPatternWizard, self).run()
