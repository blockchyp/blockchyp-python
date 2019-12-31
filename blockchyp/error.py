import json


class BlockChypError(Exception):
    """Thrown when a request fails and a more specific exception type
    has not been thrown."""

    def __init__(self, message=None, http_body=None, http_status=None):
        self._message = message
        if not self._message:
            self._message = self._try_get_message(http_body, http_status)

        super().__init__(self._message)

        self.http_body = http_body
        self.http_status = http_status

    def __repr__(self):
        return "{}(message={}, http_status={})".format(
            self.__class__.__name__,
            self._message,
            self.http_status,
        )

    @staticmethod
    def _try_get_message(http_body, http_status):
        msg = None
        if http_status:
            msg = f"Status: {http_status}"

        if not http_body:
            return msg

        try:
            fields = json.loads(http_body)
        except json.decoder.JSONDecodeError:
            return msg

        try:
            return fields["error"]
        except KeyError:
            pass

        try:
            return fields["responseDescription"]
        except KeyError:
            pass

        return msg
