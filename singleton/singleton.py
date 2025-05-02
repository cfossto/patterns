# Singleton based on __new__ (more true to a very zen-like Singleton)
class SingeltonOnNew:
  _instance = None
  
  def __new__(cls):
    if not cls._instance:
      cls._instance = super().__new__(cls)
    return cls._instance


# Singleton based on Metaclass implementation
# (more modular)
class SingletonMeta(type)

  _instances= {}

  def __call__(cls, *args, **kwargs):
    if not cls in cls._instances:
      instance = super().__call__(*args, **kwargs)
      cls.instances[cls] = instance
    return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
  def businesslogic():
    pass


# Quick test
if __name__ == '__main__":
  s1 = Singleton()
  s2 = Singleton()

  if id(s1) == id(s2):
    print("Singleton works, it is the same instance")
  else:
    print("something is wrong")
