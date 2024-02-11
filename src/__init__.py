from logging.config import dictConfig
from src.config import settings

__version__ = "0.0.1"


def config_loggers():
    values = [config.split(":") for config in settings.LOGGERS]

    return {
        key: {"handlers": ["default"], "level": value, "propagate": False}
        for key, value in values
    }


dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": True,
        "formatters": {
            "standard": {"format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"},
        },
        "handlers": {
            "default": {
                "formatter": "standard",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
            },
        },
        "loggers": {
            "": {"handlers": ["default"], "level": "INFO", "propagate": True},
            **config_loggers(),
        },
    }
)
