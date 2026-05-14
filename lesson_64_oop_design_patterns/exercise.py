# Lesson 64: Exercise — Design Patterns
from abc import ABC, abstractmethod

# TODO 1: Singleton — NotificationConfig
#   _instance = None class var
#   __new__ ensures only one instance
#   Has attribute default_channel (str)

# TODO 2: ABC — Notifier with abstract send(message: str)

# TODO 3: EmailNotifier and SlackNotifier implementing Notifier

# TODO 4: NotifierFactory.create(channel: str) -> Notifier

# TODO 5: NotificationHub
#   subscribe(notifier: Notifier)
#   broadcast(message: str)

# Test
# cfg1 = NotificationConfig()
# cfg2 = NotificationConfig()
# print(cfg1 is cfg2)  # True
#
# hub = NotificationHub()
# hub.subscribe(NotifierFactory.create("email"))
# hub.subscribe(NotifierFactory.create("slack"))
# hub.broadcast("Deployment complete!")
