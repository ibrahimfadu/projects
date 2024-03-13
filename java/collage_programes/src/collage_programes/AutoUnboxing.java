package collage_programes;

public class AutoUnboxing {

	public static void main(String[] args) {
		int i=50;
		Integer a=new Integer(i);
		Integer a2=5;
		System.out.println(a+" "+a2);
		
		Integer b=new Integer(50);
		int c=b;
		System.out.println(c);
	}

}
