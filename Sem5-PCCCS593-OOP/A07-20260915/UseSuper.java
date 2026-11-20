class Parent {
    protected int x = 10;
}

class Child extends Parent {
    int x = 20;

    void display() {
        System.out.println("Subclass x: " + x);
        System.out.println("Superclass x: " + super.x);
    }

    public static void main(String[] args) {
        Child obj = new Child();
        obj.display();
    }
}