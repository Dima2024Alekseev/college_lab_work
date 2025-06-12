function getRandomNumber(min, max) {
    return Math.floor(Math.random() * (max - min) + min)
}  
    a = getRandomNumber(1,100);
let b = a;
if (a % 2 == 0) {    
    alert('Число четное = ' +  a )
    alert(a/2);
  } else{
    alert('Число нечетное = ' + a);
    alert(a*3);
  }
