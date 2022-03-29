
    $(document).on('submit', '#add_status', function() {
    $.ajax({
        type: $(this).attr('method'),
        url: this.action,
        data: $(this).serialize(),
        context: this,
        success: function(data, status) {
            location.reload();
        },
        error: function (request, type, errorThrown) {
            $('#add_status').html(request.responseText);
        }
    });
    return false;
})
