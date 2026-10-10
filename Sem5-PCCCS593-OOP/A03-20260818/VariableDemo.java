class Student {
    String name;             // Instance variable
    int marks;               // Instance variable
    static String college = "ABC College"; // Static variable

    Student(String name, int marks) {
        this.name = name;
        this.marks = marks;
    }

    void display(int marks) {
        int bonus = 5;  // Local variable

        System.out.println("Name: " + this.name);
        System.out.println("Instance marks: " + this.marks);
        System.out.println("Local marks: " + marks);
        System.out.println("Bonus: " + bonus);
        System.out.println("College: " + Student.college);
        System.out.println();
    }
}

public class VariableDemo {
    public static void main(String[] args) {
        Student s1 = new Student("Rahul", 80);
        Student s2 = new Student("Priya", 90);

        s1.display(70);
        s2.display(85);

        Student.college = "XYZ College";

        System.out.println("Updated college: " + Student.college);
    }
}