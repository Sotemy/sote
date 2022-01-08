$(function () {

    $('#addTagBtn').on('click', function() {
        let name=$('#tag').val()
        sendReq("/admin/add/tag", {name:name, context:'add_tag'})
    })

    function sendReq(url, data) {
        req=$.ajax({
            type: "POST",
            url: url,
            data: data,
            success: function (response) {
                return alert(response, response.result)
            }
        });
    };

    function alert(response, icon) {
        Swal.fire({
            toast: true,
            title: response.result,
            text: response.text,
            icon: icon,
            confirmButtonText: 'ok'
        })
    }
});