import java.io.*;
import java.util.*;
import java.math.*;
import java.math.BigInteger;

public class boaz_wa {
	public BigInteger bc;
	public String[] bs;
	public static String ERROR = "error";
    public static BigInteger MOD_VAL = new BigInteger("1000000007");
    public static BigInteger MAX_B = new BigInteger("1152921504606846976");
	static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
	public boaz_wa() {}

	public static void main(String[] args) throws Exception {
		new boaz_wa().solve();
	}

	public static void out(Object o, boolean newline) {
		if (newline) System.out.println(o.toString());
		else System.out.print(o.toString());
		System.out.flush();
	}

	public static void out(Object o) {
		out(o, true);
	}

	public void solve() throws Exception {
		while(true) {
			boolean stop = read_input();
			if (stop) return;
			magic();
		}
	}

	public void magic() throws Exception {
		bc = new BigInteger("1");
		boolean do_modulo = false;
		for (String b_string : bs) {
			BigInteger b = new BigInteger(b_string);
            bc = bc.multiply(new BigInteger("2"));
			if (!do_modulo && b.compareTo(bc) > 0) {
                out("error");
                return;
            }
            if (bc.compareTo(MAX_B) > 0)
				do_modulo = true;
			if (do_modulo) {
				bc = bc.mod(MOD_VAL);
				bc = bc.add(MOD_VAL);
				bc = bc.mod(MOD_VAL);
			}

			bc = bc.subtract(b);
		}

        out(bc); // Forget to do modulo afterward substracting
	}

	public boolean read_input() throws Exception {
		String input = in.readLine();
		if (input == null) return true;
		long n = Long.parseLong(input);

		input = in.readLine();
		bs = input.split(" ");

		return false;
    }
}
