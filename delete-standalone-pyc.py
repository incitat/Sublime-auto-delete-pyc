#!/usr/bin/env python
from os.path import relpath
from platform import python_version
from sys import exc_info
from sublime import active_window, error_message, packages_path
import sublime_plugin
try:
    import dir
    import sublime_helper
    pkg =sublime_helper.package(__file__)
except Exception, e:
    package = relpath(__file__, packages_path())
    line = exc_info()[2].tb_lineno
    error_message("""python%s\n%s:%s\n
%s:\n%s""" % (
    python_version(), package, line,
    type(e), str(e)
    ))


def unlink_pyc(dirname):
    for filepyc in dir.files(dirname, tree=True, filter="*.pyc"):
        filepy =filepyc[:-1]
        if not dir.exists(filepy):
            dir.unlink(filepyc)


class DeletePycListener(sublime_plugin.EventListener):
    def run(self):
        for dirname in active_window().folders():
            sublime_helper.thread(
                lambda: unlink_pyc(dirname),
                status="search standalone .pyc"
            )

    def on_pre_save(self, view):
        try:
            pkg.saferun(self.run)
        except NameError:  # pkg is undefined
            pass
        except Exception, e:
            error_message(str(e))