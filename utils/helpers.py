"""
General helper methods and conversions.
"""

def format_response(data: dict) -> str:
    return f"Response status: {data.get('status', 'unknown')}"
