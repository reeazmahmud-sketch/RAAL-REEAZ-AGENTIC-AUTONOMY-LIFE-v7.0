import os
import unittest
from unittest.mock import patch

from raal.config import load_config


class RuntimeConfigTests(unittest.TestCase):
    def test_load_config_does_not_expose_log_level(self) -> None:
        with patch.dict(
            os.environ,
            {"RAAL_AGENT_NAME": "demo", "RAAL_MAX_STEPS": "8", "RAAL_LOG_LEVEL": "DEBUG"},
            clear=True,
        ):
            config = load_config()

        self.assertEqual(config.agent_name, "demo")
        self.assertEqual(config.max_steps, 8)
        self.assertFalse(hasattr(config, "log_level"))


if __name__ == "__main__":
    unittest.main()
