from abc import ABC, abstractmethod

class Notification(ABC):
  @abstractmethod
  def notify(self):
    pass


class SMSNotification(Notification):

  def notify(self):
    print("SMS notification")
    return "{SMS notification}"

class EmailNotification(Notification):

  def notify(self):
    print("Email notification")
    return "{SMS notification}"

def notificationFactory(method):
  if method == "email":
    return EmailNotification()
  elif method == "sms":
    return SMSNotification()




if __name__ == "__main__":

    notification = notificationFactory("email")
    notification.notify()
    n2 = notificationFactory("sms")
    n2.notify()

