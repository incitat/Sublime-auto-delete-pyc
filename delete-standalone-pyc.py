from sublime import active_window,error_message
import sublime_plugin
from os import walk,unlink
from os.path import join,splitext
try:
    from sublime_helper import thread
except ImportError:
    from platform import python_version
    error_message("""sublime_helper ImportError
pip-%s install sublime_helper""" % python_version()[0:3])
except Exception,e:
    error_message(str(e))

def unlink_pyc(dirname):
    for root, dirs, files in walk(dirname):
        for f in files:
            fileName, fileExtension = splitext(f)
            if fileExtension == ".pyc":
                if f[0:-1] not in files:
                    unlink(join(root, f))


class DeletePycListener(sublime_plugin.EventListener):
    def on_pre_save(self, view):
        try:
            for dirname in active_window().folders():
                thread(
                    lambda:unlink_pyc(dirname),
                    status="search standalone .pyc"
                )
        except Exception, e:
            error_message(str(e))