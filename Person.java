package task7;

public class Person {

	// Attributes
	   String personType; 
	   String personName;
	   String personTelephone;
	   String personEmail;
	   String personAddress;
	   
    // Constructor  
	public Person(String personType, String personName, String personTelephone, String personEmail, String personAddress) {
		this.personType = personType;
		this.personName = personName;
		this.personTelephone = personTelephone;
		this.personEmail = personEmail;
		this.personAddress = personAddress;
	}

	// toString
	@Override
	public String toString() {
		return  "PersonName: " + personName + 
				"PersonTelephone: " + personTelephone + 
				"PersonEmail: "	+ personEmail + 
				"PersonAddress: " + personAddress;
	}
	   
	   
	}


