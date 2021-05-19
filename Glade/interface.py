import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk


class Main:
    def __init(self):
        gladeFile = "main.glade"
        self.builder = gtk.Builder()
        self.builder.add_from_file(gladeFile)

        button = self.builder.get_object("button")
        button.connect("clicked", self.printText)

        window = self.builder.get_object("Login")
        window.connect("delete-event", gtk.main_quit)
        window.show()

    def printText(self, widget):
        print("hello WOrld!")


if __name__ == '__main__':
    main = Main()
    gtk.main()
