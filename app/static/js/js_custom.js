// получим значение в таблицы ячейки
function duty_date(el) {
    var date = el.getAttribute('data-day')
    //console.log(date)    
    
    // Подставим это значение в заголовок модального окна
    function display_date(date) {        
        document.getElementById('ModalRosterTitleDate').innerHTML = date;
    }    
    display_date(date);
}

