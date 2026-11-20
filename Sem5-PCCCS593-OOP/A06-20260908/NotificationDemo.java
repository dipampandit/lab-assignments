interface Notification {
    void send(String message);
}

class EmailNotification implements Notification {
    public void send(String message) {
        System.out.println("Email: " + message);
    }
}

class SMSNotification implements Notification {
    public void send(String message) {
        System.out.println("SMS: " + message);
    }
}

class WhatsAppNotification implements Notification {
    public void send(String message) {
        System.out.println("WhatsApp: " + message);
    }
}

public class NotificationDemo {
    public static void main(String[] args) {
        Notification n;

        n = new EmailNotification();
        n.send("Your order is confirmed.");

        n = new SMSNotification();
        n.send("Your OTP is 123456.");

        n = new WhatsAppNotification();
        n.send("Your package is on the way.");
    }
}