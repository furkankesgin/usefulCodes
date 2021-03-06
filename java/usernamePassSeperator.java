import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.PrintWriter;

public class Seperator {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
File file = new File("C:\\Users\\FURKAN\\Desktop/TEXT.txt");
		
		String passwords[] = new String[10000000];
		String usernames[] = new String[10000000];
		String s[] = new String[10000000];
		
		
		//okuma
		
		try {
		  BufferedReader br = new BufferedReader(new FileReader(file));
		  int i = 0;
		  while ((s[i] = br.readLine()) != null) { 
			// System.out.println(s[i]);
		 i++;
		  }
		  }
		  catch (Exception e) {
			System.out.println("OKUYAMADIM");
		}
 
		
		//kesme
		
		
		try {
		int i = 0; 
			while(s[i] != null) {
			passwords[i] = s[i].substring(s[i].indexOf(":")+1); 
			usernames[i] = s[i].substring(0,s[i].indexOf(":")); 
			//System.out.println(passwords[i]);
		i++;
		}
		}
		
		catch (Exception e) {
			System.out.println("BITTI");
		}
 
		
		//yazma
		
		
		try {
		PrintWriter writer = new PrintWriter("passwods.txt", "UTF-8");
       for (int i = 0; i < passwords.length; i++) {
    	   if(passwords[i] == null) {
				break;
			}
    	   writer.println(passwords[i]);
       }
		writer.close();
		
		 writer = new PrintWriter("user_names.txt", "UTF-8");
	       for (int i = 0; i < usernames.length; i++) {
			if(usernames[i] == null) {
				break;
			}
	    	   writer.println(usernames[i]);
	       }
			writer.close();
			
		}
		catch (Exception e) {
			System.out.println("YAZAMADIM");
		}
			 
		
	}

}
