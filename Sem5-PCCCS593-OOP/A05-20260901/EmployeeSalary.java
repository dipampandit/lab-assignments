interface Employee {
    double calculateSalary();
}

class FullTimeEmployee implements Employee {
    double monthlySalary;

    FullTimeEmployee(double monthlySalary) {
        this.monthlySalary = monthlySalary;
    }

    public double calculateSalary() {
        return monthlySalary;
    }
}

class PartTimeEmployee implements Employee {
    int hours;
    double hourlyRate;

    PartTimeEmployee(int hours, double hourlyRate) {
        this.hours = hours;
        this.hourlyRate = hourlyRate;
    }

    public double calculateSalary() {
        return hours * hourlyRate;
    }
}

class ContractEmployee implements Employee {
    double contractAmount;

    ContractEmployee(double contractAmount) {
        this.contractAmount = contractAmount;
    }

    public double calculateSalary() {
        return contractAmount;
    }
}

public class EmployeeSalary {
    public static void main(String[] args) {
        Employee e1 = new FullTimeEmployee(30000);
        Employee e2 = new PartTimeEmployee(80, 200);
        Employee e3 = new ContractEmployee(25000);

        System.out.println("Full Time Salary: " + e1.calculateSalary());
        System.out.println("Part Time Salary: " + e2.calculateSalary());
        System.out.println("Contract Salary: " + e3.calculateSalary());
    }
}