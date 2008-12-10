import gtk
from ipython_view import *
import pango
import gconf

class iPythonConsole(gtk.ScrolledWindow):
  def __init__(self, namespace = {}):
    gtk.ScrolledWindow.__init__(self)

    # Get font from gedit's entries in gconf
    client = gconf.client_get_default()
    default_question = client.get_bool('/apps/gedit-2/preferences/editor/font/use_default_font')
    if default_question == True:
      userfont = client.get_string('/desktop/gnome/interface/font_name')
    else:
      userfont = client.get_string('/apps/gedit-2/preferences/editor/font/editor_font')

    self.set_policy(gtk.POLICY_NEVER, gtk.POLICY_AUTOMATIC);
    self.set_shadow_type(gtk.SHADOW_IN)

    self.view = IPythonView()
    self.view.modify_font(pango.FontDescription(userfont))
    self.view.set_editable(True)
    self.view.set_wrap_mode(gtk.WRAP_WORD_CHAR)
    self.add(self.view)
    self.view.show()

    self.view.updateNamespace(namespace)
