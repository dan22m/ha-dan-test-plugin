from homeassistant.components.sensor import SensorEntity

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Додавання сенсора."""
    async_add_entities([MySensor()])

class MySensor(SensorEntity):
    def __init__(self):
        self._state = None

    @property
    def name(self):
        return "My Custom Sensor"

    @property
    def state(self):
        return self._state

    async def async_update(self):
        """Оновлення стану сенсора."""
        self._state = "Hello, HACS!"
