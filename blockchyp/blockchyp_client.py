class BlockChypClient:
    def __init__(self, creds):
        self.gateway_host = "https://api.blockchyp.com"
        self.credentials = creds
        self.https = True
        self.route_cache_ttl = 60
        self.default_timeout = 60
        self.route_cache = []
    
    def tokenize (self, public_key, card):
        pass

    def heartbeat(self):
        pass

    def enroll(self, auth_request):
        pass

    def ping(self, terminal):
        pass

    def charge(self, auth_request):
        pass

    def return_validation_error(self, desc):
        pass

    def validate_request(self, request):
        pass

    def validate_currency(self, val):
        pass

    def capture(self, request):
        pass

    def void(self, request):
        pass

    def close_batch(self, request):
        pass

    def gift_activate(self, request):
        pass

    def refund(self, auth_request):
        pass

    def preauth(self, auth_request):
        pass

    def is_terminal_routed(self, request):
        pass

    def __gateway_get(self, path, creds):
        pass

    def __get_gateway_config(self):
        pass

    def __get_terminal_config(self):
        pass

    def __gateway_post(self, path, payload):
        pass

    def __terminal_get(self, terminal, path, creds):
        pass

    def __terminal_post(self, route, path, payload):
        pass

    def __assemble_terminal_url(self, route, path):
        pass

    def __resolve_terminal_route(self, terminal_name):
        pass

class BlockChypCredentials:
    def __init__(self, api_key, bearer_token, signing_key):
        self.api_key = api_key
        self.bearer_token = bearer_token
        self.signing_key = signing_key