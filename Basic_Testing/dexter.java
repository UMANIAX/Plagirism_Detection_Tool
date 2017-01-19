package nonGraded;

import java.util.*;

public class dexter {

	int count=0;
	
	public static void main(String[] args){
		
		Scanner bucky=new Scanner(System.in);
		
		for(int t=bucky.nextInt();t>0;t--){
			
			int n=bucky.nextInt(),m=bucky.nextInt();
			
			int mach[]=new int[n];
			
			for(int i=0;i<n;i++)
				mach[i]=bucky.nextInt();
		
			int min=1000000;
			
			for(int i=0;i<n;i++){
				
				if(mach[i]<min)
					min=mach[i];
			}
			
			ArrayList<Integer> batt=new ArrayList<Integer>();
			dexter obj=new dexter();
			
			for(int i=min;i<=m;i++){
				
				if(obj.prime(i)==1)
					batt.add(i);
			}
			
			ArrayList<Integer> temp=new ArrayList<Integer>();
			
			obj.cases(temp,mach,batt,0);
			
			System.out.println(obj.count);
			obj.count=0;
		}
	}
	
	public int prime(int num){
		
		if(num==1)
			return 1;
		
		if(num==2)
			return 0;
		
		int check=0;
		
		for(int i=2;i<num;i++){
			
			if(num%i==0){
				
				check=1;
				break;
			}
		}
		
		if(check==1)
			return 1;

		return 0;
	}
	
	public void cases(ArrayList<Integer> temp,int mach[],ArrayList<Integer> batt,int index){
	
		
		for(int j=0;j<batt.size();j++){
			
			if(temp.contains(batt.get(j)))
				continue;
			
			if(mach[index]<=batt.get(j)){
			
				temp.add(index,batt.get(j));
		
				if(index==mach.length-1){
					
					temp.remove(index);
					count++;
				}
					
				else{
					
					cases(temp,mach,batt,index+1);
					temp.remove(index);
				}
			}
		}

	}
}
