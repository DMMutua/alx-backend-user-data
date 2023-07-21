#!/usr/bin/env python3
"""User Data Control"""

import logging
import re


def filter_datum(fields: list[str], redaction: str,
                 message: str, separator: str) -> str:
    """Returns A log message obfuscated.
    """
    pattern = r"\b(" + "|".join(fields) + r")=[^" + separator + r"]*"
    return re.sub(pattern, lambda match: match.group(1) + "=" +
                  redaction, message)


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class."""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: list[str]):
        """Initialization for the redacting formatter class"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Filters Values in incoming log records using `filter_datum`"""
        log_message = super().format(record)
        return filter_datum(self.fields, self.REDACTION,
                            log_message, self.SEPARATOR)


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_logger() -> logging.Logger:
    """Returns a logging.Logger object with specific settings."""

    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    logger.propagate = False
    return logger
