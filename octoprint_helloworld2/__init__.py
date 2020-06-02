

# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import octoprint.plugin

class HelloWorldPlugin(octoprint.plugin.StartupPlugin, octoprint.plugin.TemplatePlugin):
    def on_after_startup(self):
        self._logger.info("Hello World!!!!!!!!!!!!!!!!!")
        self._logger.info("Hello World2")


__plugin_name__ = "Hello World Override"
__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = HelloWorldPlugin()
