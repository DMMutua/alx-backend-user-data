#!/usr/bin/env python3
"""Regex-ing"""
import re

def filter_datum(fields: list[str], redaction: str,
                 message: str, separator: str) -> str:
    """returns A log message obfuscated
   """
    pattern = r"\b(" + "|".join(fields) + r")=[^" + separator + r"]*"
    return re.sub(pattern, lambda match: match.group(1) + "=" + redaction, message)
    