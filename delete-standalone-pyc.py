import sublime
import sublime_plugin
import os


class DeletePycListener(sublime_plugin.EventListener):
    def on_post_save(self, view):
        try:
            f = view.file_name()
            if f is not None:
                f = os.path.abspath(f)
                fpath, fext = os.path.splitext(f)
                if fext == ".py":
                    pyc_path = fpath + ".pyc"
                    if os.path.exists(pyc_path):
                        os.remove(pyc_path)
        except Exception:
            pass
