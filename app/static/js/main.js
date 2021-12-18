$(function () {

    $('.nav-item dropdown').on('click', function(){
        $(".dropdown-menu").animate({
            height: 'toggle'
        });
    });
    
    $(".userbtn").on('click', function () {
        $('.modal-title').text($(this).text());

        if($(this).text() === 'register'){

            if ($('#passwordInput2').length == 0){

                $('#userForm').append("<div class='mb-3' id='mb-2'><label for='pwd' class='form-label'>Repeat password:</label><input type='password' class='form-control' id='passwordInput2' placeholder='Repeat password' name='pswd' required></div>");
            };
        } else if ($(this).text() === 'login'){

            $('#mb-2').remove();
        };

        return $("#myModal").modal("show", { keyboard: true });

    });

    $('#checkBtn').on('click', function () {

        let login = $('#loginInput');
        let password = $('#passwordInput');
        let password2= $('#passwordInput2');
        let validornot = validateData(login, password, password2);

        if (validornot === false) {
            return $('.form-control').attr("class", "form-control is-invalid");
        };

        $('.form-control').attr("class", "form-control is-valid");
        if (password2.length > 0) {
            req=$.ajax({
                type: "POST",
                url: '/auth/register',
                data: { login: login.val(), password: password.val(), password2:password2.val()},
                success: function (text) {
                    let response = text;
                    return response;
                },
                error: function (status, error) {
    
                    return status, error;
                }
            });
        };

        req=$.ajax({
            type: "POST",
            url: '/auth/login',
            data: { login: login.val(), password: password.val() },
            success: function (text) {
                let response = text;
                return response;
            },
            error: function (status, error) {

                return status, error;
            }
        });

        req.done(function(){
            return console.log('1');
        });
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


    function validatePassword (password) {
        if (password.val().length < rule.password.min_length) {
            return false;
        };
        return true;

    };

    function validateLogin (login) {
        if (login.val().length < rule.login.min_length) {
            return false;
        };
        return true;
    };

    function validatePassword2 (password, password2){
        if (password2.val() != password.val()){
            console.log(password.val(), password2.val())
            return false;
        };
        return true;
    };

    function validateData (login, password, password2) {
        if (password2.val() === undefined) {
            return validateLogin(login) && validatePassword(password);
        }
        return validateLogin(login) && validatePassword(password) && validatePassword2(password, password2);
    };

});