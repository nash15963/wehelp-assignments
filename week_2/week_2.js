//1
function calculate(min, max){
    // 請用你的程式補完這個函式的區塊    
    let num_array =[] ;
    for(let i = min ;i < max+1 ;i++){
        num_array.push(i)
    }
    console.log( num_array.reduce((a,b) => a + b ,0)) ;
    //let reducer = (previousValue, currentValue) => previousValue + currentValue;
    //console.log(num_array.reduce(reducer));
    }
calculate(1, 3); // 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8); // 你的程式要能夠計算 4+5+6+7+8，最後印出 30
//*****************************************************/
//2
function avg(data){
    // 請用你的程式補完這個函式的區塊
    let sal_array =[]
    for(let i =0 ;i<data["employees"].length;i++){
        let sal = data["employees"][i]['salary']
        sal_array.push(sal)
    }
    let tot  = sal_array.reduce((a,b)=>a+b ,0)
    console.log(tot/sal_array.length)
    }
avg({
    "count":3,
    "employees":[
    {
    "name":"John",
    "salary":30000
    },
    {
    "name":"Bob",
    "salary":60000
    },
    {
    "name":"Jenny",
    "salary":50000
    }
    ]
}); // 呼叫 avg 函式

//*****************************************************/
//3
function maxProduct(nums){
    // 請用你的程式補完這個函式的區塊
    
    nums.sort(function(a, b) {
        return b - a;
      });
    let Max = nums[0]*nums[1]
    console.log(Max)
    }
maxProduct([5, 20, 2, 6]) // 得到 120
maxProduct([10, -20, 0, 3]) // 得到 30
maxProduct([-1, 2]) // 得到 -2
maxProduct([-1, 0, 2]) // 得到 0


//*****************************************************/
//4
function twoSum(nums, target){
    // your code here
    let temp_array =[]
    for(let i = 0 ;i<nums.length ;i++){
        for(let j = 0 ;j<nums.length ;j++){
            if(nums[i]+nums[j] == target){
                temp_array.push(i)}
    }}
    return temp_array
    //console.log(temp_array)
    }
let result=twoSum([2, 11, 7, 15], 9);
console.log(result); // show [0, 2] because nums[0]+nums[2] is 9
// 個人資測
// let result2=twoSum([5, 20, 1, 2], 3);
// console.log(result2); // show [2, 3] because nums[2]+nums[3] is 3

//*****************************************************/
//5

function maxZeros(nums){
    // 請用你的程式補完這個函式的區塊
    let temp = 0
    let big = 0
    for(let i =0 ;i<nums.length ;i++){
        if(nums[i]==0){
            temp++
            if(big<temp){
                big = temp
            }
        }
        else{temp = 0
        }
    }
    console.log(big)
    }
maxZeros([0, 1, 0, 0]); // 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]); // 得到 4
maxZeros([1, 1, 1, 1, 1]); // 得到 0
maxZeros([0, 0, 0, 1, 1]) // 得到 3






