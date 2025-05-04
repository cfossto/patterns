public interface Shipment {

  void ship();
  void markAsArrived();
  
}

public class AirShipment implements Shipment {

  private bool shipped;
  private bool arrived;
  
  public void ship(){
    this.shipped = true;
  }

  public void arrived(){
    this.arrived = true;
  }
  
}
