
from typing import Any, List

from .SingletonMeta import SingletonMeta
from .IDomainEvent import IDomainEvent
from .IDomainEventSubscriber import IDomainEventSubscriber


class DomainEventPublisher(metaclass=SingletonMeta):
    __subscribers: List[IDomainEventSubscriber]

    def __init__(self) -> None:
        self.__subscribers = []

    @staticmethod
    def of():
        return DomainEventPublisher()

    def subscribe(self, subscribers: List[IDomainEventSubscriber]):
        self.__subscribers.append(subscribers)

    def unsubscribe(self, id: int):
        self.__subscribers.remove(id, 1)

    def callHandle(self, suscriber: IDomainEventSubscriber, event):
        suscriber.handle(event)

    def publish(self, event: IDomainEvent) -> Any:

        subscribers = list(
            filter(lambda subscriber: subscriber.isSubscribedTo(event),
                   self.__subscribers))
        for idx, _ in enumerate(subscribers):
            result = subscribers[idx].handle(event)
            if result:
                return result
            # self.callHandle(event, subscriber)
