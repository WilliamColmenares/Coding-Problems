/*

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

*/

function addUp(numbers, k){
	let found = false;
	let combinations = [];

	for (let i = 0; i < numbers.length - 1; i++) {
	  for (let j = i + 1; j < numbers.length; j++) {
	    combinations.push([numbers[i], numbers[j]]);
	  }
	}
	combinations.forEach((el)=>{
		if (el[0] + el[1] === k){
			found = true;
		}
	})
	return found;
}

addUp([10, 15, 3, 7], 17)