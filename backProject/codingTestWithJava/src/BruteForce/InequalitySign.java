package BruteForce;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class InequalitySign {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int N;
    static char[] inequality = new char[10];
    static boolean[] visit = new boolean[10];
    static List<String> ans = new ArrayList<>();

    public static void main(String[] args) throws IOException{
        // 출처:
        // https://www.acmicpc.net/problem/2529
        // https://pangtrue.tistory.com/283

        N = Integer.parseInt(br.readLine());
        inequality = new char[N];
        String[] input = br.readLine().split(" ");
        for(int i=0; i<N; i++){
            inequality[i] = input[i].charAt(0);

        }

        dfs("", 0);
        Collections.sort(ans);
    
        System.out.println(ans.get(ans.size()-1));
        System.out.println(ans.get(0));
    }
    static void dfs(String num, int depth){
        if(depth==N+1){
            ans.add(num);
            return;
        }

        for(int i=0; i<=9; i++){
            if(visit[i]) continue;
            if(depth==0 || check(Character.getNumericValue(num.charAt(depth-1)), i, inequality[depth-1])){
                visit[i] = true;
                dfs(num+i, depth+1);
                visit[i] = false;
            }
        }
    }

    static boolean check(int a, int b, char c){
        if(c == '<'){
            if(a>b) return false;
        }else if(c=='>'){
            if(a<b) return false;
        }
        return true;
    }
}
