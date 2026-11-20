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

        // Change the shared static variable
        Student.college = "GKCIET";

        s1.display();
        s2.display();
    }
}