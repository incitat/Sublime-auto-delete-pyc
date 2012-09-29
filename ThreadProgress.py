import sublime

class ThreadProgress():
    callback = None
    def __init__(self, thread,callback=None):
        self.thread     = thread
        self.callback   = callback
        self.addend = 1
        self.size = 8
        self.thread.start()
        sublime.set_timeout(lambda: self.run(0), 100)

    def run(self, i):
        if not self.thread.is_alive():
            if self.thread.exception:
                sublime.message_dialog(str(self.thread.exception))
                return
            if self.callback:
                self.callback()
            return

        before = i % self.size
        after = (self.size - 1) - before
        sublime.status_message('%s [%s=%s]' % \
            (self.thread.status, ' ' * before, ' ' * after))
        if not after:
            self.addend = -1
        if not before:
            self.addend = 1
        i += self.addend
        sublime.set_timeout(lambda: self.run(i), 100)