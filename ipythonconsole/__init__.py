# -*- coding: utf-8 -*-

# __init__.py -- plugin object
#
# Copyright (C) 2006 - Éverton Ribeiro
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

# Parts from "Provides IPython console widget."
#      @author: Eitan Isaacson
#      @organization: IBM Corporation
#      @copyright: Copyright (c) 2007 IBM Corporation
#      @license: BSD
# And parts from "gedit Python Console Plugin"
#     Copyrignt (C), 2005 Raphaël Slinckx

#import pango

import gtk
import gconf
import gedit
from console import iPythonConsole

class iPythonConsolePlugin(gedit.Plugin):
  def __init__(self):
    gedit.Plugin.__init__(self)

  def activate(self, window):
    console = iPythonConsole(namespace = {'__builtins__' : __builtins__,
                                         'gedit' : gedit,
                                         'window' : window})
    bottom = window.get_bottom_panel()
    image = gtk.Image()
    image.set_from_icon_name('gnome-mime-text-x-python',
                             gtk.ICON_SIZE_MENU)
    bottom.add_item(console, _('iPython Console'), image)
    window.set_data('iPythonConsolePluginInfo', console)

  def deactivate(self, window):
    console = window.get_data("iPythonConsolePluginInfo")
    window.set_data("iPythonConsolePluginInfo", None)
    bottom = window.get_bottom_panel()
    bottom.remove_item(console)
