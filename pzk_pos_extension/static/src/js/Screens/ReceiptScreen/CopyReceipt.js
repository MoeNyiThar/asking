odoo.define('point_of_sale.CopyReceipt', function(require) {
	'use strict';

	const PosComponent = require('point_of_sale.PosComponent');
	const Registries = require('point_of_sale.Registries');
	

	class CopyReceipt extends PosComponent {
		setup() {
			super.setup();
		}
	}
	
	CopyReceipt.template = 'CopyReceipt';
	Registries.Component.add(CopyReceipt);
	return CopyReceipt;

});