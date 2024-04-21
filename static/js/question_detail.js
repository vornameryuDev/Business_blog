const backQuestionListBtn = document.querySelector('.question-detail-btn-box .list');
const updateQuestionBtn = document.querySelector('.question-detail-btn-box .update');
const deleteQuestionBtn = document.querySelector('.question-detail-btn-box .delete');


function backToQuestionList() {
    location.href = this.dataset.uri;
}
function updateQuestion() {
    location.href = this.dataset.uri;
}
function deleteQuestion() {
    location.href = this.dataset.uri;
}


backQuestionListBtn.addEventListener('click', backToQuestionList);
updateQuestionBtn.addEventListener('click', updateQuestion);
deleteQuestionBtn.addEventListener('click', deleteQuestion);