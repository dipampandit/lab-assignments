class Product {
    String name;
    double price;
    double discount;

    Product() {
        this("Unknown", 0, 0);
    }

    Product(String name, double price) {
        this(name, price, 0);
    }

    Product(String name, double price, double discount) {
        this.name = name;
        this.price = price;
        this.discount = discount;
    }

    double finalPrice() {
        return price - (price * discount / 100);
    }

    void display() {
        System.out.println("Product: " + name);
        System.out.println("Original Price: Rs. " + price);
        System.out.println("Discount: " + discount + "%");
        System.out.println("Final Price: Rs. " + finalPrice());
        System.out.println();
    }

    public static void main(String[] args) {
        Product p1 = new Product();
        Product p2 = new Product("Keyboard", 1200);
        Product p3 = new Product("Headphones", 2000, 15);

        p1.display();
        p2.display();
        p3.display();
    }
}