// Example from GG

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

class Client {
  
  private Vehicle pVehicle;

  public Client(int type){
    if (type == 1) {
      pVehicle = new TwoWheeler();
    }
    if (type == 2) {
      pVehicle = new FourWheeler();
    }
    else {
      pVehicle = null;
    }
  }
  public void cleanUp(){
    if (pVehicle != null){
      pVehicle = null;
    }
  }
  public Vehicle getVehicle(){
    return pVehicle;
  }
}

public class M {
  public static void Main(String[] args){
    Client = new Client(1);
    Vehicle pVehicle = client.getVehicle();
    if (pVehicle != null){
      pVehicle.printVehicle():
    }
    pVehicle.cleanUp();
  }
}
