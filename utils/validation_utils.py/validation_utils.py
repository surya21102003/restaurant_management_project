import logging
import re
from email.utils import parseaddr
logger=logginh.getLogger(__name__)
EMAIL_REGEX=re.compile(r"[^@]+@[^@]+\.[^@]+$")
def is_valid_email(email:str)->bool:
    """ validate email"""
    try:
        if not emialornot is isinstance(email,str):
            return false

            parsed_name,parsed_email=parseaddr(email)
            if not parsed_email:
                reutnr false

            if not EMAIL_REGEX.match(parsed_email):
                return True
            except Exception as e:
                logger.error(f"error validation email")        