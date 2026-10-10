
import java.io.*;
import java.net.*;

class arps {
    public static void main(String[] args) throws Exception {
        ServerSocket ss = new ServerSocket(5800);
        String[] ip = {"172.16.5.200", "172.16.5.201", "172.16.5.202"};
        String[] mac = {"AA:BB:CC:00:00:01", "AA:BB:CC:00:00:02", "AA:BB:CC:00:00:03"};

        Socket s = ss.accept();
        BufferedReader in = new BufferedReader(new InputStreamReader(s.getInputStream()));
        PrintWriter out = new PrintWriter(s.getOutputStream(), true);
        String addr = in.readLine(), result = "Not found";

        for (int i = 0; i < ip.length; i++)
            if (ip[i].equals(addr)) result = mac[i];

        out.println(result);
        s.close();
        ss.close();
    }
}



// Run in terminal 1 :
// >>> javac arps.java arpc.java
// >>> java arps
// Run in Terminal 2 :
// >>> java arpc