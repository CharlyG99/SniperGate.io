import gate_api
from gate_api.exceptions import ApiException

def create_order(api_key, api_secret, coin_symbol, quantity, price, side):
    # Configure APIv4 key authorization
    configuration = gate_api.Configuration(
        host="https://api.gate.io/api/v4",
        key=api_key,
        secret=api_secret
    )

    # Create an instance of the API class
    api_client = gate_api.ApiClient(configuration)
    spot_api = gate_api.SpotApi(api_client)

    order = gate_api.Order(
        currency_pair=f"{coin_symbol}_USDT",  # Assuming trading against USDT
        amount=str(quantity),
        price=str(price),
        side=side,
        type="market",  # Assuming a limit order, you can change it accordingly
        account="spot",  # Assuming spot account, change as needed
        time_in_force="gtc"  # Good till canceled
    )

    try:
        # Create an order
        api_response = spot_api.create_order(order)
        return api_response
    except ApiException as e:
        print("Exception when calling SpotApi->create_order: %s\n" % e)
