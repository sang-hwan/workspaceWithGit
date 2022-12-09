package BruteForce;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Guess {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int N, ans;
    static int[] arr;
    static char[] c_arr;
    static char[][] matrix;

    public static void main(String[] args) throws IOException{
        // 출처:
        // https://www.acmicpc.net/problem/1248
        // https://toastfactory.tistory.com/206

        N = Integer.parseInt(br.readLine());
        c_arr = br.readLine().toCharArray();
        matrix = new char[N][N];
        int idx = 0;
        for(int i=0; i<N; i++){
            for(int j=i; j<N; j++){
                matrix[i][j] = c_arr[idx++];
            }
        }
        arr = new int[N];
        dfs(0);
    }
    static void dfs(int depth){
        if(depth==N){
            for(int i=0; i<N; i++){
                System.out.println(arr[i]+" ");
            }
            System.exit(0);
            return;
        }
        for(int i=-10; i<=10; i++){
            arr[depth] = i;
            if(check(depth)) dfs(depth+1);
        }
    }

    static boolean check(int depth){
        for(int i=0; i<=depth; i++){
            int sum = 0;
            for(int j=i; j<=depth; j++){
                sum += arr[j];
                if(matrix[i][j]!=(sum==0?'0':(sum>0?'+':'-'))){
                    return false;
                }
            }
        }
        return true;
    }
}
