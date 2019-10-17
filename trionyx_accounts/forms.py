from trionyx import forms
from trionyx.forms.helper import FormHelper
from trionyx.forms.layout import Layout, Fieldset, Div, InlineForm, HTML

from .models import Account, Address


class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = ['street', 'city', 'postcode', 'country', 'state']


    def save(self, commit=True):
        self.is_valid()
        if not list(filter(None, self.cleaned_data.values())):
            return None
        return super().save(commit)

    def __init__(self, *args, **kwargs):
        """Init user form"""
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'street',
            Div(
                Div(
                    'postcode',
                    css_class='col-md-6'
                ),
                Div(
                    'city',
                    css_class='col-md-6'
                ),
                css_class='row',
            ),
            Div(
                Div(
                    'state',
                    css_class='col-md-6'
                ),
                Div(
                    'country',
                    css_class='col-md-6'
                ),
                css_class='row',
            ),
        )


@forms.register(default_create=True, default_edit=True)
class AccountForm(forms.ModelForm):

    inline_forms = {
        'billing_address': {
            'form': AddressForm,
            'fk_name': 'account',
        },
        'shipping_address': {
            'form': AddressForm,
            'fk_name': 'account',
        }
    }

    class Meta:
        model = Account
        fields = ['type', 'assigned_user', 'name', 'debtor_id', 'website', 'phone', 'email', 'description']

    def __init__(self, *args, **kwargs):
        """Init user form"""
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Fieldset(
                    'General',
                    Div(
                        Div(
                            'name',
                            css_class='col-md-6'
                        ),
                        Div(
                            'website',
                            css_class='col-md-6'
                        ),
                        css_class='row',
                    ),
                    Div(
                        Div(
                            'type',
                            css_class='col-md-6'
                        ),
                        Div(
                            'debtor_id',
                            css_class='col-md-6'
                        ),
                        css_class='row',
                    ),
                    Div(
                        Div(
                            'phone',
                            css_class='col-md-6'
                        ),
                        Div(
                            'email',
                            css_class='col-md-6'
                        ),
                        css_class='row',
                    ),
                    css_class='col-md-6',
                ),
                Fieldset(
                    'Info',
                    'assigned_user',
                    'description',
                    css_class='col-md-6',
                ),
            ),
            Div(
                Fieldset(
                    'Billing addess',
                    InlineForm('billing_address'),
                    css_class='col-md-6'
                ),
                Fieldset(
                    'shipping address',
                    InlineForm('shipping_address'),
                    css_class='col-md-6'
                ),
                css_class='row'
            ),
        )