// Basic singelton. Non thread safe.

public final class Singleton(){

  private static Singleton instance;
  private String value;

  private Singleton(String value) {
    this.value = value;
  }

  public static Singleton getInstance(String value) {
    if (instance == null) {
      instance = new Singleton(value);
    }
    return instance;
  }
}

public class TestingSingleton(){

  public static void Main(String args[]){

    Singleton singleton1 = Singleton().getInstance("This is only one.");
    Singleton singleton2 = Singleton().getInstance("Will not see the day of light.");

    System.Out.Println(singleton1.value);
    System.Out.Println(singleton2.value);
      
  }
  
}
