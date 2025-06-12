//02.1

// let a = 22, b = 33;
// let c = ++a; // ?
// let d = b++; // ?

// console.log(a);
// console.log(b);
// console.log(c);
// console.log(d);
// document.getElementById("el01").innerHTML=  "<p>Результат:</p>" + "a = " + a + ";" + 
// "<br>" + "b = "  + b + ";" + "<br>" + "c = " + c + ";" + "<br>" + "d = " + d + ";"; 
// ++a префикс увеличивает значение на 1 и возвращает его увелечиным 
// b++ постфик увеличивает значение на 1 и возвращает его исходным

//02.2
// let a = 4;
// let x = 2 + (a *= 5);


// document.getElementById("e102").innerHTML= "<p>Результат:</p>" + "a = " +  a+ ";" + "<br>" + "x= "+ x+ ";";
// a = 20;
// x = 22;
//оператор *= является оператором присваивания, который умножает текущее значение переменной на значение справа от оператора и присваивает результат переменной.
//В данном случае a = 4*5 = 20;
// x = 2 + 20 = 22

//02.3
var 
i1 = "" + 1 + 0
i2 = "" - 1 + 0
i3 = true + false
i4 = 6 / "3"
i5 = "2" * "3"
i6 = 4 + 5 + "px"
i7 = "$" + 4 + 5
i8 = "4" - 2
i9 = "4px"  2
i10 = 7 / 0
i11 = " -9 " + 5
i12 = " -9 " - 5
i13 = + 1
i14 = undefined + 1
i15 = " \t \n" - 2
console.log(i1);
console.log(i2);
console.log(i3);
console.log(i4);
console.log(i5);
console.log(i6);
console.log(i7);
console.log(i8);
console.log(i9);
console.log(i10);
console.log(i11);
console.log(i12);
console.log(i13);
console.log(i14);
console.log(i15);
document.getElementById("e103").innerHTML = "<p>Результат: </p>" + "i1 =" +i1 + ";" + "<br>"
+ "i2 =" +i2 + ";" + "<br>" 
+ "i3 =" +i3 + ";" + "<br>"
+ "i4 =" +i4 + ";" + "<br>"
+ "i5 =" +i5 + ";" + "<br>"
+ "i6 =" +i6 + ";" + "<br>"
+ "i7 =" +i7 + ";" + "<br>"
+ "i8 =" +i8 + ";" + "<br>"
+ "i9 =" +i9 + ";" + "<br>"
+ "i10 =" +i10 + ";" + "<br>"
+ "i11 =" +i11 + ";" + "<br>"
+ "i12 =" +i12 + ";" + "<br>"
+ "i13 =" +i13 + ";" + "<br>"
+ "i14 =" +i14 + ";" + "<br>"
+ "i15 =" +i15 + ";" + "<br>";
