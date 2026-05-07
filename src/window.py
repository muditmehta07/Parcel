import configparser
import os
from gi.repository import Gtk, Adw

@Gtk.Template(resource_path='/io/github/muditmehta07/Parcel/window.ui')
class ParcelWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'ParcelWindow'
    shares_list = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_samba_shares()

    def load_samba_shares(self):
        base_path = os.path.dirname(__file__)
        config_path = os.path.join(base_path, 'test_cmb.conf')
        config = configparser.ConfigParser()
        config.read(config_path)

        for section in config.sections():
            if section != 'global':
                path = config.get(section, 'path', fallback='Unknown')
                self.add_share_row(section, path)

    def add_share_row(self, name, path):
        row = Adw.ActionRow()
        row.set_title(name)
        row.set_subtitle(path)
        row.set_icon_name("folder-remote-symbolic")
        self.shares_list_append(row)
