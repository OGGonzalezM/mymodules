from odoo import models

class MinimalModel(model.Model):
	_name = 'tmodule.model'

class LessMinimalModel(model.Model):
	_name = 'tmodule.model2'

	name = fields.Char()
