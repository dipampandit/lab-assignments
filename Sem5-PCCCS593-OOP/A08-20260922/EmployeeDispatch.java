class Employee {
    double calculateSalary() {
        return 0;
    }
}

class FullTime extends Employee {
    double calculateSalary() {
        return 40000;
    }
}

class PartTime extends Employee {
    double calculateSalary() {
        return 15000;
    }
}

class Intern extends Employee {
    double calculateSalary() {
        return 8000;
    }
}

public class EmployeeDispatch {
    public static void main(String[] args) {
        Employee e;

        e = new FullTime();
        System.out.println("Full Time Salary: " + e.calculateSalary());

        e = new PartTime();
        System.out.println("Part Time Salary: " + e.calculateSalary());

        e = new Intern();
        System.out.println("Intern Salary: " + e.calculateSalary());
    }
}