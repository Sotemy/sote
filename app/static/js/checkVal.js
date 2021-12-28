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
        console.log(password, password2)
        return false;
    };
    return true;
};


function validateData(email, password, password2, login) {

    console.log(email, password, password2, login)

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