# -*- coding: UTF-8 -*-

# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.

# Full getext (please don't change)
_ = lambda x : x

# Add-on information variables
addon_info = {
	# for previously unpublished addons, please follow the community guidelines at:
	# https://bitbucket.org/nvdaaddonteam/todo/raw/master/guideLines.txt
	# add-on Name, internal for nvda
	"addon-name" : "emoticons",
	# Add-on summary, usually the user visible name of the addon.
	# Translators: Summary for this add-on to be shown on installation and add-on information.
	"addon-summary" : _("Emoticons"),
	# Add-on description
	# Translators: Long description to be shown for this add-on on add-on information from add-ons manager
	"addon-description" : _("Enables the announcement of emoticon names instead of the character representation.\n"
			"Press NVDA+E to toggle."),
	# version
	"addon-version" : "1.1-dev",
	# Author(s)
	"addon-author" : u"Chris Leo <llajta2012@gmail.com>, Noelia Ruiz Martínez <nrm1977@gmail.com>, Mesar Hameed <mhameed@src.gnome.org>",
	# URL for the add-on documentation support
	"addon-url" : "http://addons.nvda-project.org"
}


import os.path

# Define the python files that are the sources of your add-on.
# You can use glob expressions here, they will be expanded.
pythonSources = [os.path.join("addon", "*.py"), os.path.join("addon", "globalPlugins", "emoticons", "*.py")]

# Files that contain strings for translation. Usually your python sources
i18nSources = pythonSources + ["buildVars.py", "docHandler.py", os.path.join("addon", "installTasks.py")]

# Files that will be ignored when building the nvda-addon file
# Paths are relative to the addon directory, not to the root directory of your addon sources.
excludedFiles = []
