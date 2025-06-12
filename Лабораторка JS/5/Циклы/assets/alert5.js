let num = 7
function isPrime(num) {
    for (var i = 2; i < num; i++)
      if (num % i === 0) return false;
    return num > 1;
  };
 
  function getMessage(num) {
        alert(isPrime(num) ? 'Число простое': 'Число непростое')
  }