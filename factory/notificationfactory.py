"""
Simple factory for notifications. Goal is to make a factory that returns two methods of notification.
Of course, the .notify() method is very simplistic, but here the factory is in focus. Not the method itself.

Just know that this example does not have that much of other internals.. Just simplistic things here.
I could have also added functionality, such as automatic notification on class creation.
But that would be for another time and would also depend on the requests of the product owner.
"""

from abc import ABC, abstractmethod

class Notification(ABC):
  """
  All notifications should have at least a .notify() method. This ABC makes sure it is so.
  """
  
  @abstractmethod
  def notify(self):
    pass


class SMSNotification(Notification):
  """This is a SMS notification class. It handles SMS notifications. Well. Pseudosms."""
  
  def notify(self):
    print("SMS notification")
    return "{SMS notification}"

class EmailNotification(Notification):
  """This mocks a Email notification class."""

  def notify(self):
    print("Email notification")
    return "{SMS notification}"

def notificationFactory(method: str):
  """
  Factory returns notifications based on string input.
  """
  
  if method == "email":
    return EmailNotification()
  elif method == "sms":
    return SMSNotification()




if __name__ == "__main__":

    # Create an email-notification.
    email_notification = notificationFactory("email")
    email_notification.notify()
    
    # Create an SMS notification.
    n2 = notificationFactory("sms")
    n2.notify()

