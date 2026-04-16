public class 例外処理 {
    public static void main(String[] ares){
        try {
            System.out.println(10 / 0);
        } catch (ArithmeticException e) {
            System.out.println();
        }
    }
}