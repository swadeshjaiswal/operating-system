
package javaapplication1;

import java.util.Scanner;

/**
 *
 * @author Student
 */
public class Producer_Consumer {

    static int mutex=1,E=5,f=0;
    static int wait(int s){
        return --s;
    }
    static int signal(int s){
        return ++s;
    }
    static void producer(){
        mutex= wait (mutex);
        f= signal(f);
        E=wait(E);
        System.out.println("producer is done");
        mutex=signal(mutex);
    }
    static void consumer(){
        mutex=wait(mutex);
        f=wait(f);
        E= signal(E);
        System.out.println("consumer is done");
        mutex=signal(mutex);
    }
    
    public static void main(String[] args) {
        
        while(true){
                System.out.println("Enter 1 for producer");
        System.out.println("Enter 2 for consumer");
        Scanner sc =new Scanner(System.in);
        int a= sc.nextInt();
        
        switch(a){
            case 1:
                if(mutex==1 && f!=5)
                    producer();
                else
                    System.out.println("producer waiting");
                break;
            case 2:
                if (mutex==1 && E!=5) {
                    consumer();
                }
                else
                    System.out.println("consumer waiting");
                break;
            case 3:
                System.exit(a);
        }}
    }}
    

