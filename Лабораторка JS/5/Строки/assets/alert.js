let a = "london is the capital of great britain";
alert(
    a.split(/\s+/).map(word => word[0].toUpperCase() + word.substring(1)).join(' ')
    );