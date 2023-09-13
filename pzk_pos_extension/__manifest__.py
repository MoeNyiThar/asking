{
	'name': 'Pzk Pos Extension',
	'version': '14.0.0',
	'category': 'Point of Sale',
	'author': 'Moe Nyi',
	'website': 'https://yourcompany.com',
	'depends': ['point_of_sale'],
	'data' : [
		'views/pos_assets_common.xml',
	],
	'qweb': [
		'pzk_pos_extension/static/src/xml/Screens/ReceiptScreen/ReceiptScreen.xml',
		'pzk_pos_extension/static/src/xml/Screens/ReceiptScreen/CopyReceipt.xml',
	],
	'installable': True,
	'auto_install': False
}

