class A {
    int x = 10;
}

class B extends A {
    int x = 20;
}

class C extends B {
    int x = 30;

    void display() {
        System.out.println("C's x: " + x);
        System.out.println("B's x: " + super.x);
        System.out.println("A's x: " + ((A)this).x);
    }

    public static void main(String[] args) {
        C obj = new C();
        obj.display();
    }
}