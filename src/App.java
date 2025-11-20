/*
This code consists of a password manager application that works through a Command Line Interface.
This project was started on 11/18 at 2:10 AM. It was being developed because I was simply saving my passwords in a .txt file.
It wasn't organized no matter how hard we tried. With this application, the organization will be much better.

Starting Date: 11/18/2025 - Finish Date: "ongoing"

Version 0.0.0 -> 11/18/2025
Version 0.0.1 -> 11/XX/2025
Version 0.0.0 -> 11/XX/2025
Version 0.0.0 -> 11/XX/2025
Version 0.0.0 -> 11/XX/2025
*/

import java.util.Scanner;

public class App {
    static Scanner Scanner = new Scanner(System.in);

    static String UserLogIn = "";
    static String PassLogIn = "";

    static void LoginApp() { /* Just a test */
        System.out.printf("---------------LogIn App---------------\n");
        System.out.printf("\n   User/Email:\n->");
        UserLogIn = Scanner.nextLine();
        System.out.printf("\n   Password:\n->");
        PassLogIn = Scanner.nextLine();
    }

    static void ClearScreen() {
        // Clear the console screen and print the app header
        System.out.print("\033[H\033[2J");
        System.out.flush();
    }
    public static void main(String[] args) throws Exception {
        ClearScreen();
        System.out.println("Hello, World!");
    }
}
