package main;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class DriverTest {

	@Test
	public void test_demoMethod() {
		Driver driverObject = new Driver();
		int actual = driverObject.doubleIt(13);
		int expected = 26;
		
		Assertions.assertEquals(expected, actual);
	}
	
	@Test
	public void test_getRomanNumber() {
		Driver driverObject = new Driver();
		String actual = driverObject.getRomanNumber(1);
		String expected = "I";
		
		Assertions.assertTrue(expected.equals(actual));
	}
}
