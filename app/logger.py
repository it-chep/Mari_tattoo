import json
import logging
from datetime import timezone, timedelta, datetime

import structlog


class CustomJSONRenderer(structlog.processors.JSONRenderer):
    def __call__(self, logger, name, event_dict):
        formatted_event_dict = {
            "logger": logger.name,
            "level": event_dict["level"],
            "time": event_dict["timestamp"],
            "event": event_dict.get("event"),
        }
        return json.dumps(formatted_event_dict, ensure_ascii=False)


class FormattedTime:
    def __call__(self, logger, name, event_dict):
        msk_time = datetime.now(timezone(timedelta(hours=-7)))

        formatted_timestamp = msk_time.strftime("%d-%m-%Y %H:%M:%S")
        event_dict["timestamp"] = formatted_timestamp
        return event_dict


file_log = logging.FileHandler('app.log')
console_out = logging.StreamHandler()
logging.basicConfig(handlers=(file_log, console_out), format="%(message)s", level=logging.INFO, )

structlog.configure(
    processors=[
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        FormattedTime(),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        CustomJSONRenderer(),
        # structlog.dev.ConsoleRenderer()
    ],
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
    cache_logger_on_first_use=True,
)


class Logger:
    def __init__(self, logger_name):
        self.logger = structlog.get_logger(logger_name)

    def debug(self, message, **kwargs):
        self.logger.debug(message, **kwargs)

    def info(self, message, **kwargs):
        self.logger.info(message, **kwargs)

    def warning(self, message, **kwargs):
        self.logger.warning(message, **kwargs)

    def error(self, message, **kwargs):
        self.logger.error(message, **kwargs)

    def exception(self, message, **kwargs):
        self.logger.exception(message, **kwargs)

    def critical(self, message, **kwargs):
        self.logger.critical(message, **kwargs)
