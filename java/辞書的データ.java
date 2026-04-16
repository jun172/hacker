import java.util.HashMap;

public class 辞書的データ {
    public static void main(String[] args) {
        HashMap<String, String> user = new HashMap<>();
        user.put("name","John");
        user.put("email","john@example.com");

        System.out.println(user.get("name"));
    }
}
