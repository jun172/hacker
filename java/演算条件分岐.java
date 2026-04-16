public class 演算条件分岐 {
    public static void main(String[] args) {
        int a = 10;
        int b = 3;

        System.out.println(a + b);// 13
        System.out.println(a - b);// 7
        System.out.println(a * b);// 30
        System.out.println(a / b);// 3
        System.out.println(a * b);// 1

        if (a > b) {
            System.out.println("aはbより大きい");
        }else {
            System.out.println("bはa以上");
        }
    }
}
