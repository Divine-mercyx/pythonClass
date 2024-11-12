import java.util.Scanner;

public class EmployeeTest {
	public static void main(String... args) {
		Scanner input = new Scanner(System.in);

		Employee person1 = new Employee("Divine", "Obinali", 500000);
		Employee person2 = new Employee("Leke", "Opaleye", 400000);

		System.out.println(person1.getFullName());
		System.out.println(person2.getFullName());

		double raise = 1 + (10 / 100);
		double account1 = person1.getMonthlySalary() * raise;
		double account2 = person2.getMonthlySalary() * raise;


		System.out.println(account1);
		System.out.println(account2);
	}
}