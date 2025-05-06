// Base class
public class Employee {

  // Required fields
  private final String name;
  private final int id;

  // Optional fields.
  private final String department;
  private final double salary;


  // Private constructor.
  private Employee(Builder builder){
    this.name = builder.name;
    this.id = builder.id;
    this.department = builder.department;
    this.salary = builder.salary
  }

  // Nested class that contains the builder.
  public static class Builder {

    private final String name;
    private final int id;

    private final String department;
    private final double salary;

    public Builder(String name, int id){
      this.name = name;
      this.id = id;
    }

    // Optional field to append to builder
    public Builder department(string department){
      this.department = department;
      return this;
    }

    public Builder salary(double salary){
      this.salary = salary;
      return this;
    }

    public Employee build(){
      return new Employee(this);
    }
    
    @Override
    public String toString() {
        return "Employee{name='" + name + "', id=" + id +
               ", department='" + department + "', salary=" + salary + '}'; 
  }
}
