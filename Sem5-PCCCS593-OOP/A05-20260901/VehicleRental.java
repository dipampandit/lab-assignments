interface Vehicle {
    double calculateRent(int days);
}

class Car implements Vehicle {
    public double calculateRent(int days) {
        return days * 2000;
    }
}

class Bike implements Vehicle {
    public double calculateRent(int days) {
        return days * 500;
    }
}

class Bus implements Vehicle {
    public double calculateRent(int days) {
        return days * 5000;
    }
}

public class VehicleRental {
    public static void main(String[] args) {
        int days = 3;

        Vehicle car = new Car();
        Vehicle bike = new Bike();
        Vehicle bus = new Bus();

        System.out.println("Car Rent: " + car.calculateRent(days));
        System.out.println("Bike Rent: " + bike.calculateRent(days));
        System.out.println("Bus Rent: " + bus.calculateRent(days));
    }
}