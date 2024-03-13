package collage_programes;

public class Constructors {
	String lang;
	String name;
	//parameter constructor
	Constructors(String language){
		lang=language;
		System.out.println(lang+" Programming language");
	}
	//Default constructor
	Constructors(){
		System.out.println("The default constructor");
		name="java";
	}
	public static void main(String[] args) {
		Constructors s2=new Constructors();
		System.out.println("The name is "+s2.name);
		
		Constructors s1=new Constructors("Java");
		Constructors s3=new Constructors("Python");
	}
	
}
