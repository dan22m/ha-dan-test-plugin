from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

DOMAIN = "ha-dan-test-plugin"

async def async_setup(hass, config):
    """Налаштування інтеграції через configuration.yaml."""
    return True

async def async_setup_entry(hass, entry):
    """Налаштування інтеграції через UI."""
    hass.data[DOMAIN] = DataUpdateCoordinator(hass, _LOGGER, name=DOMAIN)
    return True

async def async_unload_entry(hass, entry):
    """Видалення інтеграції."""
    return True
