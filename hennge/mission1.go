package main
import "fmt"

func sqr(x int) int {
	var temp int
	temp = 0
	if (x > 0) {
		temp = x * x
	} else {
		temp = 0
	}
	return temp
}

func calc(x int) int {
	var ret int
	if (x > 0){
		var n int
		fmt.Scanf("%d",&n)
		ret =  sqr(n) + calc(x-1)
	} else {
		ret = 0
	}
	return ret
}

func exec(x int) int {
	if (x > 0){
		var n int
		fmt.Scanf("%d",&n);
		fmt.Println(calc(n));
		exec(x - 1);
	}
	return 0
}

func main() {
	var t int
	fmt.Scanf("%d",&t)
	exec(t)
}