// получим значение в таблицы ячейки
function duty_date(el) {
    var date = el.getAttribute('data-day')    
        
    // Подставим это значение в заголовок модального окна
    function display_date(date) {        
        document.getElementById('ModalRosterTitleDate').innerHTML = date;
    }
    
    display_date(date); 
    
    // во всплывающем окне добавим 0 перед номером дня и месяца
        function format_day() {
        var day_el = document.getElementById('ModalRosterTitleDate');        
        var day = day_el.outerText;
        
        if(day.toString().length < 2)
               day= '0' + day;   
                                       
        day_el.innerHTML = day;
    }
    
    format_day();

    function format_month() {
        var month_el = document.getElementById('ModalRosterTitleMonth');               
        var month = month_el.outerText;
        
        if(month.toString().length < 2)
               month= '0' + month;   
                        
        month_el.innerHTML = month;
    }
    
    format_month();
}

// добавим запись о дежурстве в БД
function add_duty(el) {    
    var day = document.getElementById('ModalRosterTitleDate'); // день    
    var month = document.getElementById('ModalRosterTitleMonth'); // месяц    
    var year = document.getElementById('ModalRosterTitleYear'); // год  
    // дата в необходимом формате
    var date = year.outerText + '-' + month.outerText + '-' + day.outerText;    
    var user_id = el.getAttribute('data_user_id'); // аттрибут с id пользователя   
      
    
    // создаём объект XMLHttpRequest
    var xhr = new XMLHttpRequest();
    // тело запроса, т.е. что мы отправляем
    //var body = 'user_id=' + encodeURIComponent(user_id) + '&date=' + encodeURIComponent(date);
    var params = 'user_id=' + encodeURIComponent(user_id) + '&date=' + encodeURIComponent(date);
    // конфигурируем его, т.е POST запрос на url /
    //xhr.open('POST', '/add_duty_date', true)
    xhr.open('GET', '/add_duty_date?' + params, true)
    // добавим заголовоки, говорят без него POST не работает 
    xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    //нужно для GET
    xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest");
    // отсылаем запрос в [body] - body или тело запроса
    //xhr.send(body);
    xhr.send();

    // код ответа сервера не 200, то это ошибка
    if (xhr.status != 200) {
        // обработать ошибку
        console.log( xhr.status + ': ' + xhr.statusText ); // пример вывода: 404: Not Found
    } else {
        // вывести результат
        console.log( xhr.responseText ); // responseText -- текст ответа.
    }
    
}