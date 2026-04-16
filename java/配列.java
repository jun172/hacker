public class 配列 {
    public static void main(String[] ares) {
        int[] numbers = {5,2,10,7,1};
        for (int i = 0; i < numbers.length; i++) {
            System.out.println(numbers[i]);
        }

        //最大値
        int max = numbers[0];
        for (int i = 1; i < numbers.length; i++) {
            if (numbers[i] > max) {
                max = numbers[i];
            }
        }
        System.out.println("最大値:"+ max);
    }
}
