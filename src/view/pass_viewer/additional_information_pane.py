# pkpass_back_view.py
#
# Copyright 2022 Pablo Sánchez Rodríguez
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk

from .pkpass_field_row import PassFieldRow


@Gtk.Template(resource_path='/me/sanchezrodriguez/passes/additional_information_pane.ui')
class AdditionalInformationPane(Gtk.Box):

    __gtype_name__ = 'AdditionalInformationPane'

    stack = Gtk.Template.Child()
    fields = Gtk.Template.Child()

    def __init__(self):
        super().__init__()

    def clean(self):
        row = self.fields.get_row_at_index(0)
        while row:
            self.fields.remove(row)
            row = self.fields.get_row_at_index(0)

    def content(self, a_pass):
        self.clean()
        fields = a_pass.additional_information()

        # Hide field list if we do not have anything to show
        if not fields:
            self.stack.set_visible_child_name('empty-page')
            return

        self.stack.set_visible_child_name('fields-page')

        for field in fields:
            label = field.label()
            value = field.value()

            passFieldRow = PassFieldRow(label, value, create_links=True)
            passFieldRow.set_halign(Gtk.Align.START)
            self.fields.append(passFieldRow)
