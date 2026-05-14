# Lesson 64: Design Patterns (Singleton, Factory, Observer, Strategy)

Design patterns are proven solutions to common software design problems.

---

## 1. Singleton — One Instance Only

Ensures a class has **only one instance**, and provides a global access point.

```python
class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.settings = {}
        return cls._instance

c1 = Config()
c2 = Config()
print(c1 is c2)  # True — same object
```

**Use cases:** Database connection pools, app config, logging handlers.

---

## 2. Factory — Delegate Object Creation

Lets a helper decide which class to instantiate.

```python
class Notification:
    def send(self, message: str) -> None:
        raise NotImplementedError

class EmailNotification(Notification):
    def send(self, message: str) -> None:
        print(f"Email: {message}")

class SMSNotification(Notification):
    def send(self, message: str) -> None:
        print(f"SMS: {message}")

def notification_factory(channel: str) -> Notification:
    options = {"email": EmailNotification, "sms": SMSNotification}
    if channel not in options:
        raise ValueError(f"Unknown channel: {channel}")
    return options[channel]()
```

**Use cases:** Creating LLM provider instances, database drivers, file parsers.

---

## 3. Observer — Event-Driven Notifications

One-to-many: when one object changes state, all dependents are notified.

```python
class EventEmitter:
    def __init__(self):
        self._listeners: dict[str, list] = {}

    def on(self, event: str, callback) -> None:
        self._listeners.setdefault(event, []).append(callback)

    def emit(self, event: str, data=None) -> None:
        for cb in self._listeners.get(event, []):
            cb(data)

emitter = EventEmitter()
emitter.on("message", lambda d: print(f"Logger: {d}"))
emitter.on("message", lambda d: print(f"Analytics: {d}"))
emitter.emit("message", "Hello!")
```

---

## 4. Strategy — Swap Algorithms at Runtime

Encapsulate interchangeable algorithms behind a common interface.

```python
class Sorter:
    def __init__(self, strategy):
        self._strategy = strategy

    def sort(self, data: list) -> list:
        return self._strategy.sort(data)

    def set_strategy(self, strategy) -> None:
        self._strategy = strategy
```

**Use cases:** Choosing LLM backends, retry strategies, ranking algorithms.

---

## Exercise

Build a **mini notification system** using all four patterns:

1. `NotificationConfig` (Singleton) — holds `default_channel: str`
2. `Notifier` ABC with abstract `send(message: str)`
3. `EmailNotifier` and `SlackNotifier` implementing `Notifier`
4. `NotifierFactory` with `create(channel: str) -> Notifier`
5. `NotificationHub` (Observer) — `subscribe(notifier)`, `broadcast(message)`
