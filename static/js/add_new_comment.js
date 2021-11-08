
$(document).ready(function (){
    $.get('/api',function (data){
    })
    var now = moment()
    now.locale('ru')
    $('.AddComment').on('click',function (e){
        e.preventDefault()
        var form = document.getElementById('commentForm')
        var formData = new FormData(form)
        var _this = $('.AddComment')
        var csrf = $('input[name=csrfmiddlewaretoken]').val()
        var data = {}
        formData.forEach(function (value,key){
            data[key]=value
        })
        $.ajax(
            {
                type:'POST',
                data:JSON.stringify(data),
                url:'/review/api',
                headers: {"X-CSRFToken":csrf},
                beforeSend: function () {
                        _this
                        .prop('disabled', true)
                        .find('.spinner-grow').removeClass('d-none');
                        },
                contentType: "application/json",
                encode:true,
            }).done(function (data){
                _this
                        .prop('disabled', false)
                        .find('.spinner-grow').addClass('d-none')
                form.reset()
                $(".AprtmentRewiewBlock").append(`<div class="card text-center"><div class="card-header"></div><div class="card-body"> <h5 class="card-title">${data.name}</h5><p class="card-text">${data.review}</p></div><div class="card-footer text-muted">${now.format('LLL')}</div></div>`)
        }).fail(_this
            .prop('disabled', true)
            .find('.spinner-grow').addClass('d-none'))
    })

})
