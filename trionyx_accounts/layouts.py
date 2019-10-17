from trionyx.views import tabs
from trionyx.layout import Container, Row, Column6, Panel, DescriptionList, Html
from trionyx.renderer import price_value_renderer

from .models import Account

@tabs.register(Account)
def order_general(obj):
    return Container(
        Row(
            Column6(
                Panel(
                    'General',
                    DescriptionList(
                        'name',
                        'type',
                        'debtor_id',
                        'website',
                        'phone',
                        'email',

                    )
                ),
            ),
            Column6(
                Panel(
                    'Info',
                    DescriptionList(
                        'assigned_user',
                        'description',
                    )
                )
            ),
        ),
        Row(
            Column6(
                Panel(
                    'Billing address',
                    DescriptionList(
                        'street',
                        'postcode',
                        'city',
                        'state',
                        'country',
                        object=obj.billing_address
                    ) if obj.billing_address else Html('<div class="alert alert-info no-margin">No billing address</div>')
                )
            ),
            Column6(
                Panel(
                    'Shipping address',
                    DescriptionList(
                        'street',
                        'postcode',
                        'city',
                        'state',
                        'country',
                        object=obj.shipping_address
                    ) if obj.shipping_address else Html('<div class="alert alert-info no-margin">No shipping address</div>'),
                )
            ),
        )
    )