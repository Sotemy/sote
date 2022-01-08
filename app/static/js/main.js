$(function () {

    $(".userbtn").on('click', function () {
        setTitleName(this);

        $('.modal-body').empty();
        $('.modal-body').append(`
        <form action="" class="needs-validation" id="loginForm" novalidate>
            <lm href='auth/login' id='lmurl'></lm>
            <div class="form-group">
                <label for="email" class="form-label">Email:</label>
                <input type="email" class="form-control" id="emailInput" placeholder="Enter username"
                    name="email" required>
            </div>
            <div class="form-group">
                <label for="password" class="form-label">Password:</label>
                <input type="password" name="password" class="form-control" id="passwordInput" placeholder="Enter password" required>
            </div>
        </form>
        <div class="mb-3">
            <a class="btn btn-info" id="resetPassword">Forgot password?</a>
        </div>`);

        if ($(this).attr('id') === 'regbtn') {

            $('.modal-body').empty();

            if ($('#passwordInput2').length === 0) {

                $('.modal-body').append(`
                <form action="" class="needs-validation" id="registerForm" novalidate>
                    <lm href='auth/register' id='lmurl'></lm>
                <div class="form-group">
                    <label for="username" class="form-label">Username:</label>
                    <input type="text" class="form-control" id="loginInput" placeholder="Enter username"
                        name="username" required>
                <div class="form-group">
                    <label for="email" class="form-label">Email:</label>
                    <input type="email" class="form-control" id="emailInput" placeholder="Enter password"
                        name="email" required>
                </div>
                </div>
                <div class="form-group">
                    <label for="password" class="form-label">Password:</label>
                    <input type="password" class="form-control" id="passwordInput" placeholder="Enter password"
                        name="pswd" required>
                </div>
               <div class='form-group' id='mb-2'>
                   <label for='password2' class='form-label'>Repeat password:</label>
                   <input type='password' class='form-control' id='passwordInput2' placeholder='Repeat password' name='password2' required>
                </div>
                </form>`);
            };
        } else if ($(this).attr('id') === 'loginbtn') {
            $('#mb-2').remove();
        };

        openModal();

        $('#resetPassword').on('click', function () {
            setTitleName(this);

            $('.modal-body').empty();
            $(this).hide();
            $('.modal-body').prepend(`
            <form action="" class="needs-validation" id="resetForm" novalidate>
            <lm href='auth/reset-password' id='lmurl'></lm>
            <div class="form-group">
            <label for="email" class="form-label">Email:</label>
            <input type="email" class="form-control" id="emailInput" placeholder="Enter password"
                name="email" required>
            </div>
            </form>
            `);

        });

        $('#registerForm').validate({
            rules: {
                email: {
                    required: true,
                    email: true,
                },
                password: {
                    required: true,
                    minlength: 5
                },
                password2 : {
					minlength : 5,
					equalTo : "#passwordInput"
				}
            },
            messages: {
                email: {
                    required: "Please enter a email address",
                    email: "Please enter a vaild email address"
                },
                password: {
                    required: "Please provide a password",
                    minlength: "Your password must be at least 5 characters long"
                },
                password2: {
                    required: "Please provide a password",
                    minlength: "Your password must be at least 5 characters long",
                    equalTo:"Must be equal to password"
                }
            },
            errorElement: 'span',
            errorPlacement: function (error, element) {
                error.addClass('invalid-feedback');
                element.closest('.form-group').append(error);
            },
            highlight: function (element, errorClass, validClass) {
                $(element).addClass('is-invalid');
            },
            unhighlight: function (element, errorClass, validClass) {
                $(element).removeClass('is-invalid');
            }
        });


        $('#loginForm').validate({
            rules: {
                email: {
                    required: true,
                    email: true,
                },
                password: {
                    required: true,
                    minlength: 5
                },
            },
            messages: {
                email: {
                    required: "Please enter a email address",
                    email: "Please enter a vaild email address"
                },
                password: {
                    required: "Please provide a password",
                    minlength: "Your password must be at least 5 characters long"
                }
            },
            errorElement: 'span',
            errorPlacement: function (error, element) {
                console.log(error, element);
                error.addClass('invalid-feedback');
                element.closest('.form-group').append(error);
            },
            highlight: function (element, errorClass, validClass) {
                console.log(element);
                $(element).addClass('is-invalid');
            },
            unhighlight: function (element, errorClass, validClass) {
                console.log(element);
                $(element).removeClass('is-invalid');
            }
        });

        $('#resetForm').validate({
            rules: {
                email: {
                    required: true,
                    email: true,
                }
            },
            messages: {
                email: {
                    required: "Please enter a email address",
                    email: "Please enter a vaild email address"
                },
            },
            errorElement: 'span',
            errorPlacement: function (error, element) {
                console.log(error, element);
                error.addClass('invalid-feedback');
                element.closest('.form-group').append(error);
            },
            highlight: function (element, errorClass, validClass) {
                console.log(element);
                $(element).addClass('is-invalid');
            },
            unhighlight: function (element, errorClass, validClass) {
                console.log(element);
                $(element).removeClass('is-invalid');
            }
        });
    
        $.validator.setDefaults({
            debug: true
        });
    });

    $('#checkBtn').on('click', function () {
        let email = $('#emailInput').val();
        let login = $('#loginInput').val();
        let password = $('#passwordInput').val();
        let password2 = $('#passwordInput2').val();
        // alert("Form successful submitted!");
        let getUrl=$('#lmurl').attr('href');
        if (getUrl === 'auth/register') {
            if ($('#registerForm').valid() != true) {
                return alert('False')
            };
            data = { login: login,email:email, password: password, password2: password2 };

        } else if (getUrl === 'auth/login') {
            if ($('#loginForm').valid() != true) {
                return alert('False')
            };
            data = { email: email, password: password };

        } else if (getUrl === 'auth/reset-password') {
            if ($('#resetForm').valid() != true) {
                return alert('False')
            }; 
            data = { email: email};
        };
        let req = $.ajax({
            type: 'POST',
            url: getUrl,
            data: data,
            success: function (jsonRes) {
                if(jsonRes.result === 'success'){
                    console.log(jsonRes.result, 'success');  
                    return $('#myModal').modal('toggle');
                };    
                console.log(jsonRes) 
                
                return console.log(jsonRes.result +' '+ jsonRes.text, 'danger');      

            },
            error: function (status, error) {
                return console.log(status + error, 'danger');
            }
        });

        req.done(function (response) {
            return response;
        });

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

});
