import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk

window = Gtk.Window()
window.set_title("BIENVENIDO")
window.connect("delete-event", Gtk.main_quit)
window.show()

caja = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
caja.show()

def activar(widget):
    print "BOTON ACTIVADO"

boton = Gtk.Button("Salir ")
boton.connect("clicked", Gtk.main_quit)
boton.show()
caja.pack_start(boton   , False, False, 10)


label = Gtk.Label("Hola Juan(peludito)")
label.show()
caja.pack_start(label, True, False, 5)

window.add(caja)
Gtk.main()

