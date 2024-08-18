import java.io.*;
import java.util.*;

/* 메모리 초과 */
/**/
class Reverse{
    public static void main(String[] args) throws Exception{
        // Get params
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String str = "";
        str = br.readLine();

        int cnt = 0;
        cnt = Integer.parseInt(str);
        for (int i=0;i<cnt;i++){
            ArrayList<String> words = new ArrayList<>();
            String line = "";
            line = br.readLine(); // hello world

            // words = [hello, word]
            String[] arr;
            arr = line.split(" ");
            for(String temp: arr){
                words.add(temp);
            }

            // word = word // temp = drow // words[1] = temp
            // word = hello // temp = olleh // words[0] = temp
            String word = "";
            String reversed = "";
            Stack<Character> stk = new Stack<>();
            for (int j=0; j<words.size();j++){
                word = words.get(j);
                String[] q;
                q = word.split("");
                for (String tmp: q){
                    // System.out.println(tmp);
                    Character c;
                    c = tmp.charAt(0);
                    stk.push(c);
                }
                for (String tmp: q){
                    reversed += stk.pop();
                }
                // System.out.println(reversed);
                reversed += " ";
                // System.out.println("-----END Word------");
            }
            // System.out.println(reversed);
            bw.write(reversed);
            bw.flush();
            System.out.println();
            // System.out.println("--------END Sentence----------");
        }
        bw.close();
        br.close();
    }
} 

// Tips!
/*
    1. Main 클래스 외 추가 클래스 생성 시, public없이 그냥 class로 생성!
    2. 입력: BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    3. 스플릿: StringTokenizer st = new StringTokenizer(br.reaLine());
                int s = Integer.parseInt(st.nextToken());
    4. 출력: BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

*/