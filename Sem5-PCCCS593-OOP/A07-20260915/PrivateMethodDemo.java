class A {
    private int a = 10;

    public int getA() {
        return a;
    }
}

class B extends A {
    private int b = 20;

    public int getB() {
        return b;
    }

    void display() {
        System.out.println("Private variable of A: " + getA());
        System.out.println("Private variable of B: " + getB());
    }

    public static void main(String[] args) {
        B obj = new B();
        obj.display();
    }
}