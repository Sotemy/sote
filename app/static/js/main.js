$(function () {
    
    $('.popover-dismiss').popover({
        trigger: 'focus'
      })

    $(".userbtn").on('click', function () {
        setTitleName(this);

        $('form').remove();
            $('.modal-body').append(`
            <form action="" class="needs-validation" id="userForm" novalidate>
            <lm href='auth/login' id='lmurl'></lm>
            <div class="mb-3">
                <label for="uname" class="form-label">Username:</label>
                <input type="text" class="form-control" id="loginInput" placeholder="Enter username"
                    name="uname" required>
            </div>
            <div class="mb-3">
                <label for="pwd" class="form-label">Password:</label>
                <input type="password" class="form-control" id="passwordInput" placeholder="Enter password"
                    name="pswd" required>
            </div>
            <button class="btn btn-info" id="resetPassword">Forgot password?</button>
           </form>`);


        $('div .mb-3').focusin(function () {
            $('.form-control').attr("class", "form-control");
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
            let key=sendOrRequestData("get", 'auth/get-key');
            console.log(key);

            $('form').remove();
            $('#resetPassword').hide();
            $('.modal-body').prepend(`
            <form>
            <lm href='auth/reset-password' id='lmurl'></lm>
            <div class="mb-3">
                <label for="pwd" class="form-label">Your username:</label>
                <input type="text" class="form-control" id="loginInput" placeholder="Enter username"
                    name="pwd" required>
            </div>
            <div class="mb-3">
                <label for="secret" class="form-label">Secret:</label>
                <input type="password" class="form-control" id="secretInput" placeholder="Enter secret"
                    name="secret" required>
            </div>
            </form>
            `);

        });
    });

    $('#checkBtn').on('click', function () {

        let login = $('#loginInput').val();
        let password = $('#passwordInput').val();
        let password2 = $('#passwordInput2').val();
        let validornot = validateData(login, password, password2);
        console.log(validornot);

        if (validornot === false) {
            return $('.form-control').attr("class", "form-control is-invalid");
        };

        $('.form-control').attr("class", "form-control is-valid");
        let getUrl=$('#lmurl').attr('href');
        if (getUrl === 'auth/register') {
            data = { login: login, password: password, password2: password2 };

        } else if (getUrl === 'auth/login') {
            data = { login: login, password: password };

        } else if (getUrl === 'auth/reset-password') {
            let secret = $('#secretInput').val();
            data = { login: login, secret: secret };
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
            console.log(password, password2)
            return false;
        };
        return true;
    };

    function validateData(login, password, password2) {

        if (password === undefined) {
            return validateLogin(login);
        };

        if (password2 === undefined) {
            return validateLogin(login) && validatePassword(password);
        };

        return validateLogin(login) && validatePassword(password) && validatePassword2(password, password2);
    };

    function sendOrRequestData (type, url, data) {
        '{ login: login.val(), password: password.val() }'
        req = $.ajax({
            type: type,
            url: url,
            data: data,
            success: function (text) {
                var jsonRes = text.result;
                if(jsonRes === 'success'){
                    return $('#myModal').modal('toggle')
                };
                return alert(jsonRes);
            },
            error: function (status, error) {
                return status, error;
            }
        });

        req.done(function (response) {
            return console.log(response.result);
        });
    }

});
