/*
This example is from GeeksForGeeks. We are trying an interesting approach here.

1. We define what a vehicle and a vehicle factory is.
2. We create 2 factories that should return vehicle based on type.
3. We get vehicles based on type.
*/

import java.io.*
  
abstract class Vehicle {
  public abstract void printVehicle();
}

class TwoWheeler extends Vehicle {
  public void printVehicle() {
    System.out.println("I am a two wheeler!")
  }
}

class FourWheeler extends Vehicle {
  System.out.println("I am a four wheeler!")  
}

public interface VehicleFactory(){
  Vehicle createVehicle();
}

public class TwoWheelerFactory implements Vehiclefactory {
  public Vehicle createVehicle(){
    return new TwoWheeler();
  }
}

public class FourWheelerFactory implements VehicleFactory {
  public Vehicle createVehicle(){
  return new FourWheeler();
  }
}


class Client {

  private Vehicle pVehicle;

  public Client(VehicleFactory factory){
    return factory.createVehicle();
  }

  public Vehicle getVehicle(){
    return pVehicle;
  }
  
}

public class M {
  public static void Main(String[] args){

    VehicleFactory twoWheelerFactory = new TwoWheelerFactory();
    Client twoWheelerClient = Client(twoWheelerFactory);
    Vehicle twoWheeler = twoWheelerClient.getVehicle();
    twoWheeler.printVehicle();
    
}
