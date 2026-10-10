class Student {
    String name;
    int marks;

    Student(String name, int marks) {
        this.name = name;
        this.marks = marks;
    }
}

public class ReferenceDemo {
    public static void main(String[] args) {
        Student s1 = new Student("Rahul", 85);

        // Both references point to the same object
        Student s2 = s1;

        System.out.println("Using s1: " + s1.name + ", " + s1.marks);
        System.out.println("Using s2: " + s2.name + ", " + s2.marks);

        // Modify data using s2
        s2.marks = 95;

        System.out.println("Marks through s1: " + s1.marks);
        System.out.println("Marks through s2: " + s2.marks);

        // Set one reference to null
        s2 = null;

        System.out.println("After setting s2 to null:");
        System.out.println("Marks through s1: " + s1.marks);
        System.out.println("s2: " + s2);
    }
}