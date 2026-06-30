"""
Interface service interacting with SAP systems.
"""

class SAPService:
    def __init__(self, connector):
        self.connector = connector

    def verify_client_info(self, client_id: str) -> dict:
        return {"exists": True}
