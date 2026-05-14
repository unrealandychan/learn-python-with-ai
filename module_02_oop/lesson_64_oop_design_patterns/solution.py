# Lesson 64: Solution
from abc import ABC, abstractmethod


class NotificationConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.default_channel = "email"
        return cls._instance


class Notifier(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        pass


class EmailNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"[Email] {message}")


class SlackNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"[Slack] {message}")


class NotifierFactory:
    _registry = {"email": EmailNotifier, "slack": SlackNotifier}

    @classmethod
    def create(cls, channel: str) -> Notifier:
        if channel not in cls._registry:
            raise ValueError(f"Unknown channel: {channel}")
        return cls._registry[channel]()


class NotificationHub:
    def __init__(self):
        self._subscribers: list[Notifier] = []

    def subscribe(self, notifier: Notifier) -> None:
        self._subscribers.append(notifier)

    def broadcast(self, message: str) -> None:
        for notifier in self._subscribers:
            notifier.send(message)


cfg1 = NotificationConfig()
cfg2 = NotificationConfig()
print(f"Singleton: {cfg1 is cfg2}")

hub = NotificationHub()
hub.subscribe(NotifierFactory.create("email"))
hub.subscribe(NotifierFactory.create("slack"))
hub.broadcast("Deployment complete!")
