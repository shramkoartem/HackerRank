import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

/* 
Instance variables are initialized using initialization blocks. 
However, the static initialization blocks can only initialize the static instance variables. 
These blocks are only executed once when the class is loaded. 
There can be multiple static initialization blocks in a class that is called in the order they appear in the program. */

    static Scanner input = new Scanner(System.in);

    static boolean flag = true;
    static int H = input.nextInt();
    static int B = input.nextInt();

static{

    try{
        if(B<=0 || H<=0){
            flag = false;
            throw new Exception("Breadth and height must be positive");
        }
    }
    catch(Exception e){
        System.out.println(e);
        }
    }


public static void main(String[] args){
		if(flag){
			int area=B*H;
			System.out.print(area);
		}
		
	}

}

