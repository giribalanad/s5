
import java.io.*;
import java.net.*;

class arpc {
    public static void main(String[] args) throws Exception {
        Socket s = new Socket("localhost", 5800);
        BufferedReader in = new BufferedReader(new InputStreamReader(s.getInputStream()));
        PrintWriter out = new PrintWriter(s.getOutputStream(), true);
        BufferedReader kb = new BufferedReader(new InputStreamReader(System.in));

        System.out.print("Enter IP address: ");
        out.println(kb.readLine());
        System.out.println("MAC address: " + in.readLine());
        s.close();
    }
}


// Run in terminal 1 :
// >>> javac arps.java arpc.java
// >>> java arps
// Run in Terminal 2 :
// >>> java arpc