import frappe


def execute():
    if not frappe.db.exists('Custom Script', 'Expense Claim-Client'):
        custom_script = frappe.new_doc('Custom Script')
        custom_script.dt = 'Expense Claim'
        custom_script.script = ''
    else:
        custom_script = frappe.get_doc('Custom Script', 'Expense Claim-Client')

    code = """
frappe.ui.form.on("Expense Claim Detail", {
	fc_claim_amount: function(frm, cdt, cdn) {
		const me = this;
		const d = frappe.get_doc(cdt, cdn);
		const transaction_date = d.expense_date || frm.doc.posting_date;
		const company_currency = erpnext.get_currency(frm.doc.company);
		frappe.model.set_value(cdt, cdn, 'fc_sanctioned_amount', d.fc_claim_amount);
		frm.events.get_exchange_rate(
			transaction_date, d.currency, company_currency,
			function(rate) {
				frappe.model.set_value(cdt, cdn, 'claim_amount', rate * d.fc_claim_amount);
				frappe.model.set_value(cdt, cdn, 'sanctioned_amount', rate * d.fc_claim_amount);
			}
		);
	}
});
"""

    custom_script.script = '{0} \n {1}'.format(custom_script.script, code)
    custom_script.save()
