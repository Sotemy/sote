$(function () {

    $(".userbtn").on('click', function () {
        setTitleName(this);

        $('form').remove();
        $('.modal-body').append(`
        <form action="" class="needs-validation" id="userForm" novalidate>
        <lm href='auth/login' id='lmurl'></lm>
        <div class="mb-3">
            <label for="uname" class="form-label">Email:</label>
            <input type="email" class="form-control" id="emailInput" placeholder="Enter username"
                name="uname" required>
        </div>
        <div class="mb-3">
            <label for="pwd" class="form-label">Password:</label>
            <input type="password" class="form-control" id="passwordInput" placeholder="Enter password"
                name="pswd" required>
        </div>
        <a class="btn btn-info" id="resetPassword">Forgot password?</a>
        </form>`);


        $('div .mb-3').focusin(function () {
            $('.form-control').attr("class", "form-control");
            $('.alertPlace').empty();
        });

        if ($(this).attr('id') === 'regbtn') {

            $('form').remove();

            if ($('#passwordInput2').length === 0) {

                $('.modal-body').append(`
                <form action="" class="needs-validation" id="userForm" novalidate>
                    <lm href='auth/register' id='lmurl'></lm>
                <div class="mb-3">
                    <label for="uname" class="form-label">Username:</label>
                    <input type="text" class="form-control" id="loginInput" placeholder="Enter username"
                        name="uname" required>
                <div class="mb-3">
                    <label for="ml" class="form-label">Email:</label>
                    <input type="email" class="form-control" id="emailInput" placeholder="Enter password"
                        name="ml" required>
                </div>
                </div>
                <div class="mb-3">
                    <label for="pwd" class="form-label">Password:</label>
                    <input type="password" class="form-control" id="passwordInput" placeholder="Enter password"
                        name="pswd" required>
                </div>
               </form>
               <div class='mb-3' id='mb-2'><label for='pwd' class='form-label'>Repeat password:</label><input type='password' class='form-control' id='passwordInput2' placeholder='Repeat password' name='pswd' required></div>`);
            };
        } else if ($(this).attr('id') === 'loginbtn') {
            $('#mb-2').remove();
        };

        openModal();

        $('#resetPassword').on('click', function () {
            setTitleName(this);

            $('form').remove();
            $(this).hide();
            $('.modal-body').prepend(`
            <form>
            <lm href='auth/reset-password' id='lmurl'></lm>
            <div class="mb-3">
                <label for="pwd" class="form-label">Your email:</label>
                <input type="email" class="form-control" id="emailInput" placeholder="Enter username"
                    name="pwd" required>
            </div>
            </form>
            `);

        });
    });

    $('#checkBtn').on('click', function () {

        let email = $('#emailInput').val();
        let login = $('#loginInput').val();
        let password = $('#passwordInput').val();
        let password2 = $('#passwordInput2').val();
        let validornot = validateData(email, password, password2, login);
        
        if (validornot === false) {
            return $('.form-control').attr("class", "form-control is-invalid");
        };

        $('.form-control').attr("class", "form-control is-valid");
        let getUrl=$('#lmurl').attr('href');
        if (getUrl === 'auth/register') {
            data = { login: login,email:email, password: password, password2: password2 };

        } else if (getUrl === 'auth/login') {
            data = { email: email, password: password };

        } else if (getUrl === 'auth/reset-password') { 
            data = { email: email};
        };
        sendOrRequestData("post",getUrl, data);

    });


    function setTitleName(arg) {
        $('.modal-title').text($(arg).text());
    };

    function openModal() {
        $('#myModal').modal('toggle', {
            keyboard: false,
            backdrop: 'static'
        });
    };


    const rule = {
        login: {
            min_length: 5
        },
        password: {
            min_length: 8,
            excepted_symbols: ['ü', 'Ü', 'ö', 'Ö', 'ä', 'Ä']
        }
    };


    function validateEmail(email) {
        if (email === undefined) {
            return false;
        };

        return true;
    };

    function validatePassword(password) {
        if (password.length < rule.password.min_length) {
            return false;
        };
        return true;

    };

    function validateLogin(login) {
        if (login.length < rule.login.min_length) {
            return false;
        };
        return true;
    };

    function validatePassword2(password, password2) {
        if (password2 != password) {
            return false;
        };
        return true;
    };

    function validateData(email, password, password2, login) {


        if (login === undefined) {
            if (password === undefined) {
                return validateEmail(email);
            }
            return validateEmail(email) && validatePassword(password);
        }

        if (password2 === undefined) {
            return validateLogin(login) && validatePassword(password);
        };

        return validateEmail(email) && validateLogin(login) && validatePassword(password) && validatePassword2(password, password2);
    };

    function sendOrRequestData (type, url, data) {
        '{ login: login.val(), password: password.val() }'

        let req = $.ajax({
            type: type,
            url: url,
            data: data,
            success: function (jsonRes) {
                if(jsonRes.result === 'success'){
                    alert(jsonRes.result, 'success');  
                    return $('#myModal').modal('toggle');
                };     

                $('.form-control').attr("class", "form-control is-invalid");
                
                return alert(jsonRes.result +' '+ jsonRes.text, 'danger');      


            },
            error: function (status, error) {
                return alert(status + error, 'danger');
            }
        });

        req.done(function (response) {
            return response;
        });
    };

    function alert(message, type) {
        let al = '<div class="alert alert-' + type + ' alert-dismissible" role="alert">' + message + '<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>';
        $('.alertPlace').append(al);
        setTimeout(function(){
            $('.alertPlace').empty();
        },5000);
    };

});
