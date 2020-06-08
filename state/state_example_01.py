from __future__ import annotations
from abc import ABC, abstractmethod

class Order:
  """ Context """

  def __init__(self) -> None:
    self.state: OrderState = PaymentPending(self)

  def pending(self) -> None:
    print("Trying to pending()")
    self.state.pending()
    print("Current state ~>", self.state)
    print()

  def approve(self) -> None:
    print("Trying to run approve()")
    self.state.approve()
    print("Current state ~>", self.state)
    print()

  def reject(self) -> None:
    print("Trying to reject()")
    self.state.reject()
    print("Current state ~>", self.state)
    print()

class OrderState(ABC):

  def __init__(self, order: Order) -> None:
    self.order = order

  @abstractmethod
  def pending(self) -> None: pass

  @abstractmethod
  def approve(self) -> None: pass

  @abstractmethod
  def reject(self) -> None: pass

  def __str__(self):
    return self.__class__.__name__

  
class PaymentPending(OrderState):

  def pending(self) -> None:
    print("payment declined")

  def approve(self) -> None:
    self.order.state = PaymentApproved(self.order)
    print("payment declined")

  def reject(self) -> None:
    self.order.state = PaymentRejected(self.order)
    print()


class PaymentApproved(OrderState):
  def pending(self) -> None:
    self.order.state = PaymentPending(self.order)
    print("pending payment")

  def approve(self) -> None:
    print("Payment already approved")

  def reject(self) -> None:
    self.order.state = PaymentRejected(self.order)
    print("payment declined")


class PaymentRejected(OrderState):
  def pending(self) -> None:
    print("Payment declined. I will not move to pending.")

  def approve(self) -> None:
    print("payment declined")

  def reject(self) -> None:
    print("payment declined")


if __name__ == "__main__":
  order = Order()
  order.pending()
  order.approve()
  order.pending()
  order.reject()
  order.pending()
  order.approve()