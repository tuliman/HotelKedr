function validation(value,key){
    let bool = false
    if (value.length<2 || !value){
        $(`input[name=${key}]`).after("<span class='error'> Поле не может быть пустым и содержать меньше 2х символов </span>")
        bool = true
    }
    return bool
}
function ValidateEmail(mail,key)

{
    var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    let bool = false
 if (! mail.match(mailformat))
  {
      $(`input[name=${key}]`).after("<span class='error'> Введите корректный Email </span>")
        bool = true
  }
 return bool
}
$(document).ready(function (){
    var now = moment()
    now.locale('ru')
    $('.SenderBocking').on('click',function (e){
        e.preventDefault()
        $('.error').remove()
        var _this = $('.SenderBocking')
        var form = document.getElementById('ReserveBocking')
        var formData = new FormData(form)
        var csrf = $('input[name=csrfmiddlewaretoken]').val()
        var data = {}
        formData.forEach(function (value,key){
            if(key==='name'||key==='phone_number'){
                if (validation(value,key)){
                    e.preventDefault()
                    return false
                }
            }
            else if(key==='email' && value){
                e.preventDefault()
                if(ValidateEmail(value,key)){
                return false
            }}
            data[key]=value
        })
        $.ajax(
            {
                type:'POST',
                data:JSON.stringify(data),
                url:'/booking/api',
                headers: {"X-CSRFToken":csrf},
                beforeSend: function () {
                        _this
                        .prop('disabled', true)
                        .find('.spinner-grow').removeClass('d-none');
                        },
                contentType: "application/json",
                encode:true,
            }).done(function (data){
                _this.prop('disabled', false).find('.spinner-grow').addClass('d-none');
                form.reset()
        }).fail(function (data){
            _this.prop('disabled', false).find('.spinner-grow').addClass('d-none');
        })
    })
})
