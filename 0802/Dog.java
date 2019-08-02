package animal;

public class Dog extends Animal implements See {

	@Override
	public void seeDoor() {
		System.out.println("看家");

	}

	@Override
	public void eat() {
		System.out.println("吃狗粮");

	}

}
