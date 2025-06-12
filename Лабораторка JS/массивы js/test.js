function rearrangeArray(arr) {
    const neg = [];
    const zero = [];
    const pos = [];
  
    for (let i = 0; i < arr.length; i++) {
      if (arr[i] < 0) {
        neg.push(arr[i]);
      } else if (arr[i] === 0) {
        zero.push(arr[i]);
      } else {
        pos.push(arr[i]);
      }
    }
  
    return neg.concat(zero, pos);
  }
  
  // Пример использования
  const arr = [-1, 2, 0, -3, 5, 0, 7, -4];
  console.log(rearrangeArray(arr)); // [-1, -3, -4, 2, 0, 0, 5, 7]