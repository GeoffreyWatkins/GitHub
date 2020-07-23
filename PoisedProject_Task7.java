package task7;

import java.util.Scanner;

public class PoisedProject_Task7 {

    public static void main(String[] args) {
        // created a scanner to get the input form the user
        PoisedProject_Task7 pp7 = new PoisedProject_Task7();
        Scanner userInput = new Scanner(System.in);

        // create the persons needed for the Project
        Person contractor = pp7.createPerson("Contractor");
        Person architect = pp7.createPerson("Architect");
        Person customer = pp7.createPerson("Customer");

        // creating a Project
        Project geoffreyProject = pp7.createProject(customer, architect, contractor);

        // give the user the option to edit anything if they wanted to do so
        System.out.println("Please select on of the options form the menu below (enter to finalise project): \n1) Change due date\n2) Make a payment\n3) Update contractor details");
        String userChoice = userInput.nextLine();

        // Edit the selected user choice
        if (userChoice.equals("1")) {
            System.out.println("Enter the Project total Due date (dd/MMM/yyyy):");
            geoffreyProject.setProjectDueDate(userInput.nextLine());
        } else if (userChoice.equals("2")) {
            System.out.println("Enter the payment amount:");
            geoffreyProject.setTotalPaid(userInput.nextDouble());
        } else if (userChoice.equals("3")) {
            System.out.println("Enter new Email address: ");
            contractor.personEmail = userInput.nextLine();
            System.out.println("Enter new Telephone number: ");
            contractor.personTelephone = userInput.nextLine();
        } else if (userChoice.equals("")){
            geoffreyProject.setProjectFinalised(true);
        } else {
            System.out.println("Invalid choice");
        }

        // Close the scanner
        userInput.close();
    }

    // Method returns a newly created person object
    public Person createPerson(String personType){
        // Create a scanner to get the user input
        Scanner userInput = new Scanner(System.in);

        //Display instructions to user
        System.out.println("Please enter the following " + personType + " details:");

        // Get relevant information from the user to create a project
        System.out.println(personType + " Name and Surname:");
        String personName = userInput.nextLine();
        System.out.println(personType + " Telephone Number:");
        String personTelephone = userInput.nextLine();
        System.out.println(personType + " Email Address:");
        String personEmail = userInput.nextLine();
        System.out.println(personType + " Physical Address:");
        String personAddress = userInput.nextLine();

        // return a new person with user inputed data
        return new Person(personType, personName, personTelephone, personEmail, personAddress);
    }

    // Method returns a newly created project object
    public Project createProject(Person customer, Person architect, Person contractor){
        // Create a scanner to get the user input
        Scanner userInput = new Scanner(System.in);

        //Display instructions to user
        System.out.println("Please enter the following project details:");

        // Get relevant information from the user to create a project
        System.out.println("Enter the Project number:");
        int projectNumber = userInput.nextInt();
        // Move to the next line after getting the int
        userInput.nextLine();
        System.out.println("Enter the Project name:");
        String projectName = userInput.nextLine();
        System.out.println("Enter the building type:");
        String buildingType = userInput.nextLine();
        System.out.println("Enter the building physical address:");
        String physicalAddress = userInput.nextLine();
        System.out.println("Enter the Project ERF:");
        String erfNumber = userInput.nextLine();
        System.out.println("Enter the Project total price:");
        double totalCost = userInput.nextDouble();
        // Move to the next line after getting the double
        userInput.nextLine();
        System.out.println("Enter the Project total paid:");
        double totalPaid = userInput.nextDouble();
        // Move to the next line after getting the double
        userInput.nextLine();
        System.out.println("Enter the Project total Due date (dd/MMM/yyyy):");
        String projectDueDate = userInput.nextLine();
        System.out.println();

        // return a new project with user inputed data
        return new Project(projectNumber, projectName, customer, buildingType, physicalAddress, erfNumber, architect, contractor, totalCost, totalPaid, projectDueDate, false);
    }
}
