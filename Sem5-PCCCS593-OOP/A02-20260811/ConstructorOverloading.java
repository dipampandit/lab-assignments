
public class ConstructorOverloading {

    int id;
    String name;

    static {
        System.out.println("Static block executed");
    }

    {
        System.out.println("Instance block executed");
    }

    // Default constructor
    ConstructorOverloading() {
        id = 0;
        name = "Unknown";
        System.out.println("Default constructor executed");
    }

    // One-parameter constructor
    ConstructorOverloading(int i) {
        id = i;
        name = "Unknown";
        System.out.println("One-parameter constructor executed");
    }

    // Two-parameter constructor
    ConstructorOverloading(int i, String n) {
        id = i;
        name = n;
        System.out.println("Two-parameter constructor executed");
    }

    void display() {
        System.out.println("ID: " + id + ", Name: " + name);
    }

    public static void main(String[] args) {
        ConstructorOverloading obj1 = new ConstructorOverloading();
        obj1.display();

        ConstructorOverloading obj2 = new ConstructorOverloading(101);
        obj2.display();

        ConstructorOverloading obj3 =
                new ConstructorOverloading(102, "Rahul");
        obj3.display();
    }
}
