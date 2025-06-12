//----- 1 задача -------

function test(str) {
  return str.replace(/\w\S*/g, function(txt){  ///\w\S*/g выражение используется для каждого слова в строке
    //Возвращает слово с заглавной первой буквой и остальными строчными
    return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
  });
}
let str = "london is the capital of great britain";
//Вызываем функцию в диалоговом окне
alert(test(str));


//----- 2 задача ----


// function getFileName(path) { //функция getFileName() принимает путь к файлу path в качестве аргумента.
//   // Извлекаем имя файла с расширением
//   let fileNameWithExtension = path.split('\\').pop().split('/').pop();//Методы split() и pop() используются для извлечения имени файла
//   //с расширением из полного пути.
//   // Удаляем расширение и возвращаем имя файла
//   return fileNameWithExtension.split('.').slice(0, -1).join('.');// методы split() и join() используются для удаления
//   // расширения и возвращения имени файла.
// }

// let path = prompt('Введите путь файла');
// alert(getFileName(path));  // Вывод: "имя_файла"




//---- 3 задача -------


// function Palindrome(str) {
//   // удаляет все небуквенные символы и приводит строку к нижнему регистру
//   str = str.replace(/[^А-Яа-я-A-Za-z0-9]/g, '').toLowerCase();
//   // создает обратную строку
//   let reverseStr = str.split('').reverse().join(''); //replace(), toLowerCase(), split(), reverse() и join()
//   //используются для создания обратной строки без учета регистра и небуквенных символов.
//   // Сравниваем исходную строку с обратной
//   return str == reverseStr;

// }
// let test = prompt("Введите слово");
// Palindrome(test);
// alert(Palindrome(test));



// ----- 4 задача ------


// function test(str) {
//   // Разбиваем строку на массив слов, переворачиваем массив и объединяем обратно в строку
//   return str.split(' ').reverse().join(' '); //используются для создания строки, где слова расположены в обратном
//   //порядке
// }

// let str = prompt('Введите слова через пробел');
// alert(test(str));  

