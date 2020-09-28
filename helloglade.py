import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GLib

class Handler:
    def __init__(self, builder):
      self.builder = builder
    
    def onDestroy(self, *args):
      Gtk.main_quit()

if __name__ == "__main__":
  builder = Gtk.Builder()
  builder.add_from_file("./gui.glade")
  builder.connect_signals(Handler(builder))

  screen = Gdk.Screen.get_default()
  provider = Gtk.CssProvider()
  provider.load_from_path("./style.css")
  Gtk.StyleContext.add_provider_for_screen(
    screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

  window = builder.get_object("winApp")
  window.show_all()

  Gtk.main()
