class Person {
    String name;
    int age;

    Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
}

class Student extends Person {
    int roll;
    String department;

    Student(String name, int age, int roll, String department) {
        super(name, age);
        this.roll = roll;
        this.department = department;
    }

    void display() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("Roll: " + roll);
        System.out.println("Department: " + department);
    }

    public static void main(String[] args) {
        Student s = new Student("Dipam", 22, 007, "CSE AI & ML");
        s.display();
    }
}