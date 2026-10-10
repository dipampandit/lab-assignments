
public class ExecutionOrder {

    static {
        System.out.println("Static block executed");
    }

    {
        System.out.println("Instance initialization executed");
    }

    {
        System.out.println("Instance block executed");
    }

    ExecutionOrder() {
        System.out.println("Constructor executed");
    }

    void display() {
        System.out.println("Instance method executed");
    }

    public static void main(String[] args) {
        ExecutionOrder obj = new ExecutionOrder();
        obj.display();
    }
}
