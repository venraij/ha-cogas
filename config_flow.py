from homeassistant import config_entries
from .const import DOMAIN
import voluptuous as vol

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input):
        errors = {}
        if user_input is not None:
            return await self.login_cogas()
        return self.async_show_form(
            step_id="user", data_schema=vol.Schema({
                    vol.Required("email"): str,
                    vol.Required("password"): str
                })
        )
    
    async def login_cogas(self, user_input):
        errors = {}