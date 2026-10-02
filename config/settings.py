import os
from dataclasses import dataclass

class ConfigurationError(ValueError):
    pass

def _required(name: str) -> str:
    value=os.getenv(name)
    if value is None or not value.strip():
        raise ConfigurationError(f"Missing required environment variable: {name}")
    return value.strip()

@dataclass(frozen=True)
class Settings:
    environment: str
    log_level: str
    max_batch_size: int
    maintenance_due_days: int

    @classmethod
    def from_env(cls):
        try:
            batch=int(_required("FLEET_MAX_BATCH_SIZE"))
            due=int(_required("FLEET_MAINTENANCE_DUE_DAYS"))
        except ValueError as exc:
            raise ConfigurationError("FLEET_MAX_BATCH_SIZE and FLEET_MAINTENANCE_DUE_DAYS must be integers") from exc
        if batch < 1 or due < 0:
            raise ConfigurationError("Fleet numeric settings are out of range")
        return cls(_required("FLEET_ENVIRONMENT"), _required("FLEET_LOG_LEVEL"), batch, due)
