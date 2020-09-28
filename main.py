#!/usr/bin/python3

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GLib
import subprocess

class Handler:
    def __init__(self, builder):
      self.builder = builder
    
    def onDestroy(self, *args):
      Gtk.main_quit()
    
    def on_bntStart_clicked(self, *args):
      self.builder.get_object("msgAbout").run()
    
    def on_btnAboutOk_clicked(self, *args):
      self.builder.get_object("msgAbout").hide()
      self.builder.get_object("winApp").hide()
      self.builder.get_object("winContent").show()
      self.builder.get_object("lblTitle").set_label(
        self.builder.get_object("notePages").get_tab_label_text(
          self.builder.get_object("notePages").get_nth_page(0)
        )
      )
      
    def on_btnNext_clicked(self, *args):
      self.builder.get_object("notePages").next_page()
      
    def on_btnPrev_clicked(self, *args):
      self.builder.get_object("notePages").prev_page()
      
    def on_btnExit_clicked(self, *args):
      self.onDestroy()
      
    def on_notePages_switch_page(self, *args):
      pages = args[0].get_n_pages()
      self.builder.get_object("lblTitle").set_label(args[0].get_tab_label_text(args[1]))
      if args[2] == 0:
        self.builder.get_object("btnPrev").set_sensitive(False)
      else:
        self.builder.get_object("btnPrev").set_sensitive(True)
      if args[2] == pages - 1:
        self.builder.get_object("btnNext").set_sensitive(False)
      else:
        self.builder.get_object("btnNext").set_sensitive(True)
    
    def on_btnGlade_clicked(self, *args):
      subprocess.call(["glade", "gui.glade"])

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
