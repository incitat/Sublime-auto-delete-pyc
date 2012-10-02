import sublime
import sublime_plugin
import os
import re


def is_python_file(view):
    return bool(re.search('Python', view.settings().get('syntax'), re.I))


def unlink_pyc(dirname="."):
    for root, dirs, files in os.walk(dirname):
        for f in files:
            fileName, fileExtension = os.path.splitext(f)
            if fileExtension == ".pyc":
                if f[0:-1] not in files:
                    os.unlink(os.path.join(root, f))


class DeletePycListener(sublime_plugin.EventListener):
    def on_pre_save(self, view):
        try:
            if is_python_file(view):
                if view.file_name():
                    unlink_pyc(os.path.dirname(view.file_name()))
        except Exception, e:
            sublime.message_dialog(str(e))