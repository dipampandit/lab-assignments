interface Payment {
    void pay(double amount);
}

class CreditCard implements Payment {
    public void pay(double amount) {
        System.out.println("Paid Rs. " + amount + " using Credit Card");
    }
}

class UPI implements Payment {
    public void pay(double amount) {
        System.out.println("Paid Rs. " + amount + " using UPI");
    }
}

class Cash implements Payment {
    public void pay(double amount) {
        System.out.println("Paid Rs. " + amount + " using Cash");
    }
}

public class PaymentDemo {
    public static void main(String[] args) {
        Payment p;

        p = new CreditCard();
        p.pay(1500);

        p = new UPI();
        p.pay(750);

        p = new Cash();
        p.pay(300);
    }
}