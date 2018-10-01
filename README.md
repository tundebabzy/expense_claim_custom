## Expense Claim Custom

Customisations for ERPNext Expense Claim

### What it does
Expense Claim Custom customises ERPNext's Expense Claim to do the following:
- Adds a text field where you can add vendor information.
- Allows you record expenses in foreign currency. This is useful where your business involves lots of travel.

### Installation
Run the usual bench commands:
```(bash)
$ bench get-app expense_claim_custom https://github.com/tundebabzy/expense_claim_custom
$ bench install-app --site my-site-name expense_claim_custom
$ bench migrate
```

After these commands, reload your server. C'est finis!

### How To Use
The following custom fields are introduced by Expense Claim Custom:

#### In Foreign Currency
This checkbox is disabled by default. If you need to record foreign currency transactions, make sure the checkbox is checked. When the checkbox is checked, the `FOREIGN CURRENCY EXPENSES` section will be visible.

#### Foreign Currency Expenses
The foreign currency expenses section contains the following fields:
- Currency
- Vendor
- FC Claim Amount
- FC Sanctioned Amount

#### Currency
A drop down list of available Currencies

#### Vendor
Text field where you can record the name of a vendor

#### FC Claimed Amount
Claimed amount in foreign currency. This will automatically be converted to the company's currency and set as Claimed Amount in the Expense Claim.

#### FC Sanctioned Amount
Sanctioned amount in foreign currency.


### License

MIT