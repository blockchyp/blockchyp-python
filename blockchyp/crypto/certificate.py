import pkg_resources

from requests.adapters import HTTPAdapter


TERMINAL_COMMON_NAME = "blockchyp-terminal"
CA_CERT_FILE = pkg_resources.resource_filename("blockchyp", "resources/blockchyp.crt")


class TerminalAdapter(HTTPAdapter):
    """Validate that the certificate was signed by the BlockChyp certificate
    authority, and that the CN matches the static terminal CN."""

    def cert_verify(self, conn, url, verify, cert):
        verify = CA_CERT_FILE
        conn.assert_hostname = TERMINAL_COMMON_NAME

        return super().cert_verify(conn, url, verify, cert)
