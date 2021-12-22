$(function () {

    $(".userbtn").on('click', function () {
        setTitleName(this);

        $('form').remove();
            $('.modal-body').append(`
            <form action="" class="needs-validation" id="userForm" novalidate>
            <lm href='auth/login'></lm>
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

            if ($('#passwordInput2').length == 0) {

                $('.modal-body').append(`
                <form action="" class="needs-validation" id="userForm" novalidate>
                    <lm href='auth/register'></lm>
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
            <lm href='auth/reset-password'></lm>
            <div class="mb-3">
                <label for="pwd" class="form-label">Your username:</label>
                <input type="text" class="form-control" id="loginInput" placeholder="Enter username"
                    name="pwd" required>
            </div>
            <div class="mb-3">
                <label for="secret" class="form-label">Password:</label>
                <input type="password" class="form-control" id="secretInput" placeholder="Enter secret"
                    name="secret" required>
            </div>
            </form>
            `);

        });
    });

    $('#checkBtn').on('click', function () {

        let login = $('#loginInput');
        let password = $('#passwordInput');
        let password2 = $('#passwordInput2');
        console.log(password.val(), password2.val());
        let secret = $('#secretInput');
        let validornot = validateData(login, password, password2);
        console.log(validornot);

        if (validornot === false) {
            return $('.form-control').attr("class", "form-control is-invalid");
        };

        $('.form-control').attr("class", "form-control is-valid");
        let title = getTitleName();
        console.log(title);
        if (getUrl === 'auth/register') {
            let data = { login: login.val(), password: password.val(), password2: password2.val() };
            sendOrRequestData("post",getUrl(), data);
        } else if (getUrl === 'auth/login') {
            let data = { login: login.val(), password: password.val() };
            sendOrRequestData("post",getUrl(), data);
        } else if (getUrl === 'auth/reset-password') {
            let data = { login: login.val(), password: secret.val() };
            sendOrRequestData("post",getUrl(), data);
        };

    });

    function getUrl() {
        $('lm').attr('href').text();
    }

    function setTitleName(arg) {
        $('.modal-title').text($(arg).text());
    };

    function getTitleName() {
        $('div .modal-title').text();
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
        if (password.val().length < rule.password.min_length) {
            return false;
        };
        return true;

    };

    function validateLogin(login) {
        if (login.val().length < rule.login.min_length) {
            return false;
        };
        return true;
    };

    function validatePassword2(password, password2) {
        if (password2.val() != password.val()) {
            console.log(password.val(), password2.val())
            return false;
        };
        return true;
    };

    function validateData(login, password, password2) {

        if (password.val() === undefined) {
            return validateLogin(login);
        };

        if (password2.val() === undefined) {
            return validateLogin(login) && validatePassword(password);
        };

        return validateLogin(login) && validatePassword(password) && validatePassword2(password, password2);
    };

    function sendOrRequestData(type, url, data) {
        '{ login: login.val(), password: password.val() }'
        req = $.ajax({
            type: type,
            url: url,
            data: data,
            success: function (text) {
                let response = text;
                return response;
            },
            error: function (status, error) {

                return status, error;
            }
        });

        req.done(function (response) {
            return console.log(response);
        });
    }

});


// $('.modal-body').append(
`
<form action="" class="needs-validation" id="userForm" novalidate>
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
<button class="btn btn-info" id="resetPassword">Forgot password?</button>`
// );
