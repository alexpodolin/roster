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
    
    // текущий url
    var cur_url = window.location.href;    
    
    // блок который мы перерисуем при изминении дежурного
    var wrap = document.getElementById('wrap')

    // создаём объект XMLHttpRequest
    var request = new XMLHttpRequest();
    // тело запроса, т.е. что мы отправляем
    var params = 'user_id=' + encodeURIComponent(user_id) + 
                    '&date=' + encodeURIComponent(full_date) + 
                    '&url=' + encodeURIComponent(cur_url);
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
                wrap.innerHTML = request.responseText                
                console.log(request.status + ': ' + request.statusText ); // пример вывода: 404: Not Found
                } else {
                console.log("Ошибка на сервере. " + request.status);
            }
        }
    } 
    
    // кусок кода спизжен из jquery
    // скроем popup окно
    $('#ModalRoster').modal('hide');    
}

// вывод таблицы на печать
function print_table(el) {
    var el_to_print = el.closest('.table__custom');   
    var month_name = el.closest('caption');

    win = window.open('');
    win.document.write('<head>');    
    win.document.write('<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">');
    win.document.write('<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>');
    win.document.write('<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>');
    win.document.write('<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js" integrity="sha384-smHYKdLADwkXOn1EmN1qk/HfnUcbVRZyYmZ4qpPea6sjB/pTJ0euyQp0Mk8ck+5T" crossorigin="anonymous"></script>');    
    win.document.write('<link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet"><link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.0.13/css/all.css" integrity="sha384-DNOHZ68U8hZfKXOrtjWvjxusGo9WQnrNx2sqG0tfsghAvtVlRW3tvkXWZh58N9jp" crossorigin="anonymous">	');   
    win.document.write('<link rel="stylesheet" href="static/css/style.css" media="all">');
    win.document.write('<link rel="stylesheet" href="js/js_custom.js">');
    win.document.write('</head>');
    win.document.write('<body>');
    win.document.write('<div class="container-fluid wrapper" id="wrap">');
    win.document.write('<div class="container-fluid">  ');

    win.document.write(el_to_print.outerHTML);
    win.document.write('</body></html>');
    
    return true;
}