import java.util.Scanner;

public class 基礎 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int answer = 7;//正解

        System.out.println("1~10の数字を当ててください");

        for (int i = 0; i < 3; i++) {
            System.out.print("あなたの予想:");
            int guess = scanner.nextInt();

            if (guess == answer) {
                System.out.println("正解!");
                break;
            }else if (guess < answer) {
                System.out.println("小さいです");
            }else {
                System.out.println("大きいです");
            }
        }

        System.out.println("ゲーム終了");
    }
}