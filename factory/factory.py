from abc import ABC, abstractmethod

class Creator(ABC):

  @abstractmethod
  def factory_method(self):
    pass

  def some_operation(self) -> str:
    product = self.factory_method()
    result = f"Creator: The same creator's code has just worked with {product.operation()}"

    return result


class ConcreteCreator1(Creator):

  def factory_method(self):
    return ConcreteProduct1

class ConcreteCreator2(Creator):

  def factory_method(self):
    return ConcreteProduct2


class Product(ABC):

  @abstractmethod
  def operation(self) -> str:
    pass


class ConcreteProduct1(Product):
  def operation(self) -> str:
    return "{Result of Product1}"

class ConcreteProduct2(Product):
  def operation(self) -> str:
    return "{Result of Product2}"


def client_code(creator: Creator) ->:
  print(f"Client: I am not aware of the creator's class, but it still works \n"
       f"{creator.some_operation()}")

client_code(ConcreteProduct1)
print("\n")
client_code(ConcreteProduct2)
print("\n")
