#include <stdio.h>

int main(void) {
	int n[9]={};
	int cnt=0;
	for(int i=1;i<=8;i++){
		scanf("%d ",&n[i]);
	}
	for(int i=1;i<=8;i++){
		if(n[i]==i){
			cnt++;
		}else if(n[i]==9-i){
			cnt--;
		}
	}
	if(cnt==8){
		printf("ascending");
	}else if(cnt==-8){
		printf("descending");
	}else{
		printf("mixed");
	}
	return 0;
}
