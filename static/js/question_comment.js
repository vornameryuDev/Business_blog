const questionCommentBtn = document.querySelector('.question-detail-btn-box .comment');
const commentBox = document.querySelector('.comment-box');
const questionCommentCreateBtn = document.querySelector(".comment-box div button");
const questionCommentTextArea = document.querySelector(".comment-box textarea#question-comment");


const HIDDEN = "hidden";
let hiddenStatus = true; //숨겨짐


function hiddenControll() {
    if (hiddenStatus) {
        commentBox.classList.remove('hidden'); //나타남
        hiddenStatus = false; //나타남
    } else {
        commentBox.classList.add('hidden'); //숨겨짐
        hiddenStatus = true; //숨겨짐
    }
}
questionCommentBtn.addEventListener('click', hiddenControll);

questionCommentCreateBtn.addEventListener('click', function() {
    console.log(questionCommentTextArea.value);
    document.getElementById('q-com-input').value = questionCommentTextArea.value;
    document.getElementById('q-comm-form').submit();
    document.getElementById('q-com-input').value = '';
})
