
// $(document).ready(function(){
//     $('.modal-footer btn-primary').on('click', function(){
//         let login=$('#loginInput').val();
//         let password=$('#passInput').val();

//         req = $.ajax({
//             url:'/auth/login',
//             type:'POST',
//             data:{login:login, password:password}
//         })
//     });
// });

$(function () {
    $("#logbtn").on('click', function () {
        $("#myModal").modal("show", { keyboard: true });

    });

    $('#checkBtn').on('click', function () {

        let login = $('#loginInput');
        let password = $('#passwordInput');
        let log = `login: ${login.val()}, password: ${password.val()}`;
        console.log(log);

        let validornot = validateData(login, password);

        console.log(validornot);

        if (validornot === null) {
            $('.form-control').attr("class", "form-control is-valid");
            req=$.ajax({
                type: "POST",
                url: '/auth/login',
                data: { login: login.val(), password: password.val() },
                success: function (text) {
                    let response = text;
                    console.log(response);
                },
                error: function (xhr, status, error) {

                    return console.log(status, error, );
                }//'\n\nError:' + xhr.responseText
            });
            req.done(function(){

            });
        } else {
            $(validornot).attr("class", "form-control is-invalid");
            console.log('problem with creditals');
        }
    });

    const rule = {
        login: {
            min_length: 5
        },
        password: {
            min_length: 8,
            excepted_symbols: ['ü', 'Ü', 'ö', 'Ö', 'ä', 'Ä']
        }
    };

    let validateData = function (login, password) {
        return validateLogin(login), validatePassword(password);
    };

    // if(login.val().length<rule.login.min_length){
    //     if (password.val().length<rule.password.min_length) {
    //         return password
    //     };
    //     return login
    // };


    let validatePassword = function (password) {
        if (password.val().length < rule.password.min_length) {
            return password
        } else {
            return null;
        };
    };

    let validateLogin = function (login) {
        if (login.val().length < rule.login.min_length) {
            return login
        } else {
            return null;
        };
    };

});
