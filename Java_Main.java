public class Java_Main {
	public void func(){
		for(int i=0;i<100;i++) {
		    if(i%2==0){
				System.out.println(i); 
			}
		}
	}
	static public void main(String args[]) {
		Java_Main obj=new Java_Main(); 
		obj.func();
	}
}