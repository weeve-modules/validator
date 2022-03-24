"""
All logic related to the module's main application
Mostly only this file requires changes
"""

from app.config import APPLICATION

def module_main(data):
    """implement module logic here

    Args:
        parsed_data ([JSON Object]): [Data received by the module and validated by data_validation function]

    Returns:
        [string, string]: [data, error]
    """
    try:
        return data, None
    except Exception:
        return None, "Unable to perform the module logic"
