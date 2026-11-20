class Bank {
    double getRateOfInterest() {
        return 0.0;
    }
}

class SBI extends Bank {
    double getRateOfInterest() {
        return 2.5;
    }
}

class HDFC extends Bank {
    double getRateOfInterest() {
        return 3.0;
    }
}

class ICICI extends Bank {
    double getRateOfInterest() {
        return 3.0;
    }
}

public class BankInterest {
    public static void main(String[] args) {
        Bank b;

        b = new SBI();
        System.out.println("SBI Interest: " + b.getRateOfInterest() + "%");

        b = new HDFC();
        System.out.println("HDFC Interest: " + b.getRateOfInterest() + "%");

        b = new ICICI();
        System.out.println("ICICI Interest: " + b.getRateOfInterest() + "%");
    }
}
