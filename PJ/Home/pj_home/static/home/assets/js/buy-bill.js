document.addEventListener('DOMContentLoaded', () => {
    // Xử lý cho .question
    document.querySelectorAll('.question').forEach(question => {
        const answer = question.nextElementSibling;

        // Đảm bảo nội dung mặc định thu nhỏ
        answer.style.display = 'none';

        // Thêm sự kiện click
        question.addEventListener('click', () => {
            if (answer.style.display === 'block') {
                answer.style.display = 'none'; // Thu gọn
            } else {
                answer.style.display = 'block'; // Hiển thị
            }
        });
    });

    // Xử lý cho .question-expanded
    document.querySelectorAll('.question-expanded').forEach(questionExpanded => {
        const answerExpanded = questionExpanded.nextElementSibling;

        // Đảm bảo nội dung mặc định thu nhỏ
        answerExpanded.style.display = 'none';

        // Thêm sự kiện click
        questionExpanded.addEventListener('click', () => {
            if (answerExpanded.style.display === 'block') {
                answerExpanded.style.display = 'none'; // Thu gọn
            } else {
                answerExpanded.style.display = 'block'; // Hiển thị
            }
        });
    });
});
