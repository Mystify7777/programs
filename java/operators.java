public class operators {
    public static void main(String[] args) {
        int i = 10;

        System.out.println(i++); // 10
        System.out.println(i); // 11    
        System.out.println(++i); // 12
        System.out.println(i); // 12

        int add = i + 3;
        System.out.println(add); // 15

        int sub = i - 3;
        System.out.println(sub); // 9

        int mul = i * 3;  
        System.out.println(mul); // 36

        int div = i / 3;
        System.out.println(div); // 4

 
        int mod = i % 3;
        System.out.println(mod); // 0

        int a = 10;
        int b = 20;

        System.out.println(a == b); // false
        System.out.println(a != b); // true
        System.out.println(a > b); // false
        System.out.println(a < b); // true
        System.out.println(a >= b); // false
        System.out.println(a <= b); // true

        boolean x = true;
        boolean y = false;

        System.out.println(x && y); // false
        System.out.println(x || y); // true
        System.out.println(!x); // false
        System.out.println(!y); // true


        System.out.println(10/0.0);
        System.out.println(0.0/0.0);
        // System.out.println(0/0);

        byte b1 = 10;
        byte b2 = 20;

        //  byte b3 = b1 + b2; // error
        byte b31 = (byte)(b1 + b2);
        System.out.println(b31); // 30
        int b12 = b1 + b2;
        System.out.println(b12); // 30

        String s1 = "Hello";
        int s2 = 10;
        int s3 = 20;

        System.out.println(s1 + s2 + s3); // Hello1020
        System.out.println(s2 + s3 + s1); // 30Hello
        System.out.println(s2 + s3 ); // 30Hello1020


        System.out.println(4 & 5);

        System.out.println(4 | 5);

        System.out.println(4 ^ 5);

        System.out.println(~4);

        System.out.println(4 << 2);

        System.out.println(4 >> 2);

        System.out.println(4 >>> 2);

        System.out.println(-4 >> 2);

        System.out.println(-4 >>> 2);

        System.out.println(4 < 5 && 5 < 6);

        System.out.println(4 < 5 || 5 < 6);

        int a1 = 10;
        int a2 = 20;

         a2 += a1; // a2 = a2+a1
        System.out.println(a2); // 30

        a2 -= a1;
        System.out.println(a2); // 20

        a2 *= a1;
        System.out.println(a2); // 200

        a2 /= a1;
        System.out.println(a2); // 20

        //ternary operator

        int a3 = 10;
        int a4 = 25;

        int a5 = a3 > a4 ? a3 : a4;
        System.out.println(a5); // 25

        //new operator

        // test t = new test();
        // t.display();

        int arr[] = new int[5];
        arr[0] = 10;


        //operator precedence

        // -- > ++ > + > - > * > / > % > << > >> > >>> > & > ^ > | > && > || > ? > = > += > -= > *= > /= > %= > &= > ^= > |= > <<= > >>= > >>>=

        //flow control

        // if else

        int age = 20;

        if(age > 18){
            System.out.println("You can vote");
        }else{
            System.out.println("You can't vote");
        }   

        //nested if else

        int age1 = 20;
        int weight = 80;    

        if(age1 > 18){
            if(weight > 40){
                System.out.println("You can vote");
            }else{
                System.out.println("You can't vote");
            }

        }else{
            System.out.println("You can't vote");
        }


        //switch case

        int day = 9;
        switch (day) {
            case 1:
                System.out.println("Monday");
                break;
            case 2:
                System.out.println("Tuesday");
                break;
            case 3:
                System.out.println("Wednesday");
                break;
            case 4:
                System.out.println("Thursday");
                break;
            case 5:
                System.out.println("Friday");
                break;
            case 6:
                System.out.println("Saturday");
                break;
            case 7:
                System.out.println("Sunday");
                break;
            default:
                System.out.println("Invalid day");
                
        }

        //loops

        //for loop
        System.out.println("For loop 1");
        for(int j = 0; j < 5; j++){
            System.out.println(j);
        }
        System.out.println("For loop 2");
        for(int j = 0; j < 5; ++j){
            System.out.println(j);
        }

        //while loop
        System.out.println("While loop");
        int k = 0;
        while(k < 5){
            System.out.println(k);
            k++;
        }

        System.out.println("While loop");
        int k1 = 0;
        while(k1 < 5){
            System.out.println(k1++);
            // k1++;
        }

        System.out.println("While loop");
        int k2 = 0;
        while(k2 < 5){
            System.out.println(++k2);
            // k++;
        }

        //do while loop
        System.out.println("Do while loop");
        int l = 0;
        do{
            System.out.println(l);
            l++;
        }while(l < 5);

        System.out.println("Do while loop 2");

        int l1 = 10;
        do{
            System.out.println(l1);
            l1++;
        }while(l1 < 5);

        //break and continue
        System.out.println("Break ");
        for(int m = 0; m < 5; m++){
            if(m == 3){
                break;
            }
            System.out.println(m);
        }
        System.out.println("Continue ");
        for(int m = 0; m < 5; m++){
            if(m == 3){
                continue;
            }
            System.out.println(m);
        }


        int arr1[] = {10, 20, 30, 40, 50};

        int arr2[] ={12345, 123, 12, 1, 0};
        //EOF
    }
}
