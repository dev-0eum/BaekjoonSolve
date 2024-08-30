import java.io.*;
import java.util.ArrayList;

public class Stack{
    public static void main(String[] args) throws Exception{
        
        // Get params
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = "";
        str = br.readLine();

        int cnt = 0;
        cnt = Integer.parseInt(str);
        
        int size = 0;
        int top = -1;
        ArrayList<Integer> arr = new ArrayList<>();

        for(int i=0;i<cnt;i++){
            String q = "";
            q = br.readLine();
            // System.out.println(i+":"+q);

            String[] cmd = q.split(" ");
            
            if(cmd[0].equals("push")){
                int tmp = Integer.parseInt(cmd[1]);
                arr.add(tmp);
                top++; 
                size++;
            }
            else if(cmd[0].equals("pop")){ // print top & del
                if(size < 1)
                    System.out.println(-1);
                else{
                    System.out.println(arr.get(top));
                    arr.remove(top--);
                    size--;
                }
            }
            else if(cmd[0].equals("top")){ // print
                if(size < 1)
                    System.out.println(-1);
                else
                    System.out.println(arr.get(top));
            }
            else if(cmd[0].equals("empty")){
                if(size==0)
                    System.out.println(1);
                else
                    System.out.println(0);
            }
            else if(cmd[0].equals("size")){
                System.out.println(size);
            }
            // System.out.println("top: "+top);
        }
    }

}
