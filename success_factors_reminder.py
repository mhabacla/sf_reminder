import yaml
import webbrowser

from pathlib import Path
from tkinter import messagebox


def main():
    try:
        config = read_yaml()

        url = config.get('SUCCESS_FACTORS').get('URL')
        if not url:
            not_url_err(config)

        popup_msg = config.get('GENERAL').get('INFO_MSG')
        popup_title = config.get('GENERAL').get('INFO_TITLE')
        messagebox.showinfo(popup_title, popup_msg)
        webbrowser.open_new(url)

    except Exception as exc:
        messagebox.showerror("Error", f'{exc}')
        exit()


def not_url_err(config):
    warn_msg = config.get('GENERAL').get('WARN_MSG')
    warn_title = config.get('GENERAL').get('WARN_TITLE')
    messagebox.showerror(warn_title, f'{warn_msg} ({config_path})')
    exit()


def read_yaml():
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


if __name__ == '__main__':
    global config_path
    config_path = Path.joinpath(Path(__file__).parent, 'conf/config.yaml')

    main()
