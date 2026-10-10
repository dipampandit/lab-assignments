
public class MultipleBlocks {

    static {
        System.out.println("Static block 1 executed");
    }

    static {
        System.out.println("Static block 2 executed");
    }

    {
        System.out.println("Instance block 1 executed");
    }

    {
        System.out.println("Instance block 2 executed");
    }

    MultipleBlocks() {
        System.out.println("Default constructor executed");
    }

    MultipleBlocks(int x) {
        System.out.println("Parameterized constructor executed");
    }

    public static void main(String[] args) {
        System.out.println("Creating first object:");
        MultipleBlocks obj1 = new MultipleBlocks();

        System.out.println("Creating second object:");
        MultipleBlocks obj2 = new MultipleBlocks(10);
    }
}
