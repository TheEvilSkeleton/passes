from gi.repository import Gtk
from .digital_pass_factory import FileIsNotAPass, FormatNotSupportedYet, PassFactory
from gettext import gettext as _

def import_action(self, *args):
    def on_file_chosen(_dialog, response):
        if response == Gtk.ResponseType.ACCEPT:
            pass_file = dialog.get_file()
            digital_pass = PassFactory.create(pass_file)

            stored_file = self.__persistence\
                .save_pass_file(pass_file, digital_pass.format())

            digital_pass.set_path(stored_file.get_path())
            self.__pass_list.insert(digital_pass)

            if not self.__pass_list.is_empty():
                self.window().show_pass_list()
                self.window().force_fold(False)

            found, index = self.__pass_list.find(digital_pass)
            if found:
                self.window().select_pass_at_index(index)

    dialog = Gtk.FileChooserNative.new(
        title=_('Import a pass'),
        parent=self,
        action=Gtk.FileChooserAction.OPEN
    )

    dialog.set_modal(True)
    dialog.set_transient_for(self)
    dialog.connect('response', on_file_chosen)
    dialog.show()

    # try:
    #     pass_file = filechooser.get_file()
    #     digital_pass = PassFactory.create(pass_file)

    #     stored_file = self.__persistence\
    #         .save_pass_file(pass_file, digital_pass.format())

    #     digital_pass.set_path(stored_file.get_path())
    #     self.__pass_list.insert(digital_pass)

    #     if not self.__pass_list.is_empty():
    #         self.window().show_pass_list()
    #         self.window().force_fold(False)

    #     found, index = self.__pass_list.find(digital_pass)
    #     if found:
    #         self.window().select_pass_at_index(index)

    # except Exception as exception:
    #     self.window().show_toast(str(exception))
