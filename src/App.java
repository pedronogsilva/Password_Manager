/*
This code consists of a password manager application that works through a Command Line Interface.
This project was started on 11/18 at 2:10 AM. It was being developed because I was simply saving my passwords in a .txt file.
It wasn't organized no matter how hard we tried. With this application, the organization will be much better.

Starting Date: 11/18/2025 - Finish Date: "ongoing"

Version 0.0.0 -> 11/18/2025
Version 0.0.1 -> 11/22/2025 -> XX/XX/202X (Visual)
Version 0.0.0 -> XX/XX/202X -> XX/XX/202X
Version 0.0.0 -> XX/XX/202X -> XX/XX/202X
Version 0.0.0 -> XX/XX/202X -> XX/XX/202X
*/

import java.util.Scanner;

public class App {
    static Scanner Scanner = new Scanner(System.in);

    static int Option;
    static String UserLogIn = "";
    static String PassLogIn = "";

    static void LoginApp() { /* Just a test */
        System.out.printf("---------------LogIn App---------------\n");
        System.out.printf("\n   User/Email:\n->");
        UserLogIn = Scanner.nextLine();
        System.out.printf("\n   Password:\n->");
        PassLogIn = Scanner.nextLine();
    }

    static void Exit() {
        ClearScreen();
        System.out.printf("---------------Exit App---------------\n");
        System.out.printf("          Exiting the App");
    }

    static void ClearScreen() {
        // Clear the console screen and print the app header
        System.out.print("\033[H\033[2J");
        System.out.flush();
    }
    public static void main(String[] args) throws Exception {
        while (true) {
            ClearScreen();

            System.out.printf("----------------Menu App---------------\n");
            System.out.printf("    [1] View Passwords\n    [2] Add Passwords\n    [3] Edit Paswords\n    [4] Delete Passwords\n    [5] Exit App\n->");
            Option = Scanner.nextInt();

            switch (Option) {
                case 1:
                    System.out.printf("1");
                    break;
                case 2:
                    System.out.printf("2");
                    break;
                case 3:
                    System.out.printf("3");
                    break;
                case 4:
                    System.out.printf("4");
                    break;
                case 5:
                    Exit();
                    return;
                default:
                    System.out.printf("Invalid Option! Please try again.\n");
                    break;
            }
        }
        //System.out.println("Hello, World!");
    }
}
