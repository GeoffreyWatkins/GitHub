package task7;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class Project {

    public final double TOTAL_COST;
    // Attributes
    public int projectNumber;
    public String projectName;
    public Person projectCustomer;
    public String buildingType;
    public String physicalAddress;
    public String erfNumber;
    public Person projectArchitect;
    public Person projectContractor;
    public double totalPaid;
    public Date projectDueDate;
    public boolean projectFinalised;
    public String projectCompletionDate;

    // Constructor
    public Project(int projectNumber, String projectName, Person projectCustomer, String buildingType, String physicalAddress, String erfNumber, Person projectArchitect, Person projectContractor, double TOTAL_COST, double totalPaid, String projectDueDate, boolean projectFinalised) {
        this.projectNumber = projectNumber;
        this.projectName = projectName;
        this.projectCustomer = projectCustomer;
        this.buildingType = buildingType;
        this.physicalAddress = physicalAddress;
        this.erfNumber = erfNumber;
        this.projectArchitect = projectArchitect;
        this.projectContractor = projectContractor;
        this.TOTAL_COST = TOTAL_COST;
        this.totalPaid = totalPaid;
        // Convert string date to a SimpleDate object formatted to a string
        this.setProjectDueDate(projectDueDate);
        this.projectFinalised = false;

    }

    // Method to update the totalPaid value
    public void setTotalPaid(double payment) {
        this.totalPaid += payment;
    }

    // Set projectDueDate to SimpleDate object from a string
    public void setProjectDueDate(String projectDueDate){
        try {
            this.projectDueDate = new SimpleDateFormat("dd/MMM/yyyy").parse(projectDueDate);
        } catch (ParseException e) {
            System.out.println("The error at Project(): " + e);
            this.projectDueDate = null;
        }
    }

    //Method to update the finalized value and display invoice if needed
    public void setProjectFinalised(boolean projectFinalised) {

        this.projectFinalised = true;
        this.projectCompletionDate = new SimpleDateFormat("dd/MMM/yyyy").format(new Date());
        double totalOwed = TOTAL_COST - totalPaid;

        // Test if the invoice is needed or not
        if (totalOwed > 0) {
            System.out.println("Project now finalised. See invoice below:\n" +
                    "==========================================================" +
                    "\nProject Name: " + this.projectName +
                    "\nCustomer Name: " + this.projectCustomer.personName +
                    "\nCustomer Telephone: " + this.projectCustomer.personTelephone +
                    "\nCustomer Email: " + this.projectCustomer.personEmail +
                    "\nTotal Cost: " + this.TOTAL_COST +
                    "\nTotal Paid: " + this.totalPaid +
                    "\nTotal Owed: " + totalOwed +
                    "\nProject Due Date: " + new SimpleDateFormat("dd/MMM/yyyy").format(this.projectDueDate) +
                    "\nProject Completed Date: " + this.projectCompletionDate);
        } else {
            System.out.println("Project has been paid for already." +
                    "\nProject Completed Date: " + this.projectCompletionDate);
        }
    }

    // toString
    @Override
    public String toString() {
        return "\nProjectNumber: " + this.projectNumber +
                "\nProjectName: " + this.projectName +
                "\nBuildingType: " + this.buildingType +
                "\nPhysicalAddress: " + this.physicalAddress +
                "\nERF Number: " + this.erfNumber +
                "\nTOTAL_COST: " + this.TOTAL_COST +
                "\nTotalPaid: " + this.totalPaid +
                "\nProjectFinishedDate: " + this.projectDueDate +
                "\nProjectFinalised: " + this.projectFinalised +
                "\nProjectCompletionDate: " + this.projectCompletionDate;
    }

}
