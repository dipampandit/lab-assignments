class Parent {
    int x = 10;
}

class Child extends Parent {
    int x = 20;

    void displayAndModify() {
        System.out.println("Before Modification:");

        System.out.println("Superclass x = " + super.x);
        System.out.println("Subclass x = " + this.x);

        super.x++;
        this.x++;

        System.out.println("\nAfter Modification:");

        System.out.println("Superclass x = " + super.x);
        System.out.println("Subclass x = " + this.x);
    }

    public static void main(String[] args) {
        Child obj = new Child();
        obj.displayAndModify();
    }
}