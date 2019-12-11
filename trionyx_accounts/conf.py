from trionyx.config import AppSettings

settings = AppSettings('ACCOUNTS', {
    'DEBTOR_ID_FORMAT': '{increment_long}',
})