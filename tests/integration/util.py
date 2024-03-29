import io
import json
import os

import blockchyp


def _get_test_config():
    # type: () -> dict

    if os.name == "nt":
        config_home = os.getenv("USERPROFILE")
    else:
        config_home = os.getenv("XDG_CONFIG_HOME")

    if not config_home:
        config_home = os.path.join(os.path.expanduser("~"), ".config")

    config_file = os.path.join(config_home, "blockchyp", "sdk-itest-config.json")

    with io.open(config_file) as f:
        content = json.load(f)

    return content


def _get_test_client(profile):
    # type: () -> blockchyp.Client

    config = _get_test_config()

    client = blockchyp.Client(
        api_key=config["apiKey"],
        bearer_token=config["bearerToken"],
        signing_key=config["signingKey"],
    )

    client.gateway_url = config.get("gatewayHost")
    client.gateway_test_url = config.get("testGatewayHost")
    client.dashboard_url = config.get("dashboardHost")

    if len(profile) > 0:
        profile_config = config["profiles"][profile]
        client.api_key = profile_config["apiKey"]
        client.bearer_token = profile_config["bearerToken"]
        client.signing_key = profile_config["signingKey"]

    return client
