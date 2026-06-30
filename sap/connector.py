"""
IS-U Smart Assistant - SAP Connector
Handles RFC connections to SAP IS-U systems.
"""


class SAPConnector:
    """Manages connections to SAP IS-U via RFC."""

    def __init__(self, config: dict = None):
        self.config = config or {}

    def connect(self) -> None:
        """Establish a connection to the SAP system."""
        raise NotImplementedError

    def call_function(self, function_name: str, **kwargs):
        """Call an SAP RFC function module."""
        raise NotImplementedError
