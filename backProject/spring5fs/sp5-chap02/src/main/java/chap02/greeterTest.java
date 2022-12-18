package chap02;

public class greeterTest {
    public static void main(String[] args) {
        Greeter greeter = new Greeter();
        greeter.setFormat("%s, 안녕하세요!");
        String msg = greeter.greet("스프링");
        System.out.println(msg);
    }
}
