"""
IS-U Smart Assistant - SAP Queries
Predefined SAP IS-U queries and data retrieval functions.
"""


class SAPQueries:
    """Collection of SAP IS-U query functions."""

    def __init__(self, connector=None):
        self.connector = connector

    def get_business_partner(self, bp_id: str) -> dict:
        """Retrieve business partner information."""
        raise NotImplementedError

    def get_contract_account(self, ca_id: str) -> dict:
        """Retrieve contract account information."""
        raise NotImplementedError
