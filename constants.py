KDA_EX_URL = "https://kdaexplorer.com/"

KDA_WS_URL = "wss://backend-dev.euclabs.net/kadena-indexer-websockets/"

CONNECT_MSG = {
    "command": "CONNECT",
    "headers": {"heart-beat": "1000,1000", "accept-version": "1.2,1.1,1.0"},
    "body": "",
}
SUBSCIRIBE_MSGS = [
    """SUBSCRIBE
id:sub-0
destination:/topic/blockchain/height

""",
    """SUBSCRIBE
id:sub-1
destination:/topic/blocks

""",
    """SUBSCRIBE
id:sub-2
destination:/topic/transactions

""",
]
