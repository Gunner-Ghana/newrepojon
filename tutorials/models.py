# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountAccount(models.Model):
    name = models.CharField(max_length=200)
    currency = models.ForeignKey('ResCurrency',     models.DO_NOTHING, related_name="+", blank=True, null=True)
    code = models.CharField(max_length=64)
    deprecated = models.BooleanField(blank=True, null=True)
    user_type = models.ForeignKey('AccountAccountType',   models.DO_NOTHING, related_name="+" )
    internal_type = models.CharField(max_length=200, blank=True, null=True)
    internal_group = models.CharField(max_length=200, blank=True, null=True)
    reconcile = models.BooleanField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    group = models.ForeignKey('AccountGroup',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    root_id = models.IntegerField()
    is_off_balance = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+" , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+",blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    asset_model = models.ForeignKey('AccountAsset',    models.DO_NOTHING, related_name="+", db_column='asset_model', blank=True, null=True)
    create_asset = models.CharField(max_length=200)
    multiple_assets_per_line = models.BooleanField(blank=True, null=True)
    cash_flow_type = models.ForeignKey('AccountFinancialReport',    models.DO_NOTHING, related_name="+", db_column='cash_flow_type', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_account'
        unique_together = (('code', 'company'),)


class AccountAccountAccountCashFlowRel(models.Model):
    account_cash_flow = models.OneToOneField('AccountCashFlow',    models.DO_NOTHING, related_name="+", primary_key=True)
    account_account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_account_account_cash_flow_rel'
        unique_together = (('account_cash_flow', 'account_account'),)


class AccountAccountAccountDayBookRel(models.Model):
    account_day_book = models.OneToOneField('AccountDayBook',    models.DO_NOTHING, related_name="+", primary_key=True)
    account_account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_account_account_day_book_rel'
        unique_together = (('account_day_book', 'account_account'),)


class AccountAccountAccountGeneralLedgerRel(models.Model):
    account_general_ledger = models.OneToOneField('AccountGeneralLedger',    models.DO_NOTHING, related_name="+", primary_key=True)
    account_account = models.ForeignKey(AccountAccount,    models.DO_NOTHING,related_name="+")

    class Meta:
        managed = True
        db_table = 'account_account_account_general_ledger_rel'
        unique_together = (('account_general_ledger', 'account_account'),)


class AccountAccountAccountJournalRel(models.Model):
    account_account = models.OneToOneField(AccountAccount,    models.DO_NOTHING, related_name="+", primary_key=True)
    account_journal = models.ForeignKey('AccountJournal',    models.DO_NOTHING,related_name="+")

    class Meta:
        managed = True
        db_table = 'account_account_account_journal_rel'
        unique_together = (('account_account', 'account_journal'),)


class AccountAccountAccountPartnerLedgerRel(models.Model):
    account_partner_ledger = models.OneToOneField('AccountPartnerLedger',    models.DO_NOTHING, related_name="+", primary_key=True)
    account_account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_account_account_partner_ledger_rel'
        unique_together = (('account_partner_ledger', 'account_account'),)


class AccountAccountAccountTag(models.Model):
    account_account = models.OneToOneField(AccountAccount,    models.DO_NOTHING, related_name="+", primary_key=True)
    account_account_tag = models.ForeignKey('AccountAccountTag',   models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_account_account_tag'
        unique_together = (('account_account', 'account_account_tag'),)


class AccountAccountDynamicBalanceSheetReportRel(models.Model):
    dynamic_balance_sheet_report = models.OneToOneField('DynamicBalanceSheetReport',    models.DO_NOTHING, related_name="+", primary_key=True)
    account_account = models.ForeignKey(AccountAccount,    models.DO_NOTHING,related_name="+")

    class Meta:
        managed = True
        db_table = 'account_account_dynamic_balance_sheet_report_rel'
        unique_together = (('dynamic_balance_sheet_report', 'account_account'),)


class AccountAccountExcludeResCurrencyProvision(models.Model):
    account_account = models.OneToOneField(AccountAccount,    models.DO_NOTHING, related_name="+", primary_key=True)
    res_currency = models.ForeignKey('ResCurrency',    models.DO_NOTHING,related_name="+")

    class Meta:
        managed = True
        db_table = 'account_account_exclude_res_currency_provision'
        unique_together = (('account_account', 'res_currency'),)


class AccountAccountFinancialReport(models.Model):
    report_line = models.OneToOneField('AccountFinancialReport',    models.DO_NOTHING, related_name="+", primary_key=True)
    account = models.ForeignKey(AccountAccount,    models.DO_NOTHING,related_name="+")

    class Meta:
        managed = True
        db_table = 'account_account_financial_report'
        unique_together = (('report_line', 'account'),)


class AccountAccountFinancialReportType(models.Model):
    report = models.OneToOneField('AccountFinancialReport',    models.DO_NOTHING, primary_key=True)
    account_type = models.ForeignKey('AccountAccountType',    models.DO_NOTHING,related_name="+")

    class Meta:
        managed = True
        db_table = 'account_account_financial_report_type'
        unique_together = (('report', 'account_type'),)


class AccountAccountTag(models.Model):
    name = models.CharField(max_length=200)
    applicability = models.CharField(max_length=200)
    color = models.IntegerField()
    active = models.BooleanField(blank=True, null=True)
    tax_negate = models.BooleanField(blank=True, null=True)
    country = models.ForeignKey('ResCountry',    models.DO_NOTHING,related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING   ,related_name="+", blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_account_tag'


class AccountAccountTagAccountGeneralLedgerRel(models.Model):
    account_general_ledger = models.OneToOneField('AccountGeneralLedger',    models.DO_NOTHING, primary_key=True)
    account_account_tag = models.ForeignKey(AccountAccountTag,    models.DO_NOTHING,related_name="+")

    class Meta:
        managed = True
        db_table = 'account_account_tag_account_general_ledger_rel'
        unique_together = (('account_general_ledger', 'account_account_tag'),)


class AccountAccountTagAccountMoveLineRel(models.Model):
    account_move_line = models.OneToOneField('AccountMoveLine',    models.DO_NOTHING, primary_key=True)
    account_account_tag = models.ForeignKey(AccountAccountTag,    models.DO_NOTHING,related_name="+")

    class Meta:
        managed = True
        db_table = 'account_account_tag_account_move_line_rel'
        unique_together = (('account_move_line', 'account_account_tag'),)


class AccountAccountTagAccountTaxRepartitionLineRel(models.Model):
    account_tax_repartition_line = models.OneToOneField('AccountTaxRepartitionLine',    models.DO_NOTHING, related_name="+", primary_key=True)
    account_account_tag = models.ForeignKey(AccountAccountTag,    models.DO_NOTHING,related_name="+")

    class Meta:
        managed = True
        db_table = 'account_account_tag_account_tax_repartition_line_rel'
        unique_together = (('account_tax_repartition_line', 'account_account_tag'),)


class AccountAccountTagDynamicBalanceSheetReportRel(models.Model):
    dynamic_balance_sheet_report = models.OneToOneField('DynamicBalanceSheetReport',    models.DO_NOTHING, related_name="+", primary_key=True)
    account_account_tag = models.ForeignKey(AccountAccountTag,    models.DO_NOTHING,related_name="+")

    class Meta:
        managed = True
        db_table = 'account_account_tag_dynamic_balance_sheet_report_rel'
        unique_together = (('dynamic_balance_sheet_report', 'account_account_tag'),)


class AccountAccountTaxDefaultRel(models.Model):
    account = models.OneToOneField(AccountAccount,    models.DO_NOTHING, related_name="+", primary_key=True)
    tax = models.ForeignKey('AccountTax',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_account_tax_default_rel'
        unique_together = (('account', 'tax'),)


class AccountAccountTemplate(models.Model):
    name = models.CharField(max_length=200)
    currency = models.ForeignKey('ResCurrency',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    code = models.CharField(max_length=64)
    user_type = models.ForeignKey('AccountAccountType',    models.DO_NOTHING, related_name="+")
    reconcile = models.BooleanField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    nocreate = models.BooleanField(blank=True, null=True)
    chart_template = models.ForeignKey('AccountChartTemplate',    models.DO_NOTHING,related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+",blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING,  related_name="+",blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_account_template'


class AccountAccountTemplateAccountTag(models.Model):
    account_account_template = models.OneToOneField(AccountAccountTemplate,    models.DO_NOTHING, related_name="+", primary_key=True)
    account_account_tag = models.ForeignKey(AccountAccountTag,    models.DO_NOTHING,related_name="+")

    class Meta:
        managed = True
        db_table = 'account_account_template_account_tag'
        unique_together = (('account_account_template', 'account_account_tag'),)


class AccountAccountTemplateTaxRel(models.Model):
    account = models.OneToOneField(AccountAccountTemplate,    models.DO_NOTHING, related_name="+", primary_key=True)
    tax = models.ForeignKey('AccountTaxTemplate',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_account_template_tax_rel'
        unique_together = (('account', 'tax'),)


class AccountAccountType(models.Model):
    name = models.CharField(max_length=200)
    include_initial_balance = models.BooleanField(blank=True, null=True)
    type = models.CharField(max_length=200)
    internal_group = models.CharField(max_length=200)
    note = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING,related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_account_type'


class AccountAccountTypeAccountPartnerLedgerRel(models.Model):
    account_partner_ledger = models.OneToOneField('AccountPartnerLedger',    models.DO_NOTHING, related_name="+", primary_key=True)
    account_account_type = models.ForeignKey(AccountAccountType,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_account_type_account_partner_ledger_rel'
        unique_together = (('account_partner_ledger', 'account_account_type'),)


class AccountAgedTrialBalance(models.Model):
    period_length = models.IntegerField()
    date_from = models.DateField(blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING,related_name="+")
    date_to = models.DateField(blank=True, null=True)
    target_move = models.CharField(max_length=200)
    result_selection = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING ,related_name="+", blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING,  related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_aged_trial_balance'


class AccountAgedTrialBalanceAccountJournalRel(models.Model):
    account_aged_trial_balance = models.OneToOneField(AccountAgedTrialBalance,    models.DO_NOTHING, related_name="+", primary_key=True)
    account_journal = models.ForeignKey('AccountJournal',    models.DO_NOTHING,related_name="+")

    class Meta:
        managed = True
        db_table = 'account_aged_trial_balance_account_journal_rel'
        unique_together = (('account_aged_trial_balance', 'account_journal'),)


class AccountAnalyticAccount(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment',    models.DO_NOTHING,related_name="+", blank=True, null=True)
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    group = models.ForeignKey('AccountAnalyticGroup',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING,  related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_analytic_account'


class AccountAnalyticAccountAccountGeneralLedgerRel(models.Model):
    account_general_ledger = models.OneToOneField('AccountGeneralLedger',    models.DO_NOTHING, related_name="+", primary_key=True)
    account_analytic_account = models.ForeignKey(AccountAnalyticAccount,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_analytic_account_account_general_ledger_rel'
        unique_together = (('account_general_ledger', 'account_analytic_account'),)


class AccountAnalyticAccountAccountTransferModelLineRel(models.Model):
    account_transfer_model_line = models.OneToOneField('AccountTransferModelLine',    models.DO_NOTHING, related_name="+", primary_key=True)
    account_analytic_account = models.ForeignKey(AccountAnalyticAccount,    models.DO_NOTHING,related_name="+")

    class Meta:
        managed = True
        db_table = 'account_analytic_account_account_transfer_model_line_rel'
        unique_together = (('account_transfer_model_line', 'account_analytic_account'),)


class AccountAnalyticAccountDynamicBalanceSheetReportRel(models.Model):
    dynamic_balance_sheet_report = models.OneToOneField('DynamicBalanceSheetReport',    models.DO_NOTHING, related_name="+", primary_key=True)
    account_analytic_account = models.ForeignKey(AccountAnalyticAccount,    models.DO_NOTHING,related_name="+")

    class Meta:
        managed = True
        db_table = 'account_analytic_account_dynamic_balance_sheet_report_rel'
        unique_together = (('dynamic_balance_sheet_report', 'account_analytic_account'),)


class AccountAnalyticDefault(models.Model):
    sequence = models.IntegerField()
    analytic = models.ForeignKey(AccountAnalyticAccount,    models.DO_NOTHING,  related_name="+",blank=True, null=True)
    product = models.ForeignKey('ProductProduct',    models.DO_NOTHING,  related_name="+",blank=True, null=True)
    partner = models.ForeignKey('ResPartner',    models.DO_NOTHING,  related_name="+",blank=True, null=True)
    account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+",blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    date_start = models.DateField(blank=True, null=True)
    date_stop = models.DateField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING,  related_name="+",blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_analytic_default'


class AccountAnalyticDefaultAccountAnalyticTagRel(models.Model):
    account_analytic_default = models.OneToOneField(AccountAnalyticDefault,    models.DO_NOTHING, related_name="+", primary_key=True)
    account_analytic_tag = models.ForeignKey('AccountAnalyticTag',    models.DO_NOTHING,related_name="+")

    class Meta:
        managed = True
        db_table = 'account_analytic_default_account_analytic_tag_rel'
        unique_together = (('account_analytic_default', 'account_analytic_tag'),)


class AccountAnalyticDistribution(models.Model):
    account = models.ForeignKey(AccountAnalyticAccount,    models.DO_NOTHING, related_name="+")
    percentage = models.FloatField()
    tag = models.ForeignKey('AccountAnalyticTag',    models.DO_NOTHING,related_name="+")
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING,related_name="+", blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_analytic_distribution'


class AccountAnalyticGroup(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey('self',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    parent_path = models.CharField(max_length=200, blank=True, null=True)
    complete_name = models.CharField(max_length=200, blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING,related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING   ,related_name="+", blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_analytic_group'


class AccountAnalyticLine(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    unit_amount = models.FloatField(blank=True, null=True)
    product_uom = models.ForeignKey('UomUom',    models.DO_NOTHING,related_name="+", blank=True, null=True)
    account = models.ForeignKey(AccountAnalyticAccount,    models.DO_NOTHING,related_name="+")
    partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, blank=True,related_name="+", null=True)
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+",blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING,related_name="+")
    currency = models.ForeignKey('ResCurrency',    models.DO_NOTHING, related_name="+",blank=True, null=True)
    group = models.ForeignKey(AccountAnalyticGroup,    models.DO_NOTHING, related_name="+",blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING ,related_name="+", blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('ProductProduct',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    general_account = models.ForeignKey(AccountAccount,    models.DO_NOTHING,related_name="+" ,blank=True, null=True)
    move = models.ForeignKey('AccountMoveLine',    models.DO_NOTHING,related_name="+", blank=True, null=True)
    code = models.CharField(max_length=8, blank=True, null=True)
    ref = models.CharField(max_length=200, blank=True, null=True)
    so_line = models.ForeignKey('SaleOrderLine',    models.DO_NOTHING,related_name="+",db_column='so_line', blank=True, null=True)
    task = models.ForeignKey('ProjectTask',    models.DO_NOTHING,related_name="+", blank=True, null=True)
    project = models.ForeignKey('ProjectProject',    models.DO_NOTHING,  related_name="+",blank=True, null=True)
    employee = models.ForeignKey('HrEmployee',    models.DO_NOTHING,related_name="+", blank=True, null=True)
    department = models.ForeignKey('HrDepartment',    models.DO_NOTHING,related_name="+", blank=True, null=True)
    holiday = models.ForeignKey('HrLeave',    models.DO_NOTHING,related_name="+", blank=True, null=True)
    validated = models.BooleanField(blank=True, null=True)
    timesheet_invoice_type = models.CharField(max_length=200, blank=True, null=True)
    timesheet_invoice = models.ForeignKey('AccountMove',    models.DO_NOTHING,related_name="+",blank=True, null=True)
    non_allow_billable = models.BooleanField(blank=True, null=True)
    is_so_line_edited = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_analytic_line'


class AccountAnalyticLineHrTimesheetMergeWizardRel(models.Model):
    hr_timesheet_merge_wizard = models.OneToOneField('HrTimesheetMergeWizard',    models.DO_NOTHING, related_name="+", primary_key=True)
    account_analytic_line = models.ForeignKey(AccountAnalyticLine,    models.DO_NOTHING,related_name="+")

    class Meta:
        managed = True
        db_table = 'account_analytic_line_hr_timesheet_merge_wizard_rel'
        unique_together = (('hr_timesheet_merge_wizard', 'account_analytic_line'),)


class AccountAnalyticLineTagRel(models.Model):
    line = models.OneToOneField(AccountAnalyticLine,    models.DO_NOTHING, related_name="+", primary_key=True)
    tag = models.ForeignKey('AccountAnalyticTag',    models.DO_NOTHING,related_name="+")

    class Meta:
        managed = True
        db_table = 'account_analytic_line_tag_rel'
        unique_together = (('line', 'tag'),)


class AccountAnalyticTag(models.Model):
    name = models.CharField(max_length=200)
    color = models.IntegerField()
    active = models.BooleanField(blank=True, null=True)
    active_analytic_distribution = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, blank=True, null=True, related_name="+")
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING , related_name="+"  , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_studio_code = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_analytic_tag'


class AccountAnalyticTagAccountAssetRel(models.Model):
    account_asset = models.OneToOneField('AccountAsset',    models.DO_NOTHING, related_name="+", primary_key=True)
    account_analytic_tag = models.ForeignKey(AccountAnalyticTag,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_analytic_tag_account_asset_rel'
        unique_together = (('account_asset', 'account_analytic_tag'),)


class AccountAnalyticTagAccountGeneralLedgerRel(models.Model):
    account_general_ledger = models.OneToOneField('AccountGeneralLedger',    models.DO_NOTHING, related_name="+", primary_key=True)
    account_analytic_tag = models.ForeignKey(AccountAnalyticTag,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_analytic_tag_account_general_ledger_rel'
        unique_together = (('account_general_ledger', 'account_analytic_tag'),)


class AccountAnalyticTagAccountMoveLineRel(models.Model):
    account_move_line = models.OneToOneField('AccountMoveLine',    models.DO_NOTHING, related_name="+", primary_key=True)
    account_analytic_tag = models.ForeignKey(AccountAnalyticTag,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_analytic_tag_account_move_line_rel'
        unique_together = (('account_move_line', 'account_analytic_tag'),)


class AccountAnalyticTagDynamicBalanceSheetReportRel(models.Model):
    dynamic_balance_sheet_report = models.OneToOneField('DynamicBalanceSheetReport',    models.DO_NOTHING, related_name="+", primary_key=True)
    account_analytic_tag = models.ForeignKey(AccountAnalyticTag,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_analytic_tag_dynamic_balance_sheet_report_rel'
        unique_together = (('dynamic_balance_sheet_report', 'account_analytic_tag'),)


class AccountAnalyticTagPurchaseOrderLineRel(models.Model):
    purchase_order_line = models.OneToOneField('PurchaseOrderLine',    models.DO_NOTHING, related_name="+", primary_key=True)
    account_analytic_tag = models.ForeignKey(AccountAnalyticTag,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_analytic_tag_purchase_order_line_rel'
        unique_together = (('purchase_order_line', 'account_analytic_tag'),)


class AccountAnalyticTagPurchaseRequisitionLineRel(models.Model):
    purchase_requisition_line = models.OneToOneField('PurchaseRequisitionLine',    models.DO_NOTHING, related_name="+", primary_key=True)
    account_analytic_tag = models.ForeignKey(AccountAnalyticTag,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_analytic_tag_purchase_requisition_line_rel'
        unique_together = (('purchase_requisition_line', 'account_analytic_tag'),)


class AccountAnalyticTagSaleOrderLineRel(models.Model):
    sale_order_line = models.OneToOneField('SaleOrderLine',    models.DO_NOTHING, related_name="+", primary_key=True)
    account_analytic_tag = models.ForeignKey(AccountAnalyticTag,    models.DO_NOTHING,  related_name="+")

    class Meta:
        managed = True
        db_table = 'account_analytic_tag_sale_order_line_rel'
        unique_together = (('sale_order_line', 'account_analytic_tag'),)


class AccountAsset(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    name = models.CharField(max_length=200)
    currency = models.ForeignKey('ResCurrency',    models.DO_NOTHING, related_name="+")
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    state = models.CharField(max_length=200, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    asset_type = models.CharField(max_length=200, blank=True, null=True)
    method = models.CharField(max_length=200, blank=True, null=True)
    method_number = models.IntegerField()
    method_period = models.CharField(max_length=200, blank=True, null=True)
    method_progress_factor = models.FloatField(blank=True, null=True)
    prorata = models.BooleanField(blank=True, null=True)
    prorata_date = models.DateField(blank=True, null=True)
    account_asset = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    account_depreciation = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    account_depreciation_expense = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    journal = models.ForeignKey('AccountJournal',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    original_value = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    book_value = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    salvage_value = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    account_analytic = models.ForeignKey(AccountAnalyticAccount,    models.DO_NOTHING, blank=True, null=True, related_name="+")
    first_depreciation_date = models.DateField(blank=True, null=True)
    acquisition_date = models.DateField(blank=True, null=True)
    disposal_date = models.DateField(blank=True, null=True)
    model = models.ForeignKey('self',    models.DO_NOTHING, blank=True, null=True, related_name="+")
    parent = models.ForeignKey('self',    models.DO_NOTHING, blank=True, null=True, related_name="+")
    already_depreciated_amount_import = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    depreciation_number_import = models.IntegerField()
    first_depreciation_date_import = models.DateField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING , related_name="+"  , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, blank=True, null=True, related_name="+")
    write_date = models.DateTimeField(blank=True, null=True)
    x_studio_asset_code = models.CharField(max_length=200, blank=True, null=True)
    x_studio_serial_number = models.CharField(max_length=200, blank=True, null=True)
    x_studio_present_location = models.CharField(max_length=200, blank=True, null=True)
    x_studio_quantity = models.CharField(max_length=200, blank=True, null=True)
    x_studio_asset_description = models.CharField(max_length=200, blank=True, null=True)
    x_studio_asset_category = models.CharField(max_length=200, blank=True, null=True)
    x_studio_company = models.CharField(max_length=200, blank=True, null=True)
    x_studio_currency = models.CharField(max_length=200, blank=True, null=True)
    x_studio_book_value = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_asset'


class AccountAssetAsset(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=32, blank=True, null=True)
    value = models.DecimalField(max_digits=65535, decimal_places=65535)
    currency = models.ForeignKey('ResCurrency',    models.DO_NOTHING, related_name="+")
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    note = models.TextField(blank=True, null=True)
    category = models.ForeignKey('AccountAssetCategory',    models.DO_NOTHING, related_name="+")
    date = models.DateField()
    state = models.CharField(max_length=200)
    active = models.BooleanField(blank=True, null=True)
    partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    method = models.CharField(max_length=200)
    method_number = models.IntegerField()
    method_period = models.IntegerField()
    method_end = models.DateField(blank=True, null=True)
    method_progress_factor = models.FloatField(blank=True, null=True)
    method_time = models.CharField(max_length=200)
    prorata = models.BooleanField(blank=True, null=True)
    salvage_value = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    invoice = models.ForeignKey('AccountMove',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, blank=True, null=True, related_name="+")
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_asset_asset'


class AccountAssetCategory(models.Model):
    active = models.BooleanField(blank=True, null=True)
    name = models.CharField(max_length=200)
    account_analytic = models.ForeignKey(AccountAnalyticAccount,    models.DO_NOTHING,  related_name="+", blank=True, null=True)
    account_asset = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+")
    account_depreciation = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+")
    account_depreciation_expense = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+")
    journal = models.ForeignKey('AccountJournal',    models.DO_NOTHING, related_name="+")
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING,  related_name="+")
    method = models.CharField(max_length=200)
    method_number = models.IntegerField()
    method_period = models.IntegerField()
    method_progress_factor = models.FloatField(blank=True, null=True)
    method_time = models.CharField(max_length=200)
    method_end = models.DateField(blank=True, null=True)
    prorata = models.BooleanField(blank=True, null=True)
    open_asset = models.BooleanField(blank=True, null=True)
    group_entries = models.BooleanField(blank=True, null=True)
    type = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING,  related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_asset_category'


class AccountAssetDepreciationLine(models.Model):
    name = models.CharField(max_length=200)
    sequence = models.IntegerField()
    asset = models.ForeignKey(AccountAssetAsset,    models.DO_NOTHING, related_name="+")
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    remaining_value = models.DecimalField(max_digits=65535, decimal_places=65535)
    depreciated_value = models.FloatField()
    depreciation_date = models.DateField(blank=True, null=True)
    move = models.ForeignKey('AccountMove',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    move_check = models.BooleanField(blank=True, null=True)
    move_posted_check = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING,  related_name="+"  , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING,  related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_asset_depreciation_line'


class AccountAssetPause(models.Model):
    date = models.DateField()
    asset = models.ForeignKey(AccountAsset,    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"  , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_asset_pause'


class AccountAssetSell(models.Model):
    asset = models.ForeignKey(AccountAsset,    models.DO_NOTHING, related_name="+")
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    action = models.CharField(max_length=200)
    invoice = models.ForeignKey('AccountMove',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    invoice_line = models.ForeignKey('AccountMoveLine',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_asset_sell'


class AccountAutomaticEntryWizard(models.Model):
    action = models.CharField(max_length=200)
    date = models.DateField()
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    percentage = models.FloatField(blank=True, null=True)
    total_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    account_type = models.CharField(max_length=200, blank=True, null=True)
    destination_account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING , related_name="+"  , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_automatic_entry_wizard'


class AccountAutomaticEntryWizardAccountMoveLineRel(models.Model):
    account_automatic_entry_wizard = models.OneToOneField(AccountAutomaticEntryWizard,    models.DO_NOTHING, related_name="+", primary_key=True)
    account_move_line = models.ForeignKey('AccountMoveLine',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_automatic_entry_wizard_account_move_line_rel'
        unique_together = (('account_automatic_entry_wizard', 'account_move_line'),)


class AccountBalanceReport(models.Model):
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    target_move = models.CharField(max_length=200)
    display_account = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_balance_report'


class AccountBalanceReportJournalRel(models.Model):
    account = models.OneToOneField(AccountBalanceReport,    models.DO_NOTHING, related_name="+", primary_key=True)
    journal = models.ForeignKey('AccountJournal',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_balance_report_journal_rel'
        unique_together = (('account', 'journal'),)


class AccountBankBookReport(models.Model):
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, blank=True, null=True, related_name="+")
    target_move = models.CharField(max_length=200)
    date_from = models.DateField()
    date_to = models.DateField()
    display_account = models.CharField(max_length=200)
    sortby = models.CharField(max_length=200)
    initial_balance = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING , blank=True, null=True, related_name="+")
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_bank_book_report'


class AccountBankStatement(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    reference = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateField()
    date_done = models.DateTimeField(blank=True, null=True)
    balance_start = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    balance_end_real = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    state = models.CharField(max_length=200)
    journal = models.ForeignKey('AccountJournal',    models.DO_NOTHING, related_name="+")
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    total_entry_encoding = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    balance_end = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    difference = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, blank=True, null=True, related_name="+")
    cashbox_start = models.ForeignKey('AccountBankStatementCashbox',    models.DO_NOTHING, blank=True, related_name="+", null=True)
    cashbox_end = models.ForeignKey('AccountBankStatementCashbox',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    previous_statement = models.ForeignKey('self',    models.DO_NOTHING, blank=True, null=True, related_name="+")
    is_valid_balance_start = models.BooleanField(blank=True, null=True)
    sequence_prefix = models.CharField(max_length=200, blank=True, null=True)
    sequence_number = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING , related_name="+"  , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    accounting_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_bank_statement'


class AccountBankStatementCashbox(models.Model):
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_bank_statement_cashbox'


class AccountBankStatementClosebalance(models.Model):
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_bank_statement_closebalance'


class AccountBankStatementImport(models.Model):
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"  , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_bank_statement_import'


class AccountBankStatementImportIrAttachmentRel(models.Model):
    account_bank_statement_import = models.OneToOneField(AccountBankStatementImport,    models.DO_NOTHING, related_name="+", primary_key=True)
    ir_attachment = models.ForeignKey('IrAttachment',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_bank_statement_import_ir_attachment_rel'
        unique_together = (('account_bank_statement_import', 'ir_attachment'),)


class AccountBankStatementImportJournalCreation(models.Model):
    journal = models.ForeignKey('AccountJournal',    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+" , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_bank_statement_import_journal_creation'


class AccountBankStatementLine(models.Model):
    move = models.ForeignKey('AccountMove',    models.DO_NOTHING,related_name="+")
    statement = models.ForeignKey(AccountBankStatement,    models.DO_NOTHING, related_name="+")
    sequence = models.IntegerField()
    account_number = models.CharField(max_length=200, blank=True, null=True)
    partner_name = models.CharField(max_length=200, blank=True, null=True)
    transaction_type = models.CharField(max_length=200, blank=True, null=True)
    payment_ref = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    foreign_currency = models.ForeignKey('ResCurrency',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    amount_residual = models.FloatField(blank=True, null=True)
    currency = models.ForeignKey('ResCurrency',    models.DO_NOTHING, related_name="+" ,blank=True, null=True)
    partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    is_reconciled = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    online_identifier = models.CharField(max_length=200, blank=True, null=True)
    online_partner_vendor_name = models.CharField(max_length=200, blank=True, null=True)
    online_partner_bank_account = models.CharField(max_length=200, blank=True, null=True)
    online_transaction_identifier = models.CharField(max_length=200, blank=True, null=True)
    online_partner_information = models.CharField(max_length=200, blank=True, null=True)
    online_account = models.ForeignKey('AccountOnlineAccount',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    online_link = models.ForeignKey('AccountOnlineLink',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    unique_import_id = models.CharField(unique=True, max_length=200, blank=True, null=True)
    move_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_bank_statement_line'


class AccountBatchDownloadWizard(models.Model):
    batch_payment = models.ForeignKey('AccountBatchPayment',    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_batch_download_wizard'


class AccountBatchErrorWizard(models.Model):
    batch_payment = models.ForeignKey('AccountBatchPayment',   models.DO_NOTHING,  related_name="+")
    show_remove_options = models.BooleanField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_batch_error_wizard'


class AccountBatchErrorWizardLine(models.Model):
    description = models.CharField(max_length=200)
    help_message = models.CharField(max_length=200, blank=True, null=True)
    error_wizard = models.ForeignKey(AccountBatchErrorWizard,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    warning_wizard = models.ForeignKey(AccountBatchErrorWizard,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+" , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_batch_error_wizard_line'


class AccountBatchErrorWizardLineAccountPaymentRel(models.Model):
    account_batch_error_wizard_line = models.OneToOneField(AccountBatchErrorWizardLine,    models.DO_NOTHING, related_name="+", primary_key=True)
    account_payment = models.ForeignKey('AccountPayment',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_batch_error_wizard_line_account_payment_rel'
        unique_together = (('account_batch_error_wizard_line', 'account_payment'),)


class AccountBatchPayment(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    state = models.CharField(max_length=200, blank=True, null=True)
    journal = models.ForeignKey('AccountJournal',    models.DO_NOTHING, related_name="+")
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    batch_type = models.CharField(max_length=200)
    payment_method = models.ForeignKey('AccountPaymentMethod',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    export_file_create_date = models.DateField(blank=True, null=True)
    export_filename = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_batch_payment'


class AccountBudgetPost(models.Model):
    name = models.CharField(max_length=200)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"  , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_budget_post'


class AccountBudgetRel(models.Model):
    budget = models.OneToOneField(AccountBudgetPost,    models.DO_NOTHING, related_name="+", primary_key=True)
    account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_budget_rel'
        unique_together = (('budget', 'account'),)


class AccountCashBookReport(models.Model):
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    target_move = models.CharField(max_length=200)
    date_from = models.DateField()
    date_to = models.DateField()
    display_account = models.CharField(max_length=200)
    sortby = models.CharField(max_length=200)
    initial_balance = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_cash_book_report'


class AccountCashFlow(models.Model):
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    target_move = models.CharField(max_length=200)
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    today = models.DateField(blank=True, null=True)
    levels = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_cash_flow'


class AccountCashFlowAccountJournalRel(models.Model):
    account_cash_flow = models.OneToOneField(AccountCashFlow,    models.DO_NOTHING, related_name="+", primary_key=True)
    account_journal = models.ForeignKey('AccountJournal',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_cash_flow_account_journal_rel'
        unique_together = (('account_cash_flow', 'account_journal'),)


class AccountCashRounding(models.Model):
    name = models.CharField(max_length=200)
    rounding = models.FloatField()
    strategy = models.CharField(max_length=200)
    rounding_method = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"  , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_cash_rounding'


class AccountCashboxLine(models.Model):
    coin_value = models.DecimalField(max_digits=65535, decimal_places=65535)
    number = models.IntegerField()
    cashbox = models.ForeignKey(AccountBankStatementCashbox,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_cashbox_line'


class AccountChangeLockDate(models.Model):
    period_lock_date = models.DateField(blank=True, null=True)
    fiscalyear_lock_date = models.DateField(blank=True, null=True)
    tax_lock_date = models.DateField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_change_lock_date'


class AccountChartTemplate(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey('self',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    code_digits = models.IntegerField()
    visible = models.BooleanField(blank=True, null=True)
    currency = models.ForeignKey('ResCurrency',    models.DO_NOTHING, related_name="+")
    use_anglo_saxon = models.BooleanField(blank=True, null=True)
    complete_tax_set = models.BooleanField(blank=True, null=True)
    bank_account_code_prefix = models.CharField(max_length=200)
    cash_account_code_prefix = models.CharField(max_length=200)
    transfer_account_code_prefix = models.CharField(max_length=200)
    income_currency_exchange_account = models.ForeignKey(AccountAccountTemplate,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    expense_currency_exchange_account = models.ForeignKey(AccountAccountTemplate,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    account_journal_suspense_account = models.ForeignKey(AccountAccountTemplate,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    default_cash_difference_income_account = models.ForeignKey(AccountAccountTemplate,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    default_cash_difference_expense_account = models.ForeignKey(AccountAccountTemplate,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    default_pos_receivable_account = models.ForeignKey(AccountAccountTemplate,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    property_account_receivable = models.ForeignKey(AccountAccountTemplate,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    property_account_payable = models.ForeignKey(AccountAccountTemplate,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    property_account_expense_categ = models.ForeignKey(AccountAccountTemplate,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    property_account_income_categ = models.ForeignKey(AccountAccountTemplate,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    property_account_expense = models.ForeignKey(AccountAccountTemplate,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    property_account_income = models.ForeignKey(AccountAccountTemplate,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    property_stock_account_input_categ = models.ForeignKey(AccountAccountTemplate,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    property_stock_account_output_categ = models.ForeignKey(AccountAccountTemplate,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    property_stock_valuation_account = models.ForeignKey(AccountAccountTemplate,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    property_tax_payable_account = models.ForeignKey(AccountAccountTemplate,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    property_tax_receivable_account = models.ForeignKey(AccountAccountTemplate,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    property_advance_tax_payment_account = models.ForeignKey(AccountAccountTemplate,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    property_cash_basis_base_account = models.ForeignKey(AccountAccountTemplate,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_chart_template'


class AccountCommonAccountReport(models.Model):
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    target_move = models.CharField(max_length=200)
    display_account = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_common_account_report'


class AccountCommonAccountReportAccountJournalRel(models.Model):
    account_common_account_report = models.OneToOneField(AccountCommonAccountReport,    models.DO_NOTHING, related_name="+", primary_key=True)
    account_journal = models.ForeignKey('AccountJournal',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_common_account_report_account_journal_rel'
        unique_together = (('account_common_account_report', 'account_journal'),)


class AccountCommonJournalReport(models.Model):
    amount_currency = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    target_move = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_common_journal_report'


class AccountCommonJournalReportAccountJournalRel(models.Model):
    account_common_journal_report = models.OneToOneField(AccountCommonJournalReport,    models.DO_NOTHING, related_name="+", primary_key=True)
    account_journal = models.ForeignKey('AccountJournal',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_common_journal_report_account_journal_rel'
        unique_together = (('account_common_journal_report', 'account_journal'),)


class AccountCommonPartnerReport(models.Model):
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    target_move = models.CharField(max_length=200)
    result_selection = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"  , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_common_partner_report'


class AccountCommonPartnerReportAccountJournalRel(models.Model):
    account_common_partner_report = models.OneToOneField(AccountCommonPartnerReport,    models.DO_NOTHING, related_name="+", primary_key=True)
    account_journal = models.ForeignKey('AccountJournal',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_common_partner_report_account_journal_rel'
        unique_together = (('account_common_partner_report', 'account_journal'),)


class AccountCommonReport(models.Model):
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    target_move = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING , related_name="+"  , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_common_report'


class AccountCommonReportAccountJournalRel(models.Model):
    account_common_report = models.OneToOneField(AccountCommonReport,    models.DO_NOTHING, related_name="+", primary_key=True)
    account_journal = models.ForeignKey('AccountJournal',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_common_report_account_journal_rel'
        unique_together = (('account_common_report', 'account_journal'),)


class AccountDayBook(models.Model):
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    date_from = models.DateField()
    date_to = models.DateField()
    target_move = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING,  related_name="+"  , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_day_book'


class AccountDayBookAccountJournalRel(models.Model):
    account_day_book = models.OneToOneField(AccountDayBook,    models.DO_NOTHING, related_name="+", primary_key=True)
    account_journal = models.ForeignKey('AccountJournal',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_day_book_account_journal_rel'
        unique_together = (('account_day_book', 'account_journal'),)


class AccountDayBookReport(models.Model):
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    target_move = models.CharField(max_length=200)
    date_from = models.DateField()
    date_to = models.DateField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_day_book_report'


class AccountDayBookReportAccountJournalRel(models.Model):
    account_day_book_report = models.OneToOneField(AccountDayBookReport,    models.DO_NOTHING, related_name="+", primary_key=True)
    account_journal = models.ForeignKey('AccountJournal',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_day_book_report_account_journal_rel'
        unique_together = (('account_day_book_report', 'account_journal'),)


class AccountEdiDocument(models.Model):
    move = models.ForeignKey('AccountMove',    models.DO_NOTHING, related_name="+")
    edi_format = models.ForeignKey('AccountEdiFormat',    models.DO_NOTHING, related_name="+")
    attachment = models.ForeignKey('IrAttachment',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"  , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_edi_document'
        unique_together = (('edi_format', 'move'),)


class AccountEdiFormat(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    code = models.CharField(unique=True, max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_edi_format'


class AccountEdiFormatAccountJournalRel(models.Model):
    account_journal = models.OneToOneField('AccountJournal',    models.DO_NOTHING, related_name="+", primary_key=True)
    account_edi_format = models.ForeignKey(AccountEdiFormat, models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_edi_format_account_journal_rel'
        unique_together = (('account_journal', 'account_edi_format'),)


class AccountFinancialHtmlReport(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    date_range = models.BooleanField(blank=True, null=True)
    comparison = models.BooleanField(blank=True, null=True)
    analytic = models.BooleanField(blank=True, null=True)
    show_journal_filter = models.BooleanField(blank=True, null=True)
    unfold_all_filter = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    generated_menu = models.ForeignKey('IrUiMenu',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    tax_report = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_financial_html_report'


class AccountFinancialHtmlReportIrFiltersRel(models.Model):
    account_financial_html_report = models.OneToOneField(AccountFinancialHtmlReport,    models.DO_NOTHING, related_name="+", primary_key=True)
    ir_filters = models.ForeignKey('IrFilters',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_financial_html_report_ir_filters_rel'
        unique_together = (('account_financial_html_report', 'ir_filters'),)


class AccountFinancialHtmlReportLine(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    code = models.CharField(unique=True, max_length=200, blank=True, null=True)
    financial_report = models.ForeignKey(AccountFinancialHtmlReport,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    parent = models.ForeignKey('self',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    parent_path = models.CharField(max_length=200, blank=True, null=True)
    sequence = models.IntegerField()
    domain = models.CharField(max_length=200, blank=True, null=True)
    formulas = models.CharField(max_length=200, blank=True, null=True)
    groupby = models.CharField(max_length=200, blank=True, null=True)
    figure_type = models.CharField(max_length=200)
    print_on_new_page = models.BooleanField(blank=True, null=True)
    green_on_positive = models.BooleanField(blank=True, null=True)
    level = models.IntegerField()
    special_date_changer = models.CharField(max_length=200, blank=True, null=True)
    show_domain = models.CharField(max_length=200, blank=True, null=True)
    hide_if_zero = models.BooleanField(blank=True, null=True)
    hide_if_empty = models.BooleanField(blank=True, null=True)
    action_id = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"  , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_financial_html_report_line'


class AccountFinancialReport(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey('self',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    sequence = models.IntegerField()
    level = models.IntegerField()
    type = models.CharField(max_length=200, blank=True, null=True)
    account_report = models.ForeignKey('self',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    sign = models.CharField(max_length=200)
    display_detail = models.CharField(max_length=200, blank=True, null=True)
    style_overwrite = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING , related_name="+"  , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_financial_report'


class AccountFinancialYearOp(models.Model):
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_financial_year_op'


class AccountFiscalPosition(models.Model):
    sequence = models.IntegerField()
    name = models.CharField(max_length=200)
    active = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    note = models.TextField(blank=True, null=True)
    auto_apply = models.BooleanField(blank=True, null=True)
    vat_required = models.BooleanField(blank=True, null=True)
    country = models.ForeignKey('ResCountry',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    country_group = models.ForeignKey('ResCountryGroup',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    zip_from = models.CharField(max_length=200, blank=True, null=True)
    zip_to = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"  , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_fiscal_position'


class AccountFiscalPositionAccount(models.Model):
    position = models.ForeignKey(AccountFiscalPosition,    models.DO_NOTHING, related_name="+")
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    account_src = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+")
    account_dest = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+" , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_fiscal_position_account'
        unique_together = (('position', 'account_src', 'account_dest'),)


class AccountFiscalPositionAccountTemplate(models.Model):
    position = models.ForeignKey('AccountFiscalPositionTemplate',    models.DO_NOTHING, related_name="+")
    account_src = models.ForeignKey(AccountAccountTemplate,    models.DO_NOTHING, related_name="+")
    account_dest = models.ForeignKey(AccountAccountTemplate,    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_fiscal_position_account_template'


class AccountFiscalPositionResCountryStateRel(models.Model):
    account_fiscal_position = models.OneToOneField(AccountFiscalPosition,    models.DO_NOTHING, related_name="+", primary_key=True)
    res_country_state = models.ForeignKey('ResCountryState',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_fiscal_position_res_country_state_rel'
        unique_together = (('account_fiscal_position', 'res_country_state'),)


class AccountFiscalPositionTax(models.Model):
    position = models.ForeignKey(AccountFiscalPosition,    models.DO_NOTHING, related_name="+")
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    tax_src = models.ForeignKey('AccountTax',    models.DO_NOTHING, related_name="+")
    tax_dest = models.ForeignKey('AccountTax',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"  , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_fiscal_position_tax'
        unique_together = (('position', 'tax_src', 'tax_dest'),)


class AccountFiscalPositionTaxTemplate(models.Model):
    position = models.ForeignKey('AccountFiscalPositionTemplate',    models.DO_NOTHING, related_name="+")
    tax_src = models.ForeignKey('AccountTaxTemplate',    models.DO_NOTHING, related_name="+")
    tax_dest = models.ForeignKey('AccountTaxTemplate',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING , related_name="+"  , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_fiscal_position_tax_template'


class AccountFiscalPositionTemplate(models.Model):
    sequence = models.IntegerField()
    name = models.CharField(max_length=200)
    chart_template = models.ForeignKey(AccountChartTemplate,    models.DO_NOTHING, related_name="+")
    note = models.TextField(blank=True, null=True)
    auto_apply = models.BooleanField(blank=True, null=True)
    vat_required = models.BooleanField(blank=True, null=True)
    country = models.ForeignKey('ResCountry',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    country_group = models.ForeignKey('ResCountryGroup',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    zip_from = models.CharField(max_length=200, blank=True, null=True)
    zip_to = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING , related_name="+"  , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_fiscal_position_template'


class AccountFiscalPositionTemplateResCountryStateRel(models.Model):
    account_fiscal_position_template = models.OneToOneField(AccountFiscalPositionTemplate,    models.DO_NOTHING, related_name="+", primary_key=True)
    res_country_state = models.ForeignKey('ResCountryState',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_fiscal_position_template_res_country_state_rel'
        unique_together = (('account_fiscal_position_template', 'res_country_state'),)


class AccountFiscalYear(models.Model):
    name = models.CharField(max_length=200)
    date_from = models.DateField()
    date_to = models.DateField()
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_fiscal_year'


class AccountFollowup(models.Model):
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"  , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_followup'


class AccountFollowupFollowupLine(models.Model):
    name = models.CharField(max_length=200)
    delay = models.IntegerField()
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    sms_description = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    send_email = models.BooleanField(blank=True, null=True)
    print_letter = models.BooleanField(blank=True, null=True)
    send_sms = models.BooleanField(blank=True, null=True)
    join_invoices = models.BooleanField(blank=True, null=True)
    manual_action = models.BooleanField(blank=True, null=True)
    manual_action_note = models.TextField(blank=True, null=True)
    manual_action_type = models.ForeignKey('MailActivityType',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    manual_action_responsible = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    auto_execute = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"  , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    send_letter = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_followup_followup_line'
        unique_together = (('company', 'delay'),)


class AccountFullReconcile(models.Model):
    name = models.CharField(max_length=200)
    exchange_move = models.ForeignKey('AccountMove',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING  , related_name="+" , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_full_reconcile'


class AccountGeneralLedger(models.Model):
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    display_account = models.CharField(max_length=200)
    titles = models.CharField(max_length=200, blank=True, null=True)
    target_move = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_general_ledger'


class AccountGeneralLedgerAccountJournalRel(models.Model):
    account_general_ledger = models.OneToOneField(AccountGeneralLedger,    models.DO_NOTHING, related_name="+", primary_key=True)
    account_journal = models.ForeignKey('AccountJournal',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_general_ledger_account_journal_rel'
        unique_together = (('account_general_ledger', 'account_journal'),)


class AccountGroup(models.Model):
    parent = models.ForeignKey('self',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    parent_path = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200)
    code_prefix_start = models.CharField(max_length=200, blank=True, null=True)
    code_prefix_end = models.CharField(max_length=200, blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING , related_name="+"  , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_group'


class AccountGroupTemplate(models.Model):
    parent = models.ForeignKey('self',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    name = models.CharField(max_length=200)
    code_prefix_start = models.CharField(max_length=200, blank=True, null=True)
    code_prefix_end = models.CharField(max_length=200, blank=True, null=True)
    chart_template = models.ForeignKey(AccountChartTemplate,    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING , related_name="+"  , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_group_template'


class AccountIncoterms(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=3)
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+" , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_incoterms'


class AccountInvoiceExtractWords(models.Model):
    invoice = models.ForeignKey('AccountMove',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    field = models.CharField(max_length=200, blank=True, null=True)
    selected_status = models.IntegerField()
    user_selected = models.BooleanField(blank=True, null=True)
    word_text = models.CharField(max_length=200, blank=True, null=True)
    word_page = models.IntegerField()
    word_box_midx = models.FloatField(db_column='word_box_midX', blank=True, null=True)  # Field name made lowercase.
    word_box_midy = models.FloatField(db_column='word_box_midY', blank=True, null=True)  # Field name made lowercase.
    word_box_width = models.FloatField(blank=True, null=True)
    word_box_height = models.FloatField(blank=True, null=True)
    word_box_angle = models.FloatField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_invoice_extract_words'


class AccountInvoiceSend(models.Model):
    is_email = models.BooleanField(blank=True, null=True)
    is_print = models.BooleanField(blank=True, null=True)
    printed = models.BooleanField(blank=True, null=True)
    composer = models.ForeignKey('MailComposeMessage',    models.DO_NOTHING, related_name="+")
    template = models.ForeignKey('MailTemplate',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING  , related_name="+" , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    snailmail_is_letter = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_invoice_send'


class AccountInvoiceTransactionRel(models.Model):
    transaction = models.OneToOneField('PaymentTransaction',    models.DO_NOTHING, related_name="+", primary_key=True)
    invoice = models.ForeignKey('AccountMove',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_invoice_transaction_rel'
        unique_together = (('transaction', 'invoice'),)


class AccountJournal(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=5)
    active = models.BooleanField(blank=True, null=True)
    type = models.CharField(max_length=200)
    default_account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    payment_debit_account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    payment_credit_account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    suspense_account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    restrict_mode_hash_table = models.BooleanField(blank=True, null=True)
    sequence = models.IntegerField()
    invoice_reference_type = models.CharField(max_length=200)
    invoice_reference_model = models.CharField(max_length=200)
    currency = models.ForeignKey('ResCurrency',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    refund_sequence = models.BooleanField(blank=True, null=True)
    sequence_override_regex = models.TextField(blank=True, null=True)
    at_least_one_inbound = models.BooleanField(blank=True, null=True)
    at_least_one_outbound = models.BooleanField(blank=True, null=True)
    profit_account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    loss_account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    bank_account = models.ForeignKey('ResPartnerBank',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    bank_statements_source = models.CharField(max_length=200, blank=True, null=True)
    sale_activity_type = models.ForeignKey('MailActivityType',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    sale_activity_user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    sale_activity_note = models.TextField(blank=True, null=True)
    alias = models.ForeignKey('MailAlias',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    secure_sequence = models.ForeignKey('IrSequence',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    show_on_dashboard = models.BooleanField(blank=True, null=True)
    color = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING , related_name="+"  , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    account_online_journal = models.ForeignKey('AccountOnlineJournal',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    bank_statement_creation = models.CharField(max_length=200, blank=True, null=True)
    account_online_account = models.ForeignKey('AccountOnlineAccount',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    account_online_link = models.ForeignKey('AccountOnlineLink',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    bank_statement_creation_groupby = models.CharField(max_length=200, blank=True, null=True)
    l10n_in_gstin_partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    check_manual_sequencing = models.BooleanField(blank=True, null=True)
    check_sequence = models.ForeignKey('IrSequence',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    multiple_invoice_type = models.CharField(max_length=200)
    text_position = models.CharField(max_length=200)
    body_text_position = models.CharField(max_length=200, blank=True, null=True)
    text_align = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_journal'
        unique_together = (('code', 'name', 'company'),)


class AccountJournalAccountJournalGroupRel(models.Model):
    account_journal_group = models.OneToOneField('AccountJournalGroup',    models.DO_NOTHING, related_name="+", primary_key=True)
    account_journal = models.ForeignKey(AccountJournal,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_journal_account_journal_group_rel'
        unique_together = (('account_journal_group', 'account_journal'),)


class AccountJournalAccountPartnerAgeingRel(models.Model):
    account_partner_ageing = models.OneToOneField('AccountPartnerAgeing',    models.DO_NOTHING, related_name="+", primary_key=True)
    account_journal = models.ForeignKey(AccountJournal,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_journal_account_partner_ageing_rel'
        unique_together = (('account_partner_ageing', 'account_journal'),)


class AccountJournalAccountPartnerLedgerRel(models.Model):
    account_partner_ledger = models.OneToOneField('AccountPartnerLedger',    models.DO_NOTHING, related_name="+", primary_key=True)
    account_journal = models.ForeignKey(AccountJournal,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_journal_account_partner_ledger_rel'
        unique_together = (('account_partner_ledger', 'account_journal'),)


class AccountJournalAccountPrintJournalRel(models.Model):
    account_print_journal = models.OneToOneField('AccountPrintJournal',    models.DO_NOTHING, related_name="+", primary_key=True)
    account_journal = models.ForeignKey(AccountJournal,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_journal_account_print_journal_rel'
        unique_together = (('account_print_journal', 'account_journal'),)


class AccountJournalAccountReconcileModelRel(models.Model):
    account_reconcile_model = models.OneToOneField('AccountReconcileModel',    models.DO_NOTHING, related_name="+", primary_key=True)
    account_journal = models.ForeignKey(AccountJournal,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_journal_account_reconcile_model_rel'
        unique_together = (('account_reconcile_model', 'account_journal'),)


class AccountJournalAccountReconcileModelTemplateRel(models.Model):
    account_reconcile_model_template = models.OneToOneField('AccountReconcileModelTemplate',    models.DO_NOTHING, related_name="+", primary_key=True)
    account_journal = models.ForeignKey(AccountJournal,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_journal_account_reconcile_model_template_rel'
        unique_together = (('account_reconcile_model_template', 'account_journal'),)


class AccountJournalAccountReportPartnerLedgerRel(models.Model):
    account_report_partner_ledger = models.OneToOneField('AccountReportPartnerLedger',    models.DO_NOTHING, related_name="+", primary_key=True)
    account_journal = models.ForeignKey(AccountJournal,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_journal_account_report_partner_ledger_rel'
        unique_together = (('account_report_partner_ledger', 'account_journal'),)


class AccountJournalAccountTrialBalanceRel(models.Model):
    account_trial_balance = models.OneToOneField('AccountTrialBalance',    models.DO_NOTHING, related_name="+", primary_key=True)
    account_journal = models.ForeignKey(AccountJournal,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_journal_account_trial_balance_rel'
        unique_together = (('account_trial_balance', 'account_journal'),)


class AccountJournalCashFlowReportRel(models.Model):
    cash_flow_report = models.OneToOneField('CashFlowReport',    models.DO_NOTHING, related_name="+", primary_key=True)
    account_journal = models.ForeignKey(AccountJournal,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_journal_cash_flow_report_rel'
        unique_together = (('cash_flow_report', 'account_journal'),)


class AccountJournalDynamicBalanceSheetReportRel(models.Model):
    dynamic_balance_sheet_report = models.OneToOneField('DynamicBalanceSheetReport',    models.DO_NOTHING, related_name="+", primary_key=True)
    account_journal = models.ForeignKey(AccountJournal,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_journal_dynamic_balance_sheet_report_rel'
        unique_together = (('dynamic_balance_sheet_report', 'account_journal'),)


class AccountJournalFinancialReportRel(models.Model):
    financial_report = models.OneToOneField('FinancialReport',    models.DO_NOTHING, related_name="+", primary_key=True)
    account_journal = models.ForeignKey(AccountJournal,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_journal_financial_report_rel'
        unique_together = (('financial_report', 'account_journal'),)


class AccountJournalGroup(models.Model):
    name = models.CharField(max_length=200)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    sequence = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_journal_group'


class AccountJournalInboundPaymentMethodRel(models.Model):
    journal = models.OneToOneField(AccountJournal,    models.DO_NOTHING, related_name="+", primary_key=True)
    inbound_payment_method = models.ForeignKey('AccountPaymentMethod',    models.DO_NOTHING, related_name="+", db_column='inbound_payment_method')

    class Meta:
        managed = True
        db_table = 'account_journal_inbound_payment_method_rel'
        unique_together = (('journal', 'inbound_payment_method'),)


class AccountJournalKitAccountTaxReportRel(models.Model):
    kit_account_tax_report = models.OneToOneField('KitAccountTaxReport',    models.DO_NOTHING, related_name="+", primary_key=True)
    account_journal = models.ForeignKey(AccountJournal,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_journal_kit_account_tax_report_rel'
        unique_together = (('kit_account_tax_report', 'account_journal'),)


class AccountJournalOutboundPaymentMethodRel(models.Model):
    journal = models.OneToOneField(AccountJournal,    models.DO_NOTHING, related_name="+", primary_key=True)
    outbound_payment_method = models.ForeignKey('AccountPaymentMethod',    models.DO_NOTHING, related_name="+", db_column='outbound_payment_method')

    class Meta:
        managed = True
        db_table = 'account_journal_outbound_payment_method_rel'
        unique_together = (('journal', 'outbound_payment_method'),)


class AccountLinkJournal(models.Model):
    number_added = models.IntegerField()
    transactions = models.TextField(blank=True, null=True)
    sync_date = models.DateField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING , related_name="+" , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_link_journal'


class AccountLinkJournalLine(models.Model):
    action = models.CharField(max_length=200, blank=True, null=True)
    journal = models.ForeignKey(AccountJournal,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    currency = models.ForeignKey('ResCurrency',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    online_account = models.ForeignKey('AccountOnlineAccount',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    account_online_wizard = models.ForeignKey(AccountLinkJournal,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    journal_statements_creation = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING , related_name="+" , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_link_journal_line'


class AccountLockDate(models.Model):
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    period_lock_date = models.DateField(blank=True, null=True)
    fiscalyear_lock_date = models.DateField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING , related_name="+"  , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_lock_date'


class AccountModelRel(models.Model):
    account_transfer_model = models.OneToOneField('AccountTransferModel',    models.DO_NOTHING, related_name="+", primary_key=True)
    account_account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_model_rel'
        unique_together = (('account_transfer_model', 'account_account'),)


class AccountMove(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    access_token = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateField()
    ref = models.CharField(max_length=200, blank=True, null=True)
    narration = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=200)
    posted_before = models.BooleanField(blank=True, null=True)
    move_type = models.CharField(max_length=200)
    to_check = models.BooleanField(blank=True, null=True)
    journal = models.ForeignKey(AccountJournal,    models.DO_NOTHING, related_name="+")
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    currency = models.ForeignKey('ResCurrency',    models.DO_NOTHING, related_name="+")
    partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+",  blank=True, null=True)
    commercial_partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    is_move_sent = models.BooleanField(blank=True, null=True)
    partner_bank = models.ForeignKey('ResPartnerBank',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    payment_reference = models.CharField(max_length=200, blank=True, null=True)
    payment = models.ForeignKey('AccountPayment',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    statement_line = models.ForeignKey(AccountBankStatementLine,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    amount_untaxed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_tax = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_residual = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_untaxed_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_tax_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_total_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_residual_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    payment_state = models.CharField(max_length=200, blank=True, null=True)
    tax_cash_basis_rec = models.ForeignKey('AccountPartialReconcile',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    tax_cash_basis_move = models.ForeignKey('self',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    auto_post = models.BooleanField(blank=True, null=True)
    reversed_entry = models.ForeignKey('self',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    fiscal_position = models.ForeignKey(AccountFiscalPosition,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    invoice_user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    invoice_date = models.DateField(blank=True, null=True)
    invoice_date_due = models.DateField(blank=True, null=True)
    invoice_origin = models.CharField(max_length=200, blank=True, null=True)
    invoice_payment_term = models.ForeignKey('AccountPaymentTerm',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    invoice_incoterm = models.ForeignKey(AccountIncoterms,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    qr_code_method = models.CharField(max_length=200, blank=True, null=True)
    invoice_source_email = models.CharField(max_length=200, blank=True, null=True)
    invoice_partner_display_name = models.CharField(max_length=200, blank=True, null=True)
    invoice_cash_rounding = models.ForeignKey(AccountCashRounding,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    secure_sequence_number = models.IntegerField()
    inalterable_hash = models.CharField(max_length=200, blank=True, null=True)
    sequence_prefix = models.CharField(max_length=200, blank=True, null=True)
    sequence_number = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING , related_name="+"  , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    edi_state = models.CharField(max_length=200, blank=True, null=True)
    duplicated_vendor_ref = models.CharField(max_length=200, blank=True, null=True)
    extract_state = models.CharField(max_length=200)
    extract_status_code = models.IntegerField()
    extract_remote_id = models.IntegerField()
    stock_move = models.ForeignKey('StockMove',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    campaign = models.ForeignKey('UtmCampaign',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    source = models.ForeignKey('UtmSource',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    medium = models.ForeignKey('UtmMedium',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    team = models.ForeignKey('CrmTeam',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    partner_shipping = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    payment_state_before_switch = models.CharField(max_length=200, blank=True, null=True)
    transfer_model = models.ForeignKey('AccountTransferModel',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    tax_closing_end_date = models.DateField(blank=True, null=True)
    tax_report_control_error = models.BooleanField(blank=True, null=True)
    asset = models.ForeignKey(AccountAsset,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    asset_remaining_value = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    asset_depreciated_value = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    asset_manually_modified = models.BooleanField(blank=True, null=True)
    asset_value_change = models.BooleanField(blank=True, null=True)
    l10n_in_gst_treatment = models.CharField(max_length=200, blank=True, null=True)
    l10n_in_state = models.ForeignKey('ResCountryState',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    l10n_in_gstin = models.CharField(max_length=200, blank=True, null=True)
    l10n_in_shipping_bill_number = models.CharField(max_length=200, blank=True, null=True)
    l10n_in_shipping_bill_date = models.DateField(blank=True, null=True)
    l10n_in_shipping_port_code = models.ForeignKey('L10NInPortCode',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    l10n_in_reseller_partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    release_to_pay = models.CharField(max_length=200, blank=True, null=True)
    release_to_pay_manual = models.CharField(max_length=200, blank=True, null=True)
    force_release_to_pay = models.BooleanField(blank=True, null=True)
    preferred_payment_method = models.ForeignKey('AccountPaymentMethod',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_studio_char_field_i7nxn = models.CharField(db_column='x_studio_char_field_I7nxN', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_supplier_contact = models.CharField(max_length=200, blank=True, null=True)
    x_studio_char_field_khsbb = models.CharField(db_column='x_studio_char_field_kHsbB', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_client_contact = models.CharField(max_length=200, blank=True, null=True)
    x_studio_cost_centre = models.ForeignKey('XCostCentresTag',    models.DO_NOTHING, related_name="+", db_column='x_studio_cost_centre', blank=True, null=True)
    x_studio_invoice_type = models.CharField(max_length=200, blank=True, null=True)
    x_studio_invoice_number = models.CharField(max_length=200, blank=True, null=True)
    website = models.ForeignKey('Website',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    has_due = models.BooleanField(blank=True, null=True)
    is_warning = models.BooleanField(blank=True, null=True)
    recurring_ref = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_move'


class AccountMoveAccountInvoiceSendRel(models.Model):
    account_invoice_send = models.OneToOneField(AccountInvoiceSend,    models.DO_NOTHING, related_name="+", primary_key=True)
    account_move = models.ForeignKey(AccountMove,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_move_account_invoice_send_rel'
        unique_together = (('account_invoice_send', 'account_move'),)


class AccountMoveAccountResequenceWizardRel(models.Model):
    account_resequence_wizard = models.OneToOneField('AccountResequenceWizard',    models.DO_NOTHING, related_name="+", primary_key=True)
    account_move = models.ForeignKey(AccountMove,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_move_account_resequence_wizard_rel'
        unique_together = (('account_resequence_wizard', 'account_move'),)


class AccountMoveLine(models.Model):
    move = models.ForeignKey(AccountMove,    models.DO_NOTHING, related_name="+")
    move_name = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    ref = models.CharField(max_length=200, blank=True, null=True)
    parent_state = models.CharField(max_length=200, blank=True, null=True)
    journal = models.ForeignKey(AccountJournal,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    company_currency = models.ForeignKey('ResCurrency',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    account_root_id = models.IntegerField()
    sequence = models.IntegerField()
    name = models.CharField(max_length=200, blank=True, null=True)
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_unit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    discount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    debit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    credit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    balance = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_subtotal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    reconciled = models.BooleanField(blank=True, null=True)
    blocked = models.BooleanField(blank=True, null=True)
    date_maturity = models.DateField(blank=True, null=True)
    currency = models.ForeignKey('ResCurrency',    models.DO_NOTHING, related_name="+")
    partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    product_uom = models.ForeignKey('UomUom',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    product = models.ForeignKey('ProductProduct',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    reconcile_model = models.ForeignKey('AccountReconcileModel',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    payment = models.ForeignKey('AccountPayment',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    statement_line = models.ForeignKey(AccountBankStatementLine,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    statement = models.ForeignKey(AccountBankStatement,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    tax_line = models.ForeignKey('AccountTax',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    tax_group = models.ForeignKey('AccountTaxGroup',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    tax_base_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tax_exigible = models.BooleanField(blank=True, null=True)
    tax_repartition_line = models.ForeignKey('AccountTaxRepartitionLine',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    tax_audit = models.CharField(max_length=200, blank=True, null=True)
    amount_residual = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_residual_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    full_reconcile = models.ForeignKey(AccountFullReconcile,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    matching_number = models.CharField(max_length=200, blank=True, null=True)
    analytic_account = models.ForeignKey(AccountAnalyticAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    display_type = models.CharField(max_length=200, blank=True, null=True)
    is_rounding_line = models.BooleanField(blank=True, null=True)
    exclude_from_invoice_tab = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    purchase_line = models.ForeignKey('PurchaseOrderLine',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    is_anglo_saxon_line = models.BooleanField(blank=True, null=True)
    expected_pay_date = models.DateField(blank=True, null=True)
    internal_note = models.TextField(blank=True, null=True)
    next_action_date = models.DateField(blank=True, null=True)
    followup_line = models.ForeignKey(AccountFollowupFollowupLine,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    followup_date = models.DateField(blank=True, null=True)
    can_be_paid = models.CharField(max_length=200, blank=True, null=True)
    asset_category = models.ForeignKey(AccountAssetCategory,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    asset_start_date = models.DateField(blank=True, null=True)
    asset_end_date = models.DateField(blank=True, null=True)
    asset_mrr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_move_line'


class AccountMoveLineAccountTaxRel(models.Model):
    account_move_line = models.OneToOneField(AccountMoveLine,    models.DO_NOTHING, related_name="+", primary_key=True)
    account_tax = models.ForeignKey('AccountTax',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_move_line_account_tax_rel'
        unique_together = (('account_move_line', 'account_tax'),)


class AccountMovePurchaseOrderRel(models.Model):
    purchase_order = models.OneToOneField('PurchaseOrder',    models.DO_NOTHING, related_name="+", primary_key=True)
    account_move = models.ForeignKey(AccountMove,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_move_purchase_order_rel'
        unique_together = (('purchase_order', 'account_move'),)


class AccountMoveReversal(models.Model):
    date_mode = models.CharField(max_length=200)
    date = models.DateField(blank=True, null=True)
    reason = models.CharField(max_length=200, blank=True, null=True)
    refund_method = models.CharField(max_length=200)
    journal = models.ForeignKey(AccountJournal,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_move_reversal'


class AccountMoveReversalMove(models.Model):
    reversal = models.OneToOneField(AccountMoveReversal,    models.DO_NOTHING, related_name="+", primary_key=True)
    move = models.ForeignKey(AccountMove,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_move_reversal_move'
        unique_together = (('reversal', 'move'),)


class AccountMoveReversalNewMove(models.Model):
    reversal = models.OneToOneField(AccountMoveReversal,    models.DO_NOTHING, related_name="+", primary_key=True)
    new_move = models.ForeignKey(AccountMove,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_move_reversal_new_move'
        unique_together = (('reversal', 'new_move'),)


class AccountMulticurrencyRevaluationWizard(models.Model):
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    date = models.DateField()
    reversal_date = models.DateField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_multicurrency_revaluation_wizard'


class AccountOnlineAccount(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    online_identifier = models.CharField(max_length=200, blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    account_number = models.CharField(max_length=200, blank=True, null=True)
    account_data = models.CharField(max_length=200, blank=True, null=True)
    account_online_link = models.ForeignKey('AccountOnlineLink',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    last_sync = models.DateField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_online_account'


class AccountOnlineJournal(models.Model):
    name = models.CharField(max_length=200)
    account_online_provider = models.ForeignKey('AccountOnlineProvider',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    account_number = models.CharField(max_length=200, blank=True, null=True)
    last_sync = models.DateField(blank=True, null=True)
    online_identifier = models.CharField(max_length=200, blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    ponto_last_synchronization_identifier = models.CharField(max_length=200, blank=True, null=True)
    yodlee_account_status = models.CharField(max_length=200, blank=True, null=True)
    yodlee_status_code = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'account_online_journal'


class AccountOnlineLink(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    last_refresh = models.DateTimeField(blank=True, null=True)
    state = models.CharField(max_length=200)
    auto_sync = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    name = models.CharField(max_length=200, blank=True, null=True)
    client_id = models.CharField(max_length=200, blank=True, null=True)
    refresh_token = models.CharField(max_length=200, blank=True, null=True)
    access_token = models.CharField(max_length=200, blank=True, null=True)
    provider_data = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_online_link'


class AccountOnlineLinkWizard(models.Model):
    journal = models.ForeignKey(AccountJournal,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    online_account = models.ForeignKey(AccountOnlineJournal,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    action = models.CharField(max_length=200, blank=True, null=True)
    account_online_wizard = models.ForeignKey('AccountOnlineWizard',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    journal_statements_creation = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_online_link_wizard'


class AccountOnlineProvider(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    provider_type = models.CharField(max_length=200, blank=True, null=True)
    provider_account_identifier = models.CharField(max_length=200, blank=True, null=True)
    provider_identifier = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, null=True)
    status_code = models.CharField(max_length=200, blank=True, null=True)
    message = models.CharField(max_length=200, blank=True, null=True)
    action_required = models.BooleanField(blank=True, null=True)
    last_refresh = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    plaid_error_type = models.CharField(max_length=200, blank=True, null=True)
    plaid_item_id = models.CharField(max_length=200, blank=True, null=True)
    ponto_token = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_online_provider'


class AccountOnlineWizard(models.Model):
    number_added = models.IntegerField()
    transactions = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, null=True)
    method = models.CharField(max_length=200, blank=True, null=True)
    message = models.CharField(max_length=200, blank=True, null=True)
    sync_date = models.DateField(blank=True, null=True)
    hide_table = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_online_wizard'


class AccountPartialReconcile(models.Model):
    debit_move = models.ForeignKey(AccountMoveLine,    models.DO_NOTHING, related_name="+")
    credit_move = models.ForeignKey(AccountMoveLine,    models.DO_NOTHING, related_name="+")
    full_reconcile = models.ForeignKey(AccountFullReconcile,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    debit_currency = models.ForeignKey('ResCurrency',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    credit_currency = models.ForeignKey('ResCurrency',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    debit_amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    credit_amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    max_date = models.DateField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_partial_reconcile'


class AccountPartnerAgeing(models.Model):
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    date_to = models.DateField(blank=True, null=True)
    target_move = models.CharField(max_length=200)
    period_length = models.IntegerField()
    date_from = models.DateField(blank=True, null=True)
    result_selection = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_partner_ageing'


class AccountPartnerAgeingResPartnerCategoryRel(models.Model):
    account_partner_ageing = models.OneToOneField(AccountPartnerAgeing,    models.DO_NOTHING, related_name="+", primary_key=True)
    res_partner_category = models.ForeignKey('ResPartnerCategory',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_partner_ageing_res_partner_category_rel'
        unique_together = (('account_partner_ageing', 'res_partner_category'),)


class AccountPartnerAgeingResPartnerRel(models.Model):
    account_partner_ageing = models.OneToOneField(AccountPartnerAgeing,    models.DO_NOTHING, related_name="+", primary_key=True)
    res_partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_partner_ageing_res_partner_rel'
        unique_together = (('account_partner_ageing', 'res_partner'),)


class AccountPartnerLedger(models.Model):
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    target_move = models.CharField(max_length=200)
    display_account = models.CharField(max_length=200)
    reconciled = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_partner_ledger'


class AccountPartnerLedgerResPartnerCategoryRel(models.Model):
    account_partner_ledger = models.OneToOneField(AccountPartnerLedger,    models.DO_NOTHING, related_name="+", primary_key=True)
    res_partner_category = models.ForeignKey('ResPartnerCategory',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_partner_ledger_res_partner_category_rel'
        unique_together = (('account_partner_ledger', 'res_partner_category'),)


class AccountPartnerLedgerResPartnerRel(models.Model):
    account_partner_ledger = models.OneToOneField(AccountPartnerLedger,    models.DO_NOTHING, related_name="+", primary_key=True)
    res_partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_partner_ledger_res_partner_rel'
        unique_together = (('account_partner_ledger', 'res_partner'),)


class AccountPayment(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    move = models.ForeignKey(AccountMove,    models.DO_NOTHING, related_name="+")
    is_reconciled = models.BooleanField(blank=True, null=True)
    is_matched = models.BooleanField(blank=True, null=True)
    partner_bank = models.ForeignKey('ResPartnerBank',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    is_internal_transfer = models.BooleanField(blank=True, null=True)
    payment_method = models.ForeignKey('AccountPaymentMethod',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    payment_type = models.CharField(max_length=200)
    partner_type = models.CharField(max_length=200)
    payment_reference = models.CharField(max_length=200, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    destination_account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    payment_transaction = models.ForeignKey('PaymentTransaction',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    payment_token = models.ForeignKey('PaymentToken',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    check_amount_in_words = models.CharField(max_length=200, blank=True, null=True)
    check_number = models.CharField(max_length=200, blank=True, null=True)
    batch_payment = models.ForeignKey(AccountBatchPayment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    bank_reference = models.CharField(max_length=200, blank=True, null=True)
    cheque_reference = models.CharField(max_length=200, blank=True, null=True)
    effective_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_payment'


class AccountPaymentAccountBankStatementLineRel(models.Model):
    account_bank_statement_line = models.OneToOneField(AccountBankStatementLine,    models.DO_NOTHING, related_name="+", primary_key=True)
    account_payment = models.ForeignKey(AccountPayment,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_payment_account_bank_statement_line_rel'
        unique_together = (('account_bank_statement_line', 'account_payment'),)


class AccountPaymentMethod(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    payment_type = models.CharField(max_length=200)
    sequence = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_payment_method'


class AccountPaymentRegister(models.Model):
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    communication = models.CharField(max_length=200, blank=True, null=True)
    group_payment = models.BooleanField(blank=True, null=True)
    currency = models.ForeignKey('ResCurrency',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    journal = models.ForeignKey(AccountJournal,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    partner_bank = models.ForeignKey('ResPartnerBank',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    payment_type = models.CharField(max_length=200, blank=True, null=True)
    partner_type = models.CharField(max_length=200, blank=True, null=True)
    source_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    source_amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    source_currency = models.ForeignKey('ResCurrency',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    can_edit_wizard = models.BooleanField(blank=True, null=True)
    can_group_payments = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    payment_method = models.ForeignKey(AccountPaymentMethod,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    payment_difference_handling = models.CharField(max_length=200, blank=True, null=True)
    writeoff_account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    writeoff_label = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    payment_token = models.ForeignKey('PaymentToken',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    bank_reference = models.CharField(max_length=200, blank=True, null=True)
    cheque_reference = models.CharField(max_length=200, blank=True, null=True)
    effective_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_payment_register'


class AccountPaymentRegisterMoveLineRel(models.Model):
    wizard = models.OneToOneField(AccountPaymentRegister,    models.DO_NOTHING, related_name="+", primary_key=True)
    line = models.ForeignKey(AccountMoveLine,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_payment_register_move_line_rel'
        unique_together = (('wizard', 'line'),)


class AccountPaymentTerm(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    sequence = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_payment_term'


class AccountPaymentTermLine(models.Model):
    value = models.CharField(max_length=200)
    value_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    days = models.IntegerField()
    day_of_the_month = models.IntegerField()
    option = models.CharField(max_length=200)
    payment = models.ForeignKey(AccountPaymentTerm,    models.DO_NOTHING, related_name="+")
    sequence = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_payment_term_line'


class AccountPrintJournal(models.Model):
    sort_selection = models.CharField(max_length=200)
    amount_currency = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    target_move = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_print_journal'


class AccountReconcileModel(models.Model):
    active = models.BooleanField(blank=True, null=True)
    name = models.CharField(max_length=200)
    sequence = models.IntegerField()
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    rule_type = models.CharField(max_length=200)
    auto_reconcile = models.BooleanField(blank=True, null=True)
    to_check = models.BooleanField(blank=True, null=True)
    matching_order = models.CharField(max_length=200)
    match_text_location_label = models.BooleanField(blank=True, null=True)
    match_text_location_note = models.BooleanField(blank=True, null=True)
    match_text_location_reference = models.BooleanField(blank=True, null=True)
    match_nature = models.CharField(max_length=200)
    match_amount = models.CharField(max_length=200, blank=True, null=True)
    match_amount_min = models.FloatField(blank=True, null=True)
    match_amount_max = models.FloatField(blank=True, null=True)
    match_label = models.CharField(max_length=200, blank=True, null=True)
    match_label_param = models.CharField(max_length=200, blank=True, null=True)
    match_note = models.CharField(max_length=200, blank=True, null=True)
    match_note_param = models.CharField(max_length=200, blank=True, null=True)
    match_transaction_type = models.CharField(max_length=200, blank=True, null=True)
    match_transaction_type_param = models.CharField(max_length=200, blank=True, null=True)
    match_same_currency = models.BooleanField(blank=True, null=True)
    match_total_amount = models.BooleanField(blank=True, null=True)
    match_total_amount_param = models.FloatField(blank=True, null=True)
    match_partner = models.BooleanField(blank=True, null=True)
    past_months_limit = models.IntegerField()
    decimal_separator = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_reconcile_model'


class AccountReconcileModelAnalyticTagRel(models.Model):
    account_reconcile_model_line = models.OneToOneField('AccountReconcileModelLine',    models.DO_NOTHING, related_name="+", primary_key=True)
    account_analytic_tag = models.ForeignKey(AccountAnalyticTag,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_reconcile_model_analytic_tag_rel'
        unique_together = (('account_reconcile_model_line', 'account_analytic_tag'),)


class AccountReconcileModelLine(models.Model):
    model = models.ForeignKey(AccountReconcileModel,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    sequence = models.IntegerField()
    account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+")
    journal = models.ForeignKey(AccountJournal,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    label = models.CharField(max_length=200, blank=True, null=True)
    amount_type = models.CharField(max_length=200)
    force_tax_included = models.BooleanField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    amount_string = models.CharField(max_length=200)
    analytic_account = models.ForeignKey(AccountAnalyticAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_reconcile_model_line'


class AccountReconcileModelLineAccountTaxRel(models.Model):
    account_reconcile_model_line = models.OneToOneField(AccountReconcileModelLine,    models.DO_NOTHING, related_name="+", primary_key=True)
    account_tax = models.ForeignKey('AccountTax',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_reconcile_model_line_account_tax_rel'
        unique_together = (('account_reconcile_model_line', 'account_tax'),)


class AccountReconcileModelLineTemplate(models.Model):
    model = models.ForeignKey('AccountReconcileModelTemplate',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    sequence = models.IntegerField()
    account = models.ForeignKey(AccountAccountTemplate,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    label = models.CharField(max_length=200, blank=True, null=True)
    amount_type = models.CharField(max_length=200)
    amount_string = models.CharField(max_length=200, blank=True, null=True)
    force_tax_included = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_reconcile_model_line_template'


class AccountReconcileModelLineTemplateAccountTaxTemplateRel(models.Model):
    account_reconcile_model_line_template = models.OneToOneField(AccountReconcileModelLineTemplate,    models.DO_NOTHING, related_name="+", primary_key=True)
    account_tax_template = models.ForeignKey('AccountTaxTemplate',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_reconcile_model_line_template_account_tax_template_rel'
        unique_together = (('account_reconcile_model_line_template', 'account_tax_template'),)


class AccountReconcileModelPartnerMapping(models.Model):
    model = models.ForeignKey(AccountReconcileModel,    models.DO_NOTHING, related_name="+")
    partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+")
    payment_ref_regex = models.CharField(max_length=200, blank=True, null=True)
    narration_regex = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_reconcile_model_partner_mapping'


class AccountReconcileModelResPartnerCategoryRel(models.Model):
    account_reconcile_model = models.OneToOneField(AccountReconcileModel,    models.DO_NOTHING, related_name="+", primary_key=True)
    res_partner_category = models.ForeignKey('ResPartnerCategory',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_reconcile_model_res_partner_category_rel'
        unique_together = (('account_reconcile_model', 'res_partner_category'),)


class AccountReconcileModelResPartnerRel(models.Model):
    account_reconcile_model = models.OneToOneField(AccountReconcileModel,    models.DO_NOTHING, related_name="+", primary_key=True)
    res_partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_reconcile_model_res_partner_rel'
        unique_together = (('account_reconcile_model', 'res_partner'),)


class AccountReconcileModelTemplate(models.Model):
    chart_template = models.ForeignKey(AccountChartTemplate,    models.DO_NOTHING, related_name="+")
    name = models.CharField(max_length=200)
    sequence = models.IntegerField()
    rule_type = models.CharField(max_length=200)
    auto_reconcile = models.BooleanField(blank=True, null=True)
    to_check = models.BooleanField(blank=True, null=True)
    matching_order = models.CharField(max_length=200, blank=True, null=True)
    match_text_location_label = models.BooleanField(blank=True, null=True)
    match_text_location_note = models.BooleanField(blank=True, null=True)
    match_text_location_reference = models.BooleanField(blank=True, null=True)
    match_nature = models.CharField(max_length=200)
    match_amount = models.CharField(max_length=200, blank=True, null=True)
    match_amount_min = models.FloatField(blank=True, null=True)
    match_amount_max = models.FloatField(blank=True, null=True)
    match_label = models.CharField(max_length=200, blank=True, null=True)
    match_label_param = models.CharField(max_length=200, blank=True, null=True)
    match_note = models.CharField(max_length=200, blank=True, null=True)
    match_note_param = models.CharField(max_length=200, blank=True, null=True)
    match_transaction_type = models.CharField(max_length=200, blank=True, null=True)
    match_transaction_type_param = models.CharField(max_length=200, blank=True, null=True)
    match_same_currency = models.BooleanField(blank=True, null=True)
    match_total_amount = models.BooleanField(blank=True, null=True)
    match_total_amount_param = models.FloatField(blank=True, null=True)
    match_partner = models.BooleanField(blank=True, null=True)
    decimal_separator = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_reconcile_model_template'


class AccountReconcileModelTemplateResPartnerCategoryRel(models.Model):
    account_reconcile_model_template = models.OneToOneField(AccountReconcileModelTemplate,    models.DO_NOTHING, related_name="+", primary_key=True)
    res_partner_category = models.ForeignKey('ResPartnerCategory',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_reconcile_model_template_res_partner_category_rel'
        unique_together = (('account_reconcile_model_template', 'res_partner_category'),)


class AccountReconcileModelTemplateResPartnerRel(models.Model):
    account_reconcile_model_template = models.OneToOneField(AccountReconcileModelTemplate,    models.DO_NOTHING, related_name="+", primary_key=True)
    res_partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_reconcile_model_template_res_partner_rel'
        unique_together = (('account_reconcile_model_template', 'res_partner'),)


class AccountRecurringEntriesLine(models.Model):
    date = models.DateField(blank=True, null=True)
    template_name = models.CharField(max_length=200, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    tmpl = models.ForeignKey('AccountRecurringPayments',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_recurring_entries_line'


class AccountRecurringPayments(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    debit_account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+", db_column='debit_account')
    credit_account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+", db_column='credit_account')
    journal = models.ForeignKey(AccountJournal,    models.DO_NOTHING, related_name="+")
    analytic_account = models.ForeignKey(AccountAnalyticAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    date = models.DateField()
    recurring_period = models.CharField(max_length=200)
    amount = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    journal_state = models.CharField(max_length=200)
    recurring_interval = models.IntegerField()
    partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    pay_time = models.CharField(max_length=200)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_recurring_payments'


class AccountReportBankbookAccountRel(models.Model):
    report = models.OneToOneField(AccountBankBookReport,    models.DO_NOTHING, related_name="+", primary_key=True)
    account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_report_bankbook_account_rel'
        unique_together = (('report', 'account'),)


class AccountReportBankbookJournalRel(models.Model):
    account = models.OneToOneField(AccountBankBookReport,    models.DO_NOTHING, related_name="+", primary_key=True)
    journal = models.ForeignKey(AccountJournal,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_report_bankbook_journal_rel'
        unique_together = (('account', 'journal'),)


class AccountReportCashbookAccountRel(models.Model):
    report = models.OneToOneField(AccountCashBookReport,    models.DO_NOTHING, related_name="+", primary_key=True)
    account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_report_cashbook_account_rel'
        unique_together = (('report', 'account'),)


class AccountReportCashbookJournalRel(models.Model):
    account = models.OneToOneField(AccountCashBookReport,    models.DO_NOTHING, related_name="+", primary_key=True)
    journal = models.ForeignKey(AccountJournal,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_report_cashbook_journal_rel'
        unique_together = (('account', 'journal'),)


class AccountReportDaybookAccountRel(models.Model):
    report = models.OneToOneField(AccountDayBookReport,    models.DO_NOTHING, related_name="+", primary_key=True)
    account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_report_daybook_account_rel'
        unique_together = (('report', 'account'),)


class AccountReportFootnote(models.Model):
    text = models.CharField(max_length=200, blank=True, null=True)
    line = models.CharField(max_length=200, blank=True, null=True)
    manager = models.ForeignKey('AccountReportManager',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_report_footnote'


class AccountReportGeneralLedger(models.Model):
    initial_balance = models.BooleanField(blank=True, null=True)
    sortby = models.CharField(max_length=200)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    target_move = models.CharField(max_length=200)
    display_account = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_report_general_ledger'


class AccountReportGeneralLedgerJournalRel(models.Model):
    account = models.OneToOneField(AccountReportGeneralLedger,    models.DO_NOTHING, related_name="+", primary_key=True)
    journal = models.ForeignKey(AccountJournal,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_report_general_ledger_journal_rel'
        unique_together = (('account', 'journal'),)


class AccountReportManager(models.Model):
    report_name = models.CharField(max_length=200)
    summary = models.CharField(max_length=200, blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    financial_report = models.ForeignKey(AccountFinancialHtmlReport,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+", blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_report_manager'


class AccountReportPartnerLedger(models.Model):
    amount_currency = models.BooleanField(blank=True, null=True)
    reconciled = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    target_move = models.CharField(max_length=200)
    result_selection = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_report_partner_ledger'


class AccountReportsExportWizard(models.Model):
    report_model = models.CharField(max_length=200)
    report_id = models.IntegerField()
    doc_name = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_reports_export_wizard'


class AccountReportsExportWizardFormat(models.Model):
    name = models.CharField(max_length=200)
    fun_to_call = models.CharField(max_length=200)
    export_wizard = models.ForeignKey(AccountReportsExportWizard,    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_reports_export_wizard_format'


class AccountResequenceWizard(models.Model):
    first_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    first_name = models.CharField(max_length=200)
    ordering = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_resequence_wizard'


class AccountSetupBankManualConfig(models.Model):
    res_partner_bank = models.ForeignKey('ResPartnerBank',    models.DO_NOTHING, related_name="+")
    new_journal_name = models.CharField(max_length=200)
    num_journals_without_account = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_setup_bank_manual_config'


class AccountTax(models.Model):
    name = models.CharField(max_length=200)
    type_tax_use = models.CharField(max_length=200)
    tax_scope = models.CharField(max_length=200, blank=True, null=True)
    amount_type = models.CharField(max_length=200)
    active = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    sequence = models.IntegerField()
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    description = models.CharField(max_length=200, blank=True, null=True)
    price_include = models.BooleanField(blank=True, null=True)
    include_base_amount = models.BooleanField(blank=True, null=True)
    analytic = models.BooleanField(blank=True, null=True)
    tax_group = models.ForeignKey('AccountTaxGroup',    models.DO_NOTHING, related_name="+")
    tax_exigibility = models.CharField(max_length=200, blank=True, null=True)
    cash_basis_transition_account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    python_compute = models.TextField(blank=True, null=True)
    python_applicable = models.TextField(blank=True, null=True)
    l10n_in_reverse_charge = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_tax'
        unique_together = (('name', 'company', 'type_tax_use', 'tax_scope'),)


class AccountTaxFiliationRel(models.Model):
    parent_tax = models.OneToOneField(AccountTax,    models.DO_NOTHING, related_name="+", db_column='parent_tax', primary_key=True)
    child_tax = models.ForeignKey(AccountTax,    models.DO_NOTHING, related_name="+", db_column='child_tax')

    class Meta:
        managed = True
        db_table = 'account_tax_filiation_rel'
        unique_together = (('parent_tax', 'child_tax'),)


class AccountTaxGroup(models.Model):
    name = models.CharField(max_length=200)
    sequence = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_tax_group'


class AccountTaxPurchaseOrderLineRel(models.Model):
    purchase_order_line = models.OneToOneField('PurchaseOrderLine',    models.DO_NOTHING, related_name="+", primary_key=True)
    account_tax = models.ForeignKey(AccountTax,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_tax_purchase_order_line_rel'
        unique_together = (('purchase_order_line', 'account_tax'),)


class AccountTaxRepartitionFinancialTags(models.Model):
    account_tax_repartition_line_template = models.OneToOneField('AccountTaxRepartitionLineTemplate',    models.DO_NOTHING, related_name="+", primary_key=True)
    account_account_tag = models.ForeignKey(AccountAccountTag,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_tax_repartition_financial_tags'
        unique_together = (('account_tax_repartition_line_template', 'account_account_tag'),)


class AccountTaxRepartitionLine(models.Model):
    factor_percent = models.FloatField()
    repartition_type = models.CharField(max_length=200)
    account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    invoice_tax = models.ForeignKey(AccountTax,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    refund_tax = models.ForeignKey(AccountTax,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    sequence = models.IntegerField()
    use_in_tax_closing = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_tax_repartition_line'


class AccountTaxRepartitionLineTemplate(models.Model):
    factor_percent = models.FloatField()
    repartition_type = models.CharField(max_length=200)
    account = models.ForeignKey(AccountAccountTemplate,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    invoice_tax = models.ForeignKey('AccountTaxTemplate',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    refund_tax = models.ForeignKey('AccountTaxTemplate',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    use_in_tax_closing = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_tax_repartition_line_template'


class AccountTaxRepartitionMinusReportLine(models.Model):
    account_tax_repartition_line_template = models.OneToOneField(AccountTaxRepartitionLineTemplate,    models.DO_NOTHING, related_name="+", primary_key=True)
    account_tax_report_line = models.ForeignKey('AccountTaxReportLine',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_tax_repartition_minus_report_line'
        unique_together = (('account_tax_repartition_line_template', 'account_tax_report_line'),)


class AccountTaxRepartitionPlusReportLine(models.Model):
    account_tax_repartition_line_template = models.OneToOneField(AccountTaxRepartitionLineTemplate,    models.DO_NOTHING, related_name="+", primary_key=True)
    account_tax_report_line = models.ForeignKey('AccountTaxReportLine',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_tax_repartition_plus_report_line'
        unique_together = (('account_tax_repartition_line_template', 'account_tax_report_line'),)


class AccountTaxReport(models.Model):
    name = models.CharField(max_length=200)
    country = models.ForeignKey('ResCountry',    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_tax_report'


class AccountTaxReportLine(models.Model):
    name = models.CharField(max_length=200)
    report_action = models.ForeignKey('IrActWindow',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    parent = models.ForeignKey('self',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    sequence = models.IntegerField()
    parent_path = models.CharField(max_length=200, blank=True, null=True)
    report = models.ForeignKey(AccountTaxReport,    models.DO_NOTHING, related_name="+")
    tag_name = models.CharField(max_length=200, blank=True, null=True)
    code = models.CharField(max_length=200, blank=True, null=True)
    formula = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_tax_report_line'


class AccountTaxReportLineTagsRel(models.Model):
    account_account_tag = models.OneToOneField(AccountAccountTag,    models.DO_NOTHING, related_name="+", primary_key=True)
    account_tax_report_line = models.ForeignKey(AccountTaxReportLine,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_tax_report_line_tags_rel'
        unique_together = (('account_account_tag', 'account_tax_report_line'),)


class AccountTaxSaleAdvancePaymentInvRel(models.Model):
    sale_advance_payment_inv = models.OneToOneField('SaleAdvancePaymentInv',    models.DO_NOTHING, related_name="+", primary_key=True)
    account_tax = models.ForeignKey(AccountTax,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_tax_sale_advance_payment_inv_rel'
        unique_together = (('sale_advance_payment_inv', 'account_tax'),)


class AccountTaxSaleOrderLineRel(models.Model):
    sale_order_line = models.OneToOneField('SaleOrderLine',    models.DO_NOTHING, related_name="+", primary_key=True)
    account_tax = models.ForeignKey(AccountTax,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_tax_sale_order_line_rel'
        unique_together = (('sale_order_line', 'account_tax'),)


class AccountTaxTemplate(models.Model):
    chart_template = models.ForeignKey(AccountChartTemplate,    models.DO_NOTHING, related_name="+")
    name = models.CharField(max_length=200)
    type_tax_use = models.CharField(max_length=200)
    tax_scope = models.CharField(max_length=200, blank=True, null=True)
    amount_type = models.CharField(max_length=200)
    active = models.BooleanField(blank=True, null=True)
    sequence = models.IntegerField()
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    description = models.CharField(max_length=200, blank=True, null=True)
    price_include = models.BooleanField(blank=True, null=True)
    include_base_amount = models.BooleanField(blank=True, null=True)
    analytic = models.BooleanField(blank=True, null=True)
    tax_group = models.ForeignKey(AccountTaxGroup,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    tax_exigibility = models.CharField(max_length=200, blank=True, null=True)
    cash_basis_transition_account = models.ForeignKey(AccountAccountTemplate,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    python_compute = models.TextField(blank=True, null=True)
    python_applicable = models.TextField(blank=True, null=True)
    l10n_in_reverse_charge = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_tax_template'
        unique_together = (('name', 'type_tax_use', 'tax_scope', 'chart_template'),)


class AccountTaxTemplateFiliationRel(models.Model):
    parent_tax = models.OneToOneField(AccountTaxTemplate,    models.DO_NOTHING, related_name="+", db_column='parent_tax', primary_key=True)
    child_tax = models.ForeignKey(AccountTaxTemplate,    models.DO_NOTHING, related_name="+", db_column='child_tax')

    class Meta:
        managed = True
        db_table = 'account_tax_template_filiation_rel'
        unique_together = (('parent_tax', 'child_tax'),)


class AccountTourUploadBill(models.Model):
    composer = models.ForeignKey('MailComposeMessage',    models.DO_NOTHING, related_name="+")
    selection = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_tour_upload_bill'


class AccountTourUploadBillEmailConfirm(models.Model):
    email_alias = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_tour_upload_bill_email_confirm'


class AccountTransferModel(models.Model):
    name = models.CharField(max_length=200)
    journal = models.ForeignKey(AccountJournal,    models.DO_NOTHING, related_name="+")
    date_start = models.DateField()
    date_stop = models.DateField(blank=True, null=True)
    frequency = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_transfer_model'


class AccountTransferModelLine(models.Model):
    transfer_model = models.ForeignKey(AccountTransferModel,    models.DO_NOTHING, related_name="+")
    account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+")
    percent = models.FloatField()
    sequence = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_transfer_model_line'
        unique_together = (('transfer_model', 'account'),)


class AccountTransferModelLineResPartnerRel(models.Model):
    account_transfer_model_line = models.OneToOneField(AccountTransferModelLine,    models.DO_NOTHING, related_name="+", primary_key=True)
    res_partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'account_transfer_model_line_res_partner_rel'
        unique_together = (('account_transfer_model_line', 'res_partner'),)


class AccountTrialBalance(models.Model):
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    target_move = models.CharField(max_length=200)
    display_account = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_trial_balance'


class AccountUnreconcile(models.Model):
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_unreconcile'


class AmazonAccount(models.Model):
    name = models.CharField(max_length=200)
    base_marketplace = models.ForeignKey('AmazonMarketplace',    models.DO_NOTHING, related_name="+")
    seller_key = models.CharField(max_length=200)
    auth_token = models.CharField(max_length=200)
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    team = models.ForeignKey('CrmTeam',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    location = models.ForeignKey('StockLocation',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    active = models.BooleanField()
    last_orders_sync = models.DateTimeField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'amazon_account'


class AmazonAccountActiveMarketplaceRel(models.Model):
    amazon_account = models.OneToOneField(AmazonAccount,    models.DO_NOTHING, related_name="+", primary_key=True)
    amazon_marketplace = models.ForeignKey('AmazonMarketplace',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'amazon_account_active_marketplace_rel'
        unique_together = (('amazon_account', 'amazon_marketplace'),)


class AmazonAccountMarketplaceRel(models.Model):
    amazon_account = models.OneToOneField(AmazonAccount,    models.DO_NOTHING, related_name="+", primary_key=True)
    amazon_marketplace = models.ForeignKey('AmazonMarketplace',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'amazon_account_marketplace_rel'
        unique_together = (('amazon_account', 'amazon_marketplace'),)


class AmazonMarketplace(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    domain = models.CharField(max_length=200)
    api_ref = models.CharField(unique=True, max_length=200)
    tax_included = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'amazon_marketplace'


class AmazonOffer(models.Model):
    account = models.ForeignKey(AmazonAccount,    models.DO_NOTHING, related_name="+")
    marketplace = models.ForeignKey(AmazonMarketplace,    models.DO_NOTHING, related_name="+")
    domain = models.CharField(max_length=200, blank=True, null=True)
    product = models.ForeignKey('ProductProduct',    models.DO_NOTHING, related_name="+")
    product_template = models.ForeignKey('ProductTemplate',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    sku = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'amazon_offer'
        unique_together = (('account', 'marketplace', 'sku'),)


class ApplicantGetRefuseReason(models.Model):
    refuse_reason = models.ForeignKey('HrApplicantRefuseReason',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'applicant_get_refuse_reason'


class ApplicantGetRefuseReasonHrApplicantRel(models.Model):
    applicant_get_refuse_reason = models.OneToOneField(ApplicantGetRefuseReason,    models.DO_NOTHING, related_name="+", primary_key=True)
    hr_applicant = models.ForeignKey('HrApplicant',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'applicant_get_refuse_reason_hr_applicant_rel'
        unique_together = (('applicant_get_refuse_reason', 'hr_applicant'),)


class AppraisalManagerRel(models.Model):
    hr_appraisal = models.OneToOneField('HrAppraisal',    models.DO_NOTHING, related_name="+", primary_key=True)
    hr_employee = models.ForeignKey('HrEmployee',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'appraisal_manager_rel'
        unique_together = (('hr_appraisal', 'hr_employee'),)


class ApprovalApprover(models.Model):
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+")
    status = models.CharField(max_length=200, blank=True, null=True)
    request = models.ForeignKey('ApprovalRequest',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_studio_position = models.CharField(max_length=200, blank=True, null=True)
    x_studio_many2one_field_hwj3w = models.ForeignKey('HrJob',    models.DO_NOTHING, related_name="+", db_column='x_studio_many2one_field_HWJ3w', blank=True, null=True)  # Field name made lowercase.
    x_studio_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'approval_approver'


class ApprovalCategory(models.Model):
    name = models.CharField(max_length=200)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    active = models.BooleanField(blank=True, null=True)
    sequence = models.IntegerField()
    description = models.CharField(max_length=200, blank=True, null=True)
    has_date = models.CharField(max_length=200)
    has_period = models.CharField(max_length=200)
    has_quantity = models.CharField(max_length=200)
    has_amount = models.CharField(max_length=200)
    has_reference = models.CharField(max_length=200)
    has_partner = models.CharField(max_length=200)
    has_payment_method = models.CharField(max_length=200)
    has_location = models.CharField(max_length=200)
    has_product = models.CharField(max_length=200)
    requirer_document = models.CharField(max_length=200)
    approval_minimum = models.IntegerField()
    approval_type = models.CharField(max_length=200, blank=True, null=True)
    is_manager_approver = models.BooleanField(blank=True, null=True)
    automated_sequence = models.BooleanField(blank=True, null=True)
    sequence_code = models.CharField(max_length=200, blank=True, null=True)
    sequence_0 = models.ForeignKey('IrSequence',    models.DO_NOTHING, related_name="+", db_column='sequence_id', blank=True, null=True)  # Field renamed because of name conflict.
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_studio_actions = models.ForeignKey('HrEmployee',    models.DO_NOTHING, related_name="+", db_column='x_studio_actions', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'approval_category'


class ApprovalCategoryResUsersRel(models.Model):
    approval_category = models.OneToOneField(ApprovalCategory,    models.DO_NOTHING, related_name="+", primary_key=True)
    res_users = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'approval_category_res_users_rel'
        unique_together = (('approval_category', 'res_users'),)


class ApprovalProductLine(models.Model):
    approval_request = models.ForeignKey('ApprovalRequest',    models.DO_NOTHING, related_name="+")
    description = models.CharField(max_length=200)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    product = models.ForeignKey('ProductProduct',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    product_uom = models.ForeignKey('UomUom',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    quantity = models.FloatField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    purchase_order_line = models.ForeignKey('PurchaseOrderLine',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    warehouse = models.ForeignKey('StockWarehouse',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_studio_date_field_qkp1m = models.DateField(db_column='x_studio_date_field_QKP1M', blank=True, null=True)  # Field name made lowercase.
    x_studio_date = models.DateField(blank=True, null=True)
    x_studio_date_field_sfibk = models.DateField(db_column='x_studio_date_field_sfiBk', blank=True, null=True)  # Field name made lowercase.
    x_studio_amount_in_ghs_1 = models.CharField(max_length=200, blank=True, null=True)
    x_currency = models.ForeignKey('ResCurrency',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_studio_amount_in_ghs = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    x_studio_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    x_studio_date_1 = models.DateField(blank=True, null=True)
    x_studio_amount_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'approval_product_line'


class ApprovalRequest(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    category = models.ForeignKey(ApprovalCategory,    models.DO_NOTHING, related_name="+")
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    date_start = models.DateTimeField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)
    quantity = models.FloatField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    date_confirmed = models.DateTimeField(blank=True, null=True)
    partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    reference = models.CharField(max_length=200, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    request_status = models.CharField(max_length=200, blank=True, null=True)
    request_owner = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_studio_many2one_field_vi8aa = models.ForeignKey('HrDepartment',    models.DO_NOTHING, related_name="+", db_column='x_studio_many2one_field_VI8aA', blank=True, null=True)  # Field name made lowercase.
    x_studio_internal_transfer = models.ForeignKey('StockPicking',    models.DO_NOTHING, related_name="+", db_column='x_studio_internal_transfer', blank=True, null=True)
    x_studio_fund_request = models.ForeignKey(AccountMove,    models.DO_NOTHING, related_name="+", db_column='x_studio_fund_request', blank=True, null=True)
    x_studio_many2one_field_l9on4 = models.ForeignKey('MaintenanceRequest',    models.DO_NOTHING, related_name="+", db_column='x_studio_many2one_field_l9oN4', blank=True, null=True)  # Field name made lowercase.
    x_studio_impress_retired = models.CharField(max_length=200, blank=True, null=True)
    x_studio_impress_retired_date = models.DateField(blank=True, null=True)
    x_studio_binary_field_xsz6e_filename = models.CharField(db_column='x_studio_binary_field_XsZ6e_filename', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_binary_field_wwgni_filename = models.CharField(db_column='x_studio_binary_field_WWgNI_filename', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_head_of_department = models.ForeignKey('HrEmployee',    models.DO_NOTHING, related_name="+", db_column='x_studio_head_of_department', blank=True, null=True)
    x_studio_date = models.DateField(blank=True, null=True)
    x_studio_received_by = models.ForeignKey('HrEmployee',    models.DO_NOTHING, related_name="+", db_column='x_studio_received_by', blank=True, null=True)
    x_studio_date_1 = models.DateField(blank=True, null=True)
    x_studio_payment_voucher_pv_no = models.CharField(max_length=200, blank=True, null=True)
    x_studio_many2one_field_keyiw = models.ForeignKey(AccountPayment,    models.DO_NOTHING, related_name="+", db_column='x_studio_many2one_field_KEyIW', blank=True, null=True)  # Field name made lowercase.
    x_studio_maintenance_request_2 = models.ForeignKey('MaintenanceRequest',    models.DO_NOTHING, related_name="+", db_column='x_studio_maintenance_request_2', blank=True, null=True)
    x_studio_many2one_field_ztxbm = models.ForeignKey('XCostCentres',    models.DO_NOTHING, related_name="+", db_column='x_studio_many2one_field_ZtxbM', blank=True, null=True)  # Field name made lowercase.
    x_studio_departmentregional = models.ForeignKey('XCostCentresTag',    models.DO_NOTHING, related_name="+", db_column='x_studio_departmentregional', blank=True, null=True)
    x_studio_text_field_qxlc8 = models.TextField(db_column='x_studio_text_field_QXlC8', blank=True, null=True)  # Field name made lowercase.
    x_currency = models.ForeignKey('ResCurrency',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_studio_vetted_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    x_studio_main_activity = models.TextField(blank=True, null=True)
    x_studio_activity_code = models.CharField(max_length=200, blank=True, null=True)
    x_studio_designation = models.ForeignKey('XCostCentresTag',    models.DO_NOTHING, related_name="+", db_column='x_studio_designation', blank=True, null=True)
    x_studio_monetary_field_zbt2a = models.DecimalField(db_column='x_studio_monetary_field_zbT2A', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
    x_studio_float_field_btz9v = models.FloatField(db_column='x_studio_float_field_btz9V', blank=True, null=True)  # Field name made lowercase.
    x_studio_no = models.CharField(max_length=200, blank=True, null=True)
    x_studio_char_field_qohc6 = models.CharField(db_column='x_studio_char_field_qOHC6', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_comments = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'approval_request'


class AssetDepreciationConfirmationWizard(models.Model):
    date = models.DateField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'asset_depreciation_confirmation_wizard'


class AssetModify(models.Model):
    name = models.TextField()
    asset = models.ForeignKey(AccountAsset,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    method_number = models.IntegerField()
    method_period_moved0 = models.CharField(max_length=200, blank=True, null=True)
    value_residual = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    salvage_value = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    account_asset = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    account_asset_counterpart = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    account_depreciation = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    account_depreciation_expense = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    method_period = models.IntegerField()
    method_end = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'asset_modify'


class AssetMoveLineRel(models.Model):
    asset = models.OneToOneField(AccountAsset,    models.DO_NOTHING, related_name="+", primary_key=True)
    line = models.ForeignKey(AccountMoveLine,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'asset_move_line_rel'
        unique_together = (('asset', 'line'),)


class AuthTotpWizard(models.Model):
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+")
    secret = models.CharField(max_length=200)
    url = models.CharField(max_length=200, blank=True, null=True)
    qrcode = models.BinaryField(blank=True, null=True)
    code = models.CharField(max_length=7, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'auth_totp_wizard'


class BadgeUnlockedDefinitionRel(models.Model):
    gamification_badge = models.OneToOneField('GamificationBadge',    models.DO_NOTHING, related_name="+", primary_key=True)
    gamification_goal_definition = models.ForeignKey('GamificationGoalDefinition',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'badge_unlocked_definition_rel'
        unique_together = (('gamification_badge', 'gamification_goal_definition'),)


class BarcodeNomenclature(models.Model):
    name = models.CharField(max_length=32)
    upc_ean_conv = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'barcode_nomenclature'


class BarcodeRule(models.Model):
    name = models.CharField(max_length=32)
    barcode_nomenclature = models.ForeignKey(BarcodeNomenclature,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    sequence = models.IntegerField()
    encoding = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    pattern = models.CharField(max_length=32)
    alias = models.CharField(max_length=32)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'barcode_rule'


class BaseAutomation(models.Model):
    action_server = models.ForeignKey('IrActServer',    models.DO_NOTHING, related_name="+")
    active = models.BooleanField(blank=True, null=True)
    trigger = models.CharField(max_length=200)
    trg_date = models.ForeignKey('IrModelFields',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    trg_date_range = models.IntegerField()
    trg_date_range_type = models.CharField(max_length=200, blank=True, null=True)
    trg_date_calendar = models.ForeignKey('ResourceCalendar',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    filter_pre_domain = models.CharField(max_length=200, blank=True, null=True)
    filter_domain = models.CharField(max_length=200, blank=True, null=True)
    last_run = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    trg_date_resource_field = models.ForeignKey('IrModelFields',    models.DO_NOTHING, related_name="+", blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'base_automation'


class BaseAutomationIrModelFieldsRel(models.Model):
    base_automation = models.OneToOneField(BaseAutomation,    models.DO_NOTHING, related_name="+", primary_key=True)
    ir_model_fields = models.ForeignKey('IrModelFields',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'base_automation_ir_model_fields_rel'
        unique_together = (('base_automation', 'ir_model_fields'),)


class BaseAutomationOnchangeFieldsRel(models.Model):
    base_automation = models.OneToOneField(BaseAutomation,    models.DO_NOTHING, related_name="+", primary_key=True)
    ir_model_fields = models.ForeignKey('IrModelFields',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'base_automation_onchange_fields_rel'
        unique_together = (('base_automation', 'ir_model_fields'),)


class BaseDocumentLayout(models.Model):
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    report_layout = models.ForeignKey('ReportLayout',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'base_document_layout'


class BaseImportImport(models.Model):
    res_model = models.CharField(max_length=200, blank=True, null=True)
    file = models.BinaryField(blank=True, null=True)
    file_name = models.CharField(max_length=200, blank=True, null=True)
    file_type = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'base_import_import'


class BaseImportMapping(models.Model):
    res_model = models.CharField(max_length=200, blank=True, null=True)
    column_name = models.CharField(max_length=200, blank=True, null=True)
    field_name = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'base_import_mapping'


class BaseImportModule(models.Model):
    module_file = models.BinaryField()
    state = models.CharField(max_length=200, blank=True, null=True)
    import_message = models.TextField(blank=True, null=True)
    force = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'base_import_module'


class BaseImportTestsModelsChar(models.Model):
    value = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'base_import_tests_models_char'


class BaseImportTestsModelsCharNoreadonly(models.Model):
    value = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'base_import_tests_models_char_noreadonly'


class BaseImportTestsModelsCharReadonly(models.Model):
    value = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'base_import_tests_models_char_readonly'


class BaseImportTestsModelsCharRequired(models.Model):
    value = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'base_import_tests_models_char_required'


class BaseImportTestsModelsCharStates(models.Model):
    value = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'base_import_tests_models_char_states'


class BaseImportTestsModelsCharStillreadonly(models.Model):
    value = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'base_import_tests_models_char_stillreadonly'


class BaseImportTestsModelsComplex(models.Model):
    f = models.FloatField(blank=True, null=True)
    m = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c = models.CharField(max_length=200, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    d = models.DateField(blank=True, null=True)
    dt = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'base_import_tests_models_complex'


class BaseImportTestsModelsFloat(models.Model):
    value = models.FloatField(blank=True, null=True)
    value2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'base_import_tests_models_float'


class BaseImportTestsModelsM2O(models.Model):
    value = models.ForeignKey('BaseImportTestsModelsM2ORelated',    models.DO_NOTHING, related_name="+", db_column='value', blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'base_import_tests_models_m2o'


class BaseImportTestsModelsM2ORelated(models.Model):
    value = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'base_import_tests_models_m2o_related'


class BaseImportTestsModelsM2ORequired(models.Model):
    value = models.ForeignKey('BaseImportTestsModelsM2ORequiredRelated',    models.DO_NOTHING, related_name="+", db_column='value')
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'base_import_tests_models_m2o_required'


class BaseImportTestsModelsM2ORequiredRelated(models.Model):
    value = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'base_import_tests_models_m2o_required_related'


class BaseImportTestsModelsO2M(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'base_import_tests_models_o2m'


class BaseImportTestsModelsO2MChild(models.Model):
    parent = models.ForeignKey(BaseImportTestsModelsO2M,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    value = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'base_import_tests_models_o2m_child'


class BaseImportTestsModelsPreview(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    somevalue = models.IntegerField()
    othervalue = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'base_import_tests_models_preview'


class BaseLanguageExport(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    lang = models.CharField(max_length=200)
    format = models.CharField(max_length=200)
    data = models.BinaryField(blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'base_language_export'


class BaseLanguageImport(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=6)
    data = models.BinaryField()
    filename = models.CharField(max_length=200)
    overwrite = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'base_language_import'


class BaseLanguageInstall(models.Model):
    lang = models.CharField(max_length=200)
    overwrite = models.BooleanField(blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'base_language_install'


class BaseLanguageInstallWebsiteRel(models.Model):
    base_language_install = models.OneToOneField(BaseLanguageInstall,    models.DO_NOTHING, related_name="+", primary_key=True)
    website = models.ForeignKey('Website',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'base_language_install_website_rel'
        unique_together = (('base_language_install', 'website'),)


class BaseModuleUninstall(models.Model):
    show_all = models.BooleanField(blank=True, null=True)
    module = models.ForeignKey('IrModuleModule',    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'base_module_uninstall'


class BaseModuleUpdate(models.Model):
    updated = models.IntegerField()
    added = models.IntegerField()
    state = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'base_module_update'


class BaseModuleUpgrade(models.Model):
    module_info = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'base_module_upgrade'


class BasePartnerMergeAutomaticWizard(models.Model):
    group_by_email = models.BooleanField(blank=True, null=True)
    group_by_name = models.BooleanField(blank=True, null=True)
    group_by_is_company = models.BooleanField(blank=True, null=True)
    group_by_vat = models.BooleanField(blank=True, null=True)
    group_by_parent_id = models.BooleanField(blank=True, null=True)
    state = models.CharField(max_length=200)
    number_group = models.IntegerField()
    current_line = models.ForeignKey('BasePartnerMergeLine',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    dst_partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    exclude_contact = models.BooleanField(blank=True, null=True)
    exclude_journal_item = models.BooleanField(blank=True, null=True)
    maximum_group = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'base_partner_merge_automatic_wizard'


class BasePartnerMergeAutomaticWizardResPartnerRel(models.Model):
    base_partner_merge_automatic_wizard = models.OneToOneField(BasePartnerMergeAutomaticWizard,    models.DO_NOTHING, related_name="+", primary_key=True)
    res_partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'base_partner_merge_automatic_wizard_res_partner_rel'
        unique_together = (('base_partner_merge_automatic_wizard', 'res_partner'),)


class BasePartnerMergeLine(models.Model):
    wizard = models.ForeignKey(BasePartnerMergeAutomaticWizard,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    min_id = models.IntegerField()
    aggr_ids = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'base_partner_merge_line'


class BaseUpdateTranslations(models.Model):
    lang = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'base_update_translations'


class BudgetBudget(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    name = models.CharField(max_length=200)
    creating_user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    date_from = models.DateField()
    date_to = models.DateField()
    state = models.CharField(max_length=200)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'budget_budget'


class BudgetLines(models.Model):
    budget = models.ForeignKey(BudgetBudget,    models.DO_NOTHING, related_name="+")
    analytic_account = models.ForeignKey(AccountAnalyticAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    general_budget = models.ForeignKey(AccountBudgetPost,    models.DO_NOTHING, related_name="+")
    date_from = models.DateField()
    date_to = models.DateField()
    paid_date = models.DateField(blank=True, null=True)
    planned_amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'budget_lines'


class BusBus(models.Model):
    channel = models.CharField(max_length=200, blank=True, null=True)
    message = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'bus_bus'


class BusPresence(models.Model):
    user = models.OneToOneField('ResUsers',    models.DO_NOTHING, related_name="+")
    last_poll = models.DateTimeField(blank=True, null=True)
    last_presence = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'bus_presence'


class CalendarAlarm(models.Model):
    name = models.CharField(max_length=200)
    alarm_type = models.CharField(max_length=200)
    duration = models.IntegerField()
    interval = models.CharField(max_length=200)
    duration_minutes = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'calendar_alarm'


class CalendarAlarmCalendarEventRel(models.Model):
    calendar_event = models.OneToOneField('CalendarEvent',    models.DO_NOTHING, related_name="+", primary_key=True)
    calendar_alarm = models.ForeignKey(CalendarAlarm,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'calendar_alarm_calendar_event_rel'
        unique_together = (('calendar_event', 'calendar_alarm'),)


class CalendarAttendee(models.Model):
    event = models.ForeignKey('CalendarEvent',    models.DO_NOTHING, related_name="+")
    partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+")
    state = models.CharField(max_length=200, blank=True, null=True)
    common_name = models.CharField(max_length=200, blank=True, null=True)
    availability = models.CharField(max_length=200, blank=True, null=True)
    access_token = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'calendar_attendee'


class CalendarContacts(models.Model):
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+")
    partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+")
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'calendar_contacts'
        unique_together = (('user', 'partner'),)


class CalendarEvent(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    name = models.CharField(max_length=200)
    start = models.DateTimeField()
    stop = models.DateTimeField()
    allday = models.BooleanField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    stop_date = models.DateField(blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    privacy = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True, null=True)
    show_as = models.CharField(max_length=200)
    res_id = models.IntegerField()
    res_model = models.ForeignKey('IrModel',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    res_model_0 = models.CharField(db_column='res_model', max_length=200, blank=True, null=True)  # Field renamed because of name conflict.
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    recurrency = models.BooleanField(blank=True, null=True)
    recurrence = models.ForeignKey('CalendarRecurrence',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    follow_recurrence = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    applicant = models.ForeignKey('HrApplicant',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    opportunity = models.ForeignKey('CrmLead',    models.DO_NOTHING, related_name="+", blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'calendar_event'


class CalendarEventResPartnerRel(models.Model):
    calendar_event = models.OneToOneField(CalendarEvent,    models.DO_NOTHING, related_name="+", primary_key=True)
    res_partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'calendar_event_res_partner_rel'
        unique_together = (('calendar_event', 'res_partner'),)


class CalendarEventType(models.Model):
    name = models.CharField(unique=True, max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'calendar_event_type'


class CalendarRecurrence(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    base_event = models.ForeignKey(CalendarEvent,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    event_tz = models.CharField(max_length=200, blank=True, null=True)
    rrule = models.CharField(max_length=200, blank=True, null=True)
    rrule_type = models.CharField(max_length=200, blank=True, null=True)
    end_type = models.CharField(max_length=200, blank=True, null=True)
    interval = models.IntegerField()
    count = models.IntegerField()
    mo = models.BooleanField(blank=True, null=True)
    tu = models.BooleanField(blank=True, null=True)
    we = models.BooleanField(blank=True, null=True)
    th = models.BooleanField(blank=True, null=True)
    fr = models.BooleanField(blank=True, null=True)
    sa = models.BooleanField(blank=True, null=True)
    su = models.BooleanField(blank=True, null=True)
    month_by = models.CharField(max_length=200, blank=True, null=True)
    day = models.IntegerField()
    weekday = models.CharField(max_length=200, blank=True, null=True)
    byday = models.CharField(max_length=200, blank=True, null=True)
    until = models.DateField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'calendar_recurrence'


class CashBoxOut(models.Model):
    name = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cash_box_out'


class CashFlowReport(models.Model):
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    target_move = models.CharField(max_length=200)
    enable_filter = models.BooleanField(blank=True, null=True)
    account_report = models.ForeignKey(AccountFinancialReport,    models.DO_NOTHING, related_name="+")
    label_filter = models.CharField(max_length=200, blank=True, null=True)
    filter_cmp = models.CharField(max_length=200)
    date_from_cmp = models.DateField(blank=True, null=True)
    date_to_cmp = models.DateField(blank=True, null=True)
    debit_credit = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cash_flow_report'


class CertCert(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cert_cert'


class ChangePasswordUser(models.Model):
    wizard = models.ForeignKey('ChangePasswordWizard',    models.DO_NOTHING, related_name="+")
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+")
    user_login = models.CharField(max_length=200, blank=True, null=True)
    new_passwd = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'change_password_user'


class ChangePasswordWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'change_password_wizard'


class ChangeProductionQty(models.Model):
    mo = models.ForeignKey('MrpProduction',    models.DO_NOTHING, related_name="+")
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'change_production_qty'


class ConfirmStockSms(models.Model):
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'confirm_stock_sms'


class ContractHistory(models.Model):
    employee_id = models.CharField(max_length=200, blank=True, null=True)
    employee_name = models.CharField(max_length=200, blank=True, null=True)
    updated_date = models.DateField(blank=True, null=True)
    changed_field = models.CharField(max_length=200, blank=True, null=True)
    current_value = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'contract_history'


class CrmConvertLeadMassLeadRel(models.Model):
    crm_lead2opportunity_partner_mass = models.OneToOneField('CrmLead2OpportunityPartnerMass',    models.DO_NOTHING, related_name="+", primary_key=True)
    crm_lead = models.ForeignKey('CrmLead',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'crm_convert_lead_mass_lead_rel'
        unique_together = (('crm_lead2opportunity_partner_mass', 'crm_lead'),)


class CrmIapLeadHelpers(models.Model):
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'crm_iap_lead_helpers'


class CrmIapLeadIndustry(models.Model):
    name = models.CharField(unique=True, max_length=200)
    reveal_id = models.CharField(max_length=200)
    color = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'crm_iap_lead_industry'


class CrmIapLeadIndustryCrmIapLeadMiningRequestRel(models.Model):
    crm_iap_lead_mining_request = models.OneToOneField('CrmIapLeadMiningRequest',    models.DO_NOTHING, related_name="+", primary_key=True)
    crm_iap_lead_industry = models.ForeignKey(CrmIapLeadIndustry,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'crm_iap_lead_industry_crm_iap_lead_mining_request_rel'
        unique_together = (('crm_iap_lead_mining_request', 'crm_iap_lead_industry'),)


class CrmIapLeadMiningRequest(models.Model):
    name = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    lead_number = models.IntegerField()
    search_type = models.CharField(max_length=200)
    error = models.TextField(blank=True, null=True)
    lead_type = models.CharField(max_length=200)
    team = models.ForeignKey('CrmTeam',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    filter_on_size = models.BooleanField(blank=True, null=True)
    company_size_min = models.IntegerField()
    company_size_max = models.IntegerField()
    contact_number = models.IntegerField()
    contact_filter_type = models.CharField(max_length=200, blank=True, null=True)
    preferred_role = models.ForeignKey('CrmIapLeadRole',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    seniority = models.ForeignKey('CrmIapLeadSeniority',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'crm_iap_lead_mining_request'


class CrmIapLeadMiningRequestCrmIapLeadRoleRel(models.Model):
    crm_iap_lead_mining_request = models.OneToOneField(CrmIapLeadMiningRequest,    models.DO_NOTHING, related_name="+", primary_key=True)
    crm_iap_lead_role = models.ForeignKey('CrmIapLeadRole',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'crm_iap_lead_mining_request_crm_iap_lead_role_rel'
        unique_together = (('crm_iap_lead_mining_request', 'crm_iap_lead_role'),)


class CrmIapLeadMiningRequestCrmTagRel(models.Model):
    crm_iap_lead_mining_request = models.OneToOneField(CrmIapLeadMiningRequest,    models.DO_NOTHING, related_name="+", primary_key=True)
    crm_tag = models.ForeignKey('CrmTag',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'crm_iap_lead_mining_request_crm_tag_rel'
        unique_together = (('crm_iap_lead_mining_request', 'crm_tag'),)


class CrmIapLeadMiningRequestResCountryRel(models.Model):
    crm_iap_lead_mining_request = models.OneToOneField(CrmIapLeadMiningRequest,    models.DO_NOTHING, related_name="+", primary_key=True)
    res_country = models.ForeignKey('ResCountry',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'crm_iap_lead_mining_request_res_country_rel'
        unique_together = (('crm_iap_lead_mining_request', 'res_country'),)


class CrmIapLeadMiningRequestResCountryStateRel(models.Model):
    crm_iap_lead_mining_request = models.OneToOneField(CrmIapLeadMiningRequest,    models.DO_NOTHING, related_name="+", primary_key=True)
    res_country_state = models.ForeignKey('ResCountryState',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'crm_iap_lead_mining_request_res_country_state_rel'
        unique_together = (('crm_iap_lead_mining_request', 'res_country_state'),)


class CrmIapLeadRole(models.Model):
    name = models.CharField(unique=True, max_length=200)
    reveal_id = models.CharField(max_length=200)
    color = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'crm_iap_lead_role'


class CrmIapLeadSeniority(models.Model):
    name = models.CharField(unique=True, max_length=200)
    reveal_id = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'crm_iap_lead_seniority'


class CrmLead(models.Model):
    campaign = models.ForeignKey('UtmCampaign',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    source = models.ForeignKey('UtmSource',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    medium = models.ForeignKey('UtmMedium',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    email_normalized = models.CharField(max_length=200, blank=True, null=True)
    message_bounce = models.IntegerField()
    email_cc = models.CharField(max_length=200, blank=True, null=True)
    message_main_attachment = models.ForeignKey('IrAttachment',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    phone_sanitized = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200)
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    referred = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    type = models.CharField(max_length=200)
    priority = models.CharField(max_length=200, blank=True, null=True)
    team = models.ForeignKey('CrmTeam',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    stage = models.ForeignKey('CrmStage',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    color = models.IntegerField()
    expected_revenue = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prorated_revenue = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    recurring_revenue = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    recurring_plan = models.ForeignKey('CrmRecurringPlan',    models.DO_NOTHING, related_name="+", db_column='recurring_plan', blank=True, null=True)
    recurring_revenue_monthly = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    recurring_revenue_monthly_prorated = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    date_closed = models.DateTimeField(blank=True, null=True)
    date_action_last = models.DateTimeField(blank=True, null=True)
    date_open = models.DateTimeField(blank=True, null=True)
    day_open = models.FloatField(blank=True, null=True)
    day_close = models.FloatField(blank=True, null=True)
    date_last_stage_update = models.DateTimeField(blank=True, null=True)
    date_conversion = models.DateTimeField(blank=True, null=True)
    date_deadline = models.DateField(blank=True, null=True)
    partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    contact_name = models.CharField(max_length=200, blank=True, null=True)
    partner_name = models.CharField(max_length=200, blank=True, null=True)
    function = models.CharField(max_length=200, blank=True, null=True)
    title = models.ForeignKey('ResPartnerTitle',    models.DO_NOTHING, related_name="+", db_column='title', blank=True, null=True)
    email_from = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    mobile = models.CharField(max_length=200, blank=True, null=True)
    phone_state = models.CharField(max_length=200, blank=True, null=True)
    email_state = models.CharField(max_length=200, blank=True, null=True)
    website = models.CharField(max_length=200, blank=True, null=True)
    lang = models.ForeignKey('ResLang',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    street = models.CharField(max_length=200, blank=True, null=True)
    street2 = models.CharField(max_length=200, blank=True, null=True)
    zip = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.ForeignKey('ResCountryState',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    country = models.ForeignKey('ResCountry',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    probability = models.FloatField(blank=True, null=True)
    automated_probability = models.FloatField(blank=True, null=True)
    lost_reason = models.ForeignKey('CrmLostReason',    models.DO_NOTHING, related_name="+", db_column='lost_reason', blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    won_status = models.CharField(max_length=2000, blank=True, null=True)
    days_to_convert = models.FloatField(blank=True, null=True)
    days_exceeding_closing = models.FloatField(blank=True, null=True)
    reveal_id = models.CharField(max_length=200, blank=True, null=True)
    lead_mining_request = models.ForeignKey(CrmIapLeadMiningRequest,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    iap_enrich_done = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'crm_lead'


class CrmLead2OpportunityPartner(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    action = models.CharField(max_length=200, blank=True, null=True)
    lead = models.ForeignKey(CrmLead,    models.DO_NOTHING, related_name="+")
    partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    team = models.ForeignKey('CrmTeam',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    force_assignment = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'crm_lead2opportunity_partner'


class CrmLead2OpportunityPartnerMass(models.Model):
    lead = models.ForeignKey(CrmLead,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    deduplicate = models.BooleanField(blank=True, null=True)
    action = models.CharField(max_length=200, blank=True, null=True)
    force_assignment = models.BooleanField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    team = models.ForeignKey('CrmTeam',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'crm_lead2opportunity_partner_mass'


class CrmLead2OpportunityPartnerMassResUsersRel(models.Model):
    crm_lead2opportunity_partner_mass = models.OneToOneField(CrmLead2OpportunityPartnerMass,    models.DO_NOTHING, related_name="+", primary_key=True)
    res_users = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'crm_lead2opportunity_partner_mass_res_users_rel'
        unique_together = (('crm_lead2opportunity_partner_mass', 'res_users'),)


class CrmLeadCrmLead2OpportunityPartnerMassRel(models.Model):
    crm_lead2opportunity_partner_mass = models.OneToOneField(CrmLead2OpportunityPartnerMass,    models.DO_NOTHING, related_name="+", primary_key=True)
    crm_lead = models.ForeignKey(CrmLead,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'crm_lead_crm_lead2opportunity_partner_mass_rel'
        unique_together = (('crm_lead2opportunity_partner_mass', 'crm_lead'),)


class CrmLeadCrmLead2OpportunityPartnerRel(models.Model):
    crm_lead2opportunity_partner = models.OneToOneField(CrmLead2OpportunityPartner,    models.DO_NOTHING, related_name="+", primary_key=True)
    crm_lead = models.ForeignKey(CrmLead,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'crm_lead_crm_lead2opportunity_partner_rel'
        unique_together = (('crm_lead2opportunity_partner', 'crm_lead'),)


class CrmLeadLost(models.Model):
    lost_reason = models.ForeignKey('CrmLostReason',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'crm_lead_lost'


class CrmLeadScoringFrequency(models.Model):
    variable = models.CharField(max_length=200, blank=True, null=True)
    value = models.CharField(max_length=200, blank=True, null=True)
    won_count = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    lost_count = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    team = models.ForeignKey('CrmTeam',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'crm_lead_scoring_frequency'


class CrmLeadScoringFrequencyField(models.Model):
    field = models.ForeignKey('IrModelFields',    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'crm_lead_scoring_frequency_field'


class CrmLeadWebsiteVisitorRel(models.Model):
    crm_lead = models.OneToOneField(CrmLead,    models.DO_NOTHING, related_name="+", primary_key=True)
    website_visitor = models.ForeignKey('WebsiteVisitor',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'crm_lead_website_visitor_rel'
        unique_together = (('crm_lead', 'website_visitor'),)


class CrmLostReason(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'crm_lost_reason'


class CrmMergeOpportunity(models.Model):
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    team = models.ForeignKey('CrmTeam',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'crm_merge_opportunity'


class CrmQuotationPartner(models.Model):
    action = models.CharField(max_length=200)
    lead = models.ForeignKey(CrmLead,    models.DO_NOTHING, related_name="+")
    partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'crm_quotation_partner'


class CrmRecurringPlan(models.Model):
    name = models.CharField(max_length=200)
    number_of_months = models.IntegerField()
    active = models.BooleanField(blank=True, null=True)
    sequence = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'crm_recurring_plan'


class CrmStage(models.Model):
    name = models.CharField(max_length=200)
    sequence = models.IntegerField()
    is_won = models.BooleanField(blank=True, null=True)
    requirements = models.TextField(blank=True, null=True)
    team = models.ForeignKey('CrmTeam',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    fold = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'crm_stage'


class CrmTag(models.Model):
    name = models.CharField(unique=True, max_length=200)
    color = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'crm_tag'


class CrmTagRel(models.Model):
    lead = models.OneToOneField(CrmLead,    models.DO_NOTHING, related_name="+", primary_key=True)
    tag = models.ForeignKey(CrmTag,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'crm_tag_rel'
        unique_together = (('lead', 'tag'),)


class CrmTeam(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    name = models.CharField(max_length=200)
    sequence = models.IntegerField()
    active = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    color = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    use_quotations = models.BooleanField(blank=True, null=True)
    invoiced_target = models.FloatField(blank=True, null=True)
    use_leads = models.BooleanField(blank=True, null=True)
    use_opportunities = models.BooleanField(blank=True, null=True)
    alias = models.ForeignKey('MailAlias',    models.DO_NOTHING, related_name="+")
    amazon_team = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'crm_team'


class CrossoveredBudget(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    name = models.CharField(max_length=200)
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    date_from = models.DateField()
    date_to = models.DateField()
    state = models.CharField(max_length=200)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'crossovered_budget'


class CrossoveredBudgetLines(models.Model):
    crossovered_budget = models.ForeignKey(CrossoveredBudget,    models.DO_NOTHING, related_name="+")
    analytic_account = models.ForeignKey(AccountAnalyticAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    general_budget = models.ForeignKey(AccountBudgetPost,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    date_from = models.DateField()
    date_to = models.DateField()
    paid_date = models.DateField(blank=True, null=True)
    planned_amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    crossovered_budget_state = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_studio_char_field_7dj0f = models.CharField(db_column='x_studio_char_field_7dj0F', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_budget_variance = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'crossovered_budget_lines'


class DecimalPrecision(models.Model):
    name = models.CharField(unique=True, max_length=200)
    digits = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'decimal_precision'


class DepartmentHistory(models.Model):
    employee_id = models.CharField(max_length=200, blank=True, null=True)
    employee_name = models.CharField(max_length=200, blank=True, null=True)
    changed_field = models.CharField(max_length=200, blank=True, null=True)
    updated_date = models.DateField(blank=True, null=True)
    current_value = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'department_history'


class DigestDigest(models.Model):
    name = models.CharField(max_length=200)
    periodicity = models.CharField(max_length=200)
    next_run_date = models.DateField(blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    kpi_res_users_connected = models.BooleanField(blank=True, null=True)
    kpi_mail_message_total = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    kpi_account_total_revenue = models.BooleanField(blank=True, null=True)
    kpi_all_sale_total = models.BooleanField(blank=True, null=True)
    kpi_account_bank_cash = models.BooleanField(blank=True, null=True)
    kpi_hr_recruitment_new_colleagues = models.BooleanField(blank=True, null=True)
    kpi_project_task_opened = models.BooleanField(blank=True, null=True)
    kpi_crm_lead_created = models.BooleanField(blank=True, null=True)
    kpi_crm_opportunities_won = models.BooleanField(blank=True, null=True)
    kpi_website_sale_total = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'digest_digest'


class DigestDigestResUsersRel(models.Model):
    digest_digest = models.OneToOneField(DigestDigest,    models.DO_NOTHING, related_name="+", primary_key=True)
    res_users = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'digest_digest_res_users_rel'
        unique_together = (('digest_digest', 'res_users'),)


class DigestTip(models.Model):
    sequence = models.IntegerField()
    name = models.CharField(max_length=200, blank=True, null=True)
    tip_description = models.TextField(blank=True, null=True)
    group = models.ForeignKey('ResGroups',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'digest_tip'


class DigestTipResUsersRel(models.Model):
    digest_tip = models.OneToOneField(DigestTip,    models.DO_NOTHING, related_name="+", primary_key=True)
    res_users = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'digest_tip_res_users_rel'
        unique_together = (('digest_tip', 'res_users'),)


class DisciplinaryAction(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200)
    employee_name = models.ForeignKey('HrEmployee',    models.DO_NOTHING, related_name="+", db_column='employee_name')
    department_name = models.ForeignKey('HrDepartment',    models.DO_NOTHING, related_name="+", db_column='department_name')
    discipline_reason = models.ForeignKey('DisciplineCategory',    models.DO_NOTHING, related_name="+", db_column='discipline_reason')
    explanation = models.TextField(blank=True, null=True)
    action = models.ForeignKey('DisciplineCategory',    models.DO_NOTHING, related_name="+", db_column='action', blank=True, null=True)
    warning_letter = models.TextField(blank=True, null=True)
    suspension_letter = models.TextField(blank=True, null=True)
    termination_letter = models.TextField(blank=True, null=True)
    warning = models.IntegerField()
    action_details = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    joined_date = models.DateField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'disciplinary_action'


class DisciplinaryActionIrAttachmentRel(models.Model):
    disciplinary_action = models.OneToOneField(DisciplinaryAction,    models.DO_NOTHING, related_name="+", primary_key=True)
    ir_attachment = models.ForeignKey('IrAttachment',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'disciplinary_action_ir_attachment_rel'
        unique_together = (('disciplinary_action', 'ir_attachment'),)


class DisciplineCategory(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    category_type = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'discipline_category'


class DmsAccRepExportWizardFormatRel(models.Model):
    account_reports_export_wizard = models.OneToOneField(AccountReportsExportWizard,    models.DO_NOTHING, related_name="+", primary_key=True)
    account_reports_export_wizard_format = models.ForeignKey(AccountReportsExportWizardFormat,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'dms_acc_rep_export_wizard_format_rel'
        unique_together = (('account_reports_export_wizard', 'account_reports_export_wizard_format'),)


class DynamicBalanceSheetReport(models.Model):
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    display_account = models.CharField(max_length=200)
    target_move = models.CharField(max_length=200)
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'dynamic_balance_sheet_report'


class EmailTemplateAttachmentRel(models.Model):
    email_template = models.OneToOneField('MailTemplate',    models.DO_NOTHING, related_name="+", primary_key=True)
    attachment = models.ForeignKey('IrAttachment',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'email_template_attachment_rel'
        unique_together = (('email_template', 'attachment'),)


class EmpNontechSkills(models.Model):
    applicant = models.ForeignKey('HrApplicant',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    employee = models.ForeignKey('HrEmployee',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    nontech = models.ForeignKey('NontechNontech',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    levels = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'emp_nontech_skills'


class EmpTechSkills(models.Model):
    applicant = models.ForeignKey('HrApplicant',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    employee = models.ForeignKey('HrEmployee',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    tech = models.ForeignKey('TechTech',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    levels = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'emp_tech_skills'


class EmployeeCategoryRel(models.Model):
    emp = models.OneToOneField('HrEmployee',    models.DO_NOTHING, related_name="+", primary_key=True)
    category = models.ForeignKey('HrEmployeeCategory',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'employee_category_rel'
        unique_together = (('emp', 'category'),)


class EmployeeCertification(models.Model):
    applicant = models.ForeignKey('HrApplicant',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    employee = models.ForeignKey('HrEmployee',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    course = models.ForeignKey(CertCert,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    levels = models.CharField(max_length=200, blank=True, null=True)
    year = models.DateField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'employee_certification'


class EmployeeEducation(models.Model):
    applicant = models.ForeignKey('HrApplicant',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    employee = models.ForeignKey('HrEmployee',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    type = models.ForeignKey('HrRecruitmentDegree',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    institute = models.ForeignKey('HrInstitute',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    score = models.CharField(max_length=200, blank=True, null=True)
    qualified_year = models.DateField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'employee_education'


class EmployeeProfession(models.Model):
    applicant = models.ForeignKey('HrApplicant',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    employee = models.ForeignKey('HrEmployee',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    job = models.ForeignKey('HrJob',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'employee_profession'


class ExpiryPickingConfirmation(models.Model):
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    workorder = models.ForeignKey('MrpWorkorder',    models.DO_NOTHING, related_name="+", blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'expiry_picking_confirmation'


class ExpiryPickingConfirmationMrpProductionRel(models.Model):
    expiry_picking_confirmation = models.OneToOneField(ExpiryPickingConfirmation,    models.DO_NOTHING, related_name="+", primary_key=True)
    mrp_production = models.ForeignKey('MrpProduction',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'expiry_picking_confirmation_mrp_production_rel'
        unique_together = (('expiry_picking_confirmation', 'mrp_production'),)


class ExpiryPickingConfirmationStockPickingRel(models.Model):
    expiry_picking_confirmation = models.OneToOneField(ExpiryPickingConfirmation,    models.DO_NOTHING, related_name="+", primary_key=True)
    stock_picking = models.ForeignKey('StockPicking',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'expiry_picking_confirmation_stock_picking_rel'
        unique_together = (('expiry_picking_confirmation', 'stock_picking'),)


class ExpiryPickingConfirmationStockProductionLotRel(models.Model):
    expiry_picking_confirmation = models.OneToOneField(ExpiryPickingConfirmation,    models.DO_NOTHING, related_name="+", primary_key=True)
    stock_production_lot = models.ForeignKey('StockProductionLot',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'expiry_picking_confirmation_stock_production_lot_rel'
        unique_together = (('expiry_picking_confirmation', 'stock_production_lot'),)


class FetchmailServer(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    server = models.CharField(max_length=200, blank=True, null=True)
    port = models.IntegerField()
    server_type = models.CharField(max_length=200)
    is_ssl = models.BooleanField(blank=True, null=True)
    attach = models.BooleanField(blank=True, null=True)
    original = models.BooleanField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    user = models.CharField(max_length=200, blank=True, null=True)
    password = models.CharField(max_length=200, blank=True, null=True)
    object = models.ForeignKey('IrModel',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    priority = models.IntegerField()
    configuration = models.TextField(blank=True, null=True)
    script = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'fetchmail_server'


class FinancialReport(models.Model):
    target_move = models.CharField(max_length=200)
    view_format = models.CharField(max_length=200, blank=True, null=True)
    enable_filter = models.BooleanField(blank=True, null=True)
    account_report = models.ForeignKey(AccountFinancialReport,    models.DO_NOTHING, related_name="+")
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    debit_credit = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'financial_report'


class FollowupLine(models.Model):
    name = models.CharField(max_length=200)
    sequence = models.IntegerField()
    delay = models.IntegerField()
    followup = models.ForeignKey(AccountFollowup,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'followup_line'


class FollowupSend(models.Model):
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'followup_send'


class FollowupSendResPartnerRel(models.Model):
    followup_send = models.OneToOneField(FollowupSend,    models.DO_NOTHING, related_name="+", primary_key=True)
    res_partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'followup_send_res_partner_rel'
        unique_together = (('followup_send', 'res_partner'),)


class GamificationBadge(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    name = models.CharField(max_length=200)
    active = models.BooleanField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    level = models.CharField(max_length=200, blank=True, null=True)
    rule_auth = models.CharField(max_length=200)
    rule_max = models.BooleanField(blank=True, null=True)
    rule_max_number = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    is_published = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'gamification_badge'


class GamificationBadgeRuleBadgeRel(models.Model):
    badge1 = models.OneToOneField(GamificationBadge,    models.DO_NOTHING, related_name="+", primary_key=True)
    badge2 = models.ForeignKey(GamificationBadge,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'gamification_badge_rule_badge_rel'
        unique_together = (('badge1', 'badge2'),)


class GamificationBadgeUser(models.Model):
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+")
    sender = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    badge = models.ForeignKey(GamificationBadge,    models.DO_NOTHING, related_name="+")
    challenge = models.ForeignKey('GamificationChallenge',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    level = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    employee = models.ForeignKey('HrEmployee',    models.DO_NOTHING, related_name="+", blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'gamification_badge_user'


class GamificationBadgeUserWizard(models.Model):
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    badge = models.ForeignKey(GamificationBadge,    models.DO_NOTHING, related_name="+")
    comment = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    employee = models.ForeignKey('HrEmployee',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'gamification_badge_user_wizard'


class GamificationChallenge(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=200)
    manager = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    user_domain = models.CharField(max_length=200, blank=True, null=True)
    period = models.CharField(max_length=200)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    reward = models.ForeignKey(GamificationBadge,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    reward_first = models.ForeignKey(GamificationBadge,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    reward_second = models.ForeignKey(GamificationBadge,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    reward_third = models.ForeignKey(GamificationBadge,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    reward_failure = models.BooleanField(blank=True, null=True)
    reward_realtime = models.BooleanField(blank=True, null=True)
    visibility_mode = models.CharField(max_length=200)
    report_message_frequency = models.CharField(max_length=200)
    report_message_group = models.ForeignKey('MailChannel',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    report_template = models.ForeignKey('MailTemplate',    models.DO_NOTHING, related_name="+")
    remind_update_delay = models.IntegerField()
    last_report_date = models.DateField(blank=True, null=True)
    next_report_date = models.DateField(blank=True, null=True)
    challenge_category = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'gamification_challenge'


class GamificationChallengeLine(models.Model):
    challenge = models.ForeignKey(GamificationChallenge,    models.DO_NOTHING, related_name="+")
    definition = models.ForeignKey('GamificationGoalDefinition',    models.DO_NOTHING, related_name="+")
    sequence = models.IntegerField()
    target_goal = models.FloatField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'gamification_challenge_line'


class GamificationChallengeUsersRel(models.Model):
    gamification_challenge = models.OneToOneField(GamificationChallenge,    models.DO_NOTHING, related_name="+", primary_key=True)
    res_users = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'gamification_challenge_users_rel'
        unique_together = (('gamification_challenge', 'res_users'),)


class GamificationGoal(models.Model):
    definition = models.ForeignKey('GamificationGoalDefinition',    models.DO_NOTHING, related_name="+")
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+")
    line = models.ForeignKey(GamificationChallengeLine,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    challenge = models.ForeignKey(GamificationChallenge,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    target_goal = models.FloatField()
    current = models.FloatField()
    state = models.CharField(max_length=200)
    to_update = models.BooleanField(blank=True, null=True)
    closed = models.BooleanField(blank=True, null=True)
    remind_update_delay = models.IntegerField()
    last_update = models.DateField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'gamification_goal'


class GamificationGoalDefinition(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    monetary = models.BooleanField(blank=True, null=True)
    suffix = models.CharField(max_length=200, blank=True, null=True)
    computation_mode = models.CharField(max_length=200)
    display_mode = models.CharField(max_length=200)
    model = models.ForeignKey('IrModel',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    field = models.ForeignKey('IrModelFields',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    field_date = models.ForeignKey('IrModelFields',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    domain = models.CharField(max_length=200)
    batch_mode = models.BooleanField(blank=True, null=True)
    batch_distinctive_field = models.ForeignKey('IrModelFields',    models.DO_NOTHING, related_name="+", db_column='batch_distinctive_field', blank=True, null=True)
    batch_user_expression = models.CharField(max_length=200, blank=True, null=True)
    compute_code = models.TextField(blank=True, null=True)
    condition = models.CharField(max_length=200)
    action = models.ForeignKey('IrActWindow',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    res_id_field = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'gamification_goal_definition'


class GamificationGoalWizard(models.Model):
    goal = models.ForeignKey(GamificationGoal,    models.DO_NOTHING, related_name="+")
    current = models.FloatField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'gamification_goal_wizard'


class GamificationInvitedUserIdsRel(models.Model):
    gamification_challenge = models.OneToOneField(GamificationChallenge,    models.DO_NOTHING, related_name="+", primary_key=True)
    res_users = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'gamification_invited_user_ids_rel'
        unique_together = (('gamification_challenge', 'res_users'),)


class GamificationKarmaRank(models.Model):
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    description_motivational = models.TextField(blank=True, null=True)
    karma_min = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'gamification_karma_rank'


class GamificationKarmaTracking(models.Model):
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+")
    old_value = models.IntegerField()
    new_value = models.IntegerField()
    consolidated = models.BooleanField(blank=True, null=True)
    tracking_date = models.DateField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'gamification_karma_tracking'


class HrApplicant(models.Model):
    campaign = models.ForeignKey('UtmCampaign',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    source = models.ForeignKey('UtmSource',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    medium = models.ForeignKey('UtmMedium',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    email_cc = models.CharField(max_length=200, blank=True, null=True)
    message_main_attachment = models.ForeignKey('IrAttachment',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    name = models.CharField(max_length=200)
    active = models.BooleanField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    email_from = models.CharField(max_length=128, blank=True, null=True)
    probability = models.FloatField(blank=True, null=True)
    partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    stage = models.ForeignKey('HrRecruitmentStage',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    last_stage = models.ForeignKey('HrRecruitmentStage',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    date_closed = models.DateTimeField(blank=True, null=True)
    date_open = models.DateTimeField(blank=True, null=True)
    date_last_stage_update = models.DateTimeField(blank=True, null=True)
    priority = models.CharField(max_length=200, blank=True, null=True)
    job = models.ForeignKey('HrJob',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    salary_proposed_extra = models.CharField(max_length=200, blank=True, null=True)
    salary_expected_extra = models.CharField(max_length=200, blank=True, null=True)
    salary_proposed = models.FloatField(blank=True, null=True)
    salary_expected = models.FloatField(blank=True, null=True)
    availability = models.DateField(blank=True, null=True)
    partner_name = models.CharField(max_length=200, blank=True, null=True)
    partner_phone = models.CharField(max_length=32, blank=True, null=True)
    partner_mobile = models.CharField(max_length=32, blank=True, null=True)
    type = models.ForeignKey('HrRecruitmentDegree',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    department = models.ForeignKey('HrDepartment',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    delay_close = models.FloatField(blank=True, null=True)
    color = models.IntegerField()
    emp = models.ForeignKey('HrEmployee',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    kanban_state = models.CharField(max_length=200)
    refuse_reason = models.ForeignKey('HrApplicantRefuseReason',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hr_applicant'


class HrApplicantCategory(models.Model):
    name = models.CharField(unique=True, max_length=200)
    color = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hr_applicant_category'


class HrApplicantHrApplicantCategoryRel(models.Model):
    hr_applicant = models.OneToOneField(HrApplicant,    models.DO_NOTHING, related_name="+", primary_key=True)
    hr_applicant_category = models.ForeignKey(HrApplicantCategory,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'hr_applicant_hr_applicant_category_rel'
        unique_together = (('hr_applicant', 'hr_applicant_category'),)


class HrApplicantRefuseReason(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hr_applicant_refuse_reason'


class HrAppraisal(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    employee = models.ForeignKey('HrEmployee',    models.DO_NOTHING, related_name="+")
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    department = models.ForeignKey('HrDepartment',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    date_close = models.DateField()
    state = models.CharField(max_length=200)
    meeting = models.ForeignKey(CalendarEvent,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    date_final_interview = models.DateField(blank=True, null=True)
    employee_feedback = models.TextField(blank=True, null=True)
    manager_feedback = models.TextField(blank=True, null=True)
    employee_feedback_published = models.BooleanField(blank=True, null=True)
    manager_feedback_published = models.BooleanField(blank=True, null=True)
    assessment_note = models.ForeignKey('HrAppraisalNote',    models.DO_NOTHING, related_name="+", db_column='assessment_note', blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_studio_organisational_goal = models.CharField(max_length=200, blank=True, null=True)
    x_studio_departmental_objective = models.CharField(max_length=200, blank=True, null=True)
    x_studio_1 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_1_1 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_2 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_3 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_2_1 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_3_1 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_1_2 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_2_2 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_3_2 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_1_3 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_2_3 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_1_4 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_2_4 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_3_3 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_1_5 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_2_5 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_3_4 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_1_6 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_2_6 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_3_5 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_1_7 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_2_7 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_3_6 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_comments = models.CharField(max_length=200, blank=True, null=True)
    x_studio_char_field_yopcj = models.CharField(db_column='x_studio_char_field_yOPcj', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_1_8 = models.BooleanField(blank=True, null=True)
    x_studio_2_8 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_3_7 = models.BooleanField(blank=True, null=True)
    x_studio_4 = models.BooleanField(blank=True, null=True)
    x_studio_5 = models.BooleanField(blank=True, null=True)
    x_studio_1_9 = models.BooleanField(blank=True, null=True)
    x_studio_4_1 = models.BooleanField(blank=True, null=True)
    x_studio_2_9 = models.BooleanField(blank=True, null=True)
    x_studio_3_8 = models.BooleanField(blank=True, null=True)
    x_studio_5_1 = models.BooleanField(blank=True, null=True)
    x_studio_4_2 = models.BooleanField(blank=True, null=True)
    x_studio_boolean_field_qebse = models.BooleanField(db_column='x_studio_boolean_field_qeBSe', blank=True, null=True)  # Field name made lowercase.
    x_studio_1_10 = models.BooleanField(blank=True, null=True)
    x_studio_5_2 = models.BooleanField(blank=True, null=True)
    x_studio_2_10 = models.BooleanField(blank=True, null=True)
    x_studio_3_9 = models.BooleanField(blank=True, null=True)
    x_studio_char_field_ugtss = models.CharField(db_column='x_studio_char_field_UgtSS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_2_11 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_1_11 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_2_13 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_3_10 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_3_11 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_2_14 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_1_12 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_3_12 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_2_12 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_1_13 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_1_14 = models.BooleanField(blank=True, null=True)
    x_studio_5_3 = models.BooleanField(blank=True, null=True)
    x_studio_3_13 = models.BooleanField(blank=True, null=True)
    x_studio_4_3 = models.BooleanField(blank=True, null=True)
    x_studio_2_15 = models.BooleanField(blank=True, null=True)
    x_studio_5_4 = models.BooleanField(blank=True, null=True)
    x_studio_3_14 = models.BooleanField(blank=True, null=True)
    x_studio_1_15 = models.BooleanField(blank=True, null=True)
    x_studio_2_16 = models.BooleanField(blank=True, null=True)
    x_studio_4_5 = models.BooleanField(blank=True, null=True)
    x_studio_5_5 = models.BooleanField(blank=True, null=True)
    x_studio_1_16 = models.BooleanField(blank=True, null=True)
    x_studio_3_15 = models.BooleanField(blank=True, null=True)
    x_studio_2_17 = models.BooleanField(blank=True, null=True)
    x_studio_4_4 = models.BooleanField(blank=True, null=True)
    x_studio_comments_1 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_2_18 = models.BooleanField(blank=True, null=True)
    x_studio_3_16 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_3_17 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_1_17 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_2_19 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_3_19 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_1_18 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_2_20 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_3_18 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_1_19 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_2_21 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_3_20 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_1_20 = models.BooleanField(blank=True, null=True)
    x_studio_2_22 = models.BooleanField(blank=True, null=True)
    x_studio_5_6 = models.BooleanField(blank=True, null=True)
    x_studio_4_6 = models.BooleanField(blank=True, null=True)
    x_studio_3_21 = models.BooleanField(blank=True, null=True)
    x_studio_1_21 = models.BooleanField(blank=True, null=True)
    x_studio_boolean_field_i15fv = models.BooleanField(db_column='x_studio_boolean_field_I15Fv', blank=True, null=True)  # Field name made lowercase.
    x_studio_3_22 = models.BooleanField(blank=True, null=True)
    x_studio_boolean_field_ukosk = models.BooleanField(db_column='x_studio_boolean_field_uKoSk', blank=True, null=True)  # Field name made lowercase.
    x_studio_2_23 = models.BooleanField(blank=True, null=True)
    x_studio_2_24 = models.BooleanField(blank=True, null=True)
    x_studio_3_23 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_1_22 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_2_25 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_3_24 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_2_26 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_3_25 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_3_26 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_1_23 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_2_27 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_3_27 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_1_24 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_2_28 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_3_28 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_comments_2 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_1_25 = models.BooleanField(blank=True, null=True)
    x_studio_2_29 = models.BooleanField(blank=True, null=True)
    x_studio_5_7 = models.BooleanField(blank=True, null=True)
    x_studio_3_29 = models.BooleanField(blank=True, null=True)
    x_studio_4_7 = models.BooleanField(blank=True, null=True)
    x_studio_1_26 = models.BooleanField(blank=True, null=True)
    x_studio_5_8 = models.BooleanField(blank=True, null=True)
    x_studio_2_30 = models.BooleanField(blank=True, null=True)
    x_studio_4_8 = models.BooleanField(blank=True, null=True)
    x_studio_3_30 = models.BooleanField(blank=True, null=True)
    x_studio_3_31 = models.BooleanField(blank=True, null=True)
    x_studio_2_31 = models.BooleanField(blank=True, null=True)
    x_studio_1_27 = models.BooleanField(blank=True, null=True)
    x_studio_5_9 = models.BooleanField(blank=True, null=True)
    x_studio_4_9 = models.BooleanField(blank=True, null=True)
    x_studio_unsatisfactory_1_to_15 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_marginal_16_to_25 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_good_26_to_35 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_very_good_36_to_45 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_excellent_46_to_50 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_remarkscomments = models.CharField(max_length=200, blank=True, null=True)
    x_studio_char_field_pjval = models.CharField(db_column='x_studio_char_field_pJvaL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_char_field_zixs6 = models.CharField(db_column='x_studio_char_field_ZIxs6', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_char_field_09b8n = models.CharField(db_column='x_studio_char_field_09B8n', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_char_field_exgki = models.CharField(db_column='x_studio_char_field_eXgkI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_date = models.DateField(blank=True, null=True)
    x_studio_date_1 = models.DateField(blank=True, null=True)
    x_studio_appraiser = models.ForeignKey('HrEmployee',    models.DO_NOTHING, related_name="+", db_column='x_studio_appraiser', blank=True, null=True)
    x_studio_appraisee = models.ForeignKey('HrEmployee',    models.DO_NOTHING, related_name="+", db_column='x_studio_appraisee', blank=True, null=True)
    x_studio_period_of_appraisal_to = models.CharField(max_length=200, blank=True, null=True)
    x_studio_company = models.CharField(max_length=200, blank=True, null=True)
    x_studio_1_date = models.DateField(blank=True, null=True)
    x_studio_institution_program = models.CharField(max_length=200, blank=True, null=True)
    x_studio_2_date = models.DateField(blank=True, null=True)
    x_studio_institution_program_1 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_institution_program_2 = models.DateField(blank=True, null=True)
    x_studio_3_date = models.DateField(blank=True, null=True)
    x_studio_institution_program_3 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_4_date = models.DateField(blank=True, null=True)
    x_studio_institution_program_4 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_many2one_field_f837x = models.ForeignKey('HrJob',    models.DO_NOTHING, related_name="+", db_column='x_studio_many2one_field_f837x', blank=True, null=True)
    x_studio_char_field_7wrxe = models.CharField(db_column='x_studio_char_field_7WrXe', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_char_field_jgu9j = models.CharField(db_column='x_studio_char_field_jGU9j', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_many2one_field_7y3g3 = models.ForeignKey('HrJob',    models.DO_NOTHING, related_name="+", db_column='x_studio_many2one_field_7Y3G3', blank=True, null=True)  # Field name made lowercase.
    x_studio_period_of_appraisal_to_1 = models.DateField(blank=True, null=True)
    x_studio_date_to = models.DateField(blank=True, null=True)
    x_studio_date_to_1 = models.DateField(blank=True, null=True)
    x_studio_date_to_2 = models.DateField(blank=True, null=True)
    x_studio_date_to_3 = models.DateField(blank=True, null=True)
    x_studio_many2one_field_mt5mq = models.ForeignKey('XInstitutions',    models.DO_NOTHING, related_name="+", db_column='x_studio_many2one_field_Mt5Mq', blank=True, null=True)  # Field name made lowercase.
    x_studio_many2one_field_nga1t = models.ForeignKey('XProgrammes',    models.DO_NOTHING, related_name="+", db_column='x_studio_many2one_field_NGa1t', blank=True, null=True)  # Field name made lowercase.
    x_studio_many2one_field_7g2cg = models.ForeignKey('XInstitutions',    models.DO_NOTHING, related_name="+", db_column='x_studio_many2one_field_7g2cg', blank=True, null=True)
    x_studio_many2one_field_edwra = models.ForeignKey('XProgrammes',    models.DO_NOTHING, related_name="+", db_column='x_studio_many2one_field_Edwra', blank=True, null=True)  # Field name made lowercase.
    x_studio_many2one_field_xdii2 = models.ForeignKey('XInstitutions',    models.DO_NOTHING, related_name="+", db_column='x_studio_many2one_field_XDiI2', blank=True, null=True)  # Field name made lowercase.
    x_studio_many2one_field_lvvpa = models.ForeignKey('XProgrammes',    models.DO_NOTHING, related_name="+", db_column='x_studio_many2one_field_lvvpA', blank=True, null=True)  # Field name made lowercase.
    x_studio_many2one_field_mvank = models.ForeignKey('XInstitutions',    models.DO_NOTHING, related_name="+", db_column='x_studio_many2one_field_MVAnk', blank=True, null=True)  # Field name made lowercase.
    x_studio_many2one_field_xsbyu = models.ForeignKey('XProgrammes',    models.DO_NOTHING, related_name="+", db_column='x_studio_many2one_field_xsBYu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'hr_appraisal'


class HrAppraisalGoal(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    name = models.CharField(max_length=200)
    employee = models.ForeignKey('HrEmployee',    models.DO_NOTHING, related_name="+")
    manager = models.ForeignKey('HrEmployee',    models.DO_NOTHING, related_name="+")
    progression = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_studio_organisational_goal = models.CharField(max_length=200, blank=True, null=True)
    x_studio_departmental_objective = models.CharField(max_length=200, blank=True, null=True)
    x_studio_1 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_1_1 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_2 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_3 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_1_2 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_2_1 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_3_1 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_1_3 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_2_2 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_3_2 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_1_4 = models.BooleanField(blank=True, null=True)
    x_studio_2_3 = models.BooleanField(blank=True, null=True)
    x_studio_3_3 = models.BooleanField(blank=True, null=True)
    x_studio_5 = models.BooleanField(blank=True, null=True)
    x_studio_4 = models.BooleanField(blank=True, null=True)
    x_studio_1_5 = models.BooleanField(blank=True, null=True)
    x_studio_2_4 = models.BooleanField(blank=True, null=True)
    x_studio_5_1 = models.BooleanField(blank=True, null=True)
    x_studio_4_1 = models.BooleanField(blank=True, null=True)
    x_studio_3_4 = models.BooleanField(blank=True, null=True)
    x_studio_1_6 = models.BooleanField(blank=True, null=True)
    x_studio_5_2 = models.BooleanField(blank=True, null=True)
    x_studio_2_5 = models.BooleanField(blank=True, null=True)
    x_studio_4_2 = models.BooleanField(blank=True, null=True)
    x_studio_3_5 = models.BooleanField(blank=True, null=True)
    x_studio_comments = models.CharField(max_length=200, blank=True, null=True)
    x_studio_comments_1 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_2_6 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_1_7 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_2_7 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_3_6 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_1_8 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_2_8 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_3_7 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_1_9 = models.BooleanField(blank=True, null=True)
    x_studio_2_9 = models.BooleanField(blank=True, null=True)
    x_studio_5_3 = models.BooleanField(blank=True, null=True)
    x_studio_4_3 = models.BooleanField(blank=True, null=True)
    x_studio_3_8 = models.BooleanField(blank=True, null=True)
    x_studio_2_10 = models.BooleanField(blank=True, null=True)
    x_studio_1_10 = models.BooleanField(blank=True, null=True)
    x_studio_5_4 = models.BooleanField(blank=True, null=True)
    x_studio_3_9 = models.BooleanField(blank=True, null=True)
    x_studio_4_4 = models.BooleanField(blank=True, null=True)
    x_studio_1_11 = models.BooleanField(blank=True, null=True)
    x_studio_3_10 = models.BooleanField(blank=True, null=True)
    x_studio_2_11 = models.BooleanField(blank=True, null=True)
    x_studio_5_5 = models.BooleanField(blank=True, null=True)
    x_studio_4_5 = models.BooleanField(blank=True, null=True)
    x_studio_comments_2 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_3_11 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_1_12 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_2_12 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_3_12 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_1_13 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_2_13 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_3_13 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_1_14 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_2_14 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_3_14 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_comments_3 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_1_17 = models.BooleanField(blank=True, null=True)
    x_studio_2_17 = models.BooleanField(blank=True, null=True)
    x_studio_3_17 = models.BooleanField(blank=True, null=True)
    x_studio_5_8 = models.BooleanField(blank=True, null=True)
    x_studio_4_8 = models.BooleanField(blank=True, null=True)
    x_studio_1_16 = models.BooleanField(blank=True, null=True)
    x_studio_2_16 = models.BooleanField(blank=True, null=True)
    x_studio_5_7 = models.BooleanField(blank=True, null=True)
    x_studio_3_16 = models.BooleanField(blank=True, null=True)
    x_studio_4_7 = models.BooleanField(blank=True, null=True)
    x_studio_1_15 = models.BooleanField(blank=True, null=True)
    x_studio_2_15 = models.BooleanField(blank=True, null=True)
    x_studio_5_6 = models.BooleanField(blank=True, null=True)
    x_studio_4_6 = models.BooleanField(blank=True, null=True)
    x_studio_3_15 = models.BooleanField(blank=True, null=True)
    x_studio_unsatisfactory_1_to_15 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_marginal_16_to_25 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_good_26_to_35 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_very_good_36_to_45 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_excellent_46_to_50 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_remarkscomments = models.CharField(max_length=200, blank=True, null=True)
    x_studio_appraisee = models.ForeignKey('HrEmployee',    models.DO_NOTHING, related_name="+", db_column='x_studio_appraisee', blank=True, null=True)
    x_studio_date = models.DateField(blank=True, null=True)
    x_studio_appraiser = models.ForeignKey('HrEmployee',    models.DO_NOTHING, related_name="+", db_column='x_studio_appraiser', blank=True, null=True)
    x_studio_date_1 = models.DateField(blank=True, null=True)
    x_studio_yes_no = models.CharField(max_length=200, blank=True, null=True)
    x_studio_many2one_field_d8uiq = models.ForeignKey('HrEmployee',    models.DO_NOTHING, related_name="+", db_column='x_studio_many2one_field_d8Uiq', blank=True, null=True)  # Field name made lowercase.
    x_studio_rating_1st_objective = models.CharField(max_length=200, blank=True, null=True)
    x_studio_rating_2nd_objective = models.CharField(max_length=200, blank=True, null=True)
    x_studio_rating_3rd_objective = models.CharField(max_length=200, blank=True, null=True)
    x_studio_options = models.CharField(max_length=200, blank=True, null=True)
    x_studio_average_score = models.FloatField(blank=True, null=True)
    x_studio_1_18 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_2_18 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_3_18 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_period_of_goals_from = models.DateField(blank=True, null=True)
    x_studio_period_of_goals_to = models.DateField(blank=True, null=True)
    x_studio_2_20 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_3_23 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_1_19 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_2_19 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_3_20 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_1_20 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_2_21 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_3_21 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_1_21 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_2_22 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_3_22 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_agreed_annual_rating_2nd_objective = models.CharField(max_length=200, blank=True, null=True)
    x_studio_comments_4 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_1_22 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_2_23 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_3_19 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_1_24 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_2_24 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_3_24 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_1_23 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_2_25 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_3_25 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_agreed_annual_rating_3rd_objective = models.CharField(max_length=200, blank=True, null=True)
    x_studio_comments_5 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_average_score_1 = models.FloatField(blank=True, null=True)
    x_studio_remarkscomments_1 = models.TextField(blank=True, null=True)
    x_studio_appraisee_1 = models.ForeignKey('HrEmployee',    models.DO_NOTHING, related_name="+", db_column='x_studio_appraisee_1', blank=True, null=True)
    x_studio_date_2 = models.DateField(blank=True, null=True)
    x_studio_appraiser_1 = models.ForeignKey('HrEmployee',    models.DO_NOTHING, related_name="+", db_column='x_studio_appraiser_1', blank=True, null=True)
    x_studio_date_3 = models.DateField(blank=True, null=True)
    x_studio_field = models.CharField(db_column='x_studio_', max_length=200, blank=True, null=True)  # Field renamed because it ended with '_'.
    x_studio_1_0 = models.CharField(db_column='x_studio__1', max_length=200, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because of name conflict.
    x_studio_2_0 = models.CharField(db_column='x_studio__2', max_length=200, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because of name conflict.
    x_studio_excellent_46_to_50_1 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_unsatisfactory_1_to_15_1 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_very_good_36_to_45_1 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_good_26_to_35_1 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_marginal_16_to_25_1 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_comments_6 = models.TextField(blank=True, null=True)
    x_studio_instructions = models.CharField(max_length=200, blank=True, null=True)
    x_studio_instruct1 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_explanation_of_ratings = models.CharField(max_length=200, blank=True, null=True)
    x_studio_char_field_toxjs = models.CharField(db_column='x_studio_char_field_ToXjS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_text_field_3juuv = models.TextField(db_column='x_studio_text_field_3jUuv', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'hr_appraisal_goal'


class HrAppraisalMailComposeMessageIrAttachmentsRel(models.Model):
    wizard = models.OneToOneField('RequestAppraisal',    models.DO_NOTHING, related_name="+", primary_key=True)
    attachment = models.ForeignKey('IrAttachment',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'hr_appraisal_mail_compose_message_ir_attachments_rel'
        unique_together = (('wizard', 'attachment'),)


class HrAppraisalNote(models.Model):
    name = models.CharField(max_length=200)
    sequence = models.IntegerField()
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hr_appraisal_note'


class HrAppraisalPlan(models.Model):
    duration = models.IntegerField()
    event = models.CharField(max_length=200)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hr_appraisal_plan'


class HrContract(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    name = models.CharField(max_length=200)
    active = models.BooleanField(blank=True, null=True)
    structure_type = models.ForeignKey('HrPayrollStructureType',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    employee = models.ForeignKey('HrEmployee',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    department = models.ForeignKey('HrDepartment',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    job = models.ForeignKey('HrJob',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    date_start = models.DateField()
    date_end = models.DateField(blank=True, null=True)
    trial_date_end = models.DateField(blank=True, null=True)
    resource_calendar = models.ForeignKey('ResourceCalendar',    models.DO_NOTHING, related_name="+")
    wage = models.DecimalField(max_digits=65535, decimal_places=65535)
    notes = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    kanban_state = models.CharField(max_length=200, blank=True, null=True)
    hr_responsible = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date_generated_from = models.DateTimeField()
    date_generated_to = models.DateTimeField()
    hourly_wage = models.DecimalField(max_digits=65535, decimal_places=65535)
    analytic_account = models.ForeignKey(AccountAnalyticAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    type = models.ForeignKey('HrContractType',    models.DO_NOTHING, related_name="+")
    x_studio_char_field_ka1um = models.CharField(db_column='x_studio_char_field_KA1um', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_rent_subsidy = models.BooleanField(blank=True, null=True)
    x_studio_fuel = models.BooleanField(blank=True, null=True)
    x_studio_maintenance = models.BooleanField(blank=True, null=True)
    x_studio_entertainment = models.BooleanField(blank=True, null=True)
    x_studio_garden_boy = models.BooleanField(blank=True, null=True)
    x_studio_domestic = models.BooleanField(blank=True, null=True)
    x_studio_security = models.BooleanField(blank=True, null=True)
    x_studio_acting = models.BooleanField(blank=True, null=True)
    x_studio_physically_challenged = models.BooleanField(blank=True, null=True)
    x_studio_level = models.FloatField(blank=True, null=True)
    x_studio_principal_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    x_studio_balanced_principal_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    x_studio_number_of_installments = models.IntegerField()
    x_studio_expected_monthly_deduction = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    x_studio_principal_amount_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    x_studio_balanced_principal_amount_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    x_studio_number_of_installments_1 = models.IntegerField()
    x_studio_expected_monthly_deduction_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    x_studio_principal_amount_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    x_studio_balanced_principal_amount_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    x_studio_number_of_installments_2 = models.IntegerField()
    x_studio_expected_monthly_deduction_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    x_studio_level_1 = models.IntegerField()
    x_studio_step_1 = models.IntegerField()
    x_studio_starting_wage = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    x_studio_step_2 = models.FloatField(blank=True, null=True)
    x_studio_step = models.IntegerField()
    x_studio_staff_number = models.CharField(max_length=200, blank=True, null=True)
    x_studio_temp_char = models.CharField(max_length=200, blank=True, null=True)
    x_studio_employee_birthdate = models.DateField(blank=True, null=True)
    x_studio_interest = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    x_studio_interest_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    x_studio_interest_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    x_studio_initial_balance_ecobnk = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    x_studio_initial_balance_bayport = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    x_studio_initial_balance_epa_ln = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    x_studio_total_deductions = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    x_studio_total_deductions_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    x_studio_total_deductions_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    x_studio_ecobank_advance_paid_chk = models.BooleanField(blank=True, null=True)
    x_studio_bayport_advance_paid_chk = models.BooleanField(blank=True, null=True)
    x_studio_welfare_advance_paid_chk = models.BooleanField(blank=True, null=True)
    x_studio_commuting = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hr_contract'


class HrContractHrPayrollIndexRel(models.Model):
    hr_payroll_index = models.OneToOneField('HrPayrollIndex',    models.DO_NOTHING, related_name="+", primary_key=True)
    hr_contract = models.ForeignKey(HrContract,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'hr_contract_hr_payroll_index_rel'
        unique_together = (('hr_payroll_index', 'hr_contract'),)


class HrContractType(models.Model):
    name = models.CharField(max_length=200)
    sequence = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hr_contract_type'


class HrDepartment(models.Model):
    name = models.CharField(max_length=200)
    complete_name = models.CharField(max_length=200, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    parent = models.ForeignKey('self',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    manager = models.ForeignKey('HrEmployee',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    color = models.IntegerField()
    message_main_attachment = models.ForeignKey('IrAttachment',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_studio_d = models.CharField(max_length=200, blank=True, null=True)
    x_studio_division = models.CharField(max_length=200, blank=True, null=True)
    x_studio_division_1 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_many2one_field_o9uon = models.ForeignKey('XDivision',    models.DO_NOTHING, related_name="+", db_column='x_studio_many2one_field_O9uOn', blank=True, null=True)  # Field name made lowercase.
    x_studio_many2one_field_h2qeo = models.ForeignKey('XUnit',    models.DO_NOTHING, related_name="+", db_column='x_studio_many2one_field_h2qeO', blank=True, null=True)  # Field name made lowercase.
    x_studio_many2one_field_zqvdg = models.ForeignKey('XUnits',    models.DO_NOTHING, related_name="+", db_column='x_studio_many2one_field_zQvDg', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'hr_department'


class HrDepartmentMailChannelRel(models.Model):
    mail_channel = models.OneToOneField('MailChannel',    models.DO_NOTHING, related_name="+", primary_key=True)
    hr_department = models.ForeignKey(HrDepartment,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'hr_department_mail_channel_rel'
        unique_together = (('mail_channel', 'hr_department'),)


class HrDepartureWizard(models.Model):
    departure_reason = models.CharField(max_length=200, blank=True, null=True)
    departure_description = models.TextField(blank=True, null=True)
    departure_date = models.DateField()
    employee = models.ForeignKey('HrEmployee',    models.DO_NOTHING, related_name="+")
    archive_private_address = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    set_date_end = models.BooleanField(blank=True, null=True)
    cancel_leaves = models.BooleanField(blank=True, null=True)
    cancel_appraisal = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hr_departure_wizard'


class HrEmployee(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    address_home = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    country = models.ForeignKey('ResCountry',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    gender = models.CharField(max_length=200, blank=True, null=True)
    marital = models.CharField(max_length=200, blank=True, null=True)
    spouse_complete_name = models.CharField(max_length=200, blank=True, null=True)
    spouse_birthdate = models.DateField(blank=True, null=True)
    children = models.IntegerField()
    place_of_birth = models.CharField(max_length=200, blank=True, null=True)
    country_of_birth = models.ForeignKey('ResCountry',    models.DO_NOTHING, related_name="+", db_column='country_of_birth', blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    ssnid = models.CharField(max_length=200, blank=True, null=True)
    sinid = models.CharField(max_length=200, blank=True, null=True)
    identification_id = models.CharField(max_length=200, blank=True, null=True)
    passport_id = models.CharField(max_length=200, blank=True, null=True)
    bank_account = models.ForeignKey('ResPartnerBank',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    permit_no = models.CharField(max_length=200, blank=True, null=True)
    visa_no = models.CharField(max_length=200, blank=True, null=True)
    visa_expire = models.DateField(blank=True, null=True)
    additional_note = models.TextField(blank=True, null=True)
    certificate = models.CharField(max_length=200, blank=True, null=True)
    study_field = models.CharField(max_length=200, blank=True, null=True)
    study_school = models.CharField(max_length=200, blank=True, null=True)
    emergency_contact = models.CharField(max_length=200, blank=True, null=True)
    emergency_phone = models.CharField(max_length=200, blank=True, null=True)
    km_home_work = models.IntegerField()
    notes = models.TextField(blank=True, null=True)
    color = models.IntegerField()
    barcode = models.CharField(unique=True, max_length=200, blank=True, null=True)
    pin = models.CharField(max_length=200, blank=True, null=True)
    departure_reason = models.CharField(max_length=200, blank=True, null=True)
    departure_description = models.TextField(blank=True, null=True)
    departure_date = models.DateField(blank=True, null=True)
    message_main_attachment = models.ForeignKey('IrAttachment',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    department = models.ForeignKey(HrDepartment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    job = models.ForeignKey('HrJob',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    job_title = models.CharField(max_length=200, blank=True, null=True)
    address = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    work_phone = models.CharField(max_length=200, blank=True, null=True)
    mobile_phone = models.CharField(max_length=200, blank=True, null=True)
    work_email = models.CharField(max_length=200, blank=True, null=True)
    work_location = models.CharField(max_length=200, blank=True, null=True)
    resource = models.ForeignKey('ResourceResource',    models.DO_NOTHING, related_name="+")
    resource_calendar = models.ForeignKey('ResourceCalendar',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    parent = models.ForeignKey('self',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    coach = models.ForeignKey('self',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    vehicle = models.CharField(max_length=200, blank=True, null=True)
    contract = models.ForeignKey(HrContract,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    contract_warning = models.BooleanField(blank=True, null=True)
    registration_number = models.CharField(max_length=200, blank=True, null=True)
    leave_manager = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_studio_tax_identification_number_tin = models.CharField(max_length=200, blank=True, null=True)
    x_studio_digital_home_address = models.CharField(max_length=200, blank=True, null=True)
    next_appraisal_date = models.DateField(blank=True, null=True)
    last_appraisal_date = models.DateField(blank=True, null=True)
    last_appraisal = models.ForeignKey(HrAppraisal,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_studio_boolean_field_nfoxi = models.BooleanField(db_column='x_studio_boolean_field_NFoXi', blank=True, null=True)  # Field name made lowercase.
    x_studio_char_field_wyfsl = models.CharField(db_column='x_studio_char_field_wyfSl', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_char_field_vkdcj = models.CharField(db_column='x_studio_char_field_vKdCJ', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_maiden_name = models.CharField(max_length=200, blank=True, null=True)
    x_studio_char_field_eut63 = models.CharField(db_column='x_studio_char_field_euT63', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_many2one_field_gndcv = models.ForeignKey('HrJob',    models.DO_NOTHING, related_name="+", db_column='x_studio_many2one_field_GndCv', blank=True, null=True)  # Field name made lowercase.
    x_studio_date_confirmed = models.DateField(blank=True, null=True)
    x_studio_home_town = models.CharField(max_length=200, blank=True, null=True)
    x_studio_name_of_spouse = models.CharField(max_length=200, blank=True, null=True)
    x_studio_qualifications = models.CharField(max_length=200, blank=True, null=True)
    x_studio_date_field_opl7k = models.DateField(db_column='x_studio_date_field_oPL7K', blank=True, null=True)  # Field name made lowercase.
    x_studio_present_appointment = models.CharField(max_length=200, blank=True, null=True)
    x_studio_dates_of_appointment_grades = models.TextField(blank=True, null=True)
    x_studio_char_field_6ppur = models.CharField(db_column='x_studio_char_field_6pPur', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_region = models.CharField(max_length=200, blank=True, null=True)
    x_studio_date_of_acceptance_letter = models.DateField(blank=True, null=True)
    x_studio_date_field_bar4h = models.DateField(db_column='x_studio_date_field_bAR4h', blank=True, null=True)  # Field name made lowercase.
    x_studio_remarks = models.CharField(max_length=200, blank=True, null=True)
    x_studio_staff_number = models.CharField(max_length=200, blank=True, null=True)
    x_studio_ssf_number = models.CharField(max_length=200, blank=True, null=True)
    x_studio_district_station = models.CharField(max_length=200, blank=True, null=True)
    x_studio_district = models.CharField(max_length=200, blank=True, null=True)
    x_studio_division = models.CharField(max_length=200, blank=True, null=True)
    x_studio_religion = models.CharField(max_length=200, blank=True, null=True)
    x_studio_height = models.CharField(max_length=200, blank=True, null=True)
    x_studio_weight = models.CharField(max_length=200, blank=True, null=True)
    x_studio_driving_license = models.CharField(max_length=200, blank=True, null=True)
    x_studio_bond1_number_of_years_of_study = models.IntegerField()
    x_studio_bond1_name_of_university = models.CharField(max_length=200, blank=True, null=True)
    x_studio_bond1_date_start = models.DateField(blank=True, null=True)
    x_studio_bond1_date_end = models.DateField(blank=True, null=True)
    x_studio_bond1_projected_years_to_be_with_epa = models.IntegerField()
    x_studio_bond1_guarantor_name = models.CharField(max_length=200, blank=True, null=True)
    x_studio_bond1_address = models.CharField(max_length=200, blank=True, null=True)
    x_studio_bond1_occupation = models.CharField(max_length=200, blank=True, null=True)
    x_studio_bond1_comments = models.TextField(blank=True, null=True)
    x_studio_bond2_number_of_years_of_study = models.IntegerField()
    x_studio_bond2_projected_years_to_be_with_epa = models.IntegerField()
    x_studio_bond2_name_of_university = models.CharField(max_length=200, blank=True, null=True)
    x_studio_bond2_date_start = models.DateField(blank=True, null=True)
    x_studio_bond2_date_end = models.DateField(blank=True, null=True)
    x_studio_bond2_guarantor_name = models.CharField(max_length=200, blank=True, null=True)
    x_studio_bond2_address = models.CharField(max_length=200, blank=True, null=True)
    x_studio_bond2_occupation = models.CharField(max_length=200, blank=True, null=True)
    x_studio_bond2_comments = models.TextField(blank=True, null=True)
    x_studio_comments_1 = models.TextField(blank=True, null=True)
    x_studio_number_of_years_of_study_2 = models.IntegerField()
    x_studio_current_date_of_appointment = models.DateField(blank=True, null=True)
    x_studio_number_of_years_of_study_1 = models.IntegerField()
    x_studio_projected_number_of_years_to_be_with_epa_3 = models.IntegerField()
    x_studio_job_position_1 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_guarantor_name_1 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_address_1 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_name_of_universityinstitute_1 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_occupation_1 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_projected_number_of_years_to_be_with_epa_1 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_bond_date_start_1 = models.DateField(blank=True, null=True)
    x_studio_comments_2 = models.TextField(blank=True, null=True)
    x_studio_bond_date_end_1 = models.DateField(blank=True, null=True)
    x_studio_projected_number_of_years_to_be_with_epa_2 = models.IntegerField()
    x_studio_date_confirmed_1 = models.DateField(blank=True, null=True)
    x_studio_bond_date_from = models.DateField(blank=True, null=True)
    x_studio_apply_for_new_bond = models.BooleanField(blank=True, null=True)
    x_studio_occupation = models.CharField(max_length=200, blank=True, null=True)
    x_studio_bond_date_to = models.DateField(blank=True, null=True)
    x_studio_address = models.CharField(max_length=200, blank=True, null=True)
    x_studio_guarantor_name = models.CharField(max_length=200, blank=True, null=True)
    x_studio_comments = models.CharField(max_length=200, blank=True, null=True)
    x_studio_name_of_universityinstitute = models.CharField(max_length=200, blank=True, null=True)
    x_studio_no_of_years_of_study = models.CharField(max_length=200, blank=True, null=True)
    x_studio_projected_number_of_years_to_be_with_epa = models.CharField(max_length=200, blank=True, null=True)
    x_studio_bond_date_start = models.DateField(blank=True, null=True)
    x_studio_number_of_years_of_study = models.CharField(max_length=200, blank=True, null=True)
    x_studio_bond_date_end = models.DateField(blank=True, null=True)
    x_studio_date_of_current_appointment = models.CharField(max_length=200, blank=True, null=True)
    x_studio_date_of_current_appointment_1 = models.DateField(blank=True, null=True)
    timesheet_cost = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    timesheet_manager = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_studio_name_of_universityinstitute_2 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_number_of_years_of_study_3 = models.IntegerField()
    x_studio_projected_number_of_years_to_be_with_epa_4 = models.IntegerField()
    x_studio_bond_date_start_2 = models.DateField(blank=True, null=True)
    x_studio_bond_date_end_2 = models.DateField(blank=True, null=True)
    x_studio_guarantor_name_2 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_address_2 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_occupation_2 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_comments_3 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_comments_4 = models.TextField(blank=True, null=True)
    x_studio_name_of_universityinstitute_3 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_number_of_years_of_study_4 = models.IntegerField()
    x_studio_projected_number_of_years_to_be_with_epa_5 = models.IntegerField()
    x_studio_bond_date_start_3 = models.DateField(blank=True, null=True)
    x_studio_bond_date_end_3 = models.DateField(blank=True, null=True)
    x_studio_guarantor_name_3 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_address_3 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_occupation_3 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_comments_5 = models.TextField(blank=True, null=True)
    x_studio_name_of_universityinstitute_4 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_number_of_years_of_study_5 = models.IntegerField()
    x_studio_projected_number_of_years_to_be_with_epa_6 = models.IntegerField()
    x_studio_bond_date_start_4 = models.DateField(blank=True, null=True)
    x_studio_bond_date_end_4 = models.DateField(blank=True, null=True)
    x_studio_guarantor_name_4 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_address_4 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_occupation_4 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_comments_6 = models.TextField(blank=True, null=True)
    x_studio_apply_for_new_bond_4 = models.BooleanField(blank=True, null=True)
    x_studio_apply_for_new_bond_5 = models.BooleanField(blank=True, null=True)
    x_studio_char_field_hap0g = models.CharField(db_column='x_studio_char_field_hAP0G', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_char_field_hibkr = models.CharField(db_column='x_studio_char_field_hiBKR', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_apply_for_new_bond2 = models.BooleanField(blank=True, null=True)
    x_studio_apply_for_new_bond_3 = models.BooleanField(blank=True, null=True)
    x_studio_wisdom_awoye = models.CharField(max_length=200, blank=True, null=True)
    x_studio_bond3_name_of_universityinstitute = models.CharField(max_length=200, blank=True, null=True)
    x_studio_apply_for_new_bond_8 = models.BooleanField(blank=True, null=True)
    x_studio_apply_for_new_bond_7 = models.BooleanField(blank=True, null=True)
    x_studio_apply_for_new_bond_6 = models.BooleanField(blank=True, null=True)
    x_studio_apply_for_new_bond_10 = models.BooleanField(blank=True, null=True)
    x_studio_apply_for_new_bond_2 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_apply_for_new_bond_11 = models.BooleanField(blank=True, null=True)
    x_studio_apply_for_new_bond_1 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_apply_for_new_bond_9 = models.BooleanField(blank=True, null=True)
    x_studio_bond3_name_of_university = models.CharField(max_length=200, blank=True, null=True)
    x_studio_bond3_number_of_years_of_study = models.IntegerField()
    x_studio_bond3_projected_years_to_be_with_epa = models.IntegerField()
    x_studio_bond3_date_start = models.DateField(blank=True, null=True)
    x_studio_bond3_date_end = models.DateField(blank=True, null=True)
    x_studio_bond3_guarantor_name = models.CharField(max_length=200, blank=True, null=True)
    x_studio_bond3_address = models.CharField(max_length=200, blank=True, null=True)
    x_studio_bond3_occupation = models.CharField(max_length=200, blank=True, null=True)
    x_studio_bond3_comments = models.TextField(blank=True, null=True)
    x_studio_bond4_name_of_university = models.CharField(max_length=200, blank=True, null=True)
    x_studio_bond4_number_of_years_of_study = models.IntegerField()
    x_studio_bond4_projected_years_to_be_with_epa = models.IntegerField()
    x_studio_bond4_date_start = models.DateField(blank=True, null=True)
    x_studio_bond4_date_end = models.DateField(blank=True, null=True)
    x_studio_bond4_guarantor_name = models.CharField(max_length=200, blank=True, null=True)
    x_studio_bond4_address = models.CharField(max_length=200, blank=True, null=True)
    x_studio_bond4_occupation = models.CharField(max_length=200, blank=True, null=True)
    x_studio_bond4_comments = models.TextField(blank=True, null=True)
    x_studio_bond5_name_of_university = models.CharField(max_length=200, blank=True, null=True)
    x_studio_bond5_number_of_years_of_study = models.IntegerField()
    x_studio_bond5_projected_years_to_be_with_epa = models.IntegerField()
    x_studio_bond5_date_start = models.DateField(blank=True, null=True)
    x_studio_bond5_date_end = models.DateField(blank=True, null=True)
    x_studio_bond5_guarantor_name = models.CharField(max_length=200, blank=True, null=True)
    x_studio_bond5_address = models.CharField(max_length=200, blank=True, null=True)
    x_studio_bond5_occupation = models.CharField(max_length=200, blank=True, null=True)
    x_studio_bond5_comments = models.TextField(blank=True, null=True)
    x_studio_professional_certificate_filename = models.CharField(max_length=200, blank=True, null=True)
    x_studio_leave_days = models.CharField(max_length=200, blank=True, null=True)
    x_studio_employee_category = models.CharField(max_length=200, blank=True, null=True)
    default_planning_role = models.ForeignKey('PlanningRole',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    employee_token = models.CharField(unique=True, max_length=200, blank=True, null=True)
    x_studio_guarantor_note = models.CharField(max_length=200, blank=True, null=True)
    x_studio_char_field_vnzaj = models.CharField(db_column='x_studio_char_field_VNZAj', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_note1 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_char_field_wwozj = models.CharField(db_column='x_studio_char_field_WWoZj', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_char_field_fq1vp = models.CharField(db_column='x_studio_char_field_fQ1Vp', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_char_field_e20ty = models.CharField(db_column='x_studio_char_field_E20TY', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_char_field_v8rcb = models.CharField(db_column='x_studio_char_field_v8RCb', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_char_field_kncum = models.CharField(db_column='x_studio_char_field_KnCUM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_char_field_tx3pz = models.CharField(db_column='x_studio_char_field_tx3Pz', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_char_field_8pd53 = models.CharField(db_column='x_studio_char_field_8PD53', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_char_field_oezog = models.CharField(db_column='x_studio_char_field_OEzOG', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_char_field_2bg3m = models.CharField(db_column='x_studio_char_field_2bG3m', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_char_field_eltbt = models.CharField(db_column='x_studio_char_field_eLtBt', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_many2one_field_6aq7d = models.ForeignKey('XDivision',    models.DO_NOTHING, related_name="+", db_column='x_studio_many2one_field_6aQ7d', blank=True, null=True)  # Field name made lowercase.
    x_studio_many2one_field_5u1cw = models.ForeignKey('XUnits',    models.DO_NOTHING, related_name="+", db_column='x_studio_many2one_field_5u1Cw', blank=True, null=True)  # Field name made lowercase.
    x_studio_institution = models.CharField(max_length=200, blank=True, null=True)
    x_studio_qualification = models.CharField(max_length=200, blank=True, null=True)
    x_studio_date_commenced = models.DateField(blank=True, null=True)
    x_studio_date_completed = models.DateField(blank=True, null=True)
    x_studio_institution_1 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_qualification_1 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_date_commenced_1 = models.DateField(blank=True, null=True)
    x_studio_date_commenced_2 = models.DateField(blank=True, null=True)
    x_studio_institution_2 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_qualification_2 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_date_commenced_3 = models.DateField(blank=True, null=True)
    x_studio_date_completed_1 = models.DateField(blank=True, null=True)
    x_studio_institution_3 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_qualification_3 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_date_commenced_4 = models.DateField(blank=True, null=True)
    x_studio_date_completed_2 = models.DateField(blank=True, null=True)
    x_studio_next_of_king = models.CharField(max_length=200, blank=True, null=True)
    x_studio_name = models.CharField(max_length=200, blank=True, null=True)
    x_studio_date_of_birth = models.DateField(blank=True, null=True)
    x_studio_home_town_1 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_name_1 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_date_of_birth_1 = models.DateField(blank=True, null=True)
    x_studio_home_town_2 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_name_2 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_gender = models.CharField(max_length=200, blank=True, null=True)
    x_studio_date_of_birth_2 = models.DateField(blank=True, null=True)
    x_studio_name_3 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_gender_1 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_date_of_birth_3 = models.DateField(blank=True, null=True)
    x_studio_name_4 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_gender_2 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_date_of_birth_4 = models.DateField(blank=True, null=True)
    x_studio_name_5 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_gender_3 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_date_of_birth_5 = models.DateField(blank=True, null=True)
    x_studio_achievements = models.TextField(blank=True, null=True)
    x_studio_job_description = models.TextField(blank=True, null=True)
    x_studio_sector = models.TextField(blank=True, null=True)
    x_studio_reasons_for_leaving = models.TextField(blank=True, null=True)
    x_studio_skillss_talents = models.TextField(blank=True, null=True)
    x_studio_name_of_institution = models.CharField(max_length=200, blank=True, null=True)
    x_studio_from = models.DateField(blank=True, null=True)
    x_studio_field = models.CharField(db_column='x_studio_', max_length=200, blank=True, null=True)  # Field renamed because it ended with '_'.
    x_studio_to = models.DateField(blank=True, null=True)
    x_studio_many2one_field_0yp2a = models.ForeignKey('XRegions',    models.DO_NOTHING, related_name="+", db_column='x_studio_many2one_field_0yp2a', blank=True, null=True)
    x_studio_many2one_field_xbsde = models.ForeignKey('XDistricts',    models.DO_NOTHING, related_name="+", db_column='x_studio_many2one_field_XbSde', blank=True, null=True)  # Field name made lowercase.
    x_studio_institution_4 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_qualification_4 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_date_commenced_5 = models.DateField(blank=True, null=True)
    x_studio_date_completed_3 = models.DateField(blank=True, null=True)
    x_studio_institution_5 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_qualification_5 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_date_commenced_6 = models.DateField(blank=True, null=True)
    x_studio_date_completed_4 = models.DateField(blank=True, null=True)
    x_studio_institution_6 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_qualification_6 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_date_commenced_7 = models.DateField(blank=True, null=True)
    x_studio_date_completed_5 = models.DateField(blank=True, null=True)
    x_studio_institution_7 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_qualification_7 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_date_commenced_8 = models.DateField(blank=True, null=True)
    x_studio_date_completed_6 = models.DateField(blank=True, null=True)
    x_studio_name_6 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_date_of_birth_6 = models.DateField(blank=True, null=True)
    x_studio_home_town_3 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_name_7 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_date_of_birth_7 = models.DateField(blank=True, null=True)
    x_studio_home_town_4 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_name_8 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_date_of_birth_8 = models.DateField(blank=True, null=True)
    x_studio_home_town_5 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_name_9 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_date_of_birth_9 = models.DateField(blank=True, null=True)
    x_studio_home_town_6 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_name_10 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_date_of_birth_10 = models.DateField(blank=True, null=True)
    x_studio_home_town_7 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_name_11 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_date_of_birth_11 = models.DateField(blank=True, null=True)
    x_studio_home_town_8 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_institution_8 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_qualification_8 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_date_commenced_9 = models.DateField(blank=True, null=True)
    x_studio_date_completed_7 = models.DateField(blank=True, null=True)
    x_studio_institution_9 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_qualification_9 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_date_commenced_10 = models.DateField(blank=True, null=True)
    x_studio_date_completed_8 = models.DateField(blank=True, null=True)
    x_studio_institution_10 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_qualification_10 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_date_commenced_11 = models.DateField(blank=True, null=True)
    x_studio_date_completed_9 = models.DateField(blank=True, null=True)
    x_studio_institution_11 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_qualification_11 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_date_commenced_12 = models.DateField(blank=True, null=True)
    x_studio_date_completed_10 = models.DateField(blank=True, null=True)
    x_studio_institution_12 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_qualification_12 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_date_commenced_13 = models.DateField(blank=True, null=True)
    x_studio_boolean_field_l6eba = models.BooleanField(db_column='x_studio_boolean_field_l6eBA', blank=True, null=True)  # Field name made lowercase.
    x_studio_date_completed_11 = models.DateField(blank=True, null=True)
    x_studio_institution_13 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_qualification_13 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_date_commenced_14 = models.DateField(blank=True, null=True)
    x_studio_date_completed_12 = models.DateField(blank=True, null=True)
    x_studio_institution_14 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_qualification_14 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_date_commenced_15 = models.DateField(blank=True, null=True)
    x_studio_date_completed_13 = models.DateField(blank=True, null=True)
    x_studio_institution_15 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_qualification_15 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_date_commenced_16 = models.DateField(blank=True, null=True)
    x_studio_date_completed_14 = models.DateField(blank=True, null=True)
    vaccine_note = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hr_employee'
        unique_together = (('registration_number', 'company'), ('user', 'company'),)


class HrEmployeeCategory(models.Model):
    name = models.CharField(unique=True, max_length=200)
    color = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hr_employee_category'


class HrEmployeeGroupRel(models.Model):
    payslip = models.OneToOneField('HrPayslipEmployees',    models.DO_NOTHING, related_name="+", primary_key=True)
    employee = models.ForeignKey(HrEmployee,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'hr_employee_group_rel'
        unique_together = (('payslip', 'employee'),)


class HrEmployeePlanningRoleRel(models.Model):
    hr_employee = models.OneToOneField(HrEmployee,    models.DO_NOTHING, related_name="+", primary_key=True)
    planning_role = models.ForeignKey('PlanningRole',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'hr_employee_planning_role_rel'
        unique_together = (('hr_employee', 'planning_role'),)


class HrEmployeePlanningSendRel(models.Model):
    planning_send = models.OneToOneField('PlanningSend',    models.DO_NOTHING, related_name="+", primary_key=True)
    hr_employee = models.ForeignKey(HrEmployee,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'hr_employee_planning_send_rel'
        unique_together = (('planning_send', 'hr_employee'),)


class HrEmployeeSlotPlanningSelectSendRel(models.Model):
    slot_planning_select_send = models.OneToOneField('SlotPlanningSelectSend',    models.DO_NOTHING, related_name="+", primary_key=True)
    hr_employee = models.ForeignKey(HrEmployee,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'hr_employee_slot_planning_select_send_rel'
        unique_together = (('slot_planning_select_send', 'hr_employee'),)


class HrEmployeeVaccineCentre(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    name = models.CharField(max_length=200)
    contact_details = models.CharField(max_length=200, blank=True, null=True)
    other_info = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hr_employee_vaccine_centre'


class HrEmployeeVaccineCertificateRel(models.Model):
    vaccination_detail = models.OneToOneField('VaccinationDetail',    models.DO_NOTHING, related_name="+", primary_key=True)
    ir_attachment = models.ForeignKey('IrAttachment',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'hr_employee_vaccine_certificate_rel'
        unique_together = (('vaccination_detail', 'ir_attachment'),)


class HrEmployeeVaccineInfo(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    name = models.CharField(max_length=200)
    dose = models.IntegerField()
    period = models.IntegerField()
    company = models.CharField(max_length=200, blank=True, null=True)
    country = models.ForeignKey('ResCountry',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    vaccine_details = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hr_employee_vaccine_info'


class HrHolidaysSummaryEmployee(models.Model):
    date_from = models.DateField()
    holiday_type = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hr_holidays_summary_employee'


class HrInstitute(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    country = models.ForeignKey('ResCountry',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    state = models.ForeignKey('ResCountryState',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hr_institute'


class HrJob(models.Model):
    name = models.CharField(max_length=200)
    expected_employees = models.IntegerField()
    no_of_employee = models.IntegerField()
    no_of_recruitment = models.IntegerField()
    no_of_hired_employee = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    requirements = models.TextField(blank=True, null=True)
    department = models.ForeignKey(HrDepartment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    state = models.CharField(max_length=200)
    message_main_attachment = models.ForeignKey('IrAttachment',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    address = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    manager = models.ForeignKey(HrEmployee,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    hr_responsible = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    alias = models.ForeignKey('MailAlias',    models.DO_NOTHING, related_name="+")
    color = models.IntegerField()
    employee_feedback_template = models.TextField(blank=True, null=True)
    manager_feedback_template = models.TextField(blank=True, null=True)
    website_meta_title = models.CharField(max_length=200, blank=True, null=True)
    website_meta_description = models.TextField(blank=True, null=True)
    website_meta_keywords = models.CharField(max_length=200, blank=True, null=True)
    website_meta_og_img = models.CharField(max_length=200, blank=True, null=True)
    seo_name = models.CharField(max_length=200, blank=True, null=True)
    website = models.ForeignKey('Website',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    is_published = models.BooleanField(blank=True, null=True)
    website_description = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hr_job'
        unique_together = (('name', 'company', 'department'),)


class HrJobHrRecruitmentStageRel(models.Model):
    hr_recruitment_stage = models.OneToOneField('HrRecruitmentStage',    models.DO_NOTHING, related_name="+", primary_key=True)
    hr_job = models.ForeignKey(HrJob,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'hr_job_hr_recruitment_stage_rel'
        unique_together = (('hr_recruitment_stage', 'hr_job'),)


class HrLeave(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    private_name = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    payslip_status = models.BooleanField(blank=True, null=True)
    report_note = models.TextField(blank=True, null=True)
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    manager = models.ForeignKey(HrEmployee,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    holiday_status = models.ForeignKey('HrLeaveType',    models.DO_NOTHING, related_name="+")
    employee = models.ForeignKey(HrEmployee,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    department = models.ForeignKey(HrDepartment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    number_of_days = models.FloatField(blank=True, null=True)
    duration_display = models.CharField(max_length=200, blank=True, null=True)
    meeting = models.ForeignKey(CalendarEvent,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    parent = models.ForeignKey('self',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    holiday_type = models.CharField(max_length=200)
    category = models.ForeignKey(HrEmployeeCategory,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    mode_company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    first_approver = models.ForeignKey(HrEmployee,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    second_approver = models.ForeignKey(HrEmployee,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    request_date_from = models.DateField(blank=True, null=True)
    request_date_to = models.DateField(blank=True, null=True)
    request_hour_from = models.CharField(max_length=200, blank=True, null=True)
    request_hour_to = models.CharField(max_length=200, blank=True, null=True)
    request_date_from_period = models.CharField(max_length=200, blank=True, null=True)
    request_unit_half = models.BooleanField(blank=True, null=True)
    request_unit_hours = models.BooleanField(blank=True, null=True)
    request_unit_custom = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hr_leave'


class HrLeaveAllocation(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    private_name = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    date_from = models.DateTimeField(blank=True, null=True)
    date_to = models.DateTimeField(blank=True, null=True)
    holiday_status = models.ForeignKey('HrLeaveType',    models.DO_NOTHING, related_name="+")
    employee = models.ForeignKey(HrEmployee,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    manager = models.ForeignKey(HrEmployee,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    number_of_days = models.FloatField(blank=True, null=True)
    parent = models.ForeignKey('self',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    first_approver = models.ForeignKey(HrEmployee,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    second_approver = models.ForeignKey(HrEmployee,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    holiday_type = models.CharField(max_length=200)
    mode_company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    department = models.ForeignKey(HrDepartment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    category = models.ForeignKey(HrEmployeeCategory,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    allocation_type = models.CharField(max_length=200)
    accrual_limit = models.IntegerField()
    number_per_interval = models.FloatField(blank=True, null=True)
    interval_number = models.IntegerField()
    unit_per_interval = models.CharField(max_length=200, blank=True, null=True)
    interval_unit = models.CharField(max_length=200, blank=True, null=True)
    nextcall = models.DateField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hr_leave_allocation'


class HrLeaveType(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200, blank=True, null=True)
    sequence = models.IntegerField()
    create_calendar_meeting = models.BooleanField(blank=True, null=True)
    color_name = models.CharField(max_length=200)
    active = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    responsible = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    leave_validation_type = models.CharField(max_length=200, blank=True, null=True)
    allocation_validation_type = models.CharField(max_length=200, blank=True, null=True)
    allocation_type = models.CharField(max_length=200, blank=True, null=True)
    validity_start = models.DateField(blank=True, null=True)
    validity_stop = models.DateField(blank=True, null=True)
    time_type = models.CharField(max_length=200, blank=True, null=True)
    request_unit = models.CharField(max_length=200)
    unpaid = models.BooleanField(blank=True, null=True)
    leave_notif_subtype = models.ForeignKey('MailMessageSubtype',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    allocation_notif_subtype = models.ForeignKey('MailMessageSubtype',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    work_entry_type = models.ForeignKey('HrWorkEntryType',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    timesheet_generate = models.BooleanField(blank=True, null=True)
    timesheet_project = models.ForeignKey('ProjectProject',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    timesheet_task = models.ForeignKey('ProjectTask',    models.DO_NOTHING, related_name="+", blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hr_leave_type'


class HrPayrollEditPayslipLine(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    sequence = models.IntegerField()
    salary_rule = models.ForeignKey('HrSalaryRule',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    rate = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    category = models.ForeignKey('HrSalaryRuleCategory',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    edit_payslip_lines_wizard = models.ForeignKey('HrPayrollEditPayslipLinesWizard',    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hr_payroll_edit_payslip_line'


class HrPayrollEditPayslipLinesWizard(models.Model):
    payslip = models.ForeignKey('HrPayslip',    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hr_payroll_edit_payslip_lines_wizard'


class HrPayrollEditPayslipWorkedDaysLine(models.Model):
    sequence = models.IntegerField()
    work_entry_type = models.ForeignKey('HrWorkEntryType',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    number_of_days = models.FloatField(blank=True, null=True)
    number_of_hours = models.FloatField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    edit_payslip_lines_wizard = models.ForeignKey(HrPayrollEditPayslipLinesWizard,    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hr_payroll_edit_payslip_worked_days_line'


class HrPayrollIndex(models.Model):
    percentage = models.FloatField(blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hr_payroll_index'


class HrPayrollStructure(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(blank=True, null=True)
    type = models.ForeignKey('HrPayrollStructureType',    models.DO_NOTHING, related_name="+")
    country = models.ForeignKey('ResCountry',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    report = models.ForeignKey('IrActReportXml',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    payslip_name = models.CharField(max_length=200, blank=True, null=True)
    use_worked_day_lines = models.BooleanField(blank=True, null=True)
    schedule_pay = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hr_payroll_structure'


class HrPayrollStructureHrPayslipInputTypeRel(models.Model):
    hr_payroll_structure = models.OneToOneField(HrPayrollStructure,    models.DO_NOTHING, related_name="+", primary_key=True)
    hr_payslip_input_type = models.ForeignKey('HrPayslipInputType',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'hr_payroll_structure_hr_payslip_input_type_rel'
        unique_together = (('hr_payroll_structure', 'hr_payslip_input_type'),)


class HrPayrollStructureHrWorkEntryTypeRel(models.Model):
    hr_payroll_structure = models.OneToOneField(HrPayrollStructure,    models.DO_NOTHING, related_name="+", primary_key=True)
    hr_work_entry_type = models.ForeignKey('HrWorkEntryType',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'hr_payroll_structure_hr_work_entry_type_rel'
        unique_together = (('hr_payroll_structure', 'hr_work_entry_type'),)


class HrPayrollStructureType(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    default_resource_calendar = models.ForeignKey('ResourceCalendar',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    country = models.ForeignKey('ResCountry',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    default_schedule_pay = models.CharField(max_length=200, blank=True, null=True)
    default_struct = models.ForeignKey(HrPayrollStructure,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    default_work_entry_type = models.ForeignKey('HrWorkEntryType',    models.DO_NOTHING, related_name="+")
    wage_type = models.CharField(max_length=200)

    class Meta:
        managed = True
        db_table = 'hr_payroll_structure_type'


class HrPayslip(models.Model):
    email_cc = models.CharField(max_length=200, blank=True, null=True)
    message_main_attachment = models.ForeignKey('IrAttachment',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    struct = models.ForeignKey(HrPayrollStructure,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=200, blank=True, null=True)
    employee = models.ForeignKey(HrEmployee,    models.DO_NOTHING, related_name="+")
    date_from = models.DateField()
    date_to = models.DateField()
    state = models.CharField(max_length=200, blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    paid = models.BooleanField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    contract = models.ForeignKey(HrContract,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    credit_note = models.BooleanField(blank=True, null=True)
    payslip_run = models.ForeignKey('HrPayslipRun',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    sum_worked_hours = models.FloatField(blank=True, null=True)
    normal_wage = models.IntegerField()
    compute_date = models.DateField(blank=True, null=True)
    warning_message = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    edited = models.BooleanField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    move = models.ForeignKey(AccountMove,    models.DO_NOTHING, related_name="+", blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hr_payslip'


class HrPayslipEmployees(models.Model):
    structure = models.ForeignKey(HrPayrollStructure,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hr_payslip_employees'


class HrPayslipInput(models.Model):
    payslip = models.ForeignKey(HrPayslip,    models.DO_NOTHING, related_name="+")
    sequence = models.IntegerField()
    input_type = models.ForeignKey('HrPayslipInputType',    models.DO_NOTHING, related_name="+")
    amount = models.FloatField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hr_payslip_input'


class HrPayslipInputType(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    country = models.ForeignKey('ResCountry',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hr_payslip_input_type'


class HrPayslipLine(models.Model):
    name = models.CharField(max_length=200)
    note = models.TextField(blank=True, null=True)
    sequence = models.IntegerField()
    code = models.CharField(max_length=200)
    slip = models.ForeignKey(HrPayslip,    models.DO_NOTHING, related_name="+")
    salary_rule = models.ForeignKey('HrSalaryRule',    models.DO_NOTHING, related_name="+")
    contract = models.ForeignKey(HrContract,    models.DO_NOTHING, related_name="+")
    employee = models.ForeignKey(HrEmployee,    models.DO_NOTHING, related_name="+")
    rate = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    category = models.ForeignKey('HrSalaryRuleCategory',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hr_payslip_line'


class HrPayslipRun(models.Model):
    name = models.CharField(max_length=200)
    state = models.CharField(max_length=200, blank=True, null=True)
    date_start = models.DateField()
    date_end = models.DateField()
    credit_note = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hr_payslip_run'


class HrPayslipWorkedDays(models.Model):
    payslip = models.ForeignKey(HrPayslip,    models.DO_NOTHING, related_name="+")
    sequence = models.IntegerField()
    work_entry_type = models.ForeignKey('HrWorkEntryType',    models.DO_NOTHING, related_name="+")
    number_of_days = models.FloatField(blank=True, null=True)
    number_of_hours = models.FloatField(blank=True, null=True)
    is_paid = models.BooleanField(blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hr_payslip_worked_days'


class HrPlan(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hr_plan'


class HrPlanActivityType(models.Model):
    activity_type = models.ForeignKey('MailActivityType',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    summary = models.CharField(max_length=200, blank=True, null=True)
    responsible = models.CharField(max_length=200)
    responsible_0 = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", db_column='responsible_id', blank=True, null=True)  # Field renamed because of name conflict.
    note = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hr_plan_activity_type'


class HrPlanHrPlanActivityTypeRel(models.Model):
    hr_plan = models.OneToOneField(HrPlan,    models.DO_NOTHING, related_name="+", primary_key=True)
    hr_plan_activity_type = models.ForeignKey(HrPlanActivityType,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'hr_plan_hr_plan_activity_type_rel'
        unique_together = (('hr_plan', 'hr_plan_activity_type'),)


class HrPlanWizard(models.Model):
    plan = models.ForeignKey(HrPlan,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    employee = models.ForeignKey(HrEmployee,    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hr_plan_wizard'


class HrRecruitmentDegree(models.Model):
    name = models.CharField(unique=True, max_length=200)
    sequence = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hr_recruitment_degree'


class HrRecruitmentSource(models.Model):
    source = models.ForeignKey('UtmSource',    models.DO_NOTHING, related_name="+")
    job = models.ForeignKey(HrJob,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    alias = models.ForeignKey('MailAlias',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hr_recruitment_source'


class HrRecruitmentStage(models.Model):
    name = models.CharField(max_length=200)
    sequence = models.IntegerField()
    requirements = models.TextField(blank=True, null=True)
    template = models.ForeignKey('MailTemplate',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    fold = models.BooleanField(blank=True, null=True)
    legend_blocked = models.CharField(max_length=200)
    legend_done = models.CharField(max_length=200)
    legend_normal = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hr_recruitment_stage'


class HrReminder(models.Model):
    name = models.CharField(max_length=200)
    model_name = models.ForeignKey('IrModel',    models.DO_NOTHING, related_name="+", db_column='model_name')
    model_field = models.ForeignKey('IrModelFields',    models.DO_NOTHING, related_name="+", db_column='model_field')
    search_by = models.CharField(max_length=200)
    days_before = models.IntegerField()
    active = models.BooleanField(blank=True, null=True)
    reminder_active = models.BooleanField(blank=True, null=True)
    date_set = models.DateField(blank=True, null=True)
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hr_reminder'


class HrRuleParameter(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(unique=True, max_length=200)
    description = models.TextField(blank=True, null=True)
    country = models.ForeignKey('ResCountry',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hr_rule_parameter'


class HrRuleParameterValue(models.Model):
    rule_parameter = models.ForeignKey(HrRuleParameter,    models.DO_NOTHING, related_name="+")
    code = models.CharField(max_length=200, blank=True, null=True)
    date_from = models.DateField()
    parameter_value = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hr_rule_parameter_value'
        unique_together = (('rule_parameter', 'date_from'),)


class HrSalaryRule(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    struct = models.ForeignKey(HrPayrollStructure,    models.DO_NOTHING, related_name="+")
    sequence = models.IntegerField()
    quantity = models.CharField(max_length=200, blank=True, null=True)
    category = models.ForeignKey('HrSalaryRuleCategory',    models.DO_NOTHING, related_name="+")
    active = models.BooleanField(blank=True, null=True)
    appears_on_payslip = models.BooleanField(blank=True, null=True)
    condition_select = models.CharField(max_length=200)
    condition_range = models.CharField(max_length=200, blank=True, null=True)
    condition_python = models.TextField()
    condition_range_min = models.FloatField(blank=True, null=True)
    condition_range_max = models.FloatField(blank=True, null=True)
    amount_select = models.CharField(max_length=200)
    amount_fix = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_percentage = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_python_compute = models.TextField(blank=True, null=True)
    amount_percentage_base = models.CharField(max_length=200, blank=True, null=True)
    partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    not_computed_in_net = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hr_salary_rule'


class HrSalaryRuleCategory(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    parent = models.ForeignKey('self',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hr_salary_rule_category'


class HrTimesheetMergeWizard(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    unit_amount = models.FloatField(blank=True, null=True)
    encoding_uom = models.ForeignKey('UomUom',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    project = models.ForeignKey('ProjectProject',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    task = models.ForeignKey('ProjectTask',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    employee = models.ForeignKey(HrEmployee,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hr_timesheet_merge_wizard'


class HrUserWorkEntryEmployee(models.Model):
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+")
    employee = models.ForeignKey(HrEmployee,    models.DO_NOTHING, related_name="+")
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hr_user_work_entry_employee'
        unique_together = (('user', 'employee'),)


class HrWorkEntry(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(blank=True, null=True)
    employee = models.ForeignKey(HrEmployee,    models.DO_NOTHING, related_name="+")
    date_start = models.DateTimeField()
    date_stop = models.DateTimeField(blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)
    work_entry_type = models.ForeignKey('HrWorkEntryType',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    conflict = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    contract = models.ForeignKey(HrContract,    models.DO_NOTHING, related_name="+")
    leave = models.ForeignKey(HrLeave,    models.DO_NOTHING, related_name="+", blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hr_work_entry'


class HrWorkEntryRegenerationWizard(models.Model):
    date_from = models.DateField()
    date_to = models.DateField()
    employee = models.ForeignKey(HrEmployee,    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hr_work_entry_regeneration_wizard'


class HrWorkEntryType(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(unique=True, max_length=200)
    color = models.IntegerField()
    sequence = models.IntegerField()
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    is_leave = models.BooleanField(blank=True, null=True)
    is_unforeseen = models.BooleanField(blank=True, null=True)
    round_days = models.CharField(max_length=200)
    round_days_type = models.CharField(max_length=200)

    class Meta:
        managed = True
        db_table = 'hr_work_entry_type'


class IapAccount(models.Model):
    service_name = models.CharField(max_length=200, blank=True, null=True)
    account_token = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'iap_account'


class IapAccountResCompanyRel(models.Model):
    iap_account = models.OneToOneField(IapAccount,    models.DO_NOTHING, related_name="+", primary_key=True)
    res_company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'iap_account_res_company_rel'
        unique_together = (('iap_account', 'res_company'),)


class IrActClient(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    help = models.TextField(blank=True, null=True)
    binding_model = models.ForeignKey('IrModel',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    binding_type = models.CharField(max_length=200)
    binding_view_types = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    tag = models.CharField(max_length=200)
    target = models.CharField(max_length=200, blank=True, null=True)
    res_model = models.CharField(max_length=200, blank=True, null=True)
    context = models.CharField(max_length=200)
    params_store = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ir_act_client'


class IrActReportXml(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    help = models.TextField(blank=True, null=True)
    binding_model = models.ForeignKey('IrModel',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    binding_type = models.CharField(max_length=200)
    binding_view_types = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    model = models.CharField(max_length=200)
    report_type = models.CharField(max_length=200)
    report_name = models.CharField(max_length=200)
    report_file = models.CharField(max_length=200, blank=True, null=True)
    multi = models.BooleanField(blank=True, null=True)
    paperformat = models.ForeignKey('ReportPaperformat',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    print_report_name = models.CharField(max_length=200, blank=True, null=True)
    attachment_use = models.BooleanField(blank=True, null=True)
    attachment = models.CharField(max_length=200, blank=True, null=True)
    jasper_output = models.CharField(max_length=200, blank=True, null=True)
    jasper_report = models.BooleanField(blank=True, null=True)
    file = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ir_act_report_xml'


class IrActServer(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    help = models.TextField(blank=True, null=True)
    binding_model = models.ForeignKey('IrModel',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    binding_type = models.CharField(max_length=200)
    binding_view_types = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    usage = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    sequence = models.IntegerField()
    model = models.ForeignKey('IrModel',    models.DO_NOTHING, related_name="+")
    model_name = models.CharField(max_length=200, blank=True, null=True)
    code = models.TextField(blank=True, null=True)
    crud_model = models.ForeignKey('IrModel',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    link_field = models.ForeignKey('IrModelFields',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    template = models.ForeignKey('MailTemplate',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    activity_type = models.ForeignKey('MailActivityType',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    activity_summary = models.CharField(max_length=200, blank=True, null=True)
    activity_note = models.TextField(blank=True, null=True)
    activity_date_deadline_range = models.IntegerField()
    activity_date_deadline_range_type = models.CharField(max_length=200, blank=True, null=True)
    activity_user_type = models.CharField(max_length=200)
    activity_user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    activity_user_field_name = models.CharField(max_length=200, blank=True, null=True)
    sms_template = models.ForeignKey('SmsTemplate',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    sms_mass_keep_log = models.BooleanField(blank=True, null=True)
    website_path = models.CharField(max_length=200, blank=True, null=True)
    website_published = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ir_act_server'


class IrActServerGroupRel(models.Model):
    act = models.OneToOneField(IrActServer,    models.DO_NOTHING, related_name="+", primary_key=True)
    gid = models.ForeignKey('ResGroups',    models.DO_NOTHING, related_name="+", db_column='gid')

    class Meta:
        managed = True
        db_table = 'ir_act_server_group_rel'
        unique_together = (('act', 'gid'),)


class IrActServerMailChannelRel(models.Model):
    ir_act_server = models.OneToOneField(IrActServer,    models.DO_NOTHING, related_name="+", primary_key=True)
    mail_channel = models.ForeignKey('MailChannel',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'ir_act_server_mail_channel_rel'
        unique_together = (('ir_act_server', 'mail_channel'),)


class IrActServerResPartnerRel(models.Model):
    ir_act_server = models.OneToOneField(IrActServer,    models.DO_NOTHING, related_name="+", primary_key=True)
    res_partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'ir_act_server_res_partner_rel'
        unique_together = (('ir_act_server', 'res_partner'),)


class IrActUrl(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    help = models.TextField(blank=True, null=True)
    binding_model = models.ForeignKey('IrModel',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    binding_type = models.CharField(max_length=200)
    binding_view_types = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    url = models.TextField()
    target = models.CharField(max_length=200)

    class Meta:
        managed = True
        db_table = 'ir_act_url'


class IrActWindow(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    help = models.TextField(blank=True, null=True)
    binding_model = models.ForeignKey('IrModel',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    binding_type = models.CharField(max_length=200)
    binding_view_types = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    view = models.ForeignKey('IrUiView',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    domain = models.CharField(max_length=200, blank=True, null=True)
    context = models.CharField(max_length=200)
    res_id = models.IntegerField()
    res_model = models.CharField(max_length=200)
    target = models.CharField(max_length=200, blank=True, null=True)
    view_mode = models.CharField(max_length=200)
    usage = models.CharField(max_length=200, blank=True, null=True)
    limit = models.IntegerField()
    search_view = models.ForeignKey('IrUiView',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    filter = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ir_act_window'


class IrActWindowGroupRel(models.Model):
    act = models.OneToOneField(IrActWindow,    models.DO_NOTHING, related_name="+", primary_key=True)
    gid = models.ForeignKey('ResGroups',    models.DO_NOTHING, related_name="+", db_column='gid')

    class Meta:
        managed = True
        db_table = 'ir_act_window_group_rel'
        unique_together = (('act', 'gid'),)


class IrActWindowView(models.Model):
    sequence = models.IntegerField()
    view = models.ForeignKey('IrUiView',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    view_mode = models.CharField(max_length=200)
    act_window = models.ForeignKey(IrActWindow,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    multi = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ir_act_window_view'
        unique_together = (('act_window', 'view_mode'),)


class IrActions(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    help = models.TextField(blank=True, null=True)
    binding_model = models.ForeignKey('IrModel',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    binding_type = models.CharField(max_length=200)
    binding_view_types = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ir_actions'


class IrActionsReportXmlFile(models.Model):
    filename = models.CharField(max_length=200, blank=True, null=True)
    report = models.ForeignKey(IrActReportXml,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    default = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ir_actions_report_xml_file'


class IrActionsTodo(models.Model):
    action_id = models.IntegerField()
    sequence = models.IntegerField()
    state = models.CharField(max_length=200)
    name = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ir_actions_todo'


class IrAttachment(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    res_model = models.CharField(max_length=200, blank=True, null=True)
    res_field = models.CharField(max_length=200, blank=True, null=True)
    res_id = models.IntegerField()
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    type = models.CharField(max_length=200)
    url = models.CharField(max_length=1024, blank=True, null=True)
    public = models.BooleanField(blank=True, null=True)
    access_token = models.CharField(max_length=200, blank=True, null=True)
    db_datas = models.BinaryField(blank=True, null=True)
    store_fname = models.CharField(max_length=200, blank=True, null=True)
    file_size = models.IntegerField()
    checksum = models.CharField(max_length=40, blank=True, null=True)
    mimetype = models.CharField(max_length=200, blank=True, null=True)
    index_content = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    original = models.ForeignKey('self',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    website = models.ForeignKey('Website',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    key = models.CharField(max_length=200, blank=True, null=True)
    theme_template = models.ForeignKey('ThemeIrAttachment',    models.DO_NOTHING, related_name="+", blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ir_attachment'


class IrAttachmentSlideChannelInviteRel(models.Model):
    slide_channel_invite = models.OneToOneField('SlideChannelInvite',    models.DO_NOTHING, related_name="+", primary_key=True)
    ir_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'ir_attachment_slide_channel_invite_rel'
        unique_together = (('slide_channel_invite', 'ir_attachment'),)


class IrConfigParameter(models.Model):
    key = models.CharField(unique=True, max_length=200)
    value = models.TextField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ir_config_parameter'


class IrCron(models.Model):
    ir_actions_server = models.ForeignKey(IrActServer,    models.DO_NOTHING, related_name="+")
    cron_name = models.CharField(max_length=200, blank=True, null=True)
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+")
    active = models.BooleanField(blank=True, null=True)
    interval_number = models.IntegerField()
    interval_type = models.CharField(max_length=200, blank=True, null=True)
    numbercall = models.IntegerField()
    doall = models.BooleanField(blank=True, null=True)
    nextcall = models.DateTimeField()
    lastcall = models.DateTimeField(blank=True, null=True)
    priority = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ir_cron'


class IrDefault(models.Model):
    field = models.ForeignKey('IrModelFields',    models.DO_NOTHING, related_name="+")
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    condition = models.CharField(max_length=200, blank=True, null=True)
    json_value = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ir_default'


class IrDemo(models.Model):
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ir_demo'


class IrDemoFailure(models.Model):
    module = models.ForeignKey('IrModuleModule',    models.DO_NOTHING, related_name="+")
    error = models.CharField(max_length=200, blank=True, null=True)
    wizard = models.ForeignKey('IrDemoFailureWizard',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ir_demo_failure'


class IrDemoFailureWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ir_demo_failure_wizard'


class IrExports(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    resource = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ir_exports'


class IrExportsLine(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    export = models.ForeignKey(IrExports,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ir_exports_line'


class IrFilters(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    domain = models.TextField()
    context = models.TextField()
    sort = models.TextField()
    model_id = models.CharField(max_length=200)
    is_default = models.BooleanField(blank=True, null=True)
    action_id = models.IntegerField()
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    # A unique constraint could not be introspected.
    class Meta:
        managed = True
        db_table = 'ir_filters'
        unique_together = (('name', 'model_id', 'user', 'action_id'),)


class IrLogging(models.Model):
    create_uid = models.IntegerField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.IntegerField()
    write_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    dbname = models.CharField(max_length=200, blank=True, null=True)
    level = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()
    path = models.CharField(max_length=200)
    func = models.CharField(max_length=200)
    line = models.CharField(max_length=200)

    class Meta:
        managed = True
        db_table = 'ir_logging'


class IrLoggingPerfLog(models.Model):
    path = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    uid = models.IntegerField()
    model = models.CharField(max_length=200, blank=True, null=True)
    method = models.CharField(max_length=200, blank=True, null=True)
    total_time = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    db_time = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    db_count = models.IntegerField()
    args = models.TextField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    stats = models.TextField(blank=True, null=True)
    db_stats = models.TextField(blank=True, null=True)
    slow_queries = models.TextField(blank=True, null=True)
    slow_recomputation = models.TextField(blank=True, null=True)
    id = models.IntegerField(primary_key="true")

    class Meta:
        managed = True
        db_table = 'ir_logging_perf_log'


class IrLoggingPerfRule(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(blank=True, null=True)
    methods = models.CharField(max_length=200, blank=True, null=True)
    log_python = models.BooleanField(blank=True, null=True)
    log_sql = models.BooleanField(blank=True, null=True)
    path = models.CharField(max_length=200, blank=True, null=True)
    rpc_min_duration = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sql_min_duration = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    recompute_min_duration = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ir_logging_perf_rule'


class IrLoggingPerfRuleIrModelRel(models.Model):
    ir_logging_perf_rule = models.OneToOneField(IrLoggingPerfRule,    models.DO_NOTHING, related_name="+", primary_key=True)
    ir_model = models.ForeignKey('IrModel',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'ir_logging_perf_rule_ir_model_rel'
        unique_together = (('ir_logging_perf_rule', 'ir_model'),)


class IrLoggingPerfRuleResUsersRel(models.Model):
    ir_logging_perf_rule = models.OneToOneField(IrLoggingPerfRule,    models.DO_NOTHING, related_name="+", primary_key=True)
    res_users = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'ir_logging_perf_rule_res_users_rel'
        unique_together = (('ir_logging_perf_rule', 'res_users'),)


class IrMailServer(models.Model):
    name = models.CharField(max_length=200)
    smtp_host = models.CharField(max_length=200)
    smtp_port = models.IntegerField()
    smtp_user = models.CharField(max_length=200, blank=True, null=True)
    smtp_pass = models.CharField(max_length=200, blank=True, null=True)
    smtp_encryption = models.CharField(max_length=200)
    smtp_debug = models.BooleanField(blank=True, null=True)
    sequence = models.IntegerField()
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ir_mail_server'


class IrModel(models.Model):
    name = models.CharField(max_length=200)
    model = models.CharField(unique=True, max_length=200)
    order = models.CharField(max_length=200)
    info = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    transient = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    is_mail_thread = models.BooleanField(blank=True, null=True)
    is_mail_activity = models.BooleanField(blank=True, null=True)
    is_mail_blacklist = models.BooleanField(blank=True, null=True)
    website_form_access = models.BooleanField(blank=True, null=True)
    website_form_default_field = models.ForeignKey('IrModelFields',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    website_form_label = models.CharField(max_length=200, blank=True, null=True)
    website_form_key = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ir_model'


class IrModelAccess(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(blank=True, null=True)
    model = models.ForeignKey(IrModel,    models.DO_NOTHING, related_name="+")
    group = models.ForeignKey('ResGroups',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    perm_read = models.BooleanField(blank=True, null=True)
    perm_write = models.BooleanField(blank=True, null=True)
    perm_create = models.BooleanField(blank=True, null=True)
    perm_unlink = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ir_model_access'


class IrModelConstraint(models.Model):
    name = models.CharField(max_length=200)
    definition = models.CharField(max_length=200, blank=True, null=True)
    message = models.CharField(max_length=200, blank=True, null=True)
    model = models.ForeignKey(IrModel,    models.DO_NOTHING, related_name="+", db_column='model')
    module = models.ForeignKey('IrModuleModule',    models.DO_NOTHING, related_name="+", db_column='module')
    type = models.CharField(max_length=1)
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ir_model_constraint'
        unique_together = (('name', 'module'),)


class IrModelData(models.Model):
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    noupdate = models.BooleanField(blank=True, null=True)
    name = models.CharField(max_length=200)
    module = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    res_id = models.IntegerField()
    studio = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ir_model_data'
        unique_together = (('module', 'name'),)


class IrModelFields(models.Model):
    name = models.CharField(max_length=200)
    complete_name = models.CharField(max_length=200, blank=True, null=True)
    model = models.CharField(max_length=200)
    relation = models.CharField(max_length=200, blank=True, null=True)
    relation_field = models.CharField(max_length=200, blank=True, null=True)
    relation_field_0 = models.ForeignKey('self',    models.DO_NOTHING, related_name="+", db_column='relation_field_id', blank=True, null=True)  # Field renamed because of name conflict.
    model_0 = models.ForeignKey(IrModel,    models.DO_NOTHING, related_name="+", db_column='model_id')  # Field renamed because of name conflict.
    field_description = models.CharField(max_length=200)
    help = models.TextField(blank=True, null=True)
    ttype = models.CharField(max_length=200)
    copied = models.BooleanField(blank=True, null=True)
    related = models.CharField(max_length=200, blank=True, null=True)
    related_field = models.ForeignKey('self',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    required = models.BooleanField(blank=True, null=True)
    readonly = models.BooleanField(blank=True, null=True)
    index = models.BooleanField(blank=True, null=True)
    translate = models.BooleanField(blank=True, null=True)
    size = models.IntegerField()
    state = models.CharField(max_length=200)
    on_delete = models.CharField(max_length=200, blank=True, null=True)
    domain = models.CharField(max_length=200, blank=True, null=True)
    group_expand = models.BooleanField(blank=True, null=True)
    selectable = models.BooleanField(blank=True, null=True)
    relation_table = models.CharField(max_length=200, blank=True, null=True)
    column1 = models.CharField(max_length=200, blank=True, null=True)
    column2 = models.CharField(max_length=200, blank=True, null=True)
    compute = models.TextField(blank=True, null=True)
    depends = models.CharField(max_length=200, blank=True, null=True)
    store = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    tracking = models.IntegerField()
    website_form_blacklisted = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ir_model_fields'
        unique_together = (('model', 'name'),)


class IrModelFieldsGroupRel(models.Model):
    field = models.OneToOneField(IrModelFields,    models.DO_NOTHING, related_name="+", primary_key=True)
    group = models.ForeignKey('ResGroups',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'ir_model_fields_group_rel'
        unique_together = (('field', 'group'),)


class IrModelFieldsSelection(models.Model):
    field = models.ForeignKey(IrModelFields,    models.DO_NOTHING, related_name="+")
    value = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    sequence = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ir_model_fields_selection'
        unique_together = (('field', 'value'),)


class IrModelRelation(models.Model):
    name = models.CharField(max_length=200)
    model = models.ForeignKey(IrModel,    models.DO_NOTHING, related_name="+", db_column='model')
    module = models.ForeignKey('IrModuleModule',    models.DO_NOTHING, related_name="+", db_column='module')
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ir_model_relation'


class IrModuleCategory(models.Model):
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    parent = models.ForeignKey('self',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    sequence = models.IntegerField()
    visible = models.BooleanField(blank=True, null=True)
    exclusive = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ir_module_category'


class IrModuleModule(models.Model):
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    website = models.CharField(max_length=200, blank=True, null=True)
    summary = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(unique=True, max_length=200)
    author = models.CharField(max_length=200, blank=True, null=True)
    icon = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=16, blank=True, null=True)
    latest_version = models.CharField(max_length=200, blank=True, null=True)
    shortdesc = models.CharField(max_length=200, blank=True, null=True)
    category = models.ForeignKey(IrModuleCategory,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    application = models.BooleanField(blank=True, null=True)
    demo = models.BooleanField(blank=True, null=True)
    web = models.BooleanField(blank=True, null=True)
    license = models.CharField(max_length=32, blank=True, null=True)
    sequence = models.IntegerField()
    auto_install = models.BooleanField(blank=True, null=True)
    to_buy = models.BooleanField(blank=True, null=True)
    maintainer = models.CharField(max_length=200, blank=True, null=True)
    contributors = models.TextField(blank=True, null=True)
    published_version = models.CharField(max_length=200, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    menus_by_module = models.TextField(blank=True, null=True)
    reports_by_module = models.TextField(blank=True, null=True)
    views_by_module = models.TextField(blank=True, null=True)
    imported = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ir_module_module'


class IrModuleModuleDependency(models.Model):
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    module = models.ForeignKey(IrModuleModule,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    auto_install_required = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ir_module_module_dependency'


class IrModuleModuleExclusion(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    module = models.ForeignKey(IrModuleModule,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ir_module_module_exclusion'


class IrProperty(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    res_id = models.CharField(max_length=200, blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    fields = models.ForeignKey(IrModelFields,    models.DO_NOTHING, related_name="+")
    value_float = models.FloatField(blank=True, null=True)
    value_integer = models.IntegerField()
    value_text = models.TextField(blank=True, null=True)
    value_binary = models.BinaryField(blank=True, null=True)
    value_reference = models.CharField(max_length=200, blank=True, null=True)
    value_datetime = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    # A unique constraint could not be introspected.
    class Meta:
        managed = True
        db_table = 'ir_property'


class IrRule(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    model = models.ForeignKey(IrModel,    models.DO_NOTHING, related_name="+")
    domain_force = models.TextField(blank=True, null=True)
    perm_read = models.BooleanField(blank=True, null=True)
    perm_write = models.BooleanField(blank=True, null=True)
    perm_create = models.BooleanField(blank=True, null=True)
    perm_unlink = models.BooleanField(blank=True, null=True)
    global_field = models.BooleanField(db_column='global', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ir_rule'


class IrSequence(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200, blank=True, null=True)
    implementation = models.CharField(max_length=200)
    active = models.BooleanField(blank=True, null=True)
    prefix = models.CharField(max_length=200, blank=True, null=True)
    suffix = models.CharField(max_length=200, blank=True, null=True)
    number_next = models.IntegerField()
    number_increment = models.IntegerField()
    padding = models.IntegerField()
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    use_date_range = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ir_sequence'


class IrSequenceDateRange(models.Model):
    date_from = models.DateField()
    date_to = models.DateField()
    sequence = models.ForeignKey(IrSequence,    models.DO_NOTHING, related_name="+")
    number_next = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ir_sequence_date_range'


class IrServerObjectLines(models.Model):
    server = models.ForeignKey(IrActServer,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    col1 = models.ForeignKey(IrModelFields,    models.DO_NOTHING, related_name="+", db_column='col1')
    value = models.TextField()
    evaluation_type = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ir_server_object_lines'


class IrTranslation(models.Model):
    name = models.CharField(max_length=200)
    res_id = models.IntegerField()
    lang = models.ForeignKey('ResLang',    models.DO_NOTHING, related_name="+", db_column='lang', blank=True, null=True)
    type = models.CharField(max_length=200, blank=True, null=True)
    src = models.TextField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    module = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)

    # A unique constraint could not be introspected.
    class Meta:
        managed = True
        db_table = 'ir_translation'
        unique_together = (('type', 'lang'), ('type', 'lang', 'name', 'res_id'), ('type', 'name', 'lang', 'res_id'),)


class IrUiMenu(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(blank=True, null=True)
    sequence = models.IntegerField()
    parent = models.ForeignKey('self',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    parent_path = models.CharField(max_length=200, blank=True, null=True)
    web_icon = models.CharField(max_length=200, blank=True, null=True)
    action = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    is_studio_configuration = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ir_ui_menu'


class IrUiMenuGroupRel(models.Model):
    menu = models.OneToOneField(IrUiMenu,    models.DO_NOTHING, related_name="+", primary_key=True)
    gid = models.ForeignKey('ResGroups',    models.DO_NOTHING, related_name="+", db_column='gid')

    class Meta:
        managed = True
        db_table = 'ir_ui_menu_group_rel'
        unique_together = (('menu', 'gid'),)


class IrUiMenuResUsersRel(models.Model):
    res_users = models.OneToOneField('ResUsers',    models.DO_NOTHING, related_name="+", primary_key=True)
    ir_ui_menu = models.ForeignKey(IrUiMenu,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'ir_ui_menu_res_users_rel'
        unique_together = (('res_users', 'ir_ui_menu'),)


class IrUiView(models.Model):
    name = models.CharField(max_length=200)
    model = models.CharField(max_length=200, blank=True, null=True)
    key = models.CharField(max_length=200, blank=True, null=True)
    priority = models.IntegerField()
    type = models.CharField(max_length=200, blank=True, null=True)
    arch_db = models.TextField(blank=True, null=True)
    arch_fs = models.CharField(max_length=200, blank=True, null=True)
    arch_updated = models.BooleanField(blank=True, null=True)
    arch_prev = models.TextField(blank=True, null=True)
    inherit = models.ForeignKey('self',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    field_parent = models.CharField(max_length=200, blank=True, null=True)
    mode = models.CharField(max_length=200)
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    customize_show = models.BooleanField(blank=True, null=True)
    website_meta_title = models.CharField(max_length=200, blank=True, null=True)
    website_meta_description = models.TextField(blank=True, null=True)
    website_meta_keywords = models.CharField(max_length=200, blank=True, null=True)
    website_meta_og_img = models.CharField(max_length=200, blank=True, null=True)
    seo_name = models.CharField(max_length=200, blank=True, null=True)
    website = models.ForeignKey('Website',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    track = models.BooleanField(blank=True, null=True)
    visibility = models.CharField(max_length=200, blank=True, null=True)
    visibility_password = models.CharField(max_length=200, blank=True, null=True)
    theme_template = models.ForeignKey('ThemeIrUiView',    models.DO_NOTHING, related_name="+", blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ir_ui_view'


class IrUiViewCustom(models.Model):
    ref = models.ForeignKey(IrUiView,    models.DO_NOTHING, related_name="+")
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+")
    arch = models.TextField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ir_ui_view_custom'


class IrUiViewGroupRel(models.Model):
    view = models.OneToOneField(IrUiView,    models.DO_NOTHING, related_name="+", primary_key=True)
    group = models.ForeignKey('ResGroups',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'ir_ui_view_group_rel'
        unique_together = (('view', 'group'),)


class JasperCreateDataTemplate(models.Model):
    model = models.ForeignKey(IrModel,    models.DO_NOTHING, related_name="+")
    depth = models.IntegerField()
    filename = models.CharField(max_length=32, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'jasper_create_data_template'


class JobFavoriteUserRel(models.Model):
    job = models.OneToOneField(HrJob,    models.DO_NOTHING, related_name="+", primary_key=True)
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'job_favorite_user_rel'
        unique_together = (('job', 'user'),)


class JournalAccountControlRel(models.Model):
    journal = models.OneToOneField(AccountJournal,    models.DO_NOTHING, related_name="+", primary_key=True)
    account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'journal_account_control_rel'
        unique_together = (('journal', 'account'),)


class JournalAccountTypeControlRel(models.Model):
    journal = models.OneToOneField(AccountJournal,    models.DO_NOTHING, related_name="+", primary_key=True)
    type = models.ForeignKey(AccountAccountType,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'journal_account_type_control_rel'
        unique_together = (('journal', 'type'),)


class KitAccountTaxReport(models.Model):
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    target_move = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'kit_account_tax_report'


class L10NInPortCode(models.Model):
    code = models.CharField(unique=True, max_length=200)
    name = models.CharField(max_length=200)
    state = models.ForeignKey('ResCountryState',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'l10n_in_port_code'


class LinkTracker(models.Model):
    campaign = models.ForeignKey('UtmCampaign',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    source = models.ForeignKey('UtmSource',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    medium = models.ForeignKey('UtmMedium',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    url = models.CharField(max_length=200)
    title = models.CharField(max_length=200, blank=True, null=True)
    label = models.CharField(max_length=200, blank=True, null=True)
    count = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'link_tracker'
        unique_together = (('url', 'campaign', 'medium', 'source'),)


class LinkTrackerClick(models.Model):
    campaign = models.ForeignKey('UtmCampaign',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    link = models.ForeignKey(LinkTracker,    models.DO_NOTHING, related_name="+")
    ip = models.CharField(max_length=200, blank=True, null=True)
    country = models.ForeignKey('ResCountry',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'link_tracker_click'


class LinkTrackerCode(models.Model):
    code = models.CharField(unique=True, max_length=200)
    link = models.ForeignKey(LinkTracker,    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'link_tracker_code'


class MailActivity(models.Model):
    res_model = models.ForeignKey(IrModel,    models.DO_NOTHING, related_name="+")
    res_model_0 = models.CharField(db_column='res_model', max_length=200, blank=True, null=True)  # Field renamed because of name conflict.
    res_id = models.IntegerField()
    res_name = models.CharField(max_length=200, blank=True, null=True)
    activity_type = models.ForeignKey('MailActivityType',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    summary = models.CharField(max_length=200, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    date_deadline = models.DateField()
    automated = models.BooleanField(blank=True, null=True)
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+")
    request_partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    recommended_activity_type = models.ForeignKey('MailActivityType',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    previous_activity_type = models.ForeignKey('MailActivityType',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    calendar_event = models.ForeignKey(CalendarEvent,    models.DO_NOTHING, related_name="+", blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mail_activity'


class MailActivityRel(models.Model):
    activity = models.OneToOneField('MailActivityType',    models.DO_NOTHING, related_name="+", primary_key=True)
    recommended = models.ForeignKey('MailActivityType',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'mail_activity_rel'
        unique_together = (('activity', 'recommended'),)


class MailActivityType(models.Model):
    name = models.CharField(max_length=200)
    summary = models.CharField(max_length=200, blank=True, null=True)
    sequence = models.IntegerField()
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    delay_count = models.IntegerField()
    delay_unit = models.CharField(max_length=200)
    delay_from = models.CharField(max_length=200)
    icon = models.CharField(max_length=200, blank=True, null=True)
    decoration_type = models.CharField(max_length=200, blank=True, null=True)
    res_model = models.ForeignKey(IrModel,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    default_next_type = models.ForeignKey('self',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    force_next = models.BooleanField(blank=True, null=True)
    category = models.CharField(max_length=200, blank=True, null=True)
    default_user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    default_description = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mail_activity_type'


class MailActivityTypeMailTemplateRel(models.Model):
    mail_activity_type = models.OneToOneField(MailActivityType,    models.DO_NOTHING, related_name="+", primary_key=True)
    mail_template = models.ForeignKey('MailTemplate',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'mail_activity_type_mail_template_rel'
        unique_together = (('mail_activity_type', 'mail_template'),)


class MailAlias(models.Model):
    alias_name = models.CharField(unique=True, max_length=200, blank=True, null=True)
    alias_model = models.ForeignKey(IrModel,    models.DO_NOTHING, related_name="+")
    alias_user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    alias_defaults = models.TextField()
    alias_force_thread_id = models.IntegerField()
    alias_parent_model = models.ForeignKey(IrModel,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    alias_parent_thread_id = models.IntegerField()
    alias_contact = models.CharField(max_length=200)
    alias_bounced_content = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mail_alias'


class MailBlacklist(models.Model):
    email = models.CharField(unique=True, max_length=200)
    active = models.BooleanField(blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mail_blacklist'


class MailBlacklistRemove(models.Model):
    email = models.CharField(max_length=200)
    reason = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mail_blacklist_remove'


class MailChannel(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(blank=True, null=True)
    channel_type = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    uuid = models.CharField(max_length=50, blank=True, null=True)
    email_send = models.BooleanField(blank=True, null=True)
    public = models.CharField(max_length=200)
    group_public = models.ForeignKey('ResGroups',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    moderation = models.BooleanField(blank=True, null=True)
    moderation_notify = models.BooleanField(blank=True, null=True)
    moderation_notify_msg = models.TextField(blank=True, null=True)
    moderation_guidelines = models.BooleanField(blank=True, null=True)
    moderation_guidelines_msg = models.TextField(blank=True, null=True)
    alias = models.ForeignKey(MailAlias,    models.DO_NOTHING, related_name="+")
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mail_channel'


class MailChannelMailWizardInviteRel(models.Model):
    mail_wizard_invite = models.OneToOneField('MailWizardInvite',    models.DO_NOTHING, related_name="+", primary_key=True)
    mail_channel = models.ForeignKey(MailChannel,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'mail_channel_mail_wizard_invite_rel'
        unique_together = (('mail_wizard_invite', 'mail_channel'),)


class MailChannelModeratorRel(models.Model):
    mail_channel = models.OneToOneField(MailChannel,    models.DO_NOTHING, related_name="+", primary_key=True)
    res_users = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'mail_channel_moderator_rel'
        unique_together = (('mail_channel', 'res_users'),)


class MailChannelPartner(models.Model):
    custom_channel_name = models.CharField(max_length=200, blank=True, null=True)
    partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    channel = models.ForeignKey(MailChannel,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    fetched_message = models.ForeignKey('MailMessage',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    seen_message = models.ForeignKey('MailMessage',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    fold_state = models.CharField(max_length=200, blank=True, null=True)
    is_minimized = models.BooleanField(blank=True, null=True)
    is_pinned = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mail_channel_partner'


class MailChannelResGroupsRel(models.Model):
    mail_channel = models.OneToOneField(MailChannel,    models.DO_NOTHING, related_name="+", primary_key=True)
    res_groups = models.ForeignKey('ResGroups',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'mail_channel_res_groups_rel'
        unique_together = (('mail_channel', 'res_groups'),)


class MailComposeMessage(models.Model):
    subject = models.CharField(max_length=200, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    parent = models.ForeignKey('MailMessage',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    template = models.ForeignKey('MailTemplate',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    layout = models.CharField(max_length=200, blank=True, null=True)
    add_sign = models.BooleanField(blank=True, null=True)
    email_from = models.CharField(max_length=200, blank=True, null=True)
    author = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    composition_mode = models.CharField(max_length=200, blank=True, null=True)
    model = models.CharField(max_length=200, blank=True, null=True)
    res_id = models.IntegerField()
    record_name = models.CharField(max_length=200, blank=True, null=True)
    use_active_domain = models.BooleanField(blank=True, null=True)
    active_domain = models.TextField(blank=True, null=True)
    message_type = models.CharField(max_length=200)
    subtype = models.ForeignKey('MailMessageSubtype',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    mail_activity_type = models.ForeignKey(MailActivityType,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    reply_to = models.CharField(max_length=200, blank=True, null=True)
    no_auto_thread = models.BooleanField(blank=True, null=True)
    is_log = models.BooleanField(blank=True, null=True)
    notify = models.BooleanField(blank=True, null=True)
    auto_delete = models.BooleanField(blank=True, null=True)
    auto_delete_message = models.BooleanField(blank=True, null=True)
    mail_server = models.ForeignKey(IrMailServer,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mail_compose_message'


class MailComposeMessageIrAttachmentsRel(models.Model):
    wizard = models.OneToOneField(MailComposeMessage,    models.DO_NOTHING, related_name="+", primary_key=True)
    attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'mail_compose_message_ir_attachments_rel'
        unique_together = (('wizard', 'attachment'),)


class MailComposeMessageResPartnerRel(models.Model):
    wizard = models.OneToOneField(MailComposeMessage,    models.DO_NOTHING, related_name="+", primary_key=True)
    partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'mail_compose_message_res_partner_rel'
        unique_together = (('wizard', 'partner'),)


class MailFollowers(models.Model):
    res_model = models.CharField(max_length=200)
    res_id = models.IntegerField()
    partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    channel = models.ForeignKey(MailChannel,    models.DO_NOTHING, related_name="+", blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mail_followers'
        unique_together = (('res_model', 'res_id', 'channel'), ('res_model', 'res_id', 'partner'),)


class MailFollowersMailMessageSubtypeRel(models.Model):
    mail_followers = models.OneToOneField(MailFollowers,    models.DO_NOTHING, related_name="+", primary_key=True)
    mail_message_subtype = models.ForeignKey('MailMessageSubtype',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'mail_followers_mail_message_subtype_rel'
        unique_together = (('mail_followers', 'mail_message_subtype'),)


class MailMail(models.Model):
    mail_message = models.ForeignKey('MailMessage',    models.DO_NOTHING, related_name="+")
    body_html = models.TextField(blank=True, null=True)
    references = models.TextField(blank=True, null=True)
    headers = models.TextField(blank=True, null=True)
    notification = models.BooleanField(blank=True, null=True)
    email_to = models.TextField(blank=True, null=True)
    email_cc = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    auto_delete = models.BooleanField(blank=True, null=True)
    failure_reason = models.TextField(blank=True, null=True)
    scheduled_date = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    fetchmail_server = models.ForeignKey(FetchmailServer,    models.DO_NOTHING, related_name="+", blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mail_mail'


class MailMailResPartnerRel(models.Model):
    mail_mail = models.OneToOneField(MailMail,    models.DO_NOTHING, related_name="+", primary_key=True)
    res_partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'mail_mail_res_partner_rel'
        unique_together = (('mail_mail', 'res_partner'),)


class MailMessage(models.Model):
    subject = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    parent = models.ForeignKey('self',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    model = models.CharField(max_length=200, blank=True, null=True)
    res_id = models.IntegerField()
    record_name = models.CharField(max_length=200, blank=True, null=True)
    message_type = models.CharField(max_length=200)
    subtype = models.ForeignKey('MailMessageSubtype',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    mail_activity_type = models.ForeignKey(MailActivityType,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    is_internal = models.BooleanField(blank=True, null=True)
    email_from = models.CharField(max_length=200, blank=True, null=True)
    author = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    no_auto_thread = models.BooleanField(blank=True, null=True)
    message_id = models.CharField(max_length=200, blank=True, null=True)
    reply_to = models.CharField(max_length=200, blank=True, null=True)
    mail_server = models.ForeignKey(IrMailServer,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    moderation_status = models.CharField(max_length=200, blank=True, null=True)
    moderator = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    email_layout_xmlid = models.CharField(max_length=200, blank=True, null=True)
    add_sign = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mail_message'


class MailMessageMailChannelRel(models.Model):
    mail_message = models.OneToOneField(MailMessage,    models.DO_NOTHING, related_name="+", primary_key=True)
    mail_channel = models.ForeignKey(MailChannel,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'mail_message_mail_channel_rel'
        unique_together = (('mail_message', 'mail_channel'),)


class MailMessageResPartnerNeedactionRel(models.Model):
    mail_message = models.ForeignKey(MailMessage,    models.DO_NOTHING, related_name="+")
    mail = models.ForeignKey(MailMail,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    res_partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    notification_type = models.CharField(max_length=200)
    notification_status = models.CharField(max_length=200, blank=True, null=True)
    is_read = models.BooleanField(blank=True, null=True)
    read_date = models.DateTimeField(blank=True, null=True)
    failure_type = models.CharField(max_length=200, blank=True, null=True)
    failure_reason = models.TextField(blank=True, null=True)
    sms = models.ForeignKey('SmsSms',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    sms_number = models.CharField(max_length=200, blank=True, null=True)
    letter = models.ForeignKey('SnailmailLetter',    models.DO_NOTHING, related_name="+", blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mail_message_res_partner_needaction_rel'


class MailMessageResPartnerNeedactionRelMailResendMessageRel(models.Model):
    mail_resend_message = models.OneToOneField('MailResendMessage',    models.DO_NOTHING, related_name="+", primary_key=True)
    mail_message_res_partner_needaction_rel = models.ForeignKey(MailMessageResPartnerNeedactionRel,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'mail_message_res_partner_needaction_rel_mail_resend_message_rel'
        unique_together = (('mail_resend_message', 'mail_message_res_partner_needaction_rel'),)


class MailMessageResPartnerRel(models.Model):
    mail_message = models.OneToOneField(MailMessage,    models.DO_NOTHING, related_name="+", primary_key=True)
    res_partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'mail_message_res_partner_rel'
        unique_together = (('mail_message', 'res_partner'),)


class MailMessageResPartnerStarredRel(models.Model):
    mail_message = models.OneToOneField(MailMessage,    models.DO_NOTHING, related_name="+", primary_key=True)
    res_partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'mail_message_res_partner_starred_rel'
        unique_together = (('mail_message', 'res_partner'),)


class MailMessageSubtype(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    internal = models.BooleanField(blank=True, null=True)
    parent = models.ForeignKey('self',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    relation_field = models.CharField(max_length=200, blank=True, null=True)
    res_model = models.CharField(max_length=200, blank=True, null=True)
    default = models.BooleanField(blank=True, null=True)
    sequence = models.IntegerField()
    hidden = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mail_message_subtype'


class MailModeration(models.Model):
    email = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    channel = models.ForeignKey(MailChannel,    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mail_moderation'
        unique_together = (('email', 'channel'),)


class MailResendCancel(models.Model):
    model = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mail_resend_cancel'


class MailResendMessage(models.Model):
    mail_message = models.ForeignKey(MailMessage,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mail_resend_message'


class MailResendPartner(models.Model):
    partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+")
    resend = models.BooleanField(blank=True, null=True)
    resend_wizard = models.ForeignKey(MailResendMessage,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    message = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mail_resend_partner'


class MailShortcode(models.Model):
    source = models.CharField(max_length=200)
    substitution = models.TextField()
    description = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mail_shortcode'


class MailTemplate(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    model = models.ForeignKey(IrModel,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    model_0 = models.CharField(db_column='model', max_length=200, blank=True, null=True)  # Field renamed because of name conflict.
    subject = models.CharField(max_length=200, blank=True, null=True)
    email_from = models.CharField(max_length=200, blank=True, null=True)
    use_default_to = models.BooleanField(blank=True, null=True)
    email_to = models.CharField(max_length=200, blank=True, null=True)
    partner_to = models.CharField(max_length=200, blank=True, null=True)
    email_cc = models.CharField(max_length=200, blank=True, null=True)
    reply_to = models.CharField(max_length=200, blank=True, null=True)
    body_html = models.TextField(blank=True, null=True)
    report_name = models.CharField(max_length=200, blank=True, null=True)
    report_template = models.ForeignKey(IrActReportXml,    models.DO_NOTHING, related_name="+", db_column='report_template', blank=True, null=True)
    mail_server = models.ForeignKey(IrMailServer,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    scheduled_date = models.CharField(max_length=200, blank=True, null=True)
    auto_delete = models.BooleanField(blank=True, null=True)
    ref_ir_act_window = models.ForeignKey(IrActWindow,    models.DO_NOTHING, related_name="+", db_column='ref_ir_act_window', blank=True, null=True)
    lang = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mail_template'


class MailTemplatePreview(models.Model):
    mail_template = models.ForeignKey(MailTemplate,    models.DO_NOTHING, related_name="+")
    resource_ref = models.CharField(max_length=200, blank=True, null=True)
    lang = models.CharField(max_length=200, blank=True, null=True)
    error_msg = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mail_template_preview'


class MailTrackingValue(models.Model):
    field = models.ForeignKey(IrModelFields,    models.DO_NOTHING, related_name="+", db_column='field')
    field_desc = models.CharField(max_length=200)
    field_type = models.CharField(max_length=200, blank=True, null=True)
    old_value_integer = models.IntegerField()
    old_value_float = models.FloatField(blank=True, null=True)
    old_value_monetary = models.FloatField(blank=True, null=True)
    old_value_char = models.CharField(max_length=200, blank=True, null=True)
    old_value_text = models.TextField(blank=True, null=True)
    old_value_datetime = models.DateTimeField(blank=True, null=True)
    new_value_integer = models.IntegerField()
    new_value_float = models.FloatField(blank=True, null=True)
    new_value_monetary = models.FloatField(blank=True, null=True)
    new_value_char = models.CharField(max_length=200, blank=True, null=True)
    new_value_text = models.TextField(blank=True, null=True)
    new_value_datetime = models.DateTimeField(blank=True, null=True)
    mail_message = models.ForeignKey(MailMessage,    models.DO_NOTHING, related_name="+")
    tracking_sequence = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mail_tracking_value'


class MailWizardInvite(models.Model):
    res_model = models.CharField(max_length=200)
    res_id = models.IntegerField()
    message = models.TextField(blank=True, null=True)
    send_mail = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mail_wizard_invite'


class MailWizardInviteResPartnerRel(models.Model):
    mail_wizard_invite = models.OneToOneField(MailWizardInvite,    models.DO_NOTHING, related_name="+", primary_key=True)
    res_partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'mail_wizard_invite_res_partner_rel'
        unique_together = (('mail_wizard_invite', 'res_partner'),)


class MaintenanceEquipment(models.Model):
    name = models.CharField(max_length=200)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    technician_user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    owner_user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    category = models.ForeignKey('MaintenanceEquipmentCategory',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    partner_ref = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    model = models.CharField(max_length=200, blank=True, null=True)
    serial_no = models.CharField(unique=True, max_length=200, blank=True, null=True)
    assign_date = models.DateField(blank=True, null=True)
    effective_date = models.DateField()
    cost = models.FloatField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    warranty_date = models.DateField(blank=True, null=True)
    color = models.IntegerField()
    scrap_date = models.DateField(blank=True, null=True)
    maintenance_count = models.IntegerField()
    maintenance_open_count = models.IntegerField()
    period = models.IntegerField()
    next_action_date = models.DateField(blank=True, null=True)
    maintenance_team = models.ForeignKey('MaintenanceTeam',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    maintenance_duration = models.FloatField(blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    employee = models.ForeignKey(HrEmployee,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    department = models.ForeignKey(HrDepartment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    equipment_assign_to = models.CharField(max_length=200)
    x_studio_char_field_uqqw6 = models.CharField(db_column='x_studio_char_field_UQqw6', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_odometer = models.CharField(max_length=200, blank=True, null=True)
    x_studio_date = models.DateField(blank=True, null=True)
    x_studio_date_to = models.DateField(blank=True, null=True)
    x_studio_warrenty_conditions = models.CharField(max_length=200, blank=True, null=True)
    x_studio_text_field_wq46z = models.TextField(db_column='x_studio_text_field_Wq46Z', blank=True, null=True)  # Field name made lowercase.
    x_studio_maker = models.CharField(max_length=200, blank=True, null=True)
    expected_mtbf = models.IntegerField()
    workcenter = models.ForeignKey('MrpWorkcenter',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_studio_used_by_1 = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'maintenance_equipment'


class MaintenanceEquipmentCategory(models.Model):
    name = models.CharField(max_length=200)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    technician_user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    color = models.IntegerField()
    note = models.TextField(blank=True, null=True)
    alias = models.ForeignKey(MailAlias,    models.DO_NOTHING, related_name="+")
    fold = models.BooleanField(blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'maintenance_equipment_category'


class MaintenanceRequest(models.Model):
    name = models.CharField(max_length=200)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    request_date = models.DateField(blank=True, null=True)
    owner_user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    category = models.ForeignKey(MaintenanceEquipmentCategory,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    equipment = models.ForeignKey(MaintenanceEquipment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    stage = models.ForeignKey('MaintenanceStage',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    priority = models.CharField(max_length=200, blank=True, null=True)
    color = models.IntegerField()
    close_date = models.DateField(blank=True, null=True)
    kanban_state = models.CharField(max_length=200)
    archive = models.BooleanField(blank=True, null=True)
    maintenance_type = models.CharField(max_length=200, blank=True, null=True)
    schedule_date = models.DateTimeField(blank=True, null=True)
    maintenance_team = models.ForeignKey('MaintenanceTeam',    models.DO_NOTHING, related_name="+")
    duration = models.FloatField(blank=True, null=True)
    email_cc = models.CharField(max_length=200, blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    employee = models.ForeignKey(HrEmployee,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_studio_comments_on_equipment = models.TextField(blank=True, null=True)
    x_studio_remarks_on_equipment = models.TextField(blank=True, null=True)
    x_studio_many2one_field_gpjbb = models.ForeignKey(HrDepartment,    models.DO_NOTHING, related_name="+", db_column='x_studio_many2one_field_GpjbB', blank=True, null=True)  # Field name made lowercase.
    x_studio_vendor = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+", db_column='x_studio_vendor', blank=True, null=True)
    x_studio_phone_no = models.CharField(max_length=200, blank=True, null=True)
    x_studio_email = models.CharField(max_length=200, blank=True, null=True)
    x_studio_maintenance_cost = models.CharField(max_length=200, blank=True, null=True)
    x_studio_maintenancecostcheck = models.BooleanField(blank=True, null=True)
    production = models.ForeignKey('MrpProduction',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    workorder = models.ForeignKey('MrpWorkorder',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_studio_1 = models.TextField(blank=True, null=True)
    x_studio_2 = models.TextField(blank=True, null=True)
    x_studio_3 = models.TextField(blank=True, null=True)
    x_studio_4 = models.TextField(blank=True, null=True)
    x_studio_5 = models.TextField(blank=True, null=True)
    x_studio_text_field_rqlt8 = models.TextField(db_column='x_studio_text_field_RqLT8', blank=True, null=True)  # Field name made lowercase.
    x_studio_1_1 = models.TextField(blank=True, null=True)
    x_studio_2_1 = models.TextField(blank=True, null=True)
    x_studio_3_1 = models.TextField(blank=True, null=True)
    x_studio_4_1 = models.TextField(blank=True, null=True)
    x_studio_5_1 = models.TextField(blank=True, null=True)
    x_studio_6 = models.TextField(blank=True, null=True)
    x_studio_maintenance_cost_1 = models.ForeignKey('ResCurrency',    models.DO_NOTHING, related_name="+", db_column='x_studio_maintenance_cost_1', blank=True, null=True)
    x_studio_monetary_field_vpfgz = models.DecimalField(db_column='x_studio_monetary_field_vPfGZ', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
    x_currency = models.ForeignKey('ResCurrency',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_studio_maintenance_date_check = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'maintenance_request'


class MaintenanceStage(models.Model):
    name = models.CharField(max_length=200)
    sequence = models.IntegerField()
    fold = models.BooleanField(blank=True, null=True)
    done = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'maintenance_stage'


class MaintenanceTeam(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    color = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'maintenance_team'


class MaintenanceTeamUsersRel(models.Model):
    maintenance_team = models.OneToOneField(MaintenanceTeam,    models.DO_NOTHING, related_name="+", primary_key=True)
    res_users = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'maintenance_team_users_rel'
        unique_together = (('maintenance_team', 'res_users'),)


class MeetingCategoryRel(models.Model):
    event = models.OneToOneField(CalendarEvent,    models.DO_NOTHING, related_name="+", primary_key=True)
    type = models.ForeignKey(CalendarEventType,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'meeting_category_rel'
        unique_together = (('event', 'type'),)


class MergeOpportunityRel(models.Model):
    merge = models.OneToOneField(CrmMergeOpportunity,    models.DO_NOTHING, related_name="+", primary_key=True)
    opportunity = models.ForeignKey(CrmLead,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'merge_opportunity_rel'
        unique_together = (('merge', 'opportunity'),)


class MessageAttachmentRel(models.Model):
    message = models.OneToOneField(MailMessage,    models.DO_NOTHING, related_name="+", primary_key=True)
    attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'message_attachment_rel'
        unique_together = (('message', 'attachment'),)


class MrpBom(models.Model):
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    code = models.CharField(max_length=200, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    type = models.CharField(max_length=200)
    product_tmpl = models.ForeignKey('ProductTemplate',    models.DO_NOTHING, related_name="+")
    product = models.ForeignKey('ProductProduct',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    product_uom = models.ForeignKey('UomUom',    models.DO_NOTHING, related_name="+")
    sequence = models.IntegerField()
    ready_to_produce = models.CharField(max_length=200)
    picking_type = models.ForeignKey('StockPickingType',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    consumption = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mrp_bom'


class MrpBomByproduct(models.Model):
    product = models.ForeignKey('ProductProduct',    models.DO_NOTHING, related_name="+")
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    product_uom = models.ForeignKey('UomUom',    models.DO_NOTHING, related_name="+")
    bom = models.ForeignKey(MrpBom,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    operation = models.ForeignKey('MrpRoutingWorkcenter',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mrp_bom_byproduct'


class MrpBomLine(models.Model):
    product = models.ForeignKey('ProductProduct',    models.DO_NOTHING, related_name="+")
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    product_uom = models.ForeignKey('UomUom',    models.DO_NOTHING, related_name="+")
    sequence = models.IntegerField()
    bom = models.ForeignKey(MrpBom,    models.DO_NOTHING, related_name="+")
    operation = models.ForeignKey('MrpRoutingWorkcenter',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mrp_bom_line'


class MrpBomLineProductTemplateAttributeValueRel(models.Model):
    mrp_bom_line = models.OneToOneField(MrpBomLine,    models.DO_NOTHING, related_name="+", primary_key=True)
    product_template_attribute_value = models.ForeignKey('ProductTemplateAttributeValue',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'mrp_bom_line_product_template_attribute_value_rel'
        unique_together = (('mrp_bom_line', 'product_template_attribute_value'),)


class MrpBomSubcontractor(models.Model):
    mrp_bom = models.OneToOneField(MrpBom,    models.DO_NOTHING, related_name="+", primary_key=True)
    res_partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'mrp_bom_subcontractor'
        unique_together = (('mrp_bom', 'res_partner'),)


class MrpConsumptionWarning(models.Model):
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mrp_consumption_warning'


class MrpConsumptionWarningLine(models.Model):
    mrp_consumption_warning = models.ForeignKey(MrpConsumptionWarning,    models.DO_NOTHING, related_name="+")
    mrp_production = models.ForeignKey('MrpProduction',    models.DO_NOTHING, related_name="+")
    product = models.ForeignKey('ProductProduct',    models.DO_NOTHING, related_name="+")
    product_consumed_qty_uom = models.FloatField(blank=True, null=True)
    product_expected_qty_uom = models.FloatField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mrp_consumption_warning_line'


class MrpConsumptionWarningMrpProductionRel(models.Model):
    mrp_consumption_warning = models.OneToOneField(MrpConsumptionWarning,    models.DO_NOTHING, related_name="+", primary_key=True)
    mrp_production = models.ForeignKey('MrpProduction',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'mrp_consumption_warning_mrp_production_rel'
        unique_together = (('mrp_consumption_warning', 'mrp_production'),)


class MrpDocument(models.Model):
    ir_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+")
    active = models.BooleanField(blank=True, null=True)
    priority = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mrp_document'


class MrpImmediateProduction(models.Model):
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mrp_immediate_production'


class MrpImmediateProductionLine(models.Model):
    immediate_production = models.ForeignKey(MrpImmediateProduction,    models.DO_NOTHING, related_name="+")
    production = models.ForeignKey('MrpProduction',    models.DO_NOTHING, related_name="+")
    to_immediate = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mrp_immediate_production_line'


class MrpMpsForecastDetails(models.Model):
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mrp_mps_forecast_details'


class MrpMpsForecastDetailsPurchaseOrderLineRel(models.Model):
    mrp_mps_forecast_details = models.OneToOneField(MrpMpsForecastDetails,    models.DO_NOTHING, related_name="+", primary_key=True)
    purchase_order_line = models.ForeignKey('PurchaseOrderLine',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'mrp_mps_forecast_details_purchase_order_line_rel'
        unique_together = (('mrp_mps_forecast_details', 'purchase_order_line'),)


class MrpMpsForecastDetailsStockMoveRel(models.Model):
    mrp_mps_forecast_details = models.OneToOneField(MrpMpsForecastDetails,    models.DO_NOTHING, related_name="+", primary_key=True)
    stock_move = models.ForeignKey('StockMove',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'mrp_mps_forecast_details_stock_move_rel'
        unique_together = (('mrp_mps_forecast_details', 'stock_move'),)


class MrpProductForecast(models.Model):
    production_schedule = models.ForeignKey('MrpProductionSchedule',    models.DO_NOTHING, related_name="+")
    date = models.DateField()
    forecast_qty = models.FloatField(blank=True, null=True)
    replenish_qty = models.FloatField(blank=True, null=True)
    replenish_qty_updated = models.BooleanField(blank=True, null=True)
    procurement_launched = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mrp_product_forecast'


class MrpProduction(models.Model):
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    priority = models.CharField(max_length=200, blank=True, null=True)
    backorder_sequence = models.IntegerField()
    origin = models.CharField(max_length=200, blank=True, null=True)
    product = models.ForeignKey('ProductProduct',    models.DO_NOTHING, related_name="+")
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    product_uom = models.ForeignKey('UomUom',    models.DO_NOTHING, related_name="+")
    lot_producing = models.ForeignKey('StockProductionLot',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    qty_producing = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    product_uom_qty = models.FloatField(blank=True, null=True)
    picking_type = models.ForeignKey('StockPickingType',    models.DO_NOTHING, related_name="+")
    location_src = models.ForeignKey('StockLocation',    models.DO_NOTHING, related_name="+")
    location_dest = models.ForeignKey('StockLocation',    models.DO_NOTHING, related_name="+")
    date_planned_start = models.DateTimeField()
    date_planned_finished = models.DateTimeField(blank=True, null=True)
    date_deadline = models.DateTimeField(blank=True, null=True)
    date_start = models.DateTimeField(blank=True, null=True)
    date_finished = models.DateTimeField(blank=True, null=True)
    bom = models.ForeignKey(MrpBom,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    reservation_state = models.CharField(max_length=200, blank=True, null=True)
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    procurement_group = models.ForeignKey('ProcurementGroup',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    product_description_variants = models.CharField(max_length=200, blank=True, null=True)
    orderpoint = models.ForeignKey('StockWarehouseOrderpoint',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    propagate_cancel = models.BooleanField(blank=True, null=True)
    is_locked = models.BooleanField(blank=True, null=True)
    production_location = models.ForeignKey('StockLocation',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    consumption = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    extra_cost = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mrp_production'
        unique_together = (('name', 'company'),)


class MrpProductionBackorder(models.Model):
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mrp_production_backorder'


class MrpProductionBackorderLine(models.Model):
    mrp_production_backorder = models.ForeignKey(MrpProductionBackorder,    models.DO_NOTHING, related_name="+")
    mrp_production = models.ForeignKey(MrpProduction,    models.DO_NOTHING, related_name="+")
    to_backorder = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mrp_production_backorder_line'


class MrpProductionMrpProductionBackorderRel(models.Model):
    mrp_production_backorder = models.OneToOneField(MrpProductionBackorder,    models.DO_NOTHING, related_name="+", primary_key=True)
    mrp_production = models.ForeignKey(MrpProduction,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'mrp_production_mrp_production_backorder_rel'
        unique_together = (('mrp_production_backorder', 'mrp_production'),)


class MrpProductionProductionRel(models.Model):
    mrp_immediate_production = models.OneToOneField(MrpImmediateProduction,    models.DO_NOTHING, related_name="+", primary_key=True)
    mrp_production = models.ForeignKey(MrpProduction,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'mrp_production_production_rel'
        unique_together = (('mrp_immediate_production', 'mrp_production'),)


class MrpProductionSchedule(models.Model):
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    product = models.ForeignKey('ProductProduct',    models.DO_NOTHING, related_name="+")
    sequence = models.IntegerField()
    warehouse = models.ForeignKey('StockWarehouse',    models.DO_NOTHING, related_name="+")
    forecast_target_qty = models.FloatField(blank=True, null=True)
    min_to_replenish_qty = models.FloatField(blank=True, null=True)
    max_to_replenish_qty = models.FloatField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mrp_production_schedule'
        unique_together = (('warehouse', 'product'),)


class MrpRoutingWorkcenter(models.Model):
    name = models.CharField(max_length=200)
    workcenter = models.ForeignKey('MrpWorkcenter',    models.DO_NOTHING, related_name="+")
    sequence = models.IntegerField()
    bom = models.ForeignKey(MrpBom,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    worksheet_type = models.CharField(max_length=200, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    worksheet_google_slide = models.CharField(max_length=200, blank=True, null=True)
    time_mode = models.CharField(max_length=200, blank=True, null=True)
    time_mode_batch = models.IntegerField()
    time_cycle_manual = models.FloatField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mrp_routing_workcenter'


class MrpUnbuild(models.Model):
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    product = models.ForeignKey('ProductProduct',    models.DO_NOTHING, related_name="+")
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    product_qty = models.FloatField()
    product_uom = models.ForeignKey('UomUom',    models.DO_NOTHING, related_name="+")
    bom = models.ForeignKey(MrpBom,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    mo = models.ForeignKey(MrpProduction,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    lot = models.ForeignKey('StockProductionLot',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    location = models.ForeignKey('StockLocation',    models.DO_NOTHING, related_name="+")
    location_dest = models.ForeignKey('StockLocation',    models.DO_NOTHING, related_name="+")
    state = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mrp_unbuild'


class MrpWorkcenter(models.Model):
    resource = models.ForeignKey('ResourceResource',    models.DO_NOTHING, related_name="+")
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    resource_calendar = models.ForeignKey('ResourceCalendar',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    time_efficiency = models.FloatField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    code = models.CharField(max_length=200, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    capacity = models.FloatField(blank=True, null=True)
    sequence = models.IntegerField()
    color = models.IntegerField()
    costs_hour = models.FloatField(blank=True, null=True)
    time_start = models.FloatField(blank=True, null=True)
    time_stop = models.FloatField(blank=True, null=True)
    working_state = models.CharField(max_length=200, blank=True, null=True)
    oee_target = models.FloatField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    costs_hour_account = models.ForeignKey(AccountAnalyticAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mrp_workcenter'


class MrpWorkcenterAlternativeRel(models.Model):
    workcenter = models.OneToOneField(MrpWorkcenter,    models.DO_NOTHING, related_name="+", primary_key=True)
    alternative_workcenter = models.ForeignKey(MrpWorkcenter,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'mrp_workcenter_alternative_rel'
        unique_together = (('workcenter', 'alternative_workcenter'),)


class MrpWorkcenterProductivity(models.Model):
    workcenter = models.ForeignKey(MrpWorkcenter,    models.DO_NOTHING, related_name="+")
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    workorder = models.ForeignKey('MrpWorkorder',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    loss = models.ForeignKey('MrpWorkcenterProductivityLoss',    models.DO_NOTHING, related_name="+")
    loss_type = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField(blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    cost_already_recorded = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mrp_workcenter_productivity'


class MrpWorkcenterProductivityLoss(models.Model):
    name = models.CharField(max_length=200)
    sequence = models.IntegerField()
    manual = models.BooleanField(blank=True, null=True)
    loss = models.ForeignKey('MrpWorkcenterProductivityLossType',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    loss_type = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mrp_workcenter_productivity_loss'


class MrpWorkcenterProductivityLossType(models.Model):
    loss_type = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mrp_workcenter_productivity_loss_type'


class MrpWorkorder(models.Model):
    name = models.CharField(max_length=200)
    workcenter = models.ForeignKey(MrpWorkcenter,    models.DO_NOTHING, related_name="+")
    product = models.ForeignKey('ProductProduct',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    product_uom = models.ForeignKey('UomUom',    models.DO_NOTHING, related_name="+")
    production = models.ForeignKey(MrpProduction,    models.DO_NOTHING, related_name="+")
    production_availability = models.CharField(max_length=200, blank=True, null=True)
    qty_produced = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    leave = models.ForeignKey('ResourceCalendarLeaves',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    date_planned_start = models.DateTimeField(blank=True, null=True)
    date_planned_finished = models.DateTimeField(blank=True, null=True)
    date_start = models.DateTimeField(blank=True, null=True)
    date_finished = models.DateTimeField(blank=True, null=True)
    duration_expected = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)
    duration_unit = models.FloatField(blank=True, null=True)
    duration_percent = models.IntegerField()
    operation = models.ForeignKey(MrpRoutingWorkcenter,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    next_work_order = models.ForeignKey('self',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    production_date = models.DateTimeField(blank=True, null=True)
    consumption = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    current_quality_check = models.ForeignKey('QualityCheckk',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    allow_producing_quantity_change = models.BooleanField(blank=True, null=True)
    is_first_step = models.BooleanField(blank=True, null=True)
    is_last_step = models.BooleanField(blank=True, null=True)
    skip_completed_checks = models.BooleanField(blank=True, null=True)
    worksheet_page = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'mrp_workorder'


class MrpWorkorderAdditionalProduct(models.Model):
    product = models.ForeignKey('ProductProduct',    models.DO_NOTHING, related_name="+")
    product_qty = models.FloatField()
    product_uom = models.ForeignKey('UomUom',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    type = models.CharField(max_length=200, blank=True, null=True)
    workorder = models.ForeignKey(MrpWorkorder,    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mrp_workorder_additional_product'


class MrpWorkorderQualityPointRel(models.Model):
    mrp_workorder = models.OneToOneField(MrpWorkorder,    models.DO_NOTHING, related_name="+", primary_key=True)
    quality_point = models.ForeignKey('QualityPoint',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'mrp_workorder_quality_point_rel'
        unique_together = (('mrp_workorder', 'quality_point'),)


class MultipleInvoice(models.Model):
    sequence = models.IntegerField()
    copy_name = models.CharField(max_length=200, blank=True, null=True)
    journal = models.ForeignKey(AccountJournal,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'multiple_invoice'


class MultipleInvoiceLayout(models.Model):
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    journal = models.ForeignKey(AccountJournal,    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'multiple_invoice_layout'


class NontechNontech(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'nontech_nontech'


class PaymentAcquirer(models.Model):
    name = models.CharField(max_length=200)
    color = models.IntegerField()
    display_as = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    sequence = models.IntegerField()
    provider = models.CharField(max_length=200)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    view_template = models.ForeignKey(IrUiView,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    registration_view_template = models.ForeignKey(IrUiView,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    state = models.CharField(max_length=200)
    capture_manually = models.BooleanField(blank=True, null=True)
    journal = models.ForeignKey(AccountJournal,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    check_validity = models.BooleanField(blank=True, null=True)
    pre_msg = models.TextField(blank=True, null=True)
    auth_msg = models.TextField(blank=True, null=True)
    pending_msg = models.TextField(blank=True, null=True)
    done_msg = models.TextField(blank=True, null=True)
    cancel_msg = models.TextField(blank=True, null=True)
    save_token = models.CharField(max_length=200, blank=True, null=True)
    fees_active = models.BooleanField(blank=True, null=True)
    fees_dom_fixed = models.FloatField(blank=True, null=True)
    fees_dom_var = models.FloatField(blank=True, null=True)
    fees_int_fixed = models.FloatField(blank=True, null=True)
    fees_int_var = models.FloatField(blank=True, null=True)
    qr_code = models.BooleanField(blank=True, null=True)
    module = models.ForeignKey(IrModuleModule,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    module_state = models.CharField(max_length=200, blank=True, null=True)
    payment_flow = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    so_reference_type = models.CharField(max_length=200, blank=True, null=True)
    website = models.ForeignKey('Website',    models.DO_NOTHING, related_name="+", blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'payment_acquirer'


class PaymentAcquirerOnboardingWizard(models.Model):
    payment_method = models.CharField(max_length=200, blank=True, null=True)
    paypal_user_type = models.CharField(max_length=200, blank=True, null=True)
    paypal_email_account = models.CharField(max_length=200, blank=True, null=True)
    paypal_seller_account = models.CharField(max_length=200, blank=True, null=True)
    paypal_pdt_token = models.CharField(max_length=200, blank=True, null=True)
    stripe_secret_key = models.CharField(max_length=200, blank=True, null=True)
    stripe_publishable_key = models.CharField(max_length=200, blank=True, null=True)
    manual_name = models.CharField(max_length=200, blank=True, null=True)
    journal_name = models.CharField(max_length=200, blank=True, null=True)
    acc_number = models.CharField(max_length=200, blank=True, null=True)
    manual_post_msg = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'payment_acquirer_onboarding_wizard'


class PaymentAcquirerPaymentIconRel(models.Model):
    payment_acquirer = models.OneToOneField(PaymentAcquirer,    models.DO_NOTHING, related_name="+", primary_key=True)
    payment_icon = models.ForeignKey('PaymentIcon',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'payment_acquirer_payment_icon_rel'
        unique_together = (('payment_acquirer', 'payment_icon'),)


class PaymentCountryRel(models.Model):
    payment = models.OneToOneField(PaymentAcquirer,    models.DO_NOTHING, related_name="+", primary_key=True)
    country = models.ForeignKey('ResCountry',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'payment_country_rel'
        unique_together = (('payment', 'country'),)


class PaymentIcon(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'payment_icon'


class PaymentLinkWizard(models.Model):
    res_model = models.CharField(max_length=200)
    res_id = models.IntegerField()
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    amount_max = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'payment_link_wizard'


class PaymentToken(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+")
    acquirer = models.ForeignKey(PaymentAcquirer,    models.DO_NOTHING, related_name="+")
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    acquirer_ref = models.CharField(max_length=200)
    active = models.BooleanField(blank=True, null=True)
    verified = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'payment_token'


class PaymentTransaction(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    acquirer = models.ForeignKey(PaymentAcquirer,    models.DO_NOTHING, related_name="+")
    type = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    state_message = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    fees = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency',    models.DO_NOTHING, related_name="+")
    reference = models.CharField(unique=True, max_length=200)
    acquirer_reference = models.CharField(max_length=200, blank=True, null=True)
    partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    partner_name = models.CharField(max_length=200, blank=True, null=True)
    partner_lang = models.CharField(max_length=200, blank=True, null=True)
    partner_email = models.CharField(max_length=200, blank=True, null=True)
    partner_zip = models.CharField(max_length=200, blank=True, null=True)
    partner_address = models.CharField(max_length=200, blank=True, null=True)
    partner_city = models.CharField(max_length=200, blank=True, null=True)
    partner_country = models.ForeignKey('ResCountry',    models.DO_NOTHING, related_name="+")
    partner_phone = models.CharField(max_length=200, blank=True, null=True)
    html_3ds = models.CharField(max_length=200, blank=True, null=True)
    callback_model = models.ForeignKey(IrModel,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    callback_res_id = models.IntegerField()
    callback_method = models.CharField(max_length=200, blank=True, null=True)
    callback_hash = models.CharField(max_length=200, blank=True, null=True)
    return_url = models.CharField(max_length=200, blank=True, null=True)
    is_processed = models.BooleanField(blank=True, null=True)
    payment_token = models.ForeignKey(PaymentToken,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    payment = models.ForeignKey(AccountPayment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'payment_transaction'


class PhoneBlacklist(models.Model):
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    number = models.CharField(unique=True, max_length=200)
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'phone_blacklist'


class PhoneBlacklistRemove(models.Model):
    phone = models.CharField(max_length=200)
    reason = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'phone_blacklist_remove'


class PlanningPlanning(models.Model):
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    include_unassigned = models.BooleanField(blank=True, null=True)
    access_token = models.CharField(max_length=200)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'planning_planning'


class PlanningPlanningPlanningSlotRel(models.Model):
    planning_planning = models.OneToOneField(PlanningPlanning,    models.DO_NOTHING, related_name="+", primary_key=True)
    planning_slot = models.ForeignKey('PlanningSlot',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'planning_planning_planning_slot_rel'
        unique_together = (('planning_planning', 'planning_slot'),)


class PlanningRecurrency(models.Model):
    repeat_interval = models.IntegerField()
    repeat_type = models.CharField(max_length=200, blank=True, null=True)
    repeat_until = models.DateTimeField(blank=True, null=True)
    last_generated_end_datetime = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'planning_recurrency'


class PlanningRole(models.Model):
    name = models.CharField(max_length=200)
    color = models.IntegerField()
    sequence = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'planning_role'


class PlanningSend(models.Model):
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    include_unassigned = models.BooleanField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'planning_send'


class PlanningSendPlanningSlotRel(models.Model):
    planning_send = models.OneToOneField(PlanningSend,    models.DO_NOTHING, related_name="+", primary_key=True)
    planning_slot = models.ForeignKey('PlanningSlot',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'planning_send_planning_slot_rel'
        unique_together = (('planning_send', 'planning_slot'),)


class PlanningSlot(models.Model):
    name = models.TextField(blank=True, null=True)
    employee = models.ForeignKey(HrEmployee,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    department = models.ForeignKey(HrDepartment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    role = models.ForeignKey(PlanningRole,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    was_copied = models.BooleanField(blank=True, null=True)
    access_token = models.CharField(max_length=200)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    allocated_hours = models.FloatField(blank=True, null=True)
    allocated_percentage = models.FloatField(blank=True, null=True)
    working_days_count = models.IntegerField()
    is_published = models.BooleanField(blank=True, null=True)
    publication_warning = models.BooleanField(blank=True, null=True)
    template = models.ForeignKey('PlanningSlotTemplate',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    template_reset = models.BooleanField(blank=True, null=True)
    previous_template = models.ForeignKey('PlanningSlotTemplate',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    recurrency = models.ForeignKey(PlanningRecurrency,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    project = models.ForeignKey('ProjectProject',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    task = models.ForeignKey('ProjectTask',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    parent = models.ForeignKey('ProjectTask',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    effective_hours = models.FloatField(blank=True, null=True)
    percentage_hours = models.FloatField(blank=True, null=True)
    order_line = models.ForeignKey('SaleOrderLine',    models.DO_NOTHING, related_name="+", blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'planning_slot'


class PlanningSlotTemplate(models.Model):
    role = models.ForeignKey(PlanningRole,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    start_time = models.FloatField(blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    project = models.ForeignKey('ProjectProject',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    task = models.ForeignKey('ProjectTask',    models.DO_NOTHING, related_name="+", blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'planning_slot_template'


class PortalShare(models.Model):
    res_model = models.CharField(max_length=200)
    res_id = models.IntegerField()
    note = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'portal_share'


class PortalShareResPartnerRel(models.Model):
    portal_share = models.OneToOneField(PortalShare,    models.DO_NOTHING, related_name="+", primary_key=True)
    res_partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'portal_share_res_partner_rel'
        unique_together = (('portal_share', 'res_partner'),)


class PortalWizard(models.Model):
    welcome_message = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'portal_wizard'


class PortalWizardUser(models.Model):
    wizard = models.ForeignKey(PortalWizard,    models.DO_NOTHING, related_name="+")
    partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+")
    email = models.CharField(max_length=200, blank=True, null=True)
    in_portal = models.BooleanField(blank=True, null=True)
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'portal_wizard_user'


class PrintPrenumberedChecks(models.Model):
    next_check_number = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'print_prenumbered_checks'


class ProcurementGroup(models.Model):
    partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    name = models.CharField(max_length=200)
    move_type = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    sale = models.ForeignKey('SaleOrder',    models.DO_NOTHING, related_name="+", blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'procurement_group'


class ProductAccessoryRel(models.Model):
    src = models.OneToOneField('ProductTemplate',    models.DO_NOTHING, related_name="+", primary_key=True)
    dest = models.ForeignKey('ProductProduct',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'product_accessory_rel'
        unique_together = (('src', 'dest'),)


class ProductAlternativeRel(models.Model):
    src = models.OneToOneField('ProductTemplate',    models.DO_NOTHING, related_name="+", primary_key=True)
    dest = models.ForeignKey('ProductTemplate',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'product_alternative_rel'
        unique_together = (('src', 'dest'),)


class ProductAttrExclusionValueIdsRel(models.Model):
    product_template_attribute_exclusion = models.OneToOneField('ProductTemplateAttributeExclusion',    models.DO_NOTHING, related_name="+", primary_key=True)
    product_template_attribute_value = models.ForeignKey('ProductTemplateAttributeValue',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'product_attr_exclusion_value_ids_rel'
        unique_together = (('product_template_attribute_exclusion', 'product_template_attribute_value'),)


class ProductAttribute(models.Model):
    name = models.CharField(max_length=200)
    sequence = models.IntegerField()
    create_variant = models.CharField(max_length=200)
    display_type = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'product_attribute'


class ProductAttributeCustomValue(models.Model):
    custom_product_template_attribute_value = models.ForeignKey('ProductTemplateAttributeValue',    models.DO_NOTHING, related_name="+")
    custom_value = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    sale_order_line = models.ForeignKey('SaleOrderLine',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'product_attribute_custom_value'
        unique_together = (('custom_product_template_attribute_value', 'sale_order_line'),)


class ProductAttributeProductTemplateRel(models.Model):
    product_attribute = models.OneToOneField(ProductAttribute,    models.DO_NOTHING, related_name="+", primary_key=True)
    product_template = models.ForeignKey('ProductTemplate',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'product_attribute_product_template_rel'
        unique_together = (('product_attribute', 'product_template'),)


class ProductAttributeValue(models.Model):
    name = models.CharField(max_length=200)
    sequence = models.IntegerField()
    attribute = models.ForeignKey(ProductAttribute,    models.DO_NOTHING, related_name="+")
    is_custom = models.BooleanField(blank=True, null=True)
    html_color = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'product_attribute_value'
        unique_together = (('name', 'attribute'),)


class ProductAttributeValueProductTemplateAttributeLineRel(models.Model):
    product_attribute_value = models.OneToOneField(ProductAttributeValue,    models.DO_NOTHING, related_name="+", primary_key=True)
    product_template_attribute_line = models.ForeignKey('ProductTemplateAttributeLine',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'product_attribute_value_product_template_attribute_line_rel'
        unique_together = (('product_attribute_value', 'product_template_attribute_line'),)


class ProductCategory(models.Model):
    name = models.CharField(max_length=200)
    complete_name = models.CharField(max_length=200, blank=True, null=True)
    parent = models.ForeignKey('self',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    parent_path = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    removal_strategy = models.ForeignKey('ProductRemoval',    models.DO_NOTHING, related_name="+", blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'product_category'


class ProductImage(models.Model):
    name = models.CharField(max_length=200)
    sequence = models.IntegerField()
    product_tmpl = models.ForeignKey('ProductTemplate',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    product_variant = models.ForeignKey('ProductProduct',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    video_url = models.CharField(max_length=200, blank=True, null=True)
    can_image_1024_be_zoomed = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'product_image'


class ProductMargin(models.Model):
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    invoice_state = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'product_margin'


class ProductPackaging(models.Model):
    name = models.CharField(max_length=200)
    sequence = models.IntegerField()
    product = models.ForeignKey('ProductProduct',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    qty = models.FloatField(blank=True, null=True)
    barcode = models.CharField(max_length=200, blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'product_packaging'


class ProductPricelist(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(blank=True, null=True)
    currency = models.ForeignKey('ResCurrency',    models.DO_NOTHING, related_name="+")
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    sequence = models.IntegerField()
    discount_policy = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    website = models.ForeignKey('Website',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    code = models.CharField(max_length=200, blank=True, null=True)
    selectable = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'product_pricelist'


class ProductPricelistItem(models.Model):
    product_tmpl = models.ForeignKey('ProductTemplate',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    product = models.ForeignKey('ProductProduct',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    categ = models.ForeignKey(ProductCategory,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    min_quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    applied_on = models.CharField(max_length=200)
    base = models.CharField(max_length=200)
    base_pricelist = models.ForeignKey(ProductPricelist,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    pricelist = models.ForeignKey(ProductPricelist,    models.DO_NOTHING, related_name="+")
    price_surcharge = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_discount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_round = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_min_margin = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_max_margin = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    currency = models.ForeignKey('ResCurrency',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    date_start = models.DateTimeField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)
    compute_price = models.CharField(max_length=200)
    fixed_price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    percent_price = models.FloatField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'product_pricelist_item'


class ProductProduct(models.Model):
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    default_code = models.CharField(max_length=200, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    product_tmpl = models.ForeignKey('ProductTemplate',    models.DO_NOTHING, related_name="+")
    barcode = models.CharField(unique=True, max_length=200, blank=True, null=True)
    combination_indices = models.CharField(max_length=200, blank=True, null=True)
    volume = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    weight = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    can_image_variant_1024_be_zoomed = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'product_product'
        unique_together = (('product_tmpl', 'combination_indices'),)


class ProductProductQualityPointRel(models.Model):
    quality_point = models.OneToOneField('QualityPoint',    models.DO_NOTHING, related_name="+", primary_key=True)
    product_product = models.ForeignKey(ProductProduct,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'product_product_quality_point_rel'
        unique_together = (('quality_point', 'product_product'),)


class ProductProductStockInventoryRel(models.Model):
    stock_inventory = models.OneToOneField('StockInventory',    models.DO_NOTHING, related_name="+", primary_key=True)
    product_product = models.ForeignKey(ProductProduct,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'product_product_stock_inventory_rel'
        unique_together = (('stock_inventory', 'product_product'),)


class ProductPublicCategory(models.Model):
    website_meta_title = models.CharField(max_length=200, blank=True, null=True)
    website_meta_description = models.TextField(blank=True, null=True)
    website_meta_keywords = models.CharField(max_length=200, blank=True, null=True)
    website_meta_og_img = models.CharField(max_length=200, blank=True, null=True)
    seo_name = models.CharField(max_length=200, blank=True, null=True)
    website = models.ForeignKey('Website',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    name = models.CharField(max_length=200)
    parent = models.ForeignKey('self',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    parent_path = models.CharField(max_length=200, blank=True, null=True)
    sequence = models.IntegerField()
    website_description = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'product_public_category'


class ProductPublicCategoryProductTemplateRel(models.Model):
    product_public_category = models.OneToOneField(ProductPublicCategory,    models.DO_NOTHING, related_name="+", primary_key=True)
    product_template = models.ForeignKey('ProductTemplate',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'product_public_category_product_template_rel'
        unique_together = (('product_public_category', 'product_template'),)


class ProductRemoval(models.Model):
    name = models.CharField(max_length=200)
    method = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'product_removal'


class ProductReplenish(models.Model):
    product = models.ForeignKey(ProductProduct,    models.DO_NOTHING, related_name="+")
    product_tmpl = models.ForeignKey('ProductTemplate',    models.DO_NOTHING, related_name="+")
    product_has_variants = models.BooleanField()
    product_uom = models.ForeignKey('UomUom',    models.DO_NOTHING, related_name="+")
    quantity = models.FloatField()
    date_planned = models.DateTimeField()
    warehouse = models.ForeignKey('StockWarehouse',    models.DO_NOTHING, related_name="+")
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'product_replenish'


class ProductReplenishStockLocationRouteRel(models.Model):
    product_replenish = models.OneToOneField(ProductReplenish,    models.DO_NOTHING, related_name="+", primary_key=True)
    stock_location_route = models.ForeignKey('StockLocationRoute',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'product_replenish_stock_location_route_rel'
        unique_together = (('product_replenish', 'stock_location_route'),)


class ProductRibbon(models.Model):
    html = models.CharField(max_length=200)
    bg_color = models.CharField(max_length=200, blank=True, null=True)
    text_color = models.CharField(max_length=200, blank=True, null=True)
    html_class = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'product_ribbon'


class ProductSupplierTaxesRel(models.Model):
    prod = models.OneToOneField('ProductTemplate',    models.DO_NOTHING, related_name="+", primary_key=True)
    tax = models.ForeignKey(AccountTax,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'product_supplier_taxes_rel'
        unique_together = (('prod', 'tax'),)


class ProductSupplierinfo(models.Model):
    name = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+", db_column='name')
    product_name = models.CharField(max_length=200, blank=True, null=True)
    product_code = models.CharField(max_length=200, blank=True, null=True)
    sequence = models.IntegerField()
    min_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    price = models.DecimalField(max_digits=65535, decimal_places=65535)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    currency = models.ForeignKey('ResCurrency',    models.DO_NOTHING, related_name="+")
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    product = models.ForeignKey(ProductProduct,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    product_tmpl = models.ForeignKey('ProductTemplate',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    delay = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    purchase_requisition_line = models.ForeignKey('PurchaseRequisitionLine',    models.DO_NOTHING, related_name="+", blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'product_supplierinfo'


class ProductTaxesRel(models.Model):
    prod = models.OneToOneField('ProductTemplate',    models.DO_NOTHING, related_name="+", primary_key=True)
    tax = models.ForeignKey(AccountTax,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'product_taxes_rel'
        unique_together = (('prod', 'tax'),)


class ProductTemplate(models.Model):
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    name = models.CharField(max_length=200)
    sequence = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    description_purchase = models.TextField(blank=True, null=True)
    description_sale = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=200)
    categ = models.ForeignKey(ProductCategory,    models.DO_NOTHING, related_name="+")
    list_price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    volume = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    weight = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sale_ok = models.BooleanField(blank=True, null=True)
    purchase_ok = models.BooleanField(blank=True, null=True)
    uom = models.ForeignKey('UomUom',    models.DO_NOTHING, related_name="+")
    uom_po = models.ForeignKey('UomUom',    models.DO_NOTHING, related_name="+")
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    color = models.IntegerField()
    default_code = models.CharField(max_length=200, blank=True, null=True)
    can_image_1024_be_zoomed = models.BooleanField(blank=True, null=True)
    has_configurable_attributes = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    sale_delay = models.FloatField(blank=True, null=True)
    tracking = models.CharField(max_length=200)
    description_picking = models.TextField(blank=True, null=True)
    description_pickingout = models.TextField(blank=True, null=True)
    description_pickingin = models.TextField(blank=True, null=True)
    purchase_method = models.CharField(max_length=200, blank=True, null=True)
    purchase_line_warn = models.CharField(max_length=200)
    purchase_line_warn_msg = models.TextField(blank=True, null=True)
    service_type = models.CharField(max_length=200, blank=True, null=True)
    sale_line_warn = models.CharField(max_length=200)
    sale_line_warn_msg = models.TextField(blank=True, null=True)
    expense_policy = models.CharField(max_length=200, blank=True, null=True)
    invoice_policy = models.CharField(max_length=200, blank=True, null=True)
    service_to_purchase = models.BooleanField(blank=True, null=True)
    l10n_in_hsn_code = models.CharField(max_length=200, blank=True, null=True)
    l10n_in_hsn_description = models.CharField(max_length=200, blank=True, null=True)
    service_tracking = models.CharField(max_length=200, blank=True, null=True)
    purchase_requisition = models.CharField(max_length=200, blank=True, null=True)
    use_expiration_date = models.BooleanField(blank=True, null=True)
    expiration_time = models.IntegerField()
    use_time = models.IntegerField()
    removal_time = models.IntegerField()
    alert_time = models.IntegerField()
    produce_delay = models.FloatField(blank=True, null=True)
    rating_last_value = models.FloatField(blank=True, null=True)
    website_meta_title = models.CharField(max_length=200, blank=True, null=True)
    website_meta_description = models.TextField(blank=True, null=True)
    website_meta_keywords = models.CharField(max_length=200, blank=True, null=True)
    website_meta_og_img = models.CharField(max_length=200, blank=True, null=True)
    seo_name = models.CharField(max_length=200, blank=True, null=True)
    website = models.ForeignKey('Website',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    is_published = models.BooleanField(blank=True, null=True)
    website_description = models.TextField(blank=True, null=True)
    website_size_x = models.IntegerField()
    website_size_y = models.IntegerField()
    website_ribbon = models.ForeignKey(ProductRibbon,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    website_sequence = models.IntegerField()
    inventory_availability = models.CharField(max_length=200, blank=True, null=True)
    available_threshold = models.FloatField(blank=True, null=True)
    custom_message = models.TextField(blank=True, null=True)
    x_studio_internal_reference = models.CharField(max_length=200, blank=True, null=True)
    x_studio_acquisition_date = models.DateField(blank=True, null=True)
    x_studio_expiration_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'product_template'


class ProductTemplateAttributeExclusion(models.Model):
    product_template_attribute_value = models.ForeignKey('ProductTemplateAttributeValue',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    product_tmpl = models.ForeignKey(ProductTemplate,    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'product_template_attribute_exclusion'


class ProductTemplateAttributeLine(models.Model):
    active = models.BooleanField(blank=True, null=True)
    product_tmpl = models.ForeignKey(ProductTemplate,    models.DO_NOTHING, related_name="+")
    attribute = models.ForeignKey(ProductAttribute,    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'product_template_attribute_line'


class ProductTemplateAttributeValue(models.Model):
    ptav_active = models.BooleanField(blank=True, null=True)
    product_attribute_value = models.ForeignKey(ProductAttributeValue,    models.DO_NOTHING, related_name="+")
    attribute_line = models.ForeignKey(ProductTemplateAttributeLine,    models.DO_NOTHING, related_name="+")
    price_extra = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    product_tmpl = models.ForeignKey(ProductTemplate,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    attribute = models.ForeignKey(ProductAttribute,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'product_template_attribute_value'
        unique_together = (('attribute_line', 'product_attribute_value'),)


class ProductTemplateAttributeValueSaleOrderLineRel(models.Model):
    sale_order_line = models.OneToOneField('SaleOrderLine',    models.DO_NOTHING, related_name="+", primary_key=True)
    product_template_attribute_value = models.ForeignKey(ProductTemplateAttributeValue,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'product_template_attribute_value_sale_order_line_rel'
        unique_together = (('sale_order_line', 'product_template_attribute_value'),)


class ProductVariantCombination(models.Model):
    product_product = models.OneToOneField(ProductProduct,    models.DO_NOTHING, related_name="+", primary_key=True)
    product_template_attribute_value = models.ForeignKey(ProductTemplateAttributeValue,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'product_variant_combination'
        unique_together = (('product_product', 'product_template_attribute_value'),)


class ProjectAllowedInternalUsersRel(models.Model):
    project_project = models.OneToOneField('ProjectProject',    models.DO_NOTHING, related_name="+", primary_key=True)
    res_users = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'project_allowed_internal_users_rel'
        unique_together = (('project_project', 'res_users'),)


class ProjectAllowedPortalUsersRel(models.Model):
    project_project = models.OneToOneField('ProjectProject',    models.DO_NOTHING, related_name="+", primary_key=True)
    res_users = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'project_allowed_portal_users_rel'
        unique_together = (('project_project', 'res_users'),)


class ProjectCreateInvoice(models.Model):
    project = models.ForeignKey('ProjectProject',    models.DO_NOTHING, related_name="+")
    sale_order = models.ForeignKey('SaleOrder',    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'project_create_invoice'


class ProjectCreateSaleOrder(models.Model):
    project = models.ForeignKey('ProjectProject',    models.DO_NOTHING, related_name="+")
    partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+")
    link_selection = models.CharField(max_length=200)
    sale_order = models.ForeignKey('SaleOrder',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'project_create_sale_order'


class ProjectCreateSaleOrderLine(models.Model):
    wizard = models.ForeignKey(ProjectCreateSaleOrder,    models.DO_NOTHING, related_name="+")
    product = models.ForeignKey(ProductProduct,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    price_unit = models.FloatField(blank=True, null=True)
    currency = models.ForeignKey('ResCurrency',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    employee = models.ForeignKey(HrEmployee,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    sale_line = models.ForeignKey('SaleOrderLine',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'project_create_sale_order_line'
        unique_together = (('wizard', 'employee'),)


class ProjectDeleteWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'project_delete_wizard'


class ProjectDeleteWizardProjectProjectRel(models.Model):
    project_delete_wizard = models.OneToOneField(ProjectDeleteWizard,    models.DO_NOTHING, related_name="+", primary_key=True)
    project_project = models.ForeignKey('ProjectProject',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'project_delete_wizard_project_project_rel'
        unique_together = (('project_delete_wizard', 'project_project'),)


class ProjectFavoriteUserRel(models.Model):
    project = models.OneToOneField('ProjectProject',    models.DO_NOTHING, related_name="+", primary_key=True)
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'project_favorite_user_rel'
        unique_together = (('project', 'user'),)


class ProjectProject(models.Model):
    access_token = models.CharField(max_length=200, blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    sequence = models.IntegerField()
    partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    partner_email = models.CharField(max_length=200, blank=True, null=True)
    partner_phone = models.CharField(max_length=200, blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    analytic_account = models.ForeignKey(AccountAnalyticAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    label_tasks = models.CharField(max_length=200, blank=True, null=True)
    color = models.IntegerField()
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    alias = models.ForeignKey(MailAlias,    models.DO_NOTHING, related_name="+")
    privacy_visibility = models.CharField(max_length=200)
    date_start = models.DateField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    subtask_project = models.ForeignKey('self',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    allow_subtasks = models.BooleanField(blank=True, null=True)
    allow_recurring_tasks = models.BooleanField(blank=True, null=True)
    rating_request_deadline = models.DateTimeField(blank=True, null=True)
    rating_active = models.BooleanField(blank=True, null=True)
    rating_status = models.CharField(max_length=200)
    rating_status_period = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    sale_line = models.ForeignKey('SaleOrderLine',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    sale_order = models.ForeignKey('SaleOrder',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    allow_timesheets = models.BooleanField(blank=True, null=True)
    allow_timesheet_timer = models.BooleanField(blank=True, null=True)
    bill_type = models.CharField(max_length=200, blank=True, null=True)
    pricing_type = models.CharField(max_length=200, blank=True, null=True)
    allow_billable = models.BooleanField(blank=True, null=True)
    timesheet_product = models.ForeignKey(ProductProduct,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    allow_forecast = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'project_project'


class ProjectProjectProjectTaskTypeDeleteWizardRel(models.Model):
    project_task_type_delete_wizard = models.OneToOneField('ProjectTaskTypeDeleteWizard',    models.DO_NOTHING, related_name="+", primary_key=True)
    project_project = models.ForeignKey(ProjectProject,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'project_project_project_task_type_delete_wizard_rel'
        unique_together = (('project_task_type_delete_wizard', 'project_project'),)


class ProjectSaleLineEmployeeMap(models.Model):
    project = models.ForeignKey(ProjectProject,    models.DO_NOTHING, related_name="+")
    employee = models.ForeignKey(HrEmployee,    models.DO_NOTHING, related_name="+")
    sale_line = models.ForeignKey('SaleOrderLine',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    timesheet_product = models.ForeignKey(ProductProduct,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    price_unit = models.FloatField(blank=True, null=True)
    currency = models.ForeignKey('ResCurrency',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'project_sale_line_employee_map'
        unique_together = (('project', 'employee'),)


class ProjectTags(models.Model):
    name = models.CharField(unique=True, max_length=200)
    color = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'project_tags'


class ProjectTagsProjectTaskRel(models.Model):
    project_task = models.OneToOneField('ProjectTask',    models.DO_NOTHING, related_name="+", primary_key=True)
    project_tags = models.ForeignKey(ProjectTags,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'project_tags_project_task_rel'
        unique_together = (('project_task', 'project_tags'),)


class ProjectTask(models.Model):
    access_token = models.CharField(max_length=200, blank=True, null=True)
    email_cc = models.CharField(max_length=200, blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    rating_last_value = models.FloatField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    priority = models.CharField(max_length=200, blank=True, null=True)
    sequence = models.IntegerField()
    stage = models.ForeignKey('ProjectTaskType',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    kanban_state = models.CharField(max_length=200)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)
    date_assign = models.DateTimeField(blank=True, null=True)
    date_deadline = models.DateField(blank=True, null=True)
    date_last_stage_update = models.DateTimeField(blank=True, null=True)
    project = models.ForeignKey(ProjectProject,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    planned_hours = models.FloatField(blank=True, null=True)
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    partner_email = models.CharField(max_length=200, blank=True, null=True)
    partner_phone = models.CharField(max_length=200, blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    color = models.IntegerField()
    displayed_image = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    parent = models.ForeignKey('self',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    email_from = models.CharField(max_length=200, blank=True, null=True)
    working_hours_open = models.FloatField(blank=True, null=True)
    working_hours_close = models.FloatField(blank=True, null=True)
    working_days_open = models.FloatField(blank=True, null=True)
    working_days_close = models.FloatField(blank=True, null=True)
    recurring_task = models.BooleanField(blank=True, null=True)
    recurrence = models.ForeignKey('ProjectTaskRecurrence',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    planned_date_begin = models.DateTimeField(blank=True, null=True)
    planned_date_end = models.DateTimeField(blank=True, null=True)
    sale_order = models.ForeignKey('SaleOrder',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    sale_line = models.ForeignKey('SaleOrderLine',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    remaining_hours = models.FloatField(blank=True, null=True)
    effective_hours = models.FloatField(blank=True, null=True)
    total_hours_spent = models.FloatField(blank=True, null=True)
    progress = models.FloatField(blank=True, null=True)
    overtime = models.FloatField(blank=True, null=True)
    subtask_effective_hours = models.FloatField(blank=True, null=True)
    timesheet_product = models.ForeignKey(ProductProduct,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    non_allow_billable = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'project_task'


class ProjectTaskCreateSaleOrder(models.Model):
    link_selection = models.CharField(max_length=200)
    task = models.ForeignKey(ProjectTask,    models.DO_NOTHING, related_name="+")
    partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+")
    product = models.ForeignKey(ProductProduct,    models.DO_NOTHING, related_name="+")
    price_unit = models.FloatField(blank=True, null=True)
    sale_order = models.ForeignKey('SaleOrder',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    sale_line = models.ForeignKey('SaleOrderLine',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'project_task_create_sale_order'


class ProjectTaskCreateTimesheet(models.Model):
    time_spent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    task = models.ForeignKey(ProjectTask,    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'project_task_create_timesheet'


class ProjectTaskRecurrence(models.Model):
    next_recurrence_date = models.DateField(blank=True, null=True)
    recurrence_left = models.IntegerField()
    repeat_interval = models.IntegerField()
    repeat_unit = models.CharField(max_length=200, blank=True, null=True)
    repeat_type = models.CharField(max_length=200, blank=True, null=True)
    repeat_until = models.DateField(blank=True, null=True)
    repeat_number = models.IntegerField()
    repeat_on_month = models.CharField(max_length=200, blank=True, null=True)
    repeat_on_year = models.CharField(max_length=200, blank=True, null=True)
    mon = models.BooleanField(blank=True, null=True)
    tue = models.BooleanField(blank=True, null=True)
    wed = models.BooleanField(blank=True, null=True)
    thu = models.BooleanField(blank=True, null=True)
    fri = models.BooleanField(blank=True, null=True)
    sat = models.BooleanField(blank=True, null=True)
    sun = models.BooleanField(blank=True, null=True)
    repeat_day = models.CharField(max_length=200, blank=True, null=True)
    repeat_week = models.CharField(max_length=200, blank=True, null=True)
    repeat_weekday = models.CharField(max_length=200, blank=True, null=True)
    repeat_month = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'project_task_recurrence'


class ProjectTaskResUsersRel(models.Model):
    project_task = models.OneToOneField(ProjectTask,    models.DO_NOTHING, related_name="+", primary_key=True)
    res_users = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'project_task_res_users_rel'
        unique_together = (('project_task', 'res_users'),)


class ProjectTaskType(models.Model):
    active = models.BooleanField(blank=True, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    sequence = models.IntegerField()
    legend_blocked = models.CharField(max_length=200)
    legend_done = models.CharField(max_length=200)
    legend_normal = models.CharField(max_length=200)
    mail_template = models.ForeignKey(MailTemplate,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    fold = models.BooleanField(blank=True, null=True)
    rating_template = models.ForeignKey(MailTemplate,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    auto_validation_kanban_state = models.BooleanField(blank=True, null=True)
    is_closed = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'project_task_type'


class ProjectTaskTypeDeleteWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'project_task_type_delete_wizard'


class ProjectTaskTypeProjectTaskTypeDeleteWizardRel(models.Model):
    project_task_type_delete_wizard = models.OneToOneField(ProjectTaskTypeDeleteWizard,    models.DO_NOTHING, related_name="+", primary_key=True)
    project_task_type = models.ForeignKey(ProjectTaskType,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'project_task_type_project_task_type_delete_wizard_rel'
        unique_together = (('project_task_type_delete_wizard', 'project_task_type'),)


class ProjectTaskTypeRel(models.Model):
    type = models.OneToOneField(ProjectTaskType,    models.DO_NOTHING, related_name="+", primary_key=True)
    project = models.ForeignKey(ProjectProject,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'project_task_type_rel'
        unique_together = (('type', 'project'),)


class PurchaseOrder(models.Model):
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    access_token = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200)
    priority = models.CharField(max_length=200, blank=True, null=True)
    origin = models.CharField(max_length=200, blank=True, null=True)
    partner_ref = models.CharField(max_length=200, blank=True, null=True)
    date_order = models.DateTimeField()
    date_approve = models.DateTimeField(blank=True, null=True)
    partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+")
    dest_address = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    currency = models.ForeignKey('ResCurrency',    models.DO_NOTHING, related_name="+")
    state = models.CharField(max_length=200, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    invoice_count = models.IntegerField()
    invoice_status = models.CharField(max_length=200, blank=True, null=True)
    date_planned = models.DateTimeField(blank=True, null=True)
    date_calendar_start = models.DateTimeField(blank=True, null=True)
    amount_untaxed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_tax = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    fiscal_position = models.ForeignKey(AccountFiscalPosition,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    payment_term = models.ForeignKey(AccountPaymentTerm,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    incoterm = models.ForeignKey(AccountIncoterms,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    currency_rate = models.FloatField(blank=True, null=True)
    mail_reminder_confirmed = models.BooleanField(blank=True, null=True)
    mail_reception_confirmed = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    picking_count = models.IntegerField()
    picking_type = models.ForeignKey('StockPickingType',    models.DO_NOTHING, related_name="+")
    group = models.ForeignKey(ProcurementGroup,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    effective_date = models.DateTimeField(blank=True, null=True)
    l10n_in_journal = models.ForeignKey(AccountJournal,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    l10n_in_gst_treatment = models.CharField(max_length=200, blank=True, null=True)
    requisition = models.ForeignKey('PurchaseRequisition',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_studio_many2one_field_7wnel = models.ForeignKey('ResCurrency',    models.DO_NOTHING, related_name="+", db_column='x_studio_many2one_field_7wnel', blank=True, null=True)
    x_studio_company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", db_column='x_studio_company', blank=True, null=True)
    x_studio_vendor = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+", db_column='x_studio_vendor', blank=True, null=True)
    x_studio_registration_no = models.CharField(max_length=200, blank=True, null=True)
    x_studio_tin_no = models.CharField(max_length=200, blank=True, null=True)
    x_studio_vat_no = models.CharField(max_length=200, blank=True, null=True)
    x_studio_ssnit_no = models.CharField(max_length=200, blank=True, null=True)
    x_studio_from = models.DateField(blank=True, null=True)
    x_studio_to = models.DateField(blank=True, null=True)
    x_studio_vendor_1 = models.CharField(max_length=200, blank=True, null=True)
    date_planned_mps = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'purchase_order'


class PurchaseOrderLine(models.Model):
    name = models.TextField()
    sequence = models.IntegerField()
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    product_uom_qty = models.FloatField(blank=True, null=True)
    date_planned = models.DateTimeField(blank=True, null=True)
    product_uom = models.ForeignKey('UomUom',    models.DO_NOTHING, related_name="+", db_column='product_uom', blank=True, null=True)
    product = models.ForeignKey(ProductProduct,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    price_unit = models.DecimalField(max_digits=65535, decimal_places=65535)
    price_subtotal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_tax = models.FloatField(blank=True, null=True)
    order = models.ForeignKey(PurchaseOrder,    models.DO_NOTHING, related_name="+")
    account_analytic = models.ForeignKey(AccountAnalyticAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    qty_invoiced = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    qty_received_method = models.CharField(max_length=200, blank=True, null=True)
    qty_received = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    qty_received_manual = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    qty_to_invoice = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    currency = models.ForeignKey('ResCurrency',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    display_type = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    orderpoint = models.ForeignKey('StockWarehouseOrderpoint',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    product_description_variants = models.CharField(max_length=200, blank=True, null=True)
    propagate_cancel = models.BooleanField(blank=True, null=True)
    sale_order = models.ForeignKey('SaleOrder',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    sale_line = models.ForeignKey('SaleOrderLine',    models.DO_NOTHING, related_name="+", blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'purchase_order_line'


class PurchaseOrderStockPickingRel(models.Model):
    purchase_order = models.OneToOneField(PurchaseOrder,    models.DO_NOTHING, related_name="+", primary_key=True)
    stock_picking = models.ForeignKey('StockPicking',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'purchase_order_stock_picking_rel'
        unique_together = (('purchase_order', 'stock_picking'),)


class PurchaseRequisition(models.Model):
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    name = models.CharField(max_length=200)
    origin = models.CharField(max_length=200, blank=True, null=True)
    vendor = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    type = models.ForeignKey('PurchaseRequisitionType',    models.DO_NOTHING, related_name="+")
    ordering_date = models.DateField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)
    schedule_date = models.DateField(blank=True, null=True)
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    state = models.CharField(max_length=200)
    currency = models.ForeignKey('ResCurrency',    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    warehouse = models.ForeignKey('StockWarehouse',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    picking_type = models.ForeignKey('StockPickingType',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'purchase_requisition'


class PurchaseRequisitionLine(models.Model):
    product = models.ForeignKey(ProductProduct,    models.DO_NOTHING, related_name="+")
    product_uom = models.ForeignKey('UomUom',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    product_description_variants = models.CharField(max_length=200, blank=True, null=True)
    price_unit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    requisition = models.ForeignKey(PurchaseRequisition,    models.DO_NOTHING, related_name="+")
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    account_analytic = models.ForeignKey(AccountAnalyticAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    schedule_date = models.DateField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    move_dest = models.ForeignKey('StockMove',    models.DO_NOTHING, related_name="+", blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'purchase_requisition_line'


class PurchaseRequisitionType(models.Model):
    name = models.CharField(max_length=200)
    sequence = models.IntegerField()
    exclusive = models.CharField(max_length=200)
    quantity_copy = models.CharField(max_length=200)
    line_copy = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'purchase_requisition_type'


class QualityAlert(models.Model):
    email_cc = models.CharField(max_length=200, blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    stage = models.ForeignKey('QualityAlertStage',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    reason = models.ForeignKey('QualityReason',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    date_assign = models.DateTimeField(blank=True, null=True)
    date_close = models.DateTimeField(blank=True, null=True)
    picking = models.ForeignKey('StockPicking',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    action_corrective = models.TextField(blank=True, null=True)
    action_preventive = models.TextField(blank=True, null=True)
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    team = models.ForeignKey('QualityAlertTeam',    models.DO_NOTHING, related_name="+")
    partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    checkk = models.ForeignKey('QualityCheckk',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    product_tmpl = models.ForeignKey(ProductTemplate,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    product = models.ForeignKey(ProductProduct,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    lot = models.ForeignKey('StockProductionLot',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    priority = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    workorder = models.ForeignKey(MrpWorkorder,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    workcenter = models.ForeignKey(MrpWorkcenter,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    production = models.ForeignKey(MrpProduction,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'quality_alert'


class QualityAlertQualityTagRel(models.Model):
    quality_alert = models.OneToOneField(QualityAlert,    models.DO_NOTHING, related_name="+", primary_key=True)
    quality_tag = models.ForeignKey('QualityTag',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'quality_alert_quality_tag_rel'
        unique_together = (('quality_alert', 'quality_tag'),)


class QualityAlertStage(models.Model):
    name = models.CharField(max_length=200)
    sequence = models.IntegerField()
    folded = models.BooleanField(blank=True, null=True)
    done = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'quality_alert_stage'


class QualityAlertStageQualityAlertTeamRel(models.Model):
    quality_alert_stage = models.OneToOneField(QualityAlertStage,    models.DO_NOTHING, related_name="+", primary_key=True)
    quality_alert_team = models.ForeignKey('QualityAlertTeam',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'quality_alert_stage_quality_alert_team_rel'
        unique_together = (('quality_alert_stage', 'quality_alert_team'),)


class QualityAlertTeam(models.Model):
    alias = models.ForeignKey(MailAlias,    models.DO_NOTHING, related_name="+")
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    name = models.CharField(max_length=200)
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    sequence = models.IntegerField()
    color = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'quality_alert_team'


class QualityCheckk(models.Model):
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    point = models.ForeignKey('QualityPoint',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    quality_state = models.CharField(max_length=200, blank=True, null=True)
    control_date = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey(ProductProduct,    models.DO_NOTHING, related_name="+")
    picking = models.ForeignKey('StockPicking',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    lot = models.ForeignKey('StockProductionLot',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    team = models.ForeignKey(QualityAlertTeam,    models.DO_NOTHING, related_name="+")
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    test_type = models.ForeignKey('QualityPointTestType',    models.DO_NOTHING, related_name="+")
    additional_note = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    workorder = models.ForeignKey(MrpWorkorder,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    workcenter = models.ForeignKey(MrpWorkcenter,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    production = models.ForeignKey(MrpProduction,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    next_check = models.ForeignKey('self',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    previous_check = models.ForeignKey('self',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    move = models.ForeignKey('StockMove',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    move_line = models.ForeignKey('StockMoveLine',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    component = models.ForeignKey(ProductProduct,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    qty_done = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    finished_product_sequence = models.FloatField(blank=True, null=True)
    measure = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    measure_success = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'quality_check'


class QualityPoint(models.Model):
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    name = models.CharField(max_length=200)
    sequence = models.IntegerField()
    title = models.CharField(max_length=200, blank=True, null=True)
    team = models.ForeignKey(QualityAlertTeam,    models.DO_NOTHING, related_name="+")
    company = models.ForeignKey('ResCompany',    models.DO_NOTHING, related_name="+")
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    test_type = models.ForeignKey('QualityPointTestType',    models.DO_NOTHING, related_name="+")
    note = models.TextField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    operation = models.ForeignKey(MrpRoutingWorkcenter,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    test_report_type = models.CharField(max_length=200)
    worksheet = models.CharField(max_length=200, blank=True, null=True)
    worksheet_page = models.IntegerField()
    component = models.ForeignKey(ProductProduct,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    failure_message = models.TextField(blank=True, null=True)
    measure_frequency_type = models.CharField(max_length=200)
    measure_frequency_value = models.FloatField(blank=True, null=True)
    measure_frequency_unit_value = models.IntegerField()
    measure_frequency_unit = models.CharField(max_length=200, blank=True, null=True)
    norm = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tolerance_min = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tolerance_max = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    norm_unit = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'quality_point'


class QualityPointStockPickingTypeRel(models.Model):
    quality_point = models.OneToOneField(QualityPoint,    models.DO_NOTHING, related_name="+", primary_key=True)
    stock_picking_type = models.ForeignKey('StockPickingType',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'quality_point_stock_picking_type_rel'
        unique_together = (('quality_point', 'stock_picking_type'),)


class QualityPointTestType(models.Model):
    name = models.CharField(max_length=200)
    technical_name = models.CharField(max_length=200)
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'quality_point_test_type'


class QualityReason(models.Model):
    name = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'quality_reason'


class QualityTag(models.Model):
    name = models.CharField(max_length=200)
    color = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'quality_tag'


class RatingRating(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    res_name = models.CharField(max_length=200, blank=True, null=True)
    res_model = models.ForeignKey(IrModel,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    res_model_0 = models.CharField(db_column='res_model', max_length=200, blank=True, null=True)  # Field renamed because of name conflict.
    res_id = models.IntegerField()
    parent_res_name = models.CharField(max_length=200, blank=True, null=True)
    parent_res_model = models.ForeignKey(IrModel,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    parent_res_model_0 = models.CharField(db_column='parent_res_model', max_length=200, blank=True, null=True)  # Field renamed because of name conflict.
    parent_res_id = models.IntegerField()
    rated_partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    rating_text = models.CharField(max_length=200, blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)
    message = models.ForeignKey(MailMessage,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    is_internal = models.BooleanField(blank=True, null=True)
    access_token = models.CharField(max_length=200, blank=True, null=True)
    consumed = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    publisher_comment = models.TextField(blank=True, null=True)
    publisher = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    publisher_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rating_rating'


class RelBadgeAuthUsers(models.Model):
    gamification_badge = models.OneToOneField(GamificationBadge,    models.DO_NOTHING, related_name="+", primary_key=True)
    res_users = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'rel_badge_auth_users'
        unique_together = (('gamification_badge', 'res_users'),)


class RelModulesLangexport(models.Model):
    wiz = models.OneToOneField(BaseLanguageExport,    models.DO_NOTHING, related_name="+", primary_key=True)
    module = models.ForeignKey(IrModuleModule,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'rel_modules_langexport'
        unique_together = (('wiz', 'module'),)


class RelServerActions(models.Model):
    server = models.OneToOneField(IrActServer,    models.DO_NOTHING, related_name="+", primary_key=True)
    action = models.ForeignKey(IrActServer,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'rel_server_actions'
        unique_together = (('server', 'action'),)


class RelSlideTag(models.Model):
    slide = models.OneToOneField('SlideSlide',    models.DO_NOTHING, related_name="+", primary_key=True)
    tag = models.ForeignKey('SlideTag',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'rel_slide_tag'
        unique_together = (('slide', 'tag'),)


class RelUploadGroups(models.Model):
    channel = models.OneToOneField('SlideChannel',    models.DO_NOTHING, related_name="+", primary_key=True)
    group = models.ForeignKey('ResGroups',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'rel_upload_groups'
        unique_together = (('channel', 'group'),)


class ReportLayout(models.Model):
    view = models.ForeignKey(IrUiView,    models.DO_NOTHING, related_name="+")
    image = models.CharField(max_length=200, blank=True, null=True)
    pdf = models.CharField(max_length=200, blank=True, null=True)
    sequence = models.IntegerField()
    name = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'report_layout'


class ReportPaperformat(models.Model):
    name = models.CharField(max_length=200)
    default = models.BooleanField(blank=True, null=True)
    format = models.CharField(max_length=200, blank=True, null=True)
    margin_top = models.FloatField(blank=True, null=True)
    margin_bottom = models.FloatField(blank=True, null=True)
    margin_left = models.FloatField(blank=True, null=True)
    margin_right = models.FloatField(blank=True, null=True)
    page_height = models.IntegerField()
    page_width = models.IntegerField()
    orientation = models.CharField(max_length=200, blank=True, null=True)
    header_line = models.BooleanField(blank=True, null=True)
    header_spacing = models.IntegerField()
    dpi = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'report_paperformat'


class ReportPaperformatParameter(models.Model):
    paperformat = models.ForeignKey(ReportPaperformat,    models.DO_NOTHING, related_name="+")
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'report_paperformat_parameter'


class RequestAppraisal(models.Model):
    subject = models.CharField(max_length=200, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    template = models.ForeignKey(MailTemplate,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    email_from = models.CharField(max_length=200)
    author = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+")
    employee = models.ForeignKey(HrEmployee,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    deadline = models.DateField()
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'request_appraisal'


class RequestAppraisalResPartnerRel(models.Model):
    request_appraisal = models.OneToOneField(RequestAppraisal,    models.DO_NOTHING, related_name="+", primary_key=True)
    res_partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'request_appraisal_res_partner_rel'
        unique_together = (('request_appraisal', 'res_partner'),)


class ResBank(models.Model):
    name = models.CharField(max_length=200)
    street = models.CharField(max_length=200, blank=True, null=True)
    street2 = models.CharField(max_length=200, blank=True, null=True)
    zip = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.ForeignKey('ResCountryState',    models.DO_NOTHING, related_name="+", db_column='state', blank=True, null=True)
    country = models.ForeignKey('ResCountry',    models.DO_NOTHING, related_name="+", db_column='country', blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    bic = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_studio_branch = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'res_bank'


class ResCompany(models.Model):
    name = models.CharField(unique=True, max_length=200)
    partner = models.ForeignKey('ResPartner',    models.DO_NOTHING, related_name="+")
    currency = models.ForeignKey('ResCurrency',    models.DO_NOTHING, related_name="+")
    sequence = models.IntegerField()
    create_date = models.DateTimeField(blank=True, null=True)
    parent = models.ForeignKey('self',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    report_header = models.TextField(blank=True, null=True)
    report_footer = models.TextField(blank=True, null=True)
    logo_web = models.BinaryField(blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    company_registry = models.CharField(max_length=200, blank=True, null=True)
    paperformat = models.ForeignKey(ReportPaperformat,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    external_report_layout = models.ForeignKey(IrUiView,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    base_onboarding_company_state = models.CharField(max_length=200, blank=True, null=True)
    font = models.CharField(max_length=200, blank=True, null=True)
    primary_color = models.CharField(max_length=200, blank=True, null=True)
    secondary_color = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    resource_calendar = models.ForeignKey('ResourceCalendar',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    hr_presence_control_email_amount = models.IntegerField()
    hr_presence_control_ip_list = models.CharField(max_length=200, blank=True, null=True)
    snailmail_color = models.BooleanField(blank=True, null=True)
    snailmail_cover = models.BooleanField(blank=True, null=True)
    snailmail_duplex = models.BooleanField(blank=True, null=True)
    nomenclature = models.ForeignKey(BarcodeNomenclature,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    internal_transit_location = models.ForeignKey('StockLocation',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    stock_move_email_validation = models.BooleanField(blank=True, null=True)
    stock_mail_confirmation_template = models.ForeignKey(MailTemplate,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    stock_move_sms_validation = models.BooleanField(blank=True, null=True)
    stock_sms_confirmation_template = models.ForeignKey('SmsTemplate',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    has_received_warning_stock_sms = models.BooleanField(blank=True, null=True)
    fiscalyear_last_day = models.IntegerField()
    fiscalyear_last_month = models.CharField(max_length=200)
    period_lock_date = models.DateField(blank=True, null=True)
    fiscalyear_lock_date = models.DateField(blank=True, null=True)
    tax_lock_date = models.DateField(blank=True, null=True)
    transfer_account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    expects_chart_of_accounts = models.BooleanField(blank=True, null=True)
    chart_template = models.ForeignKey(AccountChartTemplate,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    bank_account_code_prefix = models.CharField(max_length=200, blank=True, null=True)
    cash_account_code_prefix = models.CharField(max_length=200, blank=True, null=True)
    default_cash_difference_income_account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    default_cash_difference_expense_account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    account_journal_suspense_account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    transfer_account_code_prefix = models.CharField(max_length=200, blank=True, null=True)
    account_sale_tax = models.ForeignKey(AccountTax,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    account_purchase_tax = models.ForeignKey(AccountTax,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    tax_calculation_rounding_method = models.CharField(max_length=200, blank=True, null=True)
    currency_exchange_journal = models.ForeignKey(AccountJournal,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    income_currency_exchange_account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    expense_currency_exchange_account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    anglo_saxon_accounting = models.BooleanField(blank=True, null=True)
    property_stock_account_input_categ = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    property_stock_account_output_categ = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    property_stock_valuation_account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    tax_exigibility = models.BooleanField(blank=True, null=True)
    account_tax_fiscal_country = models.ForeignKey('ResCountry',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    incoterm = models.ForeignKey(AccountIncoterms,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    qr_code = models.BooleanField(blank=True, null=True)
    invoice_is_email = models.BooleanField(blank=True, null=True)
    invoice_is_print = models.BooleanField(blank=True, null=True)
    account_opening_move = models.ForeignKey(AccountMove,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    account_opening_date = models.DateField()
    account_setup_bank_data_state = models.CharField(max_length=200, blank=True, null=True)
    account_setup_fy_data_state = models.CharField(max_length=200, blank=True, null=True)
    account_setup_coa_state = models.CharField(max_length=200, blank=True, null=True)
    account_onboarding_invoice_layout_state = models.CharField(max_length=200, blank=True, null=True)
    account_onboarding_create_invoice_state = models.CharField(max_length=200, blank=True, null=True)
    account_onboarding_sale_tax_state = models.CharField(max_length=200, blank=True, null=True)
    account_invoice_onboarding_state = models.CharField(max_length=200, blank=True, null=True)
    account_dashboard_onboarding_state = models.CharField(max_length=200, blank=True, null=True)
    invoice_terms = models.TextField(blank=True, null=True)
    account_setup_bill_state = models.CharField(max_length=200, blank=True, null=True)
    account_default_pos_receivable_account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    expense_accrual_account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    revenue_accrual_account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    automatic_entry_default_journal = models.ForeignKey(AccountJournal,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    tax_cash_basis_journal = models.ForeignKey(AccountJournal,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    account_cash_basis_base_account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    extract_show_ocr_option_selection = models.CharField(max_length=200, blank=True, null=True)
    extract_single_line_per_tax = models.BooleanField(blank=True, null=True)
    currency_interval_unit = models.CharField(max_length=200, blank=True, null=True)
    currency_next_execution_date = models.DateField(blank=True, null=True)
    currency_provider = models.CharField(max_length=200, blank=True, null=True)
    payment_acquirer_onboarding_state = models.CharField(max_length=200, blank=True, null=True)
    payment_onboarding_payment_method = models.CharField(max_length=200, blank=True, null=True)
    po_lead = models.FloatField()
    po_lock = models.CharField(max_length=200, blank=True, null=True)
    po_double_validation = models.CharField(max_length=200, blank=True, null=True)
    po_double_validation_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    invoice_is_snailmail = models.BooleanField(blank=True, null=True)
    yodlee_access_token = models.CharField(max_length=200, blank=True, null=True)
    yodlee_user_login = models.CharField(max_length=200, blank=True, null=True)
    yodlee_user_password = models.CharField(max_length=200, blank=True, null=True)
    yodlee_user_access_token = models.CharField(max_length=200, blank=True, null=True)
    days_to_purchase = models.FloatField(blank=True, null=True)
    portal_confirmation_sign = models.BooleanField(blank=True, null=True)
    portal_confirmation_pay = models.BooleanField(blank=True, null=True)
    quotation_validity_days = models.IntegerField()
    sale_quotation_onboarding_state = models.CharField(max_length=200, blank=True, null=True)
    sale_onboarding_order_confirmation_state = models.CharField(max_length=200, blank=True, null=True)
    sale_onboarding_sample_quotation_state = models.CharField(max_length=200, blank=True, null=True)
    sale_onboarding_payment_method = models.CharField(max_length=200, blank=True, null=True)
    sale_order_template = models.ForeignKey('SaleOrderTemplate',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    security_lead = models.FloatField()
    invoicing_switch_threshold = models.DateField(blank=True, null=True)
    totals_below_sections = models.BooleanField(blank=True, null=True)
    account_tax_periodicity = models.CharField(max_length=200, blank=True, null=True)
    account_tax_periodicity_reminder_day = models.IntegerField()
    account_tax_original_periodicity_reminder_day = models.IntegerField()
    account_tax_periodicity_journal = models.ForeignKey(AccountJournal,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    account_tax_next_activity_type = models.ForeignKey(MailActivityType,    models.DO_NOTHING, related_name="+", db_column='account_tax_next_activity_type', blank=True, null=True)
    account_revaluation_journal = models.ForeignKey(AccountJournal,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    account_revaluation_expense_provision_account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    account_revaluation_income_provision_account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    gain_account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    loss_account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    appraisal_plan = models.BooleanField(blank=True, null=True)
    appraisal_employee_feedback_template = models.TextField(blank=True, null=True)
    appraisal_manager_feedback_template = models.TextField(blank=True, null=True)
    appraisal_confirm_employee_mail_template = models.ForeignKey(MailTemplate,    models.DO_NOTHING, related_name="+", db_column='appraisal_confirm_employee_mail_template', blank=True, null=True)
    appraisal_confirm_manager_mail_template = models.ForeignKey(MailTemplate,    models.DO_NOTHING, related_name="+", db_column='appraisal_confirm_manager_mail_template', blank=True, null=True)
    vat_check_vies = models.BooleanField(blank=True, null=True)
    account_check_printing_layout = models.CharField(max_length=200, blank=True, null=True)
    account_check_printing_date_label = models.BooleanField(blank=True, null=True)
    account_check_printing_multi_stub = models.BooleanField(blank=True, null=True)
    account_check_printing_margin_top = models.FloatField(blank=True, null=True)
    account_check_printing_margin_left = models.FloatField(blank=True, null=True)
    account_check_printing_margin_right = models.FloatField(blank=True, null=True)
    project_time_mode = models.ForeignKey('UomUom',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    timesheet_encode_uom = models.ForeignKey('UomUom',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    leave_timesheet_project = models.ForeignKey(ProjectProject,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    leave_timesheet_task = models.ForeignKey(ProjectTask,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    timesheet_mail_employee_allow = models.BooleanField(blank=True, null=True)
    timesheet_mail_employee_delay = models.IntegerField()
    timesheet_mail_employee_interval = models.CharField(max_length=200)
    timesheet_mail_employee_nextdate = models.DateTimeField(blank=True, null=True)
    timesheet_mail_manager_allow = models.BooleanField(blank=True, null=True)
    timesheet_mail_manager_delay = models.IntegerField()
    timesheet_mail_manager_interval = models.CharField(max_length=200)
    timesheet_mail_manager_nextdate = models.DateTimeField(blank=True, null=True)
    planning_generation_interval = models.IntegerField()
    planning_allow_self_unassign = models.BooleanField(blank=True, null=True)
    partner_gid = models.IntegerField()
    manufacturing_lead = models.FloatField()
    subcontracting_location = models.ForeignKey('StockLocation',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    manufacturing_period = models.CharField(max_length=200)
    manufacturing_period_to_display = models.IntegerField()
    mrp_mps_show_starting_inventory = models.BooleanField(blank=True, null=True)
    mrp_mps_show_demand_forecast = models.BooleanField(blank=True, null=True)
    mrp_mps_show_actual_demand = models.BooleanField(blank=True, null=True)
    mrp_mps_show_indirect_demand = models.BooleanField(blank=True, null=True)
    mrp_mps_show_to_replenish = models.BooleanField(blank=True, null=True)
    mrp_mps_show_actual_replenishment = models.BooleanField(blank=True, null=True)
    mrp_mps_show_safety_stock = models.BooleanField(blank=True, null=True)
    mrp_mps_show_available_to_promise = models.BooleanField(blank=True, null=True)
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    social_facebook = models.CharField(max_length=200, blank=True, null=True)
    social_github = models.CharField(max_length=200, blank=True, null=True)
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)
    social_youtube = models.CharField(max_length=200, blank=True, null=True)
    social_instagram = models.CharField(max_length=200, blank=True, null=True)
    website_sale_onboarding_payment_acquirer_state = models.CharField(max_length=200, blank=True, null=True)
    website_sale_dashboard_onboarding_state = models.CharField(max_length=200, blank=True, null=True)
    account_bank_reconciliation_start = models.DateField(blank=True, null=True)
    java_path = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'res_company'


class ResCompanyLdap(models.Model):
    sequence = models.IntegerField()
    company = models.ForeignKey(ResCompany,    models.DO_NOTHING, related_name="+", db_column='company')
    ldap_server = models.CharField(max_length=200)
    ldap_server_port = models.IntegerField()
    ldap_binddn = models.CharField(max_length=200, blank=True, null=True)
    ldap_password = models.CharField(max_length=200, blank=True, null=True)
    ldap_filter = models.CharField(max_length=200)
    ldap_base = models.CharField(max_length=200)
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", db_column='user', blank=True, null=True)
    create_user = models.BooleanField(blank=True, null=True)
    ldap_tls = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'res_company_ldap'


class ResCompanyUsersRel(models.Model):
    cid = models.OneToOneField(ResCompany,    models.DO_NOTHING, related_name="+", db_column='cid', primary_key=True)
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'res_company_users_rel'
        unique_together = (('cid', 'user'),)


class ResConfig(models.Model):
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'res_config'


class ResConfigInstaller(models.Model):
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'res_config_installer'


class ResConfigSettings(models.Model):
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey(ResCompany,    models.DO_NOTHING, related_name="+")
    user_default_rights = models.BooleanField(blank=True, null=True)
    external_email_server_default = models.BooleanField(blank=True, null=True)
    module_base_import = models.BooleanField(blank=True, null=True)
    module_google_calendar = models.BooleanField(blank=True, null=True)
    module_microsoft_calendar = models.BooleanField(blank=True, null=True)
    module_google_drive = models.BooleanField(blank=True, null=True)
    module_google_spreadsheet = models.BooleanField(blank=True, null=True)
    module_auth_oauth = models.BooleanField(blank=True, null=True)
    module_auth_ldap = models.BooleanField(blank=True, null=True)
    module_base_gengo = models.BooleanField(blank=True, null=True)
    module_account_inter_company_rules = models.BooleanField(blank=True, null=True)
    module_pad = models.BooleanField(blank=True, null=True)
    module_voip = models.BooleanField(blank=True, null=True)
    module_web_unsplash = models.BooleanField(blank=True, null=True)
    module_partner_autocomplete = models.BooleanField(blank=True, null=True)
    module_base_geolocalize = models.BooleanField(blank=True, null=True)
    module_google_recaptcha = models.BooleanField(blank=True, null=True)
    group_multi_currency = models.BooleanField(blank=True, null=True)
    show_effect = models.BooleanField(blank=True, null=True)
    fail_counter = models.IntegerField()
    alias_domain = models.CharField(max_length=200, blank=True, null=True)
    unsplash_access_key = models.CharField(max_length=200, blank=True, null=True)
    auth_signup_reset_password = models.BooleanField(blank=True, null=True)
    auth_signup_uninvited = models.CharField(max_length=200, blank=True, null=True)
    auth_signup_template_user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    module_hr_presence = models.BooleanField(blank=True, null=True)
    module_hr_skills = models.BooleanField(blank=True, null=True)
    hr_presence_control_login = models.BooleanField(blank=True, null=True)
    hr_presence_control_email = models.BooleanField(blank=True, null=True)
    hr_presence_control_ip = models.BooleanField(blank=True, null=True)
    module_hr_attendance = models.BooleanField(blank=True, null=True)
    hr_employee_self_edit = models.BooleanField(blank=True, null=True)
    disable_redirect_firebase_dynamic_link = models.BooleanField(blank=True, null=True)
    enable_ocn = models.BooleanField(blank=True, null=True)
    map_box_token = models.CharField(max_length=200, blank=True, null=True)
    group_discount_per_so_line = models.BooleanField(blank=True, null=True)
    group_uom = models.BooleanField(blank=True, null=True)
    group_product_variant = models.BooleanField(blank=True, null=True)
    module_sale_product_configurator = models.BooleanField(blank=True, null=True)
    module_sale_product_matrix = models.BooleanField(blank=True, null=True)
    group_stock_packaging = models.BooleanField(blank=True, null=True)
    group_product_pricelist = models.BooleanField(blank=True, null=True)
    group_sale_pricelist = models.BooleanField(blank=True, null=True)
    product_pricelist_setting = models.CharField(max_length=200, blank=True, null=True)
    product_weight_in_lbs = models.CharField(max_length=200, blank=True, null=True)
    product_volume_volume_in_cubic_feet = models.CharField(max_length=200, blank=True, null=True)
    digest_emails = models.BooleanField(blank=True, null=True)
    digest = models.ForeignKey(DigestDigest,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    module_procurement_jit = models.CharField(max_length=200, blank=True, null=True)
    module_product_expiry = models.BooleanField(blank=True, null=True)
    group_stock_production_lot = models.BooleanField(blank=True, null=True)
    group_lot_on_delivery_slip = models.BooleanField(blank=True, null=True)
    group_stock_tracking_lot = models.BooleanField(blank=True, null=True)
    group_stock_tracking_owner = models.BooleanField(blank=True, null=True)
    group_stock_adv_location = models.BooleanField(blank=True, null=True)
    group_warning_stock = models.BooleanField(blank=True, null=True)
    group_stock_sign_delivery = models.BooleanField(blank=True, null=True)
    module_stock_picking_batch = models.BooleanField(blank=True, null=True)
    module_stock_barcode = models.BooleanField(blank=True, null=True)
    module_stock_sms = models.BooleanField(blank=True, null=True)
    module_delivery = models.BooleanField(blank=True, null=True)
    module_delivery_dhl = models.BooleanField(blank=True, null=True)
    module_delivery_fedex = models.BooleanField(blank=True, null=True)
    module_delivery_ups = models.BooleanField(blank=True, null=True)
    module_delivery_usps = models.BooleanField(blank=True, null=True)
    module_delivery_bpost = models.BooleanField(blank=True, null=True)
    module_delivery_easypost = models.BooleanField(blank=True, null=True)
    group_stock_multi_locations = models.BooleanField(blank=True, null=True)
    chart_template = models.ForeignKey(AccountChartTemplate,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    module_account_accountant = models.BooleanField(blank=True, null=True)
    group_analytic_accounting = models.BooleanField(blank=True, null=True)
    group_analytic_tags = models.BooleanField(blank=True, null=True)
    group_warning_account = models.BooleanField(blank=True, null=True)
    group_cash_rounding = models.BooleanField(blank=True, null=True)
    group_show_line_subtotals_tax_excluded = models.BooleanField(blank=True, null=True)
    group_show_line_subtotals_tax_included = models.BooleanField(blank=True, null=True)
    group_show_sale_receipts = models.BooleanField(blank=True, null=True)
    group_show_purchase_receipts = models.BooleanField(blank=True, null=True)
    show_line_subtotals_tax_selection = models.CharField(max_length=200)
    module_account_budget = models.BooleanField(blank=True, null=True)
    module_account_payment = models.BooleanField(blank=True, null=True)
    module_account_reports = models.BooleanField(blank=True, null=True)
    module_account_check_printing = models.BooleanField(blank=True, null=True)
    module_account_batch_payment = models.BooleanField(blank=True, null=True)
    module_account_sepa = models.BooleanField(blank=True, null=True)
    module_account_sepa_direct_debit = models.BooleanField(blank=True, null=True)
    module_account_plaid = models.BooleanField(blank=True, null=True)
    module_account_yodlee = models.BooleanField(blank=True, null=True)
    module_account_bank_statement_import_qif = models.BooleanField(blank=True, null=True)
    module_account_bank_statement_import_ofx = models.BooleanField(blank=True, null=True)
    module_account_bank_statement_import_csv = models.BooleanField(blank=True, null=True)
    module_account_bank_statement_import_camt = models.BooleanField(blank=True, null=True)
    module_currency_rate_live = models.BooleanField(blank=True, null=True)
    module_account_intrastat = models.BooleanField(blank=True, null=True)
    module_product_margin = models.BooleanField(blank=True, null=True)
    module_l10n_eu_service = models.BooleanField(blank=True, null=True)
    module_account_taxcloud = models.BooleanField(blank=True, null=True)
    module_account_invoice_extract = models.BooleanField(blank=True, null=True)
    module_snailmail_account = models.BooleanField(blank=True, null=True)
    use_invoice_terms = models.BooleanField(blank=True, null=True)
    lock_confirmed_po = models.BooleanField(blank=True, null=True)
    po_order_approval = models.BooleanField(blank=True, null=True)
    default_purchase_method = models.CharField(max_length=200, blank=True, null=True)
    group_warning_purchase = models.BooleanField(blank=True, null=True)
    module_account_3way_match = models.BooleanField(blank=True, null=True)
    module_purchase_requisition = models.BooleanField(blank=True, null=True)
    module_purchase_product_matrix = models.BooleanField(blank=True, null=True)
    use_po_lead = models.BooleanField(blank=True, null=True)
    group_send_reminder = models.BooleanField(blank=True, null=True)
    module_stock_landed_costs = models.BooleanField(blank=True, null=True)
    module_stock_dropshipping = models.BooleanField(blank=True, null=True)
    is_installed_sale = models.BooleanField(blank=True, null=True)
    group_auto_done_setting = models.BooleanField(blank=True, null=True)
    module_sale_margin = models.BooleanField(blank=True, null=True)
    use_quotation_validity_days = models.BooleanField(blank=True, null=True)
    group_warning_sale = models.BooleanField(blank=True, null=True)
    group_sale_delivery_address = models.BooleanField(blank=True, null=True)
    group_proforma_sales = models.BooleanField(blank=True, null=True)
    default_invoice_policy = models.CharField(max_length=200, blank=True, null=True)
    deposit_default_product = models.ForeignKey(ProductProduct,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    module_product_email_template = models.BooleanField(blank=True, null=True)
    module_sale_coupon = models.BooleanField(blank=True, null=True)
    module_sale_amazon = models.BooleanField(blank=True, null=True)
    automatic_invoice = models.BooleanField(blank=True, null=True)
    template = models.ForeignKey(MailTemplate,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    confirmation_template = models.ForeignKey(MailTemplate,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    group_sale_order_template = models.BooleanField(blank=True, null=True)
    module_sale_quotation_builder = models.BooleanField(blank=True, null=True)
    group_display_incoterm = models.BooleanField(blank=True, null=True)
    group_lot_on_invoice = models.BooleanField(blank=True, null=True)
    use_security_lead = models.BooleanField(blank=True, null=True)
    default_picking_policy = models.CharField(max_length=200)
    module_account_predictive_bills = models.BooleanField(blank=True, null=True)
    group_fiscal_year = models.BooleanField(blank=True, null=True)
    module_l10n_fr_hr_payroll = models.BooleanField(blank=True, null=True)
    module_l10n_be_hr_payroll = models.BooleanField(blank=True, null=True)
    module_l10n_in_hr_payroll = models.BooleanField(blank=True, null=True)
    module_hr_payroll_account = models.BooleanField(blank=True, null=True)
    module_hr_payroll_account_sepa = models.BooleanField(blank=True, null=True)
    module_website_hr_recruitment = models.BooleanField(blank=True, null=True)
    module_hr_recruitment_survey = models.BooleanField(blank=True, null=True)
    module_hr_appraisal_survey = models.BooleanField(blank=True, null=True)
    group_l10n_in_reseller = models.BooleanField(blank=True, null=True)
    module_project_forecast = models.BooleanField(blank=True, null=True)
    module_hr_timesheet = models.BooleanField(blank=True, null=True)
    group_subtask_project = models.BooleanField(blank=True, null=True)
    group_project_rating = models.BooleanField(blank=True, null=True)
    group_project_recurring_tasks = models.BooleanField(blank=True, null=True)
    module_project_timesheet_synchro = models.BooleanField(blank=True, null=True)
    module_project_timesheet_holidays = models.BooleanField(blank=True, null=True)
    timesheet_min_duration = models.IntegerField()
    timesheet_rounding = models.IntegerField()
    invoiced_timesheet = models.CharField(max_length=200, blank=True, null=True)
    alias_prefix = models.CharField(max_length=200, blank=True, null=True)
    group_expiry_date_on_delivery_slip = models.BooleanField(blank=True, null=True)
    group_project_forecast_display_allocate_time = models.BooleanField(blank=True, null=True)
    use_manufacturing_lead = models.BooleanField(blank=True, null=True)
    group_mrp_byproducts = models.BooleanField(blank=True, null=True)
    module_mrp_mps = models.BooleanField(blank=True, null=True)
    module_mrp_plm = models.BooleanField(blank=True, null=True)
    module_mrp_workorder = models.BooleanField(blank=True, null=True)
    module_quality_control = models.BooleanField(blank=True, null=True)
    module_mrp_subcontracting = models.BooleanField(blank=True, null=True)
    group_mrp_routings = models.BooleanField(blank=True, null=True)
    group_locked_by_default = models.BooleanField(blank=True, null=True)
    group_mrp_wo_tablet_timer = models.BooleanField(blank=True, null=True)
    crm_alias_prefix = models.CharField(max_length=200, blank=True, null=True)
    generate_lead_from_alias = models.BooleanField(blank=True, null=True)
    group_use_lead = models.BooleanField(blank=True, null=True)
    group_use_recurring_revenues = models.BooleanField(blank=True, null=True)
    module_crm_iap_lead = models.BooleanField(blank=True, null=True)
    module_crm_iap_lead_website = models.BooleanField(blank=True, null=True)
    module_crm_iap_lead_enrich = models.BooleanField(blank=True, null=True)
    module_mail_client_extension = models.BooleanField(blank=True, null=True)
    lead_enrich_auto = models.CharField(max_length=200, blank=True, null=True)
    lead_mining_in_pipeline = models.BooleanField(blank=True, null=True)
    predictive_lead_scoring_start_date_str = models.CharField(max_length=200, blank=True, null=True)
    predictive_lead_scoring_fields_str = models.CharField(max_length=200, blank=True, null=True)
    website = models.ForeignKey('Website',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    group_multi_website = models.BooleanField(blank=True, null=True)
    recaptcha_public_key = models.CharField(max_length=200, blank=True, null=True)
    recaptcha_private_key = models.CharField(max_length=200, blank=True, null=True)
    recaptcha_min_score = models.FloatField(blank=True, null=True)
    module_website_sale_delivery = models.BooleanField(blank=True, null=True)
    sale_delivery_settings = models.CharField(max_length=200, blank=True, null=True)
    group_delivery_invoice_address = models.BooleanField(blank=True, null=True)
    module_website_sale_digital = models.BooleanField(blank=True, null=True)
    module_website_sale_wishlist = models.BooleanField(blank=True, null=True)
    module_website_sale_comparison = models.BooleanField(blank=True, null=True)
    module_website_sale_stock = models.BooleanField(blank=True, null=True)
    module_account = models.BooleanField(blank=True, null=True)
    inventory_availability = models.CharField(max_length=200, blank=True, null=True)
    available_threshold = models.FloatField(blank=True, null=True)
    customer_credit_limit = models.BooleanField(blank=True, null=True)
    module_website_sale_slides = models.BooleanField(blank=True, null=True)
    module_website_slides_forum = models.BooleanField(blank=True, null=True)
    module_website_slides_survey = models.BooleanField(blank=True, null=True)
    module_mass_mailing_slides = models.BooleanField(blank=True, null=True)
    web_window_title = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'res_config_settings'


class ResCountry(models.Model):
    name = models.CharField(unique=True, max_length=200)
    code = models.CharField(unique=True, max_length=2, blank=True, null=True)
    address_format = models.TextField(blank=True, null=True)
    address_view = models.ForeignKey(IrUiView,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    currency = models.ForeignKey('ResCurrency',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    phone_code = models.IntegerField()
    name_position = models.CharField(max_length=200, blank=True, null=True)
    vat_label = models.CharField(max_length=200, blank=True, null=True)
    state_required = models.BooleanField(blank=True, null=True)
    zip_required = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'res_country'


class ResCountryGroup(models.Model):
    name = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'res_country_group'


class ResCountryGroupPricelistRel(models.Model):
    pricelist = models.OneToOneField(ProductPricelist,    models.DO_NOTHING, related_name="+", primary_key=True)
    res_country_group = models.ForeignKey(ResCountryGroup,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'res_country_group_pricelist_rel'
        unique_together = (('pricelist', 'res_country_group'),)


class ResCountryResCountryGroupRel(models.Model):
    res_country = models.OneToOneField(ResCountry,    models.DO_NOTHING, related_name="+", primary_key=True)
    res_country_group = models.ForeignKey(ResCountryGroup,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'res_country_res_country_group_rel'
        unique_together = (('res_country', 'res_country_group'),)


class ResCountryState(models.Model):
    country = models.ForeignKey(ResCountry,    models.DO_NOTHING, related_name="+")
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    l10n_in_tin = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'res_country_state'
        unique_together = (('country', 'code'),)


class ResCurrency(models.Model):
    name = models.CharField(unique=True, max_length=200)
    symbol = models.CharField(max_length=200)
    rounding = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    decimal_places = models.IntegerField()
    active = models.BooleanField(blank=True, null=True)
    position = models.CharField(max_length=200, blank=True, null=True)
    currency_unit_label = models.CharField(max_length=200, blank=True, null=True)
    currency_subunit_label = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'res_currency'


class ResCurrencyRate(models.Model):
    name = models.DateField()
    rate = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    currency = models.ForeignKey(ResCurrency,    models.DO_NOTHING, related_name="+")
    company = models.ForeignKey(ResCompany,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'res_currency_rate'
        unique_together = (('name', 'currency', 'company'),)


class ResGroups(models.Model):
    name = models.CharField(max_length=200)
    comment = models.TextField(blank=True, null=True)
    category = models.ForeignKey(IrModuleCategory,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    color = models.IntegerField()
    share = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'res_groups'
        unique_together = (('category', 'name'),)


class ResGroupsImpliedRel(models.Model):
    gid = models.OneToOneField(ResGroups,    models.DO_NOTHING, related_name="+", db_column='gid', primary_key=True)
    hid = models.ForeignKey(ResGroups,    models.DO_NOTHING, related_name="+", db_column='hid')

    class Meta:
        managed = True
        db_table = 'res_groups_implied_rel'
        unique_together = (('gid', 'hid'),)


class ResGroupsReportRel(models.Model):
    uid = models.OneToOneField(IrActReportXml,    models.DO_NOTHING, related_name="+", db_column='uid', primary_key=True)
    gid = models.ForeignKey(ResGroups,    models.DO_NOTHING, related_name="+", db_column='gid')

    class Meta:
        managed = True
        db_table = 'res_groups_report_rel'
        unique_together = (('uid', 'gid'),)


class ResGroupsSlideChannelRel(models.Model):
    slide_channel = models.OneToOneField('SlideChannel',    models.DO_NOTHING, related_name="+", primary_key=True)
    res_groups = models.ForeignKey(ResGroups,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'res_groups_slide_channel_rel'
        unique_together = (('slide_channel', 'res_groups'),)


class ResGroupsUsersRel(models.Model):
    gid = models.OneToOneField(ResGroups,    models.DO_NOTHING, related_name="+", db_column='gid', primary_key=True)
    uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", db_column='uid')

    class Meta:
        managed = True
        db_table = 'res_groups_users_rel'
        unique_together = (('gid', 'uid'),)


class ResGroupsWebsiteMenuRel(models.Model):
    website_menu = models.OneToOneField('WebsiteMenu',    models.DO_NOTHING, related_name="+", primary_key=True)
    res_groups = models.ForeignKey(ResGroups,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'res_groups_website_menu_rel'
        unique_together = (('website_menu', 'res_groups'),)


class ResLang(models.Model):
    name = models.CharField(unique=True, max_length=200)
    code = models.CharField(unique=True, max_length=200)
    iso_code = models.CharField(max_length=200, blank=True, null=True)
    url_code = models.CharField(unique=True, max_length=200)
    active = models.BooleanField(blank=True, null=True)
    direction = models.CharField(max_length=200)
    date_format = models.CharField(max_length=200)
    time_format = models.CharField(max_length=200)
    week_start = models.CharField(max_length=200)
    grouping = models.CharField(max_length=200)
    decimal_point = models.CharField(max_length=200)
    thousands_sep = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'res_lang'


class ResPartner(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    company = models.ForeignKey(ResCompany,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    display_name = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    title = models.ForeignKey('ResPartnerTitle',    models.DO_NOTHING, related_name="+", db_column='title', blank=True, null=True)
    parent = models.ForeignKey('self',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    ref = models.CharField(max_length=200, blank=True, null=True)
    lang = models.CharField(max_length=200, blank=True, null=True)
    tz = models.CharField(max_length=200, blank=True, null=True)
    user = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    vat = models.CharField(max_length=200, blank=True, null=True)
    website = models.CharField(max_length=200, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    credit_limit = models.FloatField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    employee = models.BooleanField(blank=True, null=True)
    function = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=200, blank=True, null=True)
    street = models.CharField(max_length=200, blank=True, null=True)
    street2 = models.CharField(max_length=200, blank=True, null=True)
    zip = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.ForeignKey(ResCountryState,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    country = models.ForeignKey(ResCountry,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    partner_latitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    partner_longitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    mobile = models.CharField(max_length=200, blank=True, null=True)
    is_company = models.BooleanField(blank=True, null=True)
    industry = models.ForeignKey('ResPartnerIndustry',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    color = models.IntegerField()
    partner_share = models.BooleanField(blank=True, null=True)
    commercial_partner = models.ForeignKey('self',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    commercial_company_name = models.CharField(max_length=200, blank=True, null=True)
    company_name = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    email_normalized = models.CharField(max_length=200, blank=True, null=True)
    message_bounce = models.IntegerField()
    signup_token = models.CharField(max_length=200, blank=True, null=True)
    signup_type = models.CharField(max_length=200, blank=True, null=True)
    signup_expiration = models.DateTimeField(blank=True, null=True)
    phone_sanitized = models.CharField(max_length=200, blank=True, null=True)
    ocn_token = models.CharField(max_length=200, blank=True, null=True)
    contact_address_complete = models.CharField(max_length=200, blank=True, null=True)
    picking_warn = models.CharField(max_length=200, blank=True, null=True)
    picking_warn_msg = models.TextField(blank=True, null=True)
    debit_limit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    last_time_entries_checked = models.DateTimeField(blank=True, null=True)
    invoice_warn = models.CharField(max_length=200, blank=True, null=True)
    invoice_warn_msg = models.TextField(blank=True, null=True)
    supplier_rank = models.IntegerField()
    customer_rank = models.IntegerField()
    online_partner_vendor_name = models.CharField(max_length=200, blank=True, null=True)
    online_partner_bank_account = models.CharField(max_length=200, blank=True, null=True)
    purchase_warn = models.CharField(max_length=200, blank=True, null=True)
    purchase_warn_msg = models.TextField(blank=True, null=True)
    online_partner_information = models.CharField(max_length=200, blank=True, null=True)
    team = models.ForeignKey(CrmTeam,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    sale_warn = models.CharField(max_length=200, blank=True, null=True)
    sale_warn_msg = models.TextField(blank=True, null=True)
    calendar_last_notif_ack = models.DateTimeField(blank=True, null=True)
    l10n_in_gst_treatment = models.CharField(max_length=200, blank=True, null=True)
    l10n_in_shipping_gstin = models.CharField(max_length=200, blank=True, null=True)
    x_studio_registration_no = models.CharField(max_length=200, blank=True, null=True)
    x_studio_tin_no = models.CharField(max_length=200, blank=True, null=True)
    x_studio_vat_no = models.CharField(max_length=200, blank=True, null=True)
    x_studio_ssnit_no = models.CharField(max_length=200, blank=True, null=True)
    x_studio_from = models.DateField(blank=True, null=True)
    x_studio_to = models.DateField(blank=True, null=True)
    partner_gid = models.IntegerField()
    additional_info = models.CharField(max_length=200, blank=True, null=True)
    website_0 = models.ForeignKey('Website',    models.DO_NOTHING, related_name="+", db_column='website_id', blank=True, null=True)  # Field renamed because of name conflict.
    is_published = models.BooleanField(blank=True, null=True)
    website_meta_title = models.CharField(max_length=200, blank=True, null=True)
    website_meta_description = models.TextField(blank=True, null=True)
    website_meta_keywords = models.CharField(max_length=200, blank=True, null=True)
    website_meta_og_img = models.CharField(max_length=200, blank=True, null=True)
    seo_name = models.CharField(max_length=200, blank=True, null=True)
    website_description = models.TextField(blank=True, null=True)
    website_short_description = models.TextField(blank=True, null=True)
    amazon_email = models.CharField(max_length=200, blank=True, null=True)
    warning_stage = models.FloatField(blank=True, null=True)
    blocking_stage = models.FloatField(blank=True, null=True)
    active_limit = models.BooleanField(blank=True, null=True)
    x_studio_supplier_number = models.CharField(max_length=200, blank=True, null=True)
    x_studio_vendor_number = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'res_partner'


class ResPartnerAutocompleteSync(models.Model):
    partner = models.ForeignKey(ResPartner,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    synched = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'res_partner_autocomplete_sync'


class ResPartnerBank(models.Model):
    active = models.BooleanField(blank=True, null=True)
    acc_number = models.CharField(max_length=200)
    sanitized_acc_number = models.CharField(max_length=200, blank=True, null=True)
    acc_holder_name = models.CharField(max_length=200, blank=True, null=True)
    partner = models.ForeignKey(ResPartner,    models.DO_NOTHING, related_name="+")
    bank = models.ForeignKey(ResBank,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    sequence = models.IntegerField()
    currency = models.ForeignKey(ResCurrency,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    company = models.ForeignKey(ResCompany,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_studio_many2one_field_ihkod = models.ForeignKey('XBankBranch',    models.DO_NOTHING, related_name="+", db_column='x_studio_many2one_field_IHkod', blank=True, null=True)  # Field name made lowercase.
    x_studio_bank = models.ForeignKey('XMainBank',    models.DO_NOTHING, related_name="+", db_column='x_studio_bank', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'res_partner_bank'
        unique_together = (('sanitized_acc_number', 'company'),)


class ResPartnerCategory(models.Model):
    name = models.CharField(max_length=200)
    color = models.IntegerField()
    parent = models.ForeignKey('self',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    parent_path = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'res_partner_category'


class ResPartnerIndustry(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    full_name = models.CharField(max_length=200, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'res_partner_industry'


class ResPartnerResPartnerCategoryRel(models.Model):
    category = models.OneToOneField(ResPartnerCategory,    models.DO_NOTHING, related_name="+", primary_key=True)
    partner = models.ForeignKey(ResPartner,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'res_partner_res_partner_category_rel'
        unique_together = (('category', 'partner'),)


class ResPartnerSlideChannelInviteRel(models.Model):
    slide_channel_invite = models.OneToOneField('SlideChannelInvite',    models.DO_NOTHING, related_name="+", primary_key=True)
    res_partner = models.ForeignKey(ResPartner,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'res_partner_slide_channel_invite_rel'
        unique_together = (('slide_channel_invite', 'res_partner'),)


class ResPartnerTitle(models.Model):
    name = models.CharField(max_length=200)
    shortcut = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'res_partner_title'


class ResUsers(models.Model):
    active = models.BooleanField(blank=True, null=True)
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=200, blank=True, null=True)
    company = models.ForeignKey(ResCompany,    models.DO_NOTHING, related_name="+")
    partner = models.ForeignKey(ResPartner,    models.DO_NOTHING, related_name="+")
    create_date = models.DateTimeField(blank=True, null=True)
    signature = models.TextField(blank=True, null=True)
    action_id = models.IntegerField()
    share = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('self',    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    write_uid = models.ForeignKey('self',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    totp_secret = models.CharField(max_length=200, blank=True, null=True)
    notification_type = models.CharField(max_length=200)
    odoobot_state = models.CharField(max_length=200, blank=True, null=True)
    odoobot_failed = models.BooleanField(blank=True, null=True)
    sale_team = models.ForeignKey(CrmTeam,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    microsoft_calendar_rtoken = models.CharField(max_length=200, blank=True, null=True)
    microsoft_calendar_token = models.CharField(max_length=200, blank=True, null=True)
    microsoft_calendar_token_validity = models.DateTimeField(blank=True, null=True)
    target_sales_won = models.IntegerField()
    target_sales_done = models.IntegerField()
    target_sales_invoiced = models.IntegerField()
    website = models.ForeignKey('Website',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    karma = models.IntegerField()
    rank = models.ForeignKey(GamificationKarmaRank,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    next_rank = models.ForeignKey(GamificationKarmaRank,    models.DO_NOTHING, related_name="+", blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'res_users'
        unique_together = (('login', 'website'),)


class ResUsersApikeys(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+")
    scope = models.CharField(max_length=200, blank=True, null=True)
    index = models.CharField(max_length=8, blank=True, null=True)
    key = models.CharField(max_length=200, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'res_users_apikeys'


class ResUsersApikeysDescription(models.Model):
    name = models.CharField(max_length=200)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'res_users_apikeys_description'


class ResUsersIdentitycheck(models.Model):
    request = models.CharField(max_length=200, blank=True, null=True)
    password = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'res_users_identitycheck'


class ResUsersLog(models.Model):
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'res_users_log'


class ResetViewArchWizard(models.Model):
    view = models.ForeignKey(IrUiView,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    reset_mode = models.CharField(max_length=200)
    compare_view = models.ForeignKey(IrUiView,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'reset_view_arch_wizard'


class ResourceCalendar(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey(ResCompany,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    hours_per_day = models.FloatField(blank=True, null=True)
    tz = models.CharField(max_length=200)
    two_weeks_calendar = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    hours_per_week = models.FloatField(blank=True, null=True)
    full_time_required_hours = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'resource_calendar'


class ResourceCalendarAttendance(models.Model):
    name = models.CharField(max_length=200)
    dayofweek = models.CharField(max_length=200)
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    hour_from = models.FloatField()
    hour_to = models.FloatField()
    calendar = models.ForeignKey(ResourceCalendar,    models.DO_NOTHING, related_name="+")
    day_period = models.CharField(max_length=200)
    resource = models.ForeignKey('ResourceResource',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    week_type = models.CharField(max_length=200, blank=True, null=True)
    display_type = models.CharField(max_length=200, blank=True, null=True)
    sequence = models.IntegerField()
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    work_entry_type = models.ForeignKey(HrWorkEntryType,    models.DO_NOTHING, related_name="+", blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'resource_calendar_attendance'


class ResourceCalendarLeaves(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    company = models.ForeignKey(ResCompany,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    calendar = models.ForeignKey(ResourceCalendar,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    resource = models.ForeignKey('ResourceResource',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    time_type = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    work_entry_type = models.ForeignKey(HrWorkEntryType,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    holiday = models.ForeignKey(HrLeave,    models.DO_NOTHING, related_name="+", blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'resource_calendar_leaves'


class ResourceResource(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey(ResCompany,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    resource_type = models.CharField(max_length=200)
    user = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    time_efficiency = models.FloatField()
    calendar = models.ForeignKey(ResourceCalendar,    models.DO_NOTHING, related_name="+")
    tz = models.CharField(max_length=200)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'resource_resource'


class ResourceTest(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    resource = models.ForeignKey(ResourceResource,    models.DO_NOTHING, related_name="+")
    company = models.ForeignKey(ResCompany,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    resource_calendar = models.ForeignKey(ResourceCalendar,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'resource_test'


class RuleGroupRel(models.Model):
    rule_group = models.OneToOneField(IrRule,    models.DO_NOTHING, related_name="+", primary_key=True)
    group = models.ForeignKey(ResGroups,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'rule_group_rel'
        unique_together = (('rule_group', 'group'),)


class SalaryHistory(models.Model):
    employee_id = models.CharField(max_length=200, blank=True, null=True)
    employee_name = models.CharField(max_length=200, blank=True, null=True)
    updated_date = models.DateField(blank=True, null=True)
    current_value = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'salary_history'


class SaleAdvancePaymentInv(models.Model):
    advance_payment_method = models.CharField(max_length=200)
    deduct_down_payments = models.BooleanField(blank=True, null=True)
    has_down_payments = models.BooleanField(blank=True, null=True)
    product = models.ForeignKey(ProductProduct,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    count = models.IntegerField()
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    currency = models.ForeignKey(ResCurrency,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    fixed_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    deposit_account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date_start_invoice_timesheet = models.DateField(blank=True, null=True)
    date_end_invoice_timesheet = models.DateField(blank=True, null=True)
    invoicing_timesheet_enabled = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sale_advance_payment_inv'


class SaleOrder(models.Model):
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    access_token = models.CharField(max_length=200, blank=True, null=True)
    campaign = models.ForeignKey('UtmCampaign',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    source = models.ForeignKey('UtmSource',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    medium = models.ForeignKey('UtmMedium',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    name = models.CharField(max_length=200)
    origin = models.CharField(max_length=200, blank=True, null=True)
    client_order_ref = models.CharField(max_length=200, blank=True, null=True)
    reference = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    date_order = models.DateTimeField()
    validity_date = models.DateField(blank=True, null=True)
    require_signature = models.BooleanField(blank=True, null=True)
    require_payment = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    partner = models.ForeignKey(ResPartner,    models.DO_NOTHING, related_name="+")
    partner_invoice = models.ForeignKey(ResPartner,    models.DO_NOTHING, related_name="+")
    partner_shipping = models.ForeignKey(ResPartner,    models.DO_NOTHING, related_name="+")
    pricelist = models.ForeignKey(ProductPricelist,    models.DO_NOTHING, related_name="+")
    currency = models.ForeignKey(ResCurrency,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    analytic_account = models.ForeignKey(AccountAnalyticAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    invoice_status = models.CharField(max_length=200, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    amount_untaxed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_tax = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    currency_rate = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    payment_term = models.ForeignKey(AccountPaymentTerm,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    fiscal_position = models.ForeignKey(AccountFiscalPosition,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    company = models.ForeignKey(ResCompany,    models.DO_NOTHING, related_name="+")
    team = models.ForeignKey(CrmTeam,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    signed_by = models.CharField(max_length=200, blank=True, null=True)
    signed_on = models.DateTimeField(blank=True, null=True)
    commitment_date = models.DateTimeField(blank=True, null=True)
    show_update_pricelist = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    sale_order_template = models.ForeignKey('SaleOrderTemplate',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    incoterm = models.ForeignKey(AccountIncoterms,    models.DO_NOTHING, related_name="+", db_column='incoterm', blank=True, null=True)
    picking_policy = models.CharField(max_length=200)
    warehouse = models.ForeignKey('StockWarehouse',    models.DO_NOTHING, related_name="+")
    procurement_group = models.ForeignKey(ProcurementGroup,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    effective_date = models.DateField(blank=True, null=True)
    l10n_in_reseller_partner = models.ForeignKey(ResPartner,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    l10n_in_journal = models.ForeignKey(AccountJournal,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    l10n_in_gst_treatment = models.CharField(max_length=200, blank=True, null=True)
    project = models.ForeignKey(ProjectProject,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    opportunity = models.ForeignKey(CrmLead,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    cart_recovery_email_sent = models.BooleanField(blank=True, null=True)
    website = models.ForeignKey('Website',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    warning_stock = models.CharField(max_length=200, blank=True, null=True)
    amazon_order_ref = models.CharField(unique=True, max_length=200, blank=True, null=True)
    amazon_channel = models.CharField(max_length=200, blank=True, null=True)
    has_due = models.BooleanField(blank=True, null=True)
    is_warning = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sale_order'


class SaleOrderCancel(models.Model):
    order = models.ForeignKey(SaleOrder,    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sale_order_cancel'


class SaleOrderLine(models.Model):
    order = models.ForeignKey(SaleOrder,    models.DO_NOTHING, related_name="+")
    name = models.TextField()
    sequence = models.IntegerField()
    invoice_status = models.CharField(max_length=200, blank=True, null=True)
    price_unit = models.DecimalField(max_digits=65535, decimal_places=65535)
    price_subtotal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_tax = models.FloatField(blank=True, null=True)
    price_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_reduce = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_reduce_taxinc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_reduce_taxexcl = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    discount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    product = models.ForeignKey(ProductProduct,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    product_uom_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    product_uom = models.ForeignKey('UomUom',    models.DO_NOTHING, related_name="+", db_column='product_uom', blank=True, null=True)
    qty_delivered_method = models.CharField(max_length=200, blank=True, null=True)
    qty_delivered = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    qty_delivered_manual = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    qty_to_invoice = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    qty_invoiced = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    untaxed_amount_invoiced = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    untaxed_amount_to_invoice = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    salesman = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    currency = models.ForeignKey(ResCurrency,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    company = models.ForeignKey(ResCompany,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    order_partner = models.ForeignKey(ResPartner,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    is_expense = models.BooleanField(blank=True, null=True)
    is_downpayment = models.BooleanField(blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    customer_lead = models.FloatField()
    display_type = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    product_packaging = models.ForeignKey(ProductPackaging,    models.DO_NOTHING, related_name="+", db_column='product_packaging', blank=True, null=True)
    route = models.ForeignKey('StockLocationRoute',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    is_service = models.BooleanField(blank=True, null=True)
    project = models.ForeignKey(ProjectProject,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    task = models.ForeignKey(ProjectTask,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    linked_line = models.ForeignKey('self',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    warning_stock = models.CharField(max_length=200, blank=True, null=True)
    amazon_item_ref = models.CharField(unique=True, max_length=200, blank=True, null=True)
    amazon_offer = models.ForeignKey(AmazonOffer,    models.DO_NOTHING, related_name="+", blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sale_order_line'


class SaleOrderLineInvoiceRel(models.Model):
    invoice_line = models.OneToOneField(AccountMoveLine,    models.DO_NOTHING, related_name="+", primary_key=True)
    order_line = models.ForeignKey(SaleOrderLine,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'sale_order_line_invoice_rel'
        unique_together = (('invoice_line', 'order_line'),)


class SaleOrderOption(models.Model):
    order = models.ForeignKey(SaleOrder,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    line = models.ForeignKey(SaleOrderLine,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    name = models.TextField()
    product = models.ForeignKey(ProductProduct,    models.DO_NOTHING, related_name="+")
    price_unit = models.DecimalField(max_digits=65535, decimal_places=65535)
    discount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    uom = models.ForeignKey('UomUom',    models.DO_NOTHING, related_name="+")
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535)
    sequence = models.IntegerField()
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sale_order_option'


class SaleOrderTagRel(models.Model):
    order = models.OneToOneField(SaleOrder,    models.DO_NOTHING, related_name="+", primary_key=True)
    tag = models.ForeignKey(CrmTag,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'sale_order_tag_rel'
        unique_together = (('order', 'tag'),)


class SaleOrderTemplate(models.Model):
    name = models.CharField(max_length=200)
    note = models.TextField(blank=True, null=True)
    number_of_days = models.IntegerField()
    require_signature = models.BooleanField(blank=True, null=True)
    require_payment = models.BooleanField(blank=True, null=True)
    mail_template = models.ForeignKey(MailTemplate,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey(ResCompany,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sale_order_template'


class SaleOrderTemplateLine(models.Model):
    sequence = models.IntegerField()
    sale_order_template = models.ForeignKey(SaleOrderTemplate,    models.DO_NOTHING, related_name="+")
    company = models.ForeignKey(ResCompany,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    name = models.TextField()
    product = models.ForeignKey(ProductProduct,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    product_uom_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    product_uom = models.ForeignKey('UomUom',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    display_type = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sale_order_template_line'


class SaleOrderTemplateOption(models.Model):
    sale_order_template = models.ForeignKey(SaleOrderTemplate,    models.DO_NOTHING, related_name="+")
    company = models.ForeignKey(ResCompany,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    name = models.TextField()
    product = models.ForeignKey(ProductProduct,    models.DO_NOTHING, related_name="+")
    uom = models.ForeignKey('UomUom',    models.DO_NOTHING, related_name="+")
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sale_order_template_option'


class SaleOrderTransactionRel(models.Model):
    sale_order = models.OneToOneField(SaleOrder,    models.DO_NOTHING, related_name="+", primary_key=True)
    transaction = models.ForeignKey(PaymentTransaction,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'sale_order_transaction_rel'
        unique_together = (('sale_order', 'transaction'),)


class SalePaymentAcquirerOnboardingWizard(models.Model):
    paypal_user_type = models.CharField(max_length=200, blank=True, null=True)
    paypal_email_account = models.CharField(max_length=200, blank=True, null=True)
    paypal_seller_account = models.CharField(max_length=200, blank=True, null=True)
    paypal_pdt_token = models.CharField(max_length=200, blank=True, null=True)
    stripe_secret_key = models.CharField(max_length=200, blank=True, null=True)
    stripe_publishable_key = models.CharField(max_length=200, blank=True, null=True)
    manual_name = models.CharField(max_length=200, blank=True, null=True)
    journal_name = models.CharField(max_length=200, blank=True, null=True)
    acc_number = models.CharField(max_length=200, blank=True, null=True)
    manual_post_msg = models.TextField(blank=True, null=True)
    payment_method = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sale_payment_acquirer_onboarding_wizard'


class SlideAnswer(models.Model):
    sequence = models.IntegerField()
    question = models.ForeignKey('SlideQuestion',    models.DO_NOTHING, related_name="+")
    text_value = models.CharField(max_length=200)
    is_correct = models.BooleanField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'slide_answer'


class SlideChannel(models.Model):
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    rating_last_value = models.FloatField(blank=True, null=True)
    website_meta_title = models.CharField(max_length=200, blank=True, null=True)
    website_meta_description = models.TextField(blank=True, null=True)
    website_meta_keywords = models.CharField(max_length=200, blank=True, null=True)
    website_meta_og_img = models.CharField(max_length=200, blank=True, null=True)
    seo_name = models.CharField(max_length=200, blank=True, null=True)
    website = models.ForeignKey('Website',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    is_published = models.BooleanField(blank=True, null=True)
    name = models.CharField(max_length=200)
    active = models.BooleanField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    description_short = models.TextField(blank=True, null=True)
    description_html = models.TextField(blank=True, null=True)
    channel_type = models.CharField(max_length=200)
    sequence = models.IntegerField()
    user = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    color = models.IntegerField()
    slide_last_update = models.DateField(blank=True, null=True)
    promote_strategy = models.CharField(max_length=200, blank=True, null=True)
    promoted_slide = models.ForeignKey('SlideSlide',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    access_token = models.CharField(max_length=200, blank=True, null=True)
    nbr_presentation = models.IntegerField()
    nbr_document = models.IntegerField()
    nbr_video = models.IntegerField()
    nbr_infographic = models.IntegerField()
    nbr_webpage = models.IntegerField()
    nbr_quiz = models.IntegerField()
    total_slides = models.IntegerField()
    total_views = models.IntegerField()
    total_votes = models.IntegerField()
    total_time = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    allow_comment = models.BooleanField(blank=True, null=True)
    publish_template = models.ForeignKey(MailTemplate,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    share_template = models.ForeignKey(MailTemplate,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    enroll = models.CharField(max_length=200)
    enroll_msg = models.TextField(blank=True, null=True)
    visibility = models.CharField(max_length=200)
    karma_gen_slide_vote = models.IntegerField()
    karma_gen_channel_rank = models.IntegerField()
    karma_gen_channel_finish = models.IntegerField()
    karma_review = models.IntegerField()
    karma_slide_comment = models.IntegerField()
    karma_slide_vote = models.IntegerField()
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'slide_channel'


class SlideChannelInvite(models.Model):
    subject = models.CharField(max_length=200, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    template = models.ForeignKey(MailTemplate,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    channel = models.ForeignKey(SlideChannel,    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'slide_channel_invite'


class SlideChannelPartner(models.Model):
    channel = models.ForeignKey(SlideChannel,    models.DO_NOTHING, related_name="+")
    completed = models.BooleanField(blank=True, null=True)
    completion = models.IntegerField()
    completed_slides_count = models.IntegerField()
    partner = models.ForeignKey(ResPartner,    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'slide_channel_partner'


class SlideChannelTag(models.Model):
    name = models.CharField(max_length=200)
    sequence = models.IntegerField()
    group = models.ForeignKey('SlideChannelTagGroup',    models.DO_NOTHING, related_name="+")
    group_sequence = models.IntegerField()
    color = models.IntegerField()
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'slide_channel_tag'


class SlideChannelTagGroup(models.Model):
    is_published = models.BooleanField(blank=True, null=True)
    name = models.CharField(max_length=200)
    sequence = models.IntegerField()
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'slide_channel_tag_group'


class SlideChannelTagRel(models.Model):
    channel = models.OneToOneField(SlideChannel,    models.DO_NOTHING, related_name="+", primary_key=True)
    tag = models.ForeignKey(SlideChannelTag,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'slide_channel_tag_rel'
        unique_together = (('channel', 'tag'),)


class SlideEmbed(models.Model):
    slide = models.ForeignKey('SlideSlide',    models.DO_NOTHING, related_name="+")
    url = models.CharField(max_length=200)
    count_views = models.IntegerField()
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'slide_embed'


class SlideQuestion(models.Model):
    sequence = models.IntegerField()
    question = models.CharField(max_length=200)
    slide = models.ForeignKey('SlideSlide',    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'slide_question'


class SlideSlide(models.Model):
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    website_meta_title = models.CharField(max_length=200, blank=True, null=True)
    website_meta_description = models.TextField(blank=True, null=True)
    website_meta_keywords = models.CharField(max_length=200, blank=True, null=True)
    website_meta_og_img = models.CharField(max_length=200, blank=True, null=True)
    seo_name = models.CharField(max_length=200, blank=True, null=True)
    is_published = models.BooleanField(blank=True, null=True)
    name = models.CharField(max_length=200)
    active = models.BooleanField(blank=True, null=True)
    sequence = models.IntegerField()
    user = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    channel = models.ForeignKey(SlideChannel,    models.DO_NOTHING, related_name="+")
    is_preview = models.BooleanField(blank=True, null=True)
    completion_time = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    is_category = models.BooleanField(blank=True, null=True)
    category = models.ForeignKey('self',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    quiz_first_attempt_reward = models.IntegerField()
    quiz_second_attempt_reward = models.IntegerField()
    quiz_third_attempt_reward = models.IntegerField()
    quiz_fourth_attempt_reward = models.IntegerField()
    slide_type = models.CharField(max_length=200)
    url = models.CharField(max_length=200, blank=True, null=True)
    document_id = models.CharField(max_length=200, blank=True, null=True)
    slide_resource_downloadable = models.BooleanField(blank=True, null=True)
    mime_type = models.CharField(max_length=200, blank=True, null=True)
    html_content = models.TextField(blank=True, null=True)
    date_published = models.DateTimeField(blank=True, null=True)
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    slide_views = models.IntegerField()
    public_views = models.IntegerField()
    total_views = models.IntegerField()
    nbr_presentation = models.IntegerField()
    nbr_document = models.IntegerField()
    nbr_video = models.IntegerField()
    nbr_infographic = models.IntegerField()
    nbr_webpage = models.IntegerField()
    nbr_quiz = models.IntegerField()
    total_slides = models.IntegerField()
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'slide_slide'


class SlideSlideLink(models.Model):
    slide = models.ForeignKey(SlideSlide,    models.DO_NOTHING, related_name="+")
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'slide_slide_link'


class SlideSlidePartner(models.Model):
    slide = models.ForeignKey(SlideSlide,    models.DO_NOTHING, related_name="+")
    channel = models.ForeignKey(SlideChannel,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    partner = models.ForeignKey(ResPartner,    models.DO_NOTHING, related_name="+")
    vote = models.IntegerField()
    completed = models.BooleanField(blank=True, null=True)
    quiz_attempts_count = models.IntegerField()
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'slide_slide_partner'


class SlideSlideResource(models.Model):
    slide = models.ForeignKey(SlideSlide,    models.DO_NOTHING, related_name="+")
    name = models.CharField(max_length=200)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'slide_slide_resource'


class SlideTag(models.Model):
    name = models.CharField(unique=True, max_length=200)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'slide_tag'


class SlotPlanningSelectSend(models.Model):
    slot = models.ForeignKey(PlanningSlot,    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'slot_planning_select_send'


class SmsCancel(models.Model):
    model = models.CharField(max_length=200)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sms_cancel'


class SmsComposer(models.Model):
    composition_mode = models.CharField(max_length=200)
    res_model = models.CharField(max_length=200, blank=True, null=True)
    res_id = models.IntegerField()
    res_ids = models.CharField(max_length=200, blank=True, null=True)
    use_active_domain = models.BooleanField(blank=True, null=True)
    active_domain = models.TextField(blank=True, null=True)
    mass_keep_log = models.BooleanField(blank=True, null=True)
    mass_force_send = models.BooleanField(blank=True, null=True)
    mass_use_blacklist = models.BooleanField(blank=True, null=True)
    recipient_single_number_itf = models.CharField(max_length=200, blank=True, null=True)
    number_field_name = models.CharField(max_length=200, blank=True, null=True)
    numbers = models.CharField(max_length=200, blank=True, null=True)
    template = models.ForeignKey('SmsTemplate',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    body = models.TextField()
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sms_composer'


class SmsResend(models.Model):
    mail_message = models.ForeignKey(MailMessage,    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sms_resend'


class SmsResendRecipient(models.Model):
    sms_resend = models.ForeignKey(SmsResend,    models.DO_NOTHING, related_name="+")
    notification = models.ForeignKey(MailMessageResPartnerNeedactionRel,    models.DO_NOTHING, related_name="+")
    resend = models.BooleanField(blank=True, null=True)
    partner_name = models.CharField(max_length=200, blank=True, null=True)
    sms_number = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sms_resend_recipient'


class SmsSms(models.Model):
    number = models.CharField(max_length=200, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    partner = models.ForeignKey(ResPartner,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    mail_message = models.ForeignKey(MailMessage,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    state = models.CharField(max_length=200)
    error_code = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sms_sms'


class SmsTemplate(models.Model):
    lang = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    model = models.ForeignKey(IrModel,    models.DO_NOTHING, related_name="+")
    model_0 = models.CharField(db_column='model', max_length=200, blank=True, null=True)  # Field renamed because of name conflict.
    body = models.CharField(max_length=200)
    sidebar_action = models.ForeignKey(IrActWindow,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sms_template'


class SmsTemplatePreview(models.Model):
    sms_template = models.ForeignKey(SmsTemplate,    models.DO_NOTHING, related_name="+")
    lang = models.CharField(max_length=200, blank=True, null=True)
    resource_ref = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sms_template_preview'


class SnailmailConfirmFollowup(models.Model):
    model_name = models.CharField(max_length=200, blank=True, null=True)
    followup = models.ForeignKey(FollowupSend,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'snailmail_confirm_followup'


class SnailmailConfirmInvoice(models.Model):
    model_name = models.CharField(max_length=200, blank=True, null=True)
    invoice_send = models.ForeignKey(AccountInvoiceSend,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'snailmail_confirm_invoice'


class SnailmailLetter(models.Model):
    user = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    model = models.CharField(max_length=200)
    res_id = models.IntegerField()
    partner = models.ForeignKey(ResPartner,    models.DO_NOTHING, related_name="+")
    company = models.ForeignKey(ResCompany,    models.DO_NOTHING, related_name="+")
    report_template = models.ForeignKey(IrActReportXml,    models.DO_NOTHING, related_name="+", db_column='report_template', blank=True, null=True)
    attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    color = models.BooleanField(blank=True, null=True)
    cover = models.BooleanField(blank=True, null=True)
    duplex = models.BooleanField(blank=True, null=True)
    state = models.CharField(max_length=200)
    error_code = models.CharField(max_length=200, blank=True, null=True)
    info_msg = models.CharField(max_length=200, blank=True, null=True)
    message = models.ForeignKey(MailMessage,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    street = models.CharField(max_length=200, blank=True, null=True)
    street2 = models.CharField(max_length=200, blank=True, null=True)
    zip = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    state_0 = models.ForeignKey(ResCountryState,    models.DO_NOTHING, related_name="+", db_column='state_id', blank=True, null=True)  # Field renamed because of name conflict.
    country = models.ForeignKey(ResCountry,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'snailmail_letter'


class SnailmailLetterCancel(models.Model):
    model = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'snailmail_letter_cancel'


class SnailmailLetterFormatError(models.Model):
    message = models.ForeignKey(MailMessage,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    snailmail_cover = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'snailmail_letter_format_error'


class SnailmailLetterMissingRequiredFields(models.Model):
    partner = models.ForeignKey(ResPartner,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    letter = models.ForeignKey(SnailmailLetter,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    street = models.CharField(max_length=200, blank=True, null=True)
    street2 = models.CharField(max_length=200, blank=True, null=True)
    zip = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.ForeignKey(ResCountryState,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    country = models.ForeignKey(ResCountry,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'snailmail_letter_missing_required_fields'


class StockAssignSerial(models.Model):
    move = models.ForeignKey('StockMove',    models.DO_NOTHING, related_name="+")
    next_serial_number = models.CharField(max_length=200)
    next_serial_count = models.IntegerField()
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stock_assign_serial'


class StockBackorderConfirmation(models.Model):
    show_transfers = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stock_backorder_confirmation'


class StockBackorderConfirmationLine(models.Model):
    backorder_confirmation = models.ForeignKey(StockBackorderConfirmation,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    picking = models.ForeignKey('StockPicking',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    to_backorder = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stock_backorder_confirmation_line'


class StockChangeProductQty(models.Model):
    product = models.ForeignKey(ProductProduct,    models.DO_NOTHING, related_name="+")
    product_tmpl = models.ForeignKey(ProductTemplate,    models.DO_NOTHING, related_name="+")
    new_quantity = models.DecimalField(max_digits=65535, decimal_places=65535)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stock_change_product_qty'


class StockImmediateTransfer(models.Model):
    show_transfers = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stock_immediate_transfer'


class StockImmediateTransferLine(models.Model):
    immediate_transfer = models.ForeignKey(StockImmediateTransfer,    models.DO_NOTHING, related_name="+")
    picking = models.ForeignKey('StockPicking',    models.DO_NOTHING, related_name="+")
    to_immediate = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stock_immediate_transfer_line'


class StockInventory(models.Model):
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    name = models.CharField(max_length=200)
    date = models.DateTimeField()
    state = models.CharField(max_length=200, blank=True, null=True)
    company = models.ForeignKey(ResCompany,    models.DO_NOTHING, related_name="+")
    start_empty = models.BooleanField(blank=True, null=True)
    prefill_counted_quantity = models.CharField(max_length=200, blank=True, null=True)
    exhausted = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    accounting_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stock_inventory'


class StockInventoryLine(models.Model):
    is_editable = models.BooleanField(blank=True, null=True)
    inventory = models.ForeignKey(StockInventory,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    partner = models.ForeignKey(ResPartner,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    product = models.ForeignKey(ProductProduct,    models.DO_NOTHING, related_name="+")
    product_uom = models.ForeignKey('UomUom',    models.DO_NOTHING, related_name="+")
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    categ = models.ForeignKey(ProductCategory,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    location = models.ForeignKey('StockLocation',    models.DO_NOTHING, related_name="+")
    package = models.ForeignKey('StockQuantPackage',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    prod_lot = models.ForeignKey('StockProductionLot',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    company = models.ForeignKey(ResCompany,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    theoretical_qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    inventory_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stock_inventory_line'


class StockInventoryStockLocationRel(models.Model):
    stock_inventory = models.OneToOneField(StockInventory,    models.DO_NOTHING, related_name="+", primary_key=True)
    stock_location = models.ForeignKey('StockLocation',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'stock_inventory_stock_location_rel'
        unique_together = (('stock_inventory', 'stock_location'),)


class StockLocation(models.Model):
    name = models.CharField(max_length=200)
    complete_name = models.CharField(max_length=200, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    usage = models.CharField(max_length=200)
    location = models.ForeignKey('self',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    posx = models.IntegerField()
    posy = models.IntegerField()
    posz = models.IntegerField()
    parent_path = models.CharField(max_length=200, blank=True, null=True)
    company = models.ForeignKey(ResCompany,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    scrap_location = models.BooleanField(blank=True, null=True)
    return_location = models.BooleanField(blank=True, null=True)
    removal_strategy = models.ForeignKey(ProductRemoval,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    barcode = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    valuation_in_account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    valuation_out_account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_studio_code = models.CharField(max_length=200, blank=True, null=True)
    amazon_location = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stock_location'
        unique_together = (('barcode', 'company'),)


class StockLocationRoute(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(blank=True, null=True)
    sequence = models.IntegerField()
    product_selectable = models.BooleanField(blank=True, null=True)
    product_categ_selectable = models.BooleanField(blank=True, null=True)
    warehouse_selectable = models.BooleanField(blank=True, null=True)
    supplied_wh = models.ForeignKey('StockWarehouse',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    supplier_wh = models.ForeignKey('StockWarehouse',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    company = models.ForeignKey(ResCompany,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    sale_selectable = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stock_location_route'


class StockLocationRouteCateg(models.Model):
    route = models.OneToOneField(StockLocationRoute,    models.DO_NOTHING, related_name="+", primary_key=True)
    categ = models.ForeignKey(ProductCategory,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'stock_location_route_categ'
        unique_together = (('route', 'categ'),)


class StockLocationRouteMove(models.Model):
    move = models.OneToOneField('StockMove',    models.DO_NOTHING, related_name="+", primary_key=True)
    route = models.ForeignKey(StockLocationRoute,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'stock_location_route_move'
        unique_together = (('move', 'route'),)


class StockLocationRouteStockRulesReportRel(models.Model):
    stock_rules_report = models.OneToOneField('StockRulesReport',    models.DO_NOTHING, related_name="+", primary_key=True)
    stock_location_route = models.ForeignKey(StockLocationRoute,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'stock_location_route_stock_rules_report_rel'
        unique_together = (('stock_rules_report', 'stock_location_route'),)


class StockMove(models.Model):
    name = models.CharField(max_length=200)
    sequence = models.IntegerField()
    priority = models.CharField(max_length=200, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    date = models.DateTimeField()
    date_deadline = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey(ResCompany,    models.DO_NOTHING, related_name="+")
    product = models.ForeignKey(ProductProduct,    models.DO_NOTHING, related_name="+")
    description_picking = models.TextField(blank=True, null=True)
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    product_uom_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    product_uom = models.ForeignKey('UomUom',    models.DO_NOTHING, related_name="+", db_column='product_uom')
    location = models.ForeignKey(StockLocation,    models.DO_NOTHING, related_name="+")
    location_dest = models.ForeignKey(StockLocation,    models.DO_NOTHING, related_name="+")
    partner = models.ForeignKey(ResPartner,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    picking = models.ForeignKey('StockPicking',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    price_unit = models.FloatField(blank=True, null=True)
    origin = models.CharField(max_length=200, blank=True, null=True)
    procure_method = models.CharField(max_length=200)
    scrapped = models.BooleanField(blank=True, null=True)
    group = models.ForeignKey(ProcurementGroup,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    rule = models.ForeignKey('StockRule',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    propagate_cancel = models.BooleanField(blank=True, null=True)
    delay_alert_date = models.DateTimeField(blank=True, null=True)
    picking_type = models.ForeignKey('StockPickingType',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    inventory = models.ForeignKey(StockInventory,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    origin_returned_move = models.ForeignKey('self',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    restrict_partner = models.ForeignKey(ResPartner,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    warehouse = models.ForeignKey('StockWarehouse',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    additional = models.BooleanField(blank=True, null=True)
    reference = models.CharField(max_length=200, blank=True, null=True)
    package_level = models.ForeignKey('StockPackageLevel',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    next_serial = models.CharField(max_length=200, blank=True, null=True)
    next_serial_count = models.IntegerField()
    orderpoint = models.ForeignKey('StockWarehouseOrderpoint',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    to_refund = models.BooleanField(blank=True, null=True)
    purchase_line = models.ForeignKey(PurchaseOrderLine,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    created_purchase_line = models.ForeignKey(PurchaseOrderLine,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    sale_line = models.ForeignKey(SaleOrderLine,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    is_done = models.BooleanField(blank=True, null=True)
    created_production = models.ForeignKey(MrpProduction,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    production = models.ForeignKey(MrpProduction,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    raw_material_production = models.ForeignKey(MrpProduction,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    unbuild = models.ForeignKey(MrpUnbuild,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    consume_unbuild = models.ForeignKey(MrpUnbuild,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    operation = models.ForeignKey(MrpRoutingWorkcenter,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    workorder = models.ForeignKey(MrpWorkorder,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    bom_line = models.ForeignKey(MrpBomLine,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    byproduct = models.ForeignKey(MrpBomByproduct,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    unit_factor = models.FloatField(blank=True, null=True)
    is_subcontract = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stock_move'


class StockMoveLine(models.Model):
    picking = models.ForeignKey('StockPicking',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    move = models.ForeignKey(StockMove,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    company = models.ForeignKey(ResCompany,    models.DO_NOTHING, related_name="+")
    product = models.ForeignKey(ProductProduct,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    product_uom = models.ForeignKey('UomUom',    models.DO_NOTHING, related_name="+")
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    product_uom_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    qty_done = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    package = models.ForeignKey('StockQuantPackage',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    package_level = models.ForeignKey('StockPackageLevel',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    lot = models.ForeignKey('StockProductionLot',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    lot_name = models.CharField(max_length=200, blank=True, null=True)
    result_package = models.ForeignKey('StockQuantPackage',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    date = models.DateTimeField()
    owner = models.ForeignKey(ResPartner,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    location = models.ForeignKey(StockLocation,    models.DO_NOTHING, related_name="+")
    location_dest = models.ForeignKey(StockLocation,    models.DO_NOTHING, related_name="+")
    state = models.CharField(max_length=200, blank=True, null=True)
    reference = models.CharField(max_length=200, blank=True, null=True)
    description_picking = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    expiration_date = models.DateTimeField(blank=True, null=True)
    workorder = models.ForeignKey(MrpWorkorder,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    production = models.ForeignKey(MrpProduction,    models.DO_NOTHING, related_name="+", blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stock_move_line'


class StockMoveLineConsumeRel(models.Model):
    consume_line = models.OneToOneField(StockMoveLine,    models.DO_NOTHING, related_name="+", primary_key=True)
    produce_line = models.ForeignKey(StockMoveLine,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'stock_move_line_consume_rel'
        unique_together = (('consume_line', 'produce_line'),)


class StockMoveMoveRel(models.Model):
    move_orig = models.OneToOneField(StockMove,    models.DO_NOTHING, related_name="+", primary_key=True)
    move_dest = models.ForeignKey(StockMove,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'stock_move_move_rel'
        unique_together = (('move_orig', 'move_dest'),)


class StockOrderpointSnooze(models.Model):
    predefined_date = models.CharField(max_length=200, blank=True, null=True)
    snoozed_until = models.DateField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stock_orderpoint_snooze'


class StockOrderpointSnoozeStockWarehouseOrderpointRel(models.Model):
    stock_orderpoint_snooze = models.OneToOneField(StockOrderpointSnooze,    models.DO_NOTHING, related_name="+", primary_key=True)
    stock_warehouse_orderpoint = models.ForeignKey('StockWarehouseOrderpoint',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'stock_orderpoint_snooze_stock_warehouse_orderpoint_rel'
        unique_together = (('stock_orderpoint_snooze', 'stock_warehouse_orderpoint'),)


class StockPackageDestination(models.Model):
    picking = models.ForeignKey('StockPicking',    models.DO_NOTHING, related_name="+")
    location_dest = models.ForeignKey(StockLocation,    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stock_package_destination'


class StockPackageLevel(models.Model):
    package = models.ForeignKey('StockQuantPackage',    models.DO_NOTHING, related_name="+")
    picking = models.ForeignKey('StockPicking',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    location_dest = models.ForeignKey(StockLocation,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    company = models.ForeignKey(ResCompany,    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stock_package_level'


class StockPicking(models.Model):
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    origin = models.CharField(max_length=200, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    backorder = models.ForeignKey('self',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    move_type = models.CharField(max_length=200)
    state = models.CharField(max_length=200, blank=True, null=True)
    group = models.ForeignKey(ProcurementGroup,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    priority = models.CharField(max_length=200, blank=True, null=True)
    scheduled_date = models.DateTimeField(blank=True, null=True)
    date_deadline = models.DateTimeField(blank=True, null=True)
    has_deadline_issue = models.BooleanField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    date_done = models.DateTimeField(blank=True, null=True)
    location = models.ForeignKey(StockLocation,    models.DO_NOTHING, related_name="+")
    location_dest = models.ForeignKey(StockLocation,    models.DO_NOTHING, related_name="+")
    picking_type = models.ForeignKey('StockPickingType',    models.DO_NOTHING, related_name="+")
    partner = models.ForeignKey(ResPartner,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    company = models.ForeignKey(ResCompany,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    user = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    owner = models.ForeignKey(ResPartner,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    printed = models.BooleanField(blank=True, null=True)
    is_locked = models.BooleanField(blank=True, null=True)
    immediate_transfer = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    sale = models.ForeignKey(SaleOrder,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_studio_invoice_number = models.CharField(max_length=200, blank=True, null=True)
    x_studio_way_bill_number = models.CharField(max_length=200, blank=True, null=True)
    x_studio_tin_number = models.CharField(max_length=200, blank=True, null=True)
    x_studio_lpo_number = models.CharField(max_length=200, blank=True, null=True)
    x_studio_char_field_azc77 = models.CharField(db_column='x_studio_char_field_azC77', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_vat_std = models.ForeignKey(AccountTax,    models.DO_NOTHING, related_name="+", db_column='x_studio_vat_std', blank=True, null=True)
    x_studio_nhil = models.ForeignKey(AccountTax,    models.DO_NOTHING, related_name="+", db_column='x_studio_nhil', blank=True, null=True)
    x_studio_getfund = models.ForeignKey(AccountTax,    models.DO_NOTHING, related_name="+", db_column='x_studio_getfund', blank=True, null=True)
    x_studio_posted_by = models.ForeignKey(ResPartner,    models.DO_NOTHING, related_name="+", db_column='x_studio_posted_by', blank=True, null=True)
    x_studio_entries_checked_by = models.ForeignKey(ResPartner,    models.DO_NOTHING, related_name="+", db_column='x_studio_entries_checked_by', blank=True, null=True)
    x_studio_storekeeper = models.ForeignKey(ResPartner,    models.DO_NOTHING, related_name="+", db_column='x_studio_storekeeper', blank=True, null=True)
    website = models.ForeignKey('Website',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    amazon_sync_pending = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stock_picking'
        unique_together = (('name', 'company'),)


class StockPickingBackorderRel(models.Model):
    stock_backorder_confirmation = models.OneToOneField(StockBackorderConfirmation,    models.DO_NOTHING, related_name="+", primary_key=True)
    stock_picking = models.ForeignKey(StockPicking,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'stock_picking_backorder_rel'
        unique_together = (('stock_backorder_confirmation', 'stock_picking'),)


class StockPickingSmsRel(models.Model):
    confirm_stock_sms = models.OneToOneField(ConfirmStockSms,    models.DO_NOTHING, related_name="+", primary_key=True)
    stock_picking = models.ForeignKey(StockPicking,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'stock_picking_sms_rel'
        unique_together = (('confirm_stock_sms', 'stock_picking'),)


class StockPickingTransferRel(models.Model):
    stock_immediate_transfer = models.OneToOneField(StockImmediateTransfer,    models.DO_NOTHING, related_name="+", primary_key=True)
    stock_picking = models.ForeignKey(StockPicking,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'stock_picking_transfer_rel'
        unique_together = (('stock_immediate_transfer', 'stock_picking'),)


class StockPickingType(models.Model):
    name = models.CharField(max_length=200)
    color = models.IntegerField()
    sequence = models.IntegerField()
    sequence_0 = models.ForeignKey(IrSequence,    models.DO_NOTHING, related_name="+", db_column='sequence_id', blank=True, null=True)  # Field renamed because of name conflict.
    sequence_code = models.CharField(max_length=200)
    default_location_src = models.ForeignKey(StockLocation,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    default_location_dest = models.ForeignKey(StockLocation,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    code = models.CharField(max_length=200)
    return_picking_type = models.ForeignKey('self',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    show_entire_packs = models.BooleanField(blank=True, null=True)
    warehouse = models.ForeignKey('StockWarehouse',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    use_create_lots = models.BooleanField(blank=True, null=True)
    use_existing_lots = models.BooleanField(blank=True, null=True)
    show_operations = models.BooleanField(blank=True, null=True)
    show_reserved = models.BooleanField(blank=True, null=True)
    barcode = models.CharField(max_length=200, blank=True, null=True)
    company = models.ForeignKey(ResCompany,    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    use_create_components_lots = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stock_picking_type'


class StockProductionLot(models.Model):
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    name = models.CharField(max_length=200)
    ref = models.CharField(max_length=200, blank=True, null=True)
    product = models.ForeignKey(ProductProduct,    models.DO_NOTHING, related_name="+")
    product_uom = models.ForeignKey('UomUom',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    company = models.ForeignKey(ResCompany,    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    expiration_date = models.DateTimeField(blank=True, null=True)
    use_date = models.DateTimeField(blank=True, null=True)
    removal_date = models.DateTimeField(blank=True, null=True)
    alert_date = models.DateTimeField(blank=True, null=True)
    product_expiry_reminded = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stock_production_lot'


class StockPutawayRule(models.Model):
    product = models.ForeignKey(ProductProduct,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    category = models.ForeignKey(ProductCategory,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    location_in = models.ForeignKey(StockLocation,    models.DO_NOTHING, related_name="+")
    location_out = models.ForeignKey(StockLocation,    models.DO_NOTHING, related_name="+")
    sequence = models.IntegerField()
    company = models.ForeignKey(ResCompany,    models.DO_NOTHING, related_name="+")
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stock_putaway_rule'


class StockQuant(models.Model):
    product = models.ForeignKey(ProductProduct,    models.DO_NOTHING, related_name="+")
    company = models.ForeignKey(ResCompany,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    location = models.ForeignKey(StockLocation,    models.DO_NOTHING, related_name="+")
    lot = models.ForeignKey(StockProductionLot,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    package = models.ForeignKey('StockQuantPackage',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    owner = models.ForeignKey(ResPartner,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    quantity = models.FloatField(blank=True, null=True)
    reserved_quantity = models.FloatField()
    in_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    removal_date = models.DateTimeField(blank=True, null=True)
    x_expired_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stock_quant'


class StockQuantPackage(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    packaging = models.ForeignKey(ProductPackaging,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    location = models.ForeignKey(StockLocation,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    company = models.ForeignKey(ResCompany,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stock_quant_package'


class StockQuantityHistory(models.Model):
    inventory_datetime = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stock_quantity_history'


class StockReturnPicking(models.Model):
    picking = models.ForeignKey(StockPicking,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    move_dest_exists = models.BooleanField(blank=True, null=True)
    original_location = models.ForeignKey(StockLocation,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    parent_location = models.ForeignKey(StockLocation,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    location = models.ForeignKey(StockLocation,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stock_return_picking'


class StockReturnPickingLine(models.Model):
    product = models.ForeignKey(ProductProduct,    models.DO_NOTHING, related_name="+")
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535)
    wizard = models.ForeignKey(StockReturnPicking,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    move = models.ForeignKey(StockMove,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    to_refund = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stock_return_picking_line'


class StockRouteProduct(models.Model):
    route = models.OneToOneField(StockLocationRoute,    models.DO_NOTHING, related_name="+", primary_key=True)
    product = models.ForeignKey(ProductTemplate,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'stock_route_product'
        unique_together = (('route', 'product'),)


class StockRouteWarehouse(models.Model):
    route = models.OneToOneField(StockLocationRoute,    models.DO_NOTHING, related_name="+", primary_key=True)
    warehouse = models.ForeignKey('StockWarehouse',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'stock_route_warehouse'
        unique_together = (('route', 'warehouse'),)


class StockRule(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(blank=True, null=True)
    group_propagation_option = models.CharField(max_length=200, blank=True, null=True)
    group = models.ForeignKey(ProcurementGroup,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    action = models.CharField(max_length=200)
    sequence = models.IntegerField()
    company = models.ForeignKey(ResCompany,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    location = models.ForeignKey(StockLocation,    models.DO_NOTHING, related_name="+")
    location_src = models.ForeignKey(StockLocation,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    route = models.ForeignKey(StockLocationRoute,    models.DO_NOTHING, related_name="+")
    procure_method = models.CharField(max_length=200)
    route_sequence = models.IntegerField()
    picking_type = models.ForeignKey(StockPickingType,    models.DO_NOTHING, related_name="+")
    delay = models.IntegerField()
    partner_address = models.ForeignKey(ResPartner,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    propagate_cancel = models.BooleanField(blank=True, null=True)
    warehouse = models.ForeignKey('StockWarehouse',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    propagate_warehouse = models.ForeignKey('StockWarehouse',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    auto = models.CharField(max_length=200)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stock_rule'


class StockRulesReport(models.Model):
    product = models.ForeignKey(ProductProduct,    models.DO_NOTHING, related_name="+")
    product_tmpl = models.ForeignKey(ProductTemplate,    models.DO_NOTHING, related_name="+")
    product_has_variants = models.BooleanField()
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stock_rules_report'


class StockRulesReportStockWarehouseRel(models.Model):
    stock_rules_report = models.OneToOneField(StockRulesReport,    models.DO_NOTHING, related_name="+", primary_key=True)
    stock_warehouse = models.ForeignKey('StockWarehouse',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'stock_rules_report_stock_warehouse_rel'
        unique_together = (('stock_rules_report', 'stock_warehouse'),)


class StockSchedulerCompute(models.Model):
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stock_scheduler_compute'


class StockScrap(models.Model):
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    name = models.CharField(max_length=200)
    company = models.ForeignKey(ResCompany,    models.DO_NOTHING, related_name="+")
    origin = models.CharField(max_length=200, blank=True, null=True)
    product = models.ForeignKey(ProductProduct,    models.DO_NOTHING, related_name="+")
    product_uom = models.ForeignKey('UomUom',    models.DO_NOTHING, related_name="+")
    lot = models.ForeignKey(StockProductionLot,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    package = models.ForeignKey(StockQuantPackage,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    owner = models.ForeignKey(ResPartner,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    move = models.ForeignKey(StockMove,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    picking = models.ForeignKey(StockPicking,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    location = models.ForeignKey(StockLocation,    models.DO_NOTHING, related_name="+")
    scrap_location = models.ForeignKey(StockLocation,    models.DO_NOTHING, related_name="+")
    scrap_qty = models.FloatField()
    state = models.CharField(max_length=200, blank=True, null=True)
    date_done = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    production = models.ForeignKey(MrpProduction,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    workorder = models.ForeignKey(MrpWorkorder,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_studio_many2one_field_zkx7t = models.ForeignKey(StockProductionLot,    models.DO_NOTHING, related_name="+", db_column='x_studio_many2one_field_zKx7t', blank=True, null=True)  # Field name made lowercase.
    x_studio_expiration_date = models.CharField(max_length=200, blank=True, null=True)
    x_studio_description = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stock_scrap'


class StockTraceabilityReport(models.Model):
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stock_traceability_report'


class StockTrackConfirmation(models.Model):
    inventory = models.ForeignKey(StockInventory,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stock_track_confirmation'


class StockTrackLine(models.Model):
    product = models.ForeignKey(ProductProduct,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    tracking = models.CharField(max_length=200, blank=True, null=True)
    wizard = models.ForeignKey(StockTrackConfirmation,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stock_track_line'


class StockValuationLayer(models.Model):
    company = models.ForeignKey(ResCompany,    models.DO_NOTHING, related_name="+")
    product = models.ForeignKey(ProductProduct,    models.DO_NOTHING, related_name="+")
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    unit_cost = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    value = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    remaining_qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    remaining_value = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    stock_valuation_layer = models.ForeignKey('self',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    stock_move = models.ForeignKey(StockMove,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    account_move = models.ForeignKey(AccountMove,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stock_valuation_layer'


class StockValuationLayerRevaluation(models.Model):
    company = models.ForeignKey(ResCompany,    models.DO_NOTHING, related_name="+")
    product = models.ForeignKey(ProductProduct,    models.DO_NOTHING, related_name="+")
    added_value = models.DecimalField(max_digits=65535, decimal_places=65535)
    reason = models.CharField(max_length=200, blank=True, null=True)
    account_journal = models.ForeignKey(AccountJournal,    models.DO_NOTHING, related_name="+")
    account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stock_valuation_layer_revaluation'


class StockWarehouse(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey(ResCompany,    models.DO_NOTHING, related_name="+")
    partner = models.ForeignKey(ResPartner,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    view_location = models.ForeignKey(StockLocation,    models.DO_NOTHING, related_name="+")
    lot_stock = models.ForeignKey(StockLocation,    models.DO_NOTHING, related_name="+")
    code = models.CharField(max_length=5)
    reception_steps = models.CharField(max_length=200)
    delivery_steps = models.CharField(max_length=200)
    wh_input_stock_loc = models.ForeignKey(StockLocation,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    wh_qc_stock_loc = models.ForeignKey(StockLocation,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    wh_output_stock_loc = models.ForeignKey(StockLocation,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    wh_pack_stock_loc = models.ForeignKey(StockLocation,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    mto_pull = models.ForeignKey(StockRule,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    pick_type = models.ForeignKey(StockPickingType,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    pack_type = models.ForeignKey(StockPickingType,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    out_type = models.ForeignKey(StockPickingType,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    in_type = models.ForeignKey(StockPickingType,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    int_type = models.ForeignKey(StockPickingType,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    crossdock_route = models.ForeignKey(StockLocationRoute,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    reception_route = models.ForeignKey(StockLocationRoute,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    delivery_route = models.ForeignKey(StockLocationRoute,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    sequence = models.IntegerField()
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    buy_to_resupply = models.BooleanField(blank=True, null=True)
    buy_pull = models.ForeignKey(StockRule,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    l10n_in_purchase_journal = models.ForeignKey(AccountJournal,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    l10n_in_sale_journal = models.ForeignKey(AccountJournal,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    manufacture_to_resupply = models.BooleanField(blank=True, null=True)
    manufacture_pull = models.ForeignKey(StockRule,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    manufacture_mto_pull = models.ForeignKey(StockRule,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    pbm_mto_pull = models.ForeignKey(StockRule,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    sam_rule = models.ForeignKey(StockRule,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    manu_type = models.ForeignKey(StockPickingType,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    pbm_type = models.ForeignKey(StockPickingType,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    sam_type = models.ForeignKey(StockPickingType,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    manufacture_steps = models.CharField(max_length=200)
    pbm_route = models.ForeignKey(StockLocationRoute,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    pbm_loc = models.ForeignKey(StockLocation,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    sam_loc = models.ForeignKey(StockLocation,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    subcontracting_to_resupply = models.BooleanField(blank=True, null=True)
    subcontracting_mto_pull = models.ForeignKey(StockRule,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    subcontracting_pull = models.ForeignKey(StockRule,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    subcontracting_route = models.ForeignKey(StockLocationRoute,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    subcontracting_type = models.ForeignKey(StockPickingType,    models.DO_NOTHING, related_name="+", blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stock_warehouse'
        unique_together = (('code', 'company'), ('name', 'company'),)


class StockWarehouseOrderpoint(models.Model):
    name = models.CharField(max_length=200)
    trigger = models.CharField(max_length=200)
    active = models.BooleanField(blank=True, null=True)
    snoozed_until = models.DateField(blank=True, null=True)
    warehouse = models.ForeignKey(StockWarehouse,    models.DO_NOTHING, related_name="+")
    location = models.ForeignKey(StockLocation,    models.DO_NOTHING, related_name="+")
    product = models.ForeignKey(ProductProduct,    models.DO_NOTHING, related_name="+")
    product_category = models.ForeignKey(ProductCategory,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    product_min_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    product_max_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    qty_multiple = models.DecimalField(max_digits=65535, decimal_places=65535)
    group = models.ForeignKey(ProcurementGroup,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    company = models.ForeignKey(ResCompany,    models.DO_NOTHING, related_name="+")
    route = models.ForeignKey(StockLocationRoute,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    qty_to_order = models.FloatField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    supplier = models.ForeignKey(ProductSupplierinfo,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    bom = models.ForeignKey(MrpBom,    models.DO_NOTHING, related_name="+", blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stock_warehouse_orderpoint'


class StockWarnInsufficientQtyScrap(models.Model):
    scrap = models.ForeignKey(StockScrap,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    product = models.ForeignKey(ProductProduct,    models.DO_NOTHING, related_name="+")
    location = models.ForeignKey(StockLocation,    models.DO_NOTHING, related_name="+")
    quantity = models.FloatField()
    product_uom_name = models.CharField(max_length=200)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stock_warn_insufficient_qty_scrap'


class StockWarnInsufficientQtyUnbuild(models.Model):
    product = models.ForeignKey(ProductProduct,    models.DO_NOTHING, related_name="+")
    location = models.ForeignKey(StockLocation,    models.DO_NOTHING, related_name="+")
    quantity = models.FloatField()
    product_uom_name = models.CharField(max_length=200)
    unbuild = models.ForeignKey(MrpUnbuild,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stock_warn_insufficient_qty_unbuild'


class StockWhResupplyTable(models.Model):
    supplied_wh = models.OneToOneField(StockWarehouse,    models.DO_NOTHING, related_name="+", primary_key=True)
    supplier_wh = models.ForeignKey(StockWarehouse,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'stock_wh_resupply_table'
        unique_together = (('supplied_wh', 'supplier_wh'),)


class StudioApprovalEntry(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    user = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+")
    rule = models.ForeignKey('StudioApprovalRule',    models.DO_NOTHING, related_name="+")
    model = models.CharField(max_length=200, blank=True, null=True)
    method = models.CharField(max_length=200, blank=True, null=True)
    action_id = models.IntegerField()
    res_id = models.IntegerField()
    approved = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'studio_approval_entry'
        unique_together = (('rule', 'model', 'res_id'),)


class StudioApprovalRule(models.Model):
    active = models.BooleanField(blank=True, null=True)
    group = models.ForeignKey(ResGroups,    models.DO_NOTHING, related_name="+")
    model = models.ForeignKey(IrModel,    models.DO_NOTHING, related_name="+")
    method = models.CharField(max_length=200, blank=True, null=True)
    action_id = models.IntegerField()
    name = models.CharField(max_length=200, blank=True, null=True)
    message = models.CharField(max_length=200, blank=True, null=True)
    exclusive_user = models.BooleanField(blank=True, null=True)
    model_name = models.CharField(max_length=200, blank=True, null=True)
    domain = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'studio_approval_rule'


class SummaryEmpRel(models.Model):
    sum = models.OneToOneField(HrHolidaysSummaryEmployee,    models.DO_NOTHING, related_name="+", primary_key=True)
    emp = models.ForeignKey(HrEmployee,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'summary_emp_rel'
        unique_together = (('sum', 'emp'),)


class TaxAdjustmentsWizard(models.Model):
    reason = models.CharField(max_length=200)
    journal = models.ForeignKey(AccountJournal,    models.DO_NOTHING, related_name="+")
    date = models.DateField()
    debit_account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+")
    credit_account = models.ForeignKey(AccountAccount,    models.DO_NOTHING, related_name="+")
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    adjustment_type = models.CharField(max_length=200)
    tax_report_line = models.ForeignKey(AccountTaxReportLine,    models.DO_NOTHING, related_name="+")
    company_currency = models.ForeignKey(ResCurrency,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tax_adjustments_wizard'


class TeamFavoriteUserRel(models.Model):
    team = models.OneToOneField(CrmTeam,    models.DO_NOTHING, related_name="+", primary_key=True)
    user = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'team_favorite_user_rel'
        unique_together = (('team', 'user'),)


class TechTech(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tech_tech'


class ThemeIrAttachment(models.Model):
    name = models.CharField(max_length=200)
    key = models.CharField(max_length=200)
    url = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'theme_ir_attachment'


class ThemeIrUiView(models.Model):
    name = models.CharField(max_length=200)
    key = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=200, blank=True, null=True)
    priority = models.IntegerField()
    mode = models.CharField(max_length=200, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    arch = models.TextField(blank=True, null=True)
    arch_fs = models.CharField(max_length=200, blank=True, null=True)
    inherit_id = models.CharField(max_length=200, blank=True, null=True)
    customize_show = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'theme_ir_ui_view'


class ThemeWebsiteMenu(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200, blank=True, null=True)
    page = models.ForeignKey('ThemeWebsitePage',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    new_window = models.BooleanField(blank=True, null=True)
    sequence = models.IntegerField()
    parent = models.ForeignKey('self',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'theme_website_menu'


class ThemeWebsitePage(models.Model):
    url = models.CharField(max_length=200, blank=True, null=True)
    view = models.ForeignKey(ThemeIrUiView,    models.DO_NOTHING, related_name="+")
    website_indexed = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'theme_website_page'


class TimerTimer(models.Model):
    timer_start = models.DateTimeField(blank=True, null=True)
    timer_pause = models.DateTimeField(blank=True, null=True)
    res_model = models.CharField(max_length=200)
    res_id = models.IntegerField()
    user = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'timer_timer'
        unique_together = (('res_model', 'res_id', 'user'),)


class TimesheetCost(models.Model):
    employee_id = models.CharField(max_length=200, blank=True, null=True)
    employee_name = models.CharField(max_length=200, blank=True, null=True)
    updated_date = models.DateField(blank=True, null=True)
    current_value = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'timesheet_cost'


class UomCategory(models.Model):
    name = models.CharField(max_length=200)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'uom_category'


class UomUom(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(UomCategory,    models.DO_NOTHING, related_name="+")
    factor = models.DecimalField(max_digits=65535, decimal_places=65535)
    rounding = models.DecimalField(max_digits=65535, decimal_places=65535)
    active = models.BooleanField(blank=True, null=True)
    uom_type = models.CharField(max_length=200)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    l10n_in_code = models.CharField(max_length=200, blank=True, null=True)
    timesheet_widget = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'uom_uom'


class UtmCampaign(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+")
    stage = models.ForeignKey('UtmStage',    models.DO_NOTHING, related_name="+")
    is_website = models.BooleanField(blank=True, null=True)
    color = models.IntegerField()
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey(ResCompany,    models.DO_NOTHING, related_name="+", blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'utm_campaign'


class UtmMedium(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'utm_medium'


class UtmSource(models.Model):
    name = models.CharField(max_length=200)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'utm_source'


class UtmStage(models.Model):
    name = models.CharField(max_length=200)
    sequence = models.IntegerField()
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'utm_stage'


class UtmTag(models.Model):
    name = models.CharField(unique=True, max_length=200)
    color = models.IntegerField()
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'utm_tag'


class UtmTagRel(models.Model):
    tag = models.OneToOneField(UtmCampaign,    models.DO_NOTHING, related_name="+", primary_key=True)
    campaign = models.ForeignKey(UtmTag,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'utm_tag_rel'
        unique_together = (('tag', 'campaign'),)


class VaccinationDetail(models.Model):
    employee = models.ForeignKey(HrEmployee,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    sequence = models.IntegerField()
    vaccine = models.ForeignKey(HrEmployeeVaccineInfo,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    vaccination_centre = models.ForeignKey(HrEmployeeVaccineCentre,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    vaccinated_by = models.CharField(max_length=200, blank=True, null=True)
    vaccine_dose = models.CharField(max_length=200, blank=True, null=True)
    dose_date = models.DateField(blank=True, null=True)
    vaccinated_country = models.ForeignKey(ResCountry,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    vaccinated_state = models.ForeignKey(ResCountryState,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    vaccine_company = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'vaccination_detail'


class ValidateAccountMove(models.Model):
    force_post = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'validate_account_move'


class WebEditorConverterTest(models.Model):
    char = models.CharField(max_length=200, blank=True, null=True)
    integer = models.IntegerField()
    float = models.FloatField(blank=True, null=True)
    numeric = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    many2one = models.ForeignKey('WebEditorConverterTestSub',    models.DO_NOTHING, related_name="+", db_column='many2one', blank=True, null=True)
    binary = models.BinaryField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)
    selection_str = models.CharField(max_length=200, blank=True, null=True)
    html = models.TextField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'web_editor_converter_test'


class WebEditorConverterTestSub(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'web_editor_converter_test_sub'


class WebTourTour(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'web_tour_tour'


class Website(models.Model):
    name = models.CharField(max_length=200)
    domain = models.CharField(max_length=200, blank=True, null=True)
    company = models.ForeignKey(ResCompany,    models.DO_NOTHING, related_name="+")
    default_lang = models.ForeignKey(ResLang,    models.DO_NOTHING, related_name="+")
    auto_redirect_lang = models.BooleanField(blank=True, null=True)
    cookies_bar = models.BooleanField(blank=True, null=True)
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    social_facebook = models.CharField(max_length=200, blank=True, null=True)
    social_github = models.CharField(max_length=200, blank=True, null=True)
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)
    social_youtube = models.CharField(max_length=200, blank=True, null=True)
    social_instagram = models.CharField(max_length=200, blank=True, null=True)
    has_social_default_image = models.BooleanField(blank=True, null=True)
    google_analytics_key = models.CharField(max_length=200, blank=True, null=True)
    google_management_client_id = models.CharField(max_length=200, blank=True, null=True)
    google_management_client_secret = models.CharField(max_length=200, blank=True, null=True)
    google_search_console = models.CharField(max_length=200, blank=True, null=True)
    google_maps_api_key = models.CharField(max_length=200, blank=True, null=True)
    user = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+")
    cdn_activated = models.BooleanField(blank=True, null=True)
    cdn_url = models.CharField(max_length=200, blank=True, null=True)
    cdn_filters = models.TextField(blank=True, null=True)
    homepage = models.ForeignKey('WebsitePage',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    custom_code_head = models.TextField(blank=True, null=True)
    custom_code_footer = models.TextField(blank=True, null=True)
    robots_txt = models.TextField(blank=True, null=True)
    theme = models.ForeignKey(IrModuleModule,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    specific_user_account = models.BooleanField(blank=True, null=True)
    auth_signup_uninvited = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    crm_default_team = models.ForeignKey(CrmTeam,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    crm_default_user = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    salesperson = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    salesteam = models.ForeignKey(CrmTeam,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    cart_recovery_mail_template = models.ForeignKey(MailTemplate,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    cart_abandoned_delay = models.FloatField(blank=True, null=True)
    shop_ppg = models.IntegerField()
    shop_ppr = models.IntegerField()
    warehouse = models.ForeignKey(StockWarehouse,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    karma_profile_min = models.IntegerField()
    website_slide_google_app_key = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'website'


class WebsiteCountryGroupRel(models.Model):
    website = models.OneToOneField(Website,    models.DO_NOTHING, related_name="+", primary_key=True)
    country_group = models.ForeignKey(ResCountryGroup,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'website_country_group_rel'
        unique_together = (('website', 'country_group'),)


class WebsiteLangRel(models.Model):
    website = models.OneToOneField(Website,    models.DO_NOTHING, related_name="+", primary_key=True)
    lang = models.ForeignKey(ResLang,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'website_lang_rel'
        unique_together = (('website', 'lang'),)


class WebsiteMenu(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200, blank=True, null=True)
    page = models.ForeignKey('WebsitePage',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    new_window = models.BooleanField(blank=True, null=True)
    sequence = models.IntegerField()
    website = models.ForeignKey(Website,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    parent = models.ForeignKey('self',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    parent_path = models.CharField(max_length=200, blank=True, null=True)
    mega_menu_content = models.TextField(blank=True, null=True)
    mega_menu_classes = models.CharField(max_length=200, blank=True, null=True)
    theme_template = models.ForeignKey(ThemeWebsiteMenu,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'website_menu'


class WebsitePage(models.Model):
    url = models.CharField(max_length=200, blank=True, null=True)
    view = models.ForeignKey(IrUiView,    models.DO_NOTHING, related_name="+")
    website_indexed = models.BooleanField(blank=True, null=True)
    date_publish = models.DateTimeField(blank=True, null=True)
    cache_time = models.IntegerField()
    cache_key_expr = models.CharField(max_length=200, blank=True, null=True)
    header_overlay = models.BooleanField(blank=True, null=True)
    header_color = models.CharField(max_length=200, blank=True, null=True)
    header_visible = models.BooleanField(blank=True, null=True)
    footer_visible = models.BooleanField(blank=True, null=True)
    website = models.ForeignKey(Website,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    theme_template = models.ForeignKey(ThemeWebsitePage,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    is_published = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'website_page'


class WebsiteRewrite(models.Model):
    name = models.CharField(max_length=200)
    website = models.ForeignKey(Website,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    url_from = models.CharField(max_length=200, blank=True, null=True)
    route = models.ForeignKey('WebsiteRoute',    models.DO_NOTHING, related_name="+", blank=True, null=True)
    url_to = models.CharField(max_length=200, blank=True, null=True)
    redirect_type = models.CharField(max_length=200, blank=True, null=True)
    sequence = models.IntegerField()
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'website_rewrite'


class WebsiteRobots(models.Model):
    content = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'website_robots'


class WebsiteRoute(models.Model):
    path = models.CharField(max_length=200, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'website_route'


class WebsiteSaleExtraField(models.Model):
    website = models.ForeignKey(Website,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    sequence = models.IntegerField()
    field = models.ForeignKey(IrModelFields,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'website_sale_extra_field'


class WebsiteSalePaymentAcquirerOnboardingWizard(models.Model):
    payment_method = models.CharField(max_length=200, blank=True, null=True)
    paypal_user_type = models.CharField(max_length=200, blank=True, null=True)
    paypal_email_account = models.CharField(max_length=200, blank=True, null=True)
    paypal_seller_account = models.CharField(max_length=200, blank=True, null=True)
    paypal_pdt_token = models.CharField(max_length=200, blank=True, null=True)
    stripe_secret_key = models.CharField(max_length=200, blank=True, null=True)
    stripe_publishable_key = models.CharField(max_length=200, blank=True, null=True)
    manual_name = models.CharField(max_length=200, blank=True, null=True)
    journal_name = models.CharField(max_length=200, blank=True, null=True)
    acc_number = models.CharField(max_length=200, blank=True, null=True)
    manual_post_msg = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'website_sale_payment_acquirer_onboarding_wizard'


class WebsiteSnippetFilter(models.Model):
    name = models.CharField(max_length=200)
    action_server = models.ForeignKey(IrActServer,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    field_names = models.CharField(max_length=200)
    filter = models.ForeignKey(IrFilters,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    limit = models.IntegerField()
    website = models.ForeignKey(Website,    models.DO_NOTHING, related_name="+")
    is_published = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'website_snippet_filter'


class WebsiteTrack(models.Model):
    visitor = models.ForeignKey('WebsiteVisitor',    models.DO_NOTHING, related_name="+")
    page = models.ForeignKey(WebsitePage,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    visit_datetime = models.DateTimeField()
    product = models.ForeignKey(ProductProduct,    models.DO_NOTHING, related_name="+", blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'website_track'


class WebsiteVisitor(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    access_token = models.CharField(unique=True, max_length=200)
    active = models.BooleanField(blank=True, null=True)
    website = models.ForeignKey(Website,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    partner = models.OneToOneField(ResPartner,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    country = models.ForeignKey(ResCountry,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    lang = models.ForeignKey(ResLang,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    timezone = models.CharField(max_length=200, blank=True, null=True)
    visit_count = models.IntegerField()
    create_date = models.DateTimeField(blank=True, null=True)
    last_connection_datetime = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'website_visitor'


class WhatsappMessageWizard(models.Model):
    user = models.ForeignKey(ResPartner,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    message = models.TextField()
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'whatsapp_message_wizard'


class WizardIrModelMenuCreate(models.Model):
    menu = models.ForeignKey(IrUiMenu,    models.DO_NOTHING, related_name="+")
    name = models.CharField(max_length=200)
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'wizard_ir_model_menu_create'


class X(models.Model):
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'x_'


class XA(models.Model):
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_name = models.CharField(max_length=200, blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_active = models.BooleanField(blank=True, null=True)
    x_studio_sequence = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'x_a'


class XAccountTaxStockPickingRel(models.Model):
    stock_picking = models.OneToOneField(StockPicking,    models.DO_NOTHING, related_name="+", primary_key=True)
    account_tax = models.ForeignKey(AccountTax,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'x_account_tax_stock_picking_rel'
        unique_together = (('stock_picking', 'account_tax'),)


class XAnnex(models.Model):
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_name = models.CharField(max_length=200, blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_active = models.BooleanField(blank=True, null=True)
    x_studio_sequence = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'x_annex'


class XAssessment(models.Model):
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_name = models.CharField(max_length=200, blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_active = models.BooleanField(blank=True, null=True)
    x_studio_sequence = models.IntegerField()
    x_studio_date = models.DateField(blank=True, null=True)
    x_studio_tags = models.CharField(max_length=200, blank=True, null=True)
    x_studio_company = models.CharField(max_length=200, blank=True, null=True)
    x_studio_comments = models.CharField(max_length=200, blank=True, null=True)
    x_studio_comments_1 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_unsatisfactory_10_to_15 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_marginal_16_to_25 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_good_26_to_35 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_very_good_36_to_45 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_excellent_46_to_50 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_comments_2 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_appraisees_name = models.CharField(max_length=200, blank=True, null=True)
    x_studio_appraisees_name_1 = models.ForeignKey(HrEmployee,    models.DO_NOTHING, related_name="+", db_column='x_studio_appraisees_name_1', blank=True, null=True)
    x_studio_appraisers_name = models.ForeignKey(HrEmployee,    models.DO_NOTHING, related_name="+", db_column='x_studio_appraisers_name', blank=True, null=True)
    x_studio_date_1 = models.DateField(blank=True, null=True)
    x_studio_date_2 = models.DateField(blank=True, null=True)
    x_studio_char_field_cuak6 = models.CharField(db_column='x_studio_char_field_CUAk6', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_text_field_n2iph = models.TextField(db_column='x_studio_text_field_n2IpH', blank=True, null=True)  # Field name made lowercase.
    x_studio_char_field_gxd1k = models.CharField(db_column='x_studio_char_field_GxD1k', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_text_field_rg5f5 = models.TextField(db_column='x_studio_text_field_RG5F5', blank=True, null=True)  # Field name made lowercase.
    x_studio_char_field_7iibn = models.CharField(db_column='x_studio_char_field_7Iibn', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_text_field_e4wnf = models.TextField(db_column='x_studio_text_field_e4wnF', blank=True, null=True)  # Field name made lowercase.
    x_studio_char_field_rs3iz = models.CharField(db_column='x_studio_char_field_RS3IZ', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_comments_discussion = models.CharField(max_length=200, blank=True, null=True)
    x_studio_appraisers_comments = models.CharField(max_length=200, blank=True, null=True)
    x_studio_name_of_appraiser = models.CharField(max_length=200, blank=True, null=True)
    x_studio_name_of_appraiser_1 = models.ForeignKey(HrEmployee,    models.DO_NOTHING, related_name="+", db_column='x_studio_name_of_appraiser_1', blank=True, null=True)
    x_studio_date_3 = models.DateField(blank=True, null=True)
    x_studio_job_position = models.CharField(max_length=200, blank=True, null=True)
    x_studio_comment = models.CharField(max_length=200, blank=True, null=True)
    x_studio_name_appraisee = models.ForeignKey(HrEmployee,    models.DO_NOTHING, related_name="+", db_column='x_studio_name_appraisee', blank=True, null=True)
    x_studio_date_4 = models.DateField(blank=True, null=True)
    x_studio_comments_3 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_name_of_officer = models.ForeignKey(HrEmployee,    models.DO_NOTHING, related_name="+", db_column='x_studio_name_of_officer', blank=True, null=True)
    x_studio_date_5 = models.DateField(blank=True, null=True)
    x_studio_job_position_1 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_char_field_a4fox = models.CharField(db_column='x_studio_char_field_A4FOx', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_notes = models.TextField(blank=True, null=True)
    x_studio_total_max_10 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_unsatisfactory_10_to_3_field = models.CharField(db_column='x_studio_unsatisfactory_10_to_3_', max_length=200, blank=True, null=True)  # Field renamed because it ended with '_'.
    x_studio_marginal_31_to_50 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_good_51_to_70_field = models.CharField(db_column='x_studio_good_51_to_70_', max_length=200, blank=True, null=True)  # Field renamed because it ended with '_'.
    x_studio_very_good_71_to_90 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_excellent_91_to_100 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_char_field_dxd2i = models.CharField(db_column='x_studio_char_field_dxD2i', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_remarkscomments = models.CharField(max_length=200, blank=True, null=True)
    x_studio_char_field_cs9k0 = models.CharField(db_column='x_studio_char_field_CS9K0', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_appraisee_name = models.ForeignKey(HrEmployee,    models.DO_NOTHING, related_name="+", db_column='x_studio_appraisee_name', blank=True, null=True)
    x_studio_appraisers_name_1 = models.ForeignKey(HrEmployee,    models.DO_NOTHING, related_name="+", db_column='x_studio_appraisers_name_1', blank=True, null=True)
    x_studio_date_6 = models.DateField(blank=True, null=True)
    x_studio_date_8 = models.DateField(blank=True, null=True)
    x_studio_comments_4 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_name_of_officer_1 = models.ForeignKey(HrEmployee,    models.DO_NOTHING, related_name="+", db_column='x_studio_name_of_officer_1', blank=True, null=True)
    x_studio_date_7 = models.DateField(blank=True, null=True)
    x_studio_job_position_2 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_char_field_siofk = models.CharField(db_column='x_studio_char_field_SIoFk', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_notes_2 = models.TextField(blank=True, null=True)
    x_studio_char_field_opsgj = models.CharField(db_column='x_studio_char_field_OpSGJ', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_field = models.ForeignKey(HrEmployee,    models.DO_NOTHING, related_name="+", db_column='x_studio_', blank=True, null=True)  # Field renamed because it ended with '_'.
    x_studio_many2one_field_a7knd = models.ForeignKey(HrEmployee,    models.DO_NOTHING, related_name="+", db_column='x_studio_many2one_field_a7kNd', blank=True, null=True)  # Field name made lowercase.
    x_studio_many2one_field_ppxhr = models.ForeignKey(HrDepartment,    models.DO_NOTHING, related_name="+", db_column='x_studio_many2one_field_ppXHr', blank=True, null=True)  # Field name made lowercase.
    x_studio_many2one_field_ubrsp = models.ForeignKey(X,    models.DO_NOTHING, related_name="+", db_column='x_studio_many2one_field_UbRSP', blank=True, null=True)  # Field name made lowercase.
    x_studio_char_field_pzdgx = models.CharField(db_column='x_studio_char_field_pzDgX', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_period_of_assessment_to = models.DateField(blank=True, null=True)
    x_studio_average_performance = models.FloatField(blank=True, null=True)
    x_studio_score = models.FloatField(blank=True, null=True)
    x_studio_score_1 = models.FloatField(blank=True, null=True)
    x_studio_total = models.FloatField(blank=True, null=True)
    x_studio_total_score_for_assessment_of_performance = models.FloatField(blank=True, null=True)
    x_studio_comments_discussion_1 = models.TextField(blank=True, null=True)
    x_studio_comments_5 = models.TextField(blank=True, null=True)
    x_studio_many2one_field_vdiyo = models.ForeignKey(HrJob,    models.DO_NOTHING, related_name="+", db_column='x_studio_many2one_field_VDiYo', blank=True, null=True)  # Field name made lowercase.
    x_studio_many2one_field_v8itn = models.ForeignKey(HrJob,    models.DO_NOTHING, related_name="+", db_column='x_studio_many2one_field_V8iTn', blank=True, null=True)  # Field name made lowercase.
    x_studio_comments_6 = models.TextField(blank=True, null=True)
    x_studio_comments_7 = models.TextField(blank=True, null=True)
    x_studio_many2one_field_ehqfb = models.ForeignKey(HrJob,    models.DO_NOTHING, related_name="+", db_column='x_studio_many2one_field_EHqfB', blank=True, null=True)  # Field name made lowercase.
    x_studio_many2one_field_rkwqr = models.ForeignKey(HrJob,    models.DO_NOTHING, related_name="+", db_column='x_studio_many2one_field_rkWqr', blank=True, null=True)  # Field name made lowercase.
    x_studio_assessment_goals_score = models.FloatField(blank=True, null=True)
    x_studio_assessment_ratings_score = models.FloatField(blank=True, null=True)
    x_studio_unsatisfactory = models.CharField(max_length=200, blank=True, null=True)
    x_studio_good_51_to_70 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_marginal_31_to_50_1 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_very_good_71_to_90_1 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_excellent_91_to_100_1 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_comments_8 = models.TextField(blank=True, null=True)
    x_studio_comments_9 = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'x_assessment'


class XAssessmentTags(models.Model):
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_name = models.CharField(max_length=200, blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_active = models.BooleanField(blank=True, null=True)
    x_studio_sequence = models.IntegerField()
    x_color = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'x_assessment_tags'


class XAssessmentTagsTag(models.Model):
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_name = models.CharField(max_length=200)
    x_color = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'x_assessment_tags_tag'


class XAssessmentTagsTagRel(models.Model):
    x_assessment_tags = models.OneToOneField(XAssessmentTags,    models.DO_NOTHING, related_name="+", primary_key=True)
    x_tag = models.ForeignKey(XAssessmentTagsTag,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'x_assessment_tags_tag_rel'
        unique_together = (('x_assessment_tags', 'x_tag'),)


class XAssetCategory(models.Model):
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_name = models.CharField(max_length=200, blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_active = models.BooleanField(blank=True, null=True)
    x_studio_sequence = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'x_asset_category'


class XAssetCategoryTag(models.Model):
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_name = models.CharField(max_length=200)
    x_color = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'x_asset_category_tag'


class XAssetCategoryTagRel(models.Model):
    x_asset_category = models.OneToOneField(XAssetCategory,    models.DO_NOTHING, related_name="+", primary_key=True)
    x_tag = models.ForeignKey(XAssetCategoryTag,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'x_asset_category_tag_rel'
        unique_together = (('x_asset_category', 'x_tag'),)


class XBankBranch(models.Model):
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_name = models.CharField(max_length=200, blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_active = models.BooleanField(blank=True, null=True)
    x_studio_sequence = models.IntegerField()
    x_studio_char_field_7qetk = models.CharField(db_column='x_studio_char_field_7QeTk', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_bank_identifier_code = models.CharField(max_length=200, blank=True, null=True)
    x_studio_bank_identifier_code_1 = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'x_bank_branch'


class XConfiguaration(models.Model):
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_name = models.CharField(max_length=200, blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_active = models.BooleanField(blank=True, null=True)
    x_studio_sequence = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'x_configuaration'


class XCostCentres(models.Model):
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_name = models.CharField(max_length=200, blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_active = models.BooleanField(blank=True, null=True)
    x_studio_sequence = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'x_cost_centres'


class XCostCentresTag(models.Model):
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_name = models.CharField(max_length=200)
    x_color = models.IntegerField()
    x_studio_code = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'x_cost_centres_tag'


class XCostCentresTagRel(models.Model):
    x_cost_centres = models.OneToOneField(XCostCentres,    models.DO_NOTHING, related_name="+", primary_key=True)
    x_tag = models.ForeignKey(XCostCentresTag,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'x_cost_centres_tag_rel'
        unique_together = (('x_cost_centres', 'x_tag'),)


class XDeductionLine(models.Model):
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_name = models.CharField(max_length=200, blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_active = models.BooleanField(blank=True, null=True)
    x_studio_sequence = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'x_deduction_line'


class XDeductionType(models.Model):
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_name = models.CharField(max_length=200, blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_active = models.BooleanField(blank=True, null=True)
    x_studio_sequence = models.IntegerField()
    x_studio_name_of_deduction = models.CharField(max_length=200, blank=True, null=True)
    x_studio_status = models.CharField(max_length=200, blank=True, null=True)
    x_studio_description = models.CharField(max_length=200, blank=True, null=True)
    x_studio_company_name = models.CharField(max_length=200, blank=True, null=True)
    x_studio_company_short_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'x_deduction_type'


class XDeductions(models.Model):
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_name = models.CharField(max_length=200, blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_active = models.BooleanField(blank=True, null=True)
    x_studio_sequence = models.IntegerField()
    x_studio_name_of_deduction = models.CharField(max_length=200, blank=True, null=True)
    x_studio_status = models.CharField(max_length=200, blank=True, null=True)
    x_studio_principal_amount = models.FloatField(blank=True, null=True)
    x_studio_interest_amount = models.FloatField(blank=True, null=True)
    x_studio_number_of_monthly_instalments = models.IntegerField()
    x_studio_initial_balance = models.FloatField(blank=True, null=True)
    x_studio_current_balance = models.FloatField(blank=True, null=True)
    x_studio_start_date = models.DateTimeField(blank=True, null=True)
    x_studio_end_date = models.DateTimeField(blank=True, null=True)
    x_studio_many2one_field_ofpon = models.ForeignKey(XDeductionType,    models.DO_NOTHING, related_name="+", db_column='x_studio_many2one_field_ofpon', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'x_deductions'


class XDepartments(models.Model):
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_name = models.CharField(max_length=200, blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_active = models.BooleanField(blank=True, null=True)
    x_studio_sequence = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'x_departments'


class XDistricts(models.Model):
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_name = models.CharField(max_length=200, blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_active = models.BooleanField(blank=True, null=True)
    x_studio_sequence = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'x_districts'


class XDivision(models.Model):
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_name = models.CharField(max_length=200, blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_active = models.BooleanField(blank=True, null=True)
    x_studio_sequence = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'x_division'


class XEqStaffMovement(models.Model):
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_name = models.CharField(max_length=200, blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_active = models.BooleanField(blank=True, null=True)
    x_studio_partner = models.ForeignKey(ResPartner,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_studio_partner_phone = models.CharField(max_length=200, blank=True, null=True)
    x_studio_partner_email = models.CharField(max_length=200, blank=True, null=True)
    x_studio_notes = models.TextField(blank=True, null=True)
    x_studio_sequence = models.IntegerField()
    x_studio_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'x_eq_staff_movement'


class XHrEmployeeIrAttachmentRel(models.Model):
    hr_employee = models.OneToOneField(HrEmployee,    models.DO_NOTHING, related_name="+", primary_key=True)
    ir_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'x_hr_employee_ir_attachment_rel'
        unique_together = (('hr_employee', 'ir_attachment'),)


class XHrEmployeeIrAttachmentRel1(models.Model):
    hr_employee = models.OneToOneField(HrEmployee,    models.DO_NOTHING, related_name="+", primary_key=True)
    ir_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'x_hr_employee_ir_attachment_rel_1'
        unique_together = (('hr_employee', 'ir_attachment'),)


class XHrEmployeeIrAttachmentRel2(models.Model):
    hr_employee = models.OneToOneField(HrEmployee,    models.DO_NOTHING, related_name="+", primary_key=True)
    ir_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'x_hr_employee_ir_attachment_rel_2'
        unique_together = (('hr_employee', 'ir_attachment'),)


class XHrEmployeeIrAttachmentRel3(models.Model):
    hr_employee = models.OneToOneField(HrEmployee,    models.DO_NOTHING, related_name="+", primary_key=True)
    ir_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'x_hr_employee_ir_attachment_rel_3'
        unique_together = (('hr_employee', 'ir_attachment'),)


class XHrEmployeeIrAttachmentRel4(models.Model):
    hr_employee = models.OneToOneField(HrEmployee,    models.DO_NOTHING, related_name="+", primary_key=True)
    ir_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'x_hr_employee_ir_attachment_rel_4'
        unique_together = (('hr_employee', 'ir_attachment'),)


class XHrEmployeeXProfessionalCertifiRel(models.Model):
    hr_employee = models.OneToOneField(HrEmployee,    models.DO_NOTHING, related_name="+", primary_key=True)
    x_professional_certifi = models.ForeignKey('XProfessionalCertifi',    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'x_hr_employee_x_professional_certifi_rel'
        unique_together = (('hr_employee', 'x_professional_certifi'),)


class XHrEmployeeXStaffMovementRel(models.Model):
    x_staff_movement = models.OneToOneField('XStaffMovement',    models.DO_NOTHING, related_name="+", primary_key=True)
    hr_employee = models.ForeignKey(HrEmployee,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'x_hr_employee_x_staff_movement_rel'
        unique_together = (('x_staff_movement', 'hr_employee'),)


class XInstitution(models.Model):
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'x_institution'


class XInstitutions(models.Model):
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_name = models.CharField(max_length=200, blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_active = models.BooleanField(blank=True, null=True)
    x_studio_sequence = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'x_institutions'


class XLEMovement(models.Model):
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_name = models.CharField(max_length=200, blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_active = models.BooleanField(blank=True, null=True)
    x_studio_user = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_studio_partner = models.ForeignKey(ResPartner,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_studio_partner_phone = models.CharField(max_length=200, blank=True, null=True)
    x_studio_partner_email = models.CharField(max_length=200, blank=True, null=True)
    x_studio_sequence = models.IntegerField()
    x_studio_stage = models.ForeignKey('XLEMovementStage',    models.DO_NOTHING, related_name="+")
    x_studio_priority = models.BooleanField(blank=True, null=True)
    x_studio_kanban_state = models.CharField(max_length=200, blank=True, null=True)
    x_studio_date = models.DateField(blank=True, null=True)
    x_studio_tags = models.ForeignKey('XLaboratoryEquipmentTag',    models.DO_NOTHING, related_name="+", db_column='x_studio_tags', blank=True, null=True)
    x_studio_char_field_naigh = models.CharField(db_column='x_studio_char_field_NAiGh', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_date_returned = models.DateField(blank=True, null=True)
    x_studio_purpose_of_collecting_the_items = models.CharField(max_length=200, blank=True, null=True)
    x_studio_location_assigned = models.CharField(max_length=200, blank=True, null=True)
    x_studio_condition_of_equipments = models.TextField(blank=True, null=True)
    x_studio_head_of_department = models.ForeignKey(ResPartner,    models.DO_NOTHING, related_name="+", db_column='x_studio_head_of_department', blank=True, null=True)
    x_studio_char_field_gv5h3 = models.CharField(db_column='x_studio_char_field_Gv5h3', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_char_field_wiz9u = models.CharField(db_column='x_studio_char_field_WIz9U', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_char_field_f5woi = models.CharField(db_column='x_studio_char_field_F5woi', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_street = models.CharField(max_length=200, blank=True, null=True)
    x_studio_purpose_of_taken_equipments = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'x_l_e_movement'


class XLEMovementStage(models.Model):
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_name = models.CharField(max_length=200)
    x_studio_sequence = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'x_l_e_movement_stage'


class XLaboratoryEnvironme(models.Model):
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_name = models.CharField(max_length=200, blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_active = models.BooleanField(blank=True, null=True)
    x_studio_user = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_studio_partner = models.ForeignKey(ResPartner,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_studio_partner_phone = models.CharField(max_length=200, blank=True, null=True)
    x_studio_partner_email = models.CharField(max_length=200, blank=True, null=True)
    x_studio_notes = models.TextField(blank=True, null=True)
    x_studio_sequence = models.IntegerField()
    x_studio_stage = models.ForeignKey('XLaboratoryEnvironmeStage',    models.DO_NOTHING, related_name="+")
    x_studio_priority = models.BooleanField(blank=True, null=True)
    x_studio_kanban_state = models.CharField(max_length=200, blank=True, null=True)
    x_studio_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'x_laboratory_environme'


class XLaboratoryEnvironmeStage(models.Model):
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_name = models.CharField(max_length=200)
    x_studio_sequence = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'x_laboratory_environme_stage'


class XLaboratoryEnvironmeTag(models.Model):
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_name = models.CharField(max_length=200)
    x_color = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'x_laboratory_environme_tag'


class XLaboratoryEnvironmeTagRel(models.Model):
    x_laboratory_environme = models.OneToOneField(XLaboratoryEnvironme,    models.DO_NOTHING, related_name="+", primary_key=True)
    x_tag = models.ForeignKey(XLaboratoryEnvironmeTag,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'x_laboratory_environme_tag_rel'
        unique_together = (('x_laboratory_environme', 'x_tag'),)


class XLaboratoryEquipment(models.Model):
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_name = models.CharField(max_length=200, blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_active = models.BooleanField(blank=True, null=True)
    x_studio_user = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_studio_notes = models.TextField(blank=True, null=True)
    x_studio_sequence = models.IntegerField()
    x_studio_stage = models.ForeignKey('XLaboratoryEquipmentStage',    models.DO_NOTHING, related_name="+")
    x_studio_priority = models.BooleanField(blank=True, null=True)
    x_studio_kanban_state = models.CharField(max_length=200, blank=True, null=True)
    x_studio_date = models.DateField(blank=True, null=True)
    x_studio_eq_officer = models.ForeignKey(HrEmployee,    models.DO_NOTHING, related_name="+", db_column='x_studio_eq_officer', blank=True, null=True)
    x_studio_date_returned = models.DateField(blank=True, null=True)
    x_studio_purpose_of_movement = models.CharField(max_length=200, blank=True, null=True)
    x_studio_location = models.CharField(max_length=200, blank=True, null=True)
    x_studio_head_of_department = models.ForeignKey(ResPartner,    models.DO_NOTHING, related_name="+", db_column='x_studio_head_of_department', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'x_laboratory_equipment'


class XLaboratoryEquipmentStage(models.Model):
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_name = models.CharField(max_length=200)
    x_studio_sequence = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'x_laboratory_equipment_stage'


class XLaboratoryEquipmentTag(models.Model):
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_name = models.CharField(max_length=200)
    x_color = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'x_laboratory_equipment_tag'


class XLaboratoryEquipmentTagRel(models.Model):
    x_laboratory_equipment = models.OneToOneField(XLaboratoryEquipment,    models.DO_NOTHING, related_name="+", primary_key=True)
    x_tag = models.ForeignKey(XLaboratoryEquipmentTag,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'x_laboratory_equipment_tag_rel'
        unique_together = (('x_laboratory_equipment', 'x_tag'),)


class XLevels(models.Model):
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_name = models.CharField(max_length=200, blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_active = models.BooleanField(blank=True, null=True)
    x_studio_sequence = models.IntegerField()
    x_studio_step_1 = models.FloatField(blank=True, null=True)
    x_studio_step_2 = models.FloatField(blank=True, null=True)
    x_studio_step_3 = models.FloatField(blank=True, null=True)
    x_studio_step_4 = models.FloatField(blank=True, null=True)
    x_studio_step_5 = models.FloatField(blank=True, null=True)
    x_studio_step_6 = models.FloatField(blank=True, null=True)
    x_studio_step_7 = models.FloatField(blank=True, null=True)
    x_studio_step_8 = models.FloatField(blank=True, null=True)
    x_studio_boolean_field_fn8bs = models.BooleanField(db_column='x_studio_boolean_field_fN8bS', blank=True, null=True)  # Field name made lowercase.
    x_studio_step_9 = models.FloatField(blank=True, null=True)
    x_studio_step_10 = models.FloatField(blank=True, null=True)
    x_studio_step_11 = models.FloatField(blank=True, null=True)
    x_studio_text_trial = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'x_levels'


class XLevelsAndSteps(models.Model):
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_name = models.CharField(max_length=200, blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_active = models.BooleanField(blank=True, null=True)
    x_studio_sequence = models.IntegerField()
    x_studio_step_1 = models.FloatField(blank=True, null=True)
    x_studio_step_2 = models.FloatField(blank=True, null=True)
    x_studio_step_3 = models.FloatField(blank=True, null=True)
    x_studio_step_4 = models.FloatField(blank=True, null=True)
    x_studio_step_5 = models.FloatField(blank=True, null=True)
    x_studio_step_6 = models.FloatField(blank=True, null=True)
    x_studio_step_7 = models.FloatField(blank=True, null=True)
    x_studio_step_8 = models.FloatField(blank=True, null=True)
    x_studio_step_9 = models.FloatField(blank=True, null=True)
    x_studio_step_10 = models.FloatField(blank=True, null=True)
    x_studio_step_11 = models.FloatField(blank=True, null=True)
    x_studio_step_1_1 = models.FloatField(blank=True, null=True)
    x_studio_step_2_1 = models.FloatField(blank=True, null=True)
    x_studio_step_3_1 = models.FloatField(blank=True, null=True)
    x_studio_step_4_1 = models.FloatField(blank=True, null=True)
    x_studio_step_5_1 = models.FloatField(blank=True, null=True)
    x_studio_step_6_1 = models.FloatField(blank=True, null=True)
    x_studio_step_7_1 = models.FloatField(blank=True, null=True)
    x_studio_step_8_1 = models.FloatField(blank=True, null=True)
    x_studio_step_9_1 = models.FloatField(blank=True, null=True)
    x_studio_step_10_1 = models.FloatField(blank=True, null=True)
    x_studio_step_11_1 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'x_levels_and_steps'


class XMainBank(models.Model):
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_name = models.CharField(max_length=200, blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_active = models.BooleanField(blank=True, null=True)
    x_studio_sequence = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'x_main_bank'


class XMaintenanceEquipmentXLEMovementRel(models.Model):
    x_l_e_movement = models.OneToOneField(XLEMovement,    models.DO_NOTHING, related_name="+", primary_key=True)
    maintenance_equipment = models.ForeignKey(MaintenanceEquipment,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'x_maintenance_equipment_x_l_e_movement_rel'
        unique_together = (('x_l_e_movement', 'maintenance_equipment'),)


class XMaintenanceEquipmentXLEMovementRel1(models.Model):
    x_l_e_movement = models.OneToOneField(XLEMovement,    models.DO_NOTHING, related_name="+", primary_key=True)
    maintenance_equipment = models.ForeignKey(MaintenanceEquipment,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'x_maintenance_equipment_x_l_e_movement_rel_1'
        unique_together = (('x_l_e_movement', 'maintenance_equipment'),)


class XMaintenanceEquipmentXStaffMovementRel(models.Model):
    x_staff_movement = models.OneToOneField('XStaffMovement',    models.DO_NOTHING, related_name="+", primary_key=True)
    maintenance_equipment = models.ForeignKey(MaintenanceEquipment,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'x_maintenance_equipment_x_staff_movement_rel'
        unique_together = (('x_staff_movement', 'maintenance_equipment'),)


class XOrganogram(models.Model):
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_name = models.CharField(max_length=200, blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_active = models.BooleanField(blank=True, null=True)
    x_studio_sequence = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'x_organogram'


class XPayrollConstants(models.Model):
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_name = models.CharField(max_length=200, blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_active = models.BooleanField(blank=True, null=True)
    x_studio_sequence = models.IntegerField()
    x_studio_junior_staff = models.FloatField(blank=True, null=True)
    x_studio_senior_staff = models.FloatField(blank=True, null=True)
    x_studio_executive_staff = models.FloatField(blank=True, null=True)
    x_studio_executive_staff_1 = models.FloatField(blank=True, null=True)
    x_studio_garden_boy = models.FloatField(blank=True, null=True)
    x_studio_domestic = models.FloatField(blank=True, null=True)
    x_studio_security = models.FloatField(blank=True, null=True)
    x_studio_staff_with_vehicles = models.FloatField(blank=True, null=True)
    x_studio_staff_without_vehicles = models.FloatField(blank=True, null=True)
    x_studio_conversion_rate = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'x_payroll_constants'


class XProfessionalCertifi(models.Model):
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'x_professional_certifi'


class XProgramme(models.Model):
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'x_programme'


class XProgrammes(models.Model):
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_name = models.CharField(max_length=200, blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_active = models.BooleanField(blank=True, null=True)
    x_studio_sequence = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'x_programmes'


class XRatings(models.Model):
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_name = models.CharField(max_length=200, blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_active = models.BooleanField(blank=True, null=True)
    x_studio_sequence = models.IntegerField()
    x_studio_unsatisfactory = models.BooleanField(blank=True, null=True)
    x_studio_poor = models.BooleanField(blank=True, null=True)
    x_studio_satisfactory = models.BooleanField(blank=True, null=True)
    x_studio_very_good = models.BooleanField(blank=True, null=True)
    x_studio_excellent = models.BooleanField(blank=True, null=True)
    x_studio_unsatisfactory_1 = models.BooleanField(blank=True, null=True)
    x_studio_poor_1 = models.BooleanField(blank=True, null=True)
    x_studio_satisfactory_1 = models.BooleanField(blank=True, null=True)
    x_studio_very_good_1 = models.BooleanField(blank=True, null=True)
    x_studio_excellent_1 = models.BooleanField(blank=True, null=True)
    x_studio_unsatisfactory_2 = models.BooleanField(blank=True, null=True)
    x_studio_poor_2 = models.BooleanField(blank=True, null=True)
    x_studio_satisfactory_2 = models.BooleanField(blank=True, null=True)
    x_studio_very_good_2 = models.BooleanField(blank=True, null=True)
    x_studio_excellent_2 = models.BooleanField(blank=True, null=True)
    x_studio_unsatisfactory_3 = models.BooleanField(blank=True, null=True)
    x_studio_poor_3 = models.BooleanField(blank=True, null=True)
    x_studio_satisfactory_3 = models.BooleanField(blank=True, null=True)
    x_studio_very_good_3 = models.BooleanField(blank=True, null=True)
    x_studio_excellent_3 = models.BooleanField(blank=True, null=True)
    x_studio_unsatisfactory_4 = models.BooleanField(blank=True, null=True)
    x_studio_poor_4 = models.BooleanField(blank=True, null=True)
    x_studio_satisfactory_4 = models.BooleanField(blank=True, null=True)
    x_studio_very_good_4 = models.BooleanField(blank=True, null=True)
    x_studio_excellent_4 = models.BooleanField(blank=True, null=True)
    x_studio_unsatisfactory_5 = models.BooleanField(blank=True, null=True)
    x_studio_poor_5 = models.BooleanField(blank=True, null=True)
    x_studio_satisfactory_5 = models.BooleanField(blank=True, null=True)
    x_studio_very_good_5 = models.BooleanField(blank=True, null=True)
    x_studio_excellent_5 = models.BooleanField(blank=True, null=True)
    x_studio_unsatisfactory_6 = models.BooleanField(blank=True, null=True)
    x_studio_poor_6 = models.BooleanField(blank=True, null=True)
    x_studio_satisfactory_6 = models.BooleanField(blank=True, null=True)
    x_studio_very_good_6 = models.BooleanField(blank=True, null=True)
    x_studio_excellent_6 = models.BooleanField(blank=True, null=True)
    x_studio_unsatisfactory_7 = models.BooleanField(blank=True, null=True)
    x_studio_poor_7 = models.BooleanField(blank=True, null=True)
    x_studio_satisfactory_7 = models.BooleanField(blank=True, null=True)
    x_studio_very_good_7 = models.BooleanField(blank=True, null=True)
    x_studio_excellent_7 = models.BooleanField(blank=True, null=True)
    x_studio_unsatisfactory_8 = models.BooleanField(blank=True, null=True)
    x_studio_poor_8 = models.BooleanField(blank=True, null=True)
    x_studio_satisfactory_8 = models.BooleanField(blank=True, null=True)
    x_studio_very_good_8 = models.BooleanField(blank=True, null=True)
    x_studio_excellent_8 = models.BooleanField(blank=True, null=True)
    x_studio_unsatisfactory_9 = models.BooleanField(blank=True, null=True)
    x_studio_poor_9 = models.BooleanField(blank=True, null=True)
    x_studio_satisfactory_9 = models.BooleanField(blank=True, null=True)
    x_studio_very_good_9 = models.BooleanField(blank=True, null=True)
    x_studio_excellent_9 = models.BooleanField(blank=True, null=True)
    x_studio_many2one_field_1k3vv = models.ForeignKey(HrEmployee,    models.DO_NOTHING, related_name="+", db_column='x_studio_many2one_field_1k3Vv', blank=True, null=True)  # Field name made lowercase.
    x_studio_period_of_ratings_from = models.DateField(blank=True, null=True)
    x_studio_period_of_ratings_to = models.DateField(blank=True, null=True)
    x_studio_ratings = models.CharField(max_length=200, blank=True, null=True)
    x_studio_ratings_1 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_ratings_2 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_ratings_3 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_ratings_4 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_ratings_5 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_ratings_6 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_ratings_7 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_ratings_8 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_ratings_9 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_average_performance = models.FloatField(blank=True, null=True)
    x_studio_comments = models.CharField(max_length=200, blank=True, null=True)
    x_studio_appraisees_name = models.ForeignKey(HrEmployee,    models.DO_NOTHING, related_name="+", db_column='x_studio_appraisees_name', blank=True, null=True)
    x_studio_appraisers_name = models.ForeignKey(HrEmployee,    models.DO_NOTHING, related_name="+", db_column='x_studio_appraisers_name', blank=True, null=True)
    x_studio_date = models.DateField(blank=True, null=True)
    x_studio_date_1 = models.DateField(blank=True, null=True)
    x_studio_comments_1 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_ratings_10 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_ratings_11 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_ratings_12 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_ratings_13 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_ratings_14 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_comments_2 = models.TextField(blank=True, null=True)
    x_studio_appraisees_name_1 = models.ForeignKey(HrEmployee,    models.DO_NOTHING, related_name="+", db_column='x_studio_appraisees_name_1', blank=True, null=True)
    x_studio_appraisers_name_1 = models.ForeignKey(HrEmployee,    models.DO_NOTHING, related_name="+", db_column='x_studio_appraisers_name_1', blank=True, null=True)
    x_studio_date_2 = models.DateField(blank=True, null=True)
    x_studio_date_3 = models.DateField(blank=True, null=True)
    x_studio_char_field_qklu3 = models.CharField(db_column='x_studio_char_field_qKlU3', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_char_field_wdurz = models.CharField(db_column='x_studio_char_field_WDUrZ', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_char_field_vtuhe = models.CharField(db_column='x_studio_char_field_vTUHE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_char_field_pn50z = models.CharField(db_column='x_studio_char_field_Pn50z', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_char_field_eyctv = models.CharField(db_column='x_studio_char_field_EYCTv', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_char_field_nssfw = models.CharField(db_column='x_studio_char_field_NSsfw', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_char_field_bp0aw = models.CharField(db_column='x_studio_char_field_BP0AW', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_excellent_46_to_50 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_very_good_36_to_45 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_good_26_to_35 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_unsatisfactory_10_to_15 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_marginal_16_to_25 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_comments_3 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_comments_4 = models.TextField(blank=True, null=True)
    x_studio_core_competencies = models.CharField(max_length=200, blank=True, null=True)
    x_studio_average_score_for_assessment_of_performance = models.CharField(max_length=200, blank=True, null=True)
    x_studio_unsatisfactory_10_to_15_rat_sum = models.CharField(max_length=200, blank=True, null=True)
    x_studio_marginal_16_to_25_1_rate_sum = models.CharField(max_length=200, blank=True, null=True)
    x_studio_good_26_to_35_1_rate_sum = models.CharField(max_length=200, blank=True, null=True)
    x_studio_very_good_36_to_45_1_rate_sum = models.CharField(max_length=200, blank=True, null=True)
    x_studio_excellent_46_to_50_1_rate_sum = models.CharField(max_length=200, blank=True, null=True)
    x_studio_date_4 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_appraisee_date_rate_sum = models.DateField(blank=True, null=True)
    x_studio_appraiser_date_rate_sum = models.DateField(blank=True, null=True)
    x_studio_remarks_rate_sum = models.CharField(max_length=200, blank=True, null=True)
    x_studio_boolean_field_wulvc = models.BooleanField(db_column='x_studio_boolean_field_wuLvC', blank=True, null=True)  # Field name made lowercase.
    x_studio_rating_job_skills = models.CharField(max_length=200, blank=True, null=True)
    x_studio_ratings_job_skills = models.BooleanField(blank=True, null=True)
    x_studio_ratings_init_create = models.CharField(max_length=200, blank=True, null=True)
    x_studio_ratings_team_work = models.CharField(max_length=200, blank=True, null=True)
    x_studio_ratings_comm = models.CharField(max_length=200, blank=True, null=True)
    x_studio_ratings_qlty_wrk = models.CharField(max_length=200, blank=True, null=True)
    x_studio_ratings_dev_bdgt = models.CharField(max_length=200, blank=True, null=True)
    x_studio_ratings_org_mgt = models.CharField(max_length=200, blank=True, null=True)
    x_studio_ratings_ldrshp = models.CharField(max_length=200, blank=True, null=True)
    x_studio_ratings_attdnc = models.CharField(max_length=200, blank=True, null=True)
    x_studio_ratings_dev_staff = models.CharField(max_length=200, blank=True, null=True)
    x_studio_char_field_aaxgq = models.CharField(db_column='x_studio_char_field_AAXGq', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_technical_skills = models.CharField(max_length=200, blank=True, null=True)
    x_studio_initiative_and_creativity = models.CharField(max_length=200, blank=True, null=True)
    x_studio_team_work = models.CharField(max_length=200, blank=True, null=True)
    x_studio_communication = models.CharField(max_length=200, blank=True, null=True)
    x_studio_char_field_9dyvt = models.CharField(db_column='x_studio_char_field_9dyVT', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_quality_of_work = models.CharField(max_length=200, blank=True, null=True)
    x_studio_developing_budgets = models.CharField(max_length=200, blank=True, null=True)
    x_studio_organization = models.CharField(max_length=200, blank=True, null=True)
    x_studio_decision_making = models.CharField(max_length=200, blank=True, null=True)
    x_studio_attendance = models.CharField(max_length=200, blank=True, null=True)
    x_studio_develop_staff = models.CharField(max_length=200, blank=True, null=True)
    x_studio_char_field_7y5kz = models.CharField(db_column='x_studio_char_field_7Y5kz', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_char_field_vu6ex = models.CharField(db_column='x_studio_char_field_VU6ex', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_to_which_required_skills_are_mastered = models.CharField(max_length=200, blank=True, null=True)
    x_studio_refer_to_agencys_policies_and_documents = models.CharField(max_length=200, blank=True, null=True)
    x_studio_refer_to_agencys_policies_and_documents_1 = models.CharField(max_length=200, blank=True, null=True)
    x_studio_char_field_i3yzi = models.CharField(db_column='x_studio_char_field_I3Yzi', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_and_to_manage_others_to_achieve_shared_goals = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'x_ratings'


class XRegions(models.Model):
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_name = models.CharField(max_length=200, blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_active = models.BooleanField(blank=True, null=True)
    x_studio_sequence = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'x_regions'


class XResPartnerXStaffMovementRel(models.Model):
    x_staff_movement = models.OneToOneField('XStaffMovement',    models.DO_NOTHING, related_name="+", primary_key=True)
    res_partner = models.ForeignKey(ResPartner,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'x_res_partner_x_staff_movement_rel'
        unique_together = (('x_staff_movement', 'res_partner'),)


class XStaffMovement(models.Model):
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_name = models.CharField(max_length=200, blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_active = models.BooleanField(blank=True, null=True)
    x_studio_partner = models.ForeignKey(ResPartner,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_studio_partner_phone = models.CharField(max_length=200, blank=True, null=True)
    x_studio_partner_email = models.CharField(max_length=200, blank=True, null=True)
    x_studio_sequence = models.IntegerField()
    x_studio_date = models.DateField(blank=True, null=True)
    x_studio_location = models.CharField(max_length=200, blank=True, null=True)
    x_studio_purpose_of_movement = models.CharField(max_length=200, blank=True, null=True)
    x_studio_company_visited = models.CharField(max_length=200, blank=True, null=True)
    x_studio_head_of_department = models.ForeignKey(ResPartner,    models.DO_NOTHING, related_name="+", db_column='x_studio_head_of_department', blank=True, null=True)
    x_priority = models.CharField(max_length=200, blank=True, null=True)
    x_studio_date_to = models.DateField(blank=True, null=True)
    x_studio_date_taken = models.DateField(blank=True, null=True)
    x_studio_date_returned = models.DateField(blank=True, null=True)
    x_studio_purpose_of_taken_equipment = models.TextField(blank=True, null=True)
    x_studio_condition_of_equipment = models.TextField(blank=True, null=True)
    x_studio_selection_field_8ymig = models.CharField(db_column='x_studio_selection_field_8ymiG', max_length=200, blank=True, null=True)  # Field name made lowercase.
    x_studio_return_condition = models.TextField(blank=True, null=True)
    x_studio_return_approved_by = models.ForeignKey(HrEmployee,    models.DO_NOTHING, related_name="+", db_column='x_studio_return_approved_by', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'x_staff_movement'


class XTags(models.Model):
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'x_tags'


class XUnit(models.Model):
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'x_unit'


class XUnits(models.Model):
    create_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+"   , blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    x_name = models.CharField(max_length=200, blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment,    models.DO_NOTHING, related_name="+", blank=True, null=True)
    x_active = models.BooleanField(blank=True, null=True)
    x_studio_sequence = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'x_units'


class XXAssessmentXAssessmentTagsRel(models.Model):
    x_assessment = models.OneToOneField(XAssessment,    models.DO_NOTHING, related_name="+", primary_key=True)
    x_assessment_tags = models.ForeignKey(XAssessmentTags,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'x_x_assessment_x_assessment_tags_rel'
        unique_together = (('x_assessment', 'x_assessment_tags'),)


class XXAssessmentXAssessmentTagsRel1(models.Model):
    x_assessment = models.OneToOneField(XAssessment,    models.DO_NOTHING, related_name="+", primary_key=True)
    x_assessment_tags = models.ForeignKey(XAssessmentTags,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'x_x_assessment_x_assessment_tags_rel_1'
        unique_together = (('x_assessment', 'x_assessment_tags'),)


class XXAssessmentXAssessmentTagsRel2(models.Model):
    x_assessment = models.OneToOneField(XAssessment,    models.DO_NOTHING, related_name="+", primary_key=True)
    x_assessment_tags = models.ForeignKey(XAssessmentTags,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'x_x_assessment_x_assessment_tags_rel_2'
        unique_together = (('x_assessment', 'x_assessment_tags'),)


class XXAssessmentXTagsRel(models.Model):
    x_assessment = models.OneToOneField(XAssessment,    models.DO_NOTHING, related_name="+", primary_key=True)
    x_tags = models.ForeignKey(XTags,    models.DO_NOTHING, related_name="+")

    class Meta:
        managed = True
        db_table = 'x_x_assessment_x_tags_rel'
        unique_together = (('x_assessment', 'x_tags'),)
