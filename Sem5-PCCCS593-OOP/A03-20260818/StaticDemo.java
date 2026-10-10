class Student {
    static String college = "ABC College";
    String name;

    Student(String name) {
        this.name = name;
    }

    void display() {
        System.out.println(name + " studies at " + college);
    }
}

public class StaticDemo {
    public static void main(String[] args) {
        Student s1 = new Student("Rahul");
        Student s2 = new Student("Priya");

        // Access static variable through objects
        System.out.println(s1.college);
        System.out.println(s2.college);

        // Access static variable through class
        System.out.println(Student.college);

        // Change the shared static variable
        Student.college = "XYZ College";

        s1.display();
        s2.display();
    }
}