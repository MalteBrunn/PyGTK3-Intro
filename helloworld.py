import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class myApp:
  def __init__(self):
    self.window = Gtk.Window()
    self.window.set_title("Hello World")
    self.window.connect(
      "destroy", 
      self.onDestroy
    )
    self.hbox = Gtk.HBox()
    self.label = Gtk.Label("Hello World")
    self.button = Gtk.Button("Close")
    self.button.connect(
      "clicked",
      self.onClick
    )
    self.hbox.add(self.label)
    self.hbox.add(self.button)
    self.window.add(self.hbox)
    self.window.show_all()
    
  def onDestroy(self, *args):
    Gtk.main_quit()
    
  def onClick(self, *args):
    Gtk.main_quit()
    
app = myApp()
Gtk.main()
