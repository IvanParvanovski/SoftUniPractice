def process_order(order, client,
                  *,
                  suppress_notifications=False,
                  suppress_payment=False,):
    pass


def open_order(order, client):
    pass


def archive_order(order, client):
    pass


order = None
client = None
process_order(order, client,
              suppress_notifications=False,
              suppress_payment=False)

# process_order(order, client, True, True)

