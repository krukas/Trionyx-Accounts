from trionyx import models
from trionyx.data import COUNTRIES


class AccountType(models.BaseModel):
    name = models.CharField(max_length=128)


class Account(models.BaseModel):
    type = models.ForeignKey(AccountType, models.SET_NULL, null=True, blank=True, related_name='accounts')
    assigned_user = models.ForeignKey('trionyx.user', models.SET_NULL, null=True, blank=True, related_name='assigned_accounts')

    name = models.CharField(max_length=255)
    # TODO Make option to auto generate debtor number WorkBundle?
    debtor_id = models.CharField(max_length=64, default='', blank=True)
    website = models.URLField(default='', blank=True)
    phone = models.CharField(max_length=32, default='', blank=True)
    email = models.EmailField(default='', blank=True)
    description = models.TextField(default='', blank=True)

    billing_address = models.ForeignKey('trionyx_accounts.address', models.SET_NULL, null=True, blank=True, related_name='+')
    shipping_address = models.ForeignKey('trionyx_accounts.address', models.SET_NULL, null=True, blank=True, related_name='+')


class Contact(models.BaseModel):
    account = models.ForeignKey(Account, models.CASCADE, related_name='contacts')
    assigned_user = models.ForeignKey('trionyx.user', models.SET_NULL, null=True, blank=True, related_name='assigned_contacts')

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, default='', blank=True)

    email = models.EmailField(default='', blank=True)
    phone = models.CharField(max_length=32, default='', blank=True)
    mobile_phone = models.CharField(max_length=32, default='', blank=True)
    title = models.CharField(max_length=255, default='', blank=True)
    description = models.TextField(default='', blank=True)

    address = models.ForeignKey('trionyx_accounts.address', models.SET_NULL, null=True, blank=True, related_name='+')

    def get_absolute_url(self):
        return self.account.get_absolute_url()


class Address(models.BaseModel):
    account = models.ForeignKey(Account, models.CASCADE, related_name='addresses')

    street = models.CharField(max_length=255, default='', blank=True)
    city = models.CharField(max_length=255, default='', blank=True)
    state = models.CharField(max_length=255, default='', blank=True)
    postcode = models.CharField(max_length=32, default='', blank=True)
    country = models.CharField(max_length=2, choices=COUNTRIES, default='', blank=True)

    def get_absolute_url(self):
        return self.account.get_absolute_url()
