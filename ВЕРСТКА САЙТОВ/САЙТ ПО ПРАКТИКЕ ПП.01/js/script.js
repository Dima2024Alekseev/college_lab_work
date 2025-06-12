const drop = noselect
function noselect() {
    return false
}



setInterval(() => {
    if (document.ondragstart !== drop) {
        console.log("Копирование запрещено")
        document.ondragstart = noselect
        document.onselectstart = noselect
        document.oncontextmenu = noselect
    }
    else {
        console.log('Равны')
    }
},
    10000
)

