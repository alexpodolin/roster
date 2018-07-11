function get_date(el) {
    
    // день
    var day = el.getAttribute('data-day');
    if(day.toString().length < 2)
               day= '0' + day;
    
    // месяц
    var month = el.getAttribute('data-month');
    if(month.toString().length < 2)
               month= '0' + month;
    // год
    var year = el.getAttribute('data-year')
    
    //полная дата в нужном виде
    var full_date = day + '.' + month + '.' + year
    var date = document.getElementById('ModalDate');
    date.innerHTML = full_date   
    

}

// ф-ия добавления дежурного
function add_duty(el) {
    var full_date = document.getElementById('ModalDate').textContent;
        full_date = full_date.split('.').reverse().join('-');
    var user_id = el.getAttribute('data_user_id');
    
    var wrapper = document.getElementById('wrapper');
        
    // создаём объект XMLHttpRequest
    var request = new XMLHttpRequest();
    // тело запроса, т.е. что мы отправляем
    var params = 'user_id=' + encodeURIComponent(user_id) + '&date=' + encodeURIComponent(full_date);
    // конфигурируем его, т.е POST запрос на url /
    //request.open('POST', '/add_duty_date', true)
    request.open('GET', '/add_duty_date?' + params, true)
    // добавим заголовоки, говорят без него POST не работает 
    request.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    //нужно для GET
    request.setRequestHeader("X-Requested-With", "XMLHttpRequest");
    // отсылаем запрос в [body] - body или тело запроса
    //request.send(body);
    request.send();

    request.onreadystatechange = function() {
        if (request.readyState == 4) {
            if (request.status == 200) {
                wrapper.innerHTML = request.responseText
                console.log(wrapper)
                console.log( xhr.status + ': ' + xhr.statusText ); // пример вывода: 404: Not Found
                } else {
                console.log("Ошибка на сервере. " + request.status);
            }
        }
    } 
    
    //кусок кода спизжен из jquery
    $('#ModalRoster').modal('hide');    
}

