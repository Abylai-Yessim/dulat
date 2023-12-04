document.addEventListener('DOMContentLoaded', function () {
        var userOptions = document.querySelector('.user-options');
        var userIcon = document.querySelector('.fa-user');

        userIcon.addEventListener('click', function () {
            userOptions.style.display = (userOptions.style.display === 'none' || userOptions.style.display === '') ? 'block' : 'none';
        });
    });

    $(document).ready(function() {
        // Attach click event to delete buttons
        $('.delete-button').click(function() {
            var commentId = $(this).closest('.comment').data('comment-id');
            // Send AJAX request to delete_comment view
            $.post('/back/comment/delete/' + commentId + '/', function(response) {
                if (response.success) {
                    // Remove the comment from the UI
                    $('[data-comment-id=' + commentId + ']').remove();
                } else {
                    // Handle error (display a message, etc.)
                    console.log('Error deleting comment');
                }
            });
        });
    });