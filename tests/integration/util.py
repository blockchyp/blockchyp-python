import io
import json
import os

import blockchyp


def _get_test_client():
    # type: () -> blockchyp.Client

    if os.name == "nt":
        config_home = os.getenv("USERPROFILE")
    else:
        config_home = os.getenv("XDG_CONFIG_HOME")

    if not config_home:
        config_home = os.path.join(os.path.expanduser("~"), ".config")

    config_file = os.path.join(config_home, "blockchyp", "sdk-itest-config.json")

    with io.open(config_file) as f:
        content = json.load(f)

    client = blockchyp.Client(
        api_key=content["apiKey"],
        bearer_token=content["bearerToken"],
        signing_key=content["signingKey"],
    )

    client.api_url = content.get("gateway", content.get("gatewayHost"))
    client.api_test_url = content.get("testGateway", content.get("testGatewayHost"))

    return client
