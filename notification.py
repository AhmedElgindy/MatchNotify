from notifypy import Notify


class Notification:

    def __init__(
        self, title, message, icon=None, timeout=None, urgency=None
    ) -> None:  # noqa
        self.title = title
        self.message = message
        self.icon = icon
        self.timeout = timeout
        self.urgency = urgency

    def send(self):
        notify = Notify()
        notify.title = self.title
        notify.message = self.message
        if self.icon:
            notify.icon = self.icon
        notify.timeout = self.timeout
        if self.urgency:
            notify.urgency = self.urgency
        notify.send()
