public class ArrayRony {
    public static void main(String[] args) {
        int count = 0;
        int[] numbers = {9, 2, 3, 0, 0, 4, 0, 0, 0, 6};
        for(int i : numbers){
            if(i == 0){
                count++;
                continue;
            }else{
                System.out.print(i+" ");
            }
        }
        for(int i=0; i<count; i++){
            System.out.print("0 ");
        }
    }
}
