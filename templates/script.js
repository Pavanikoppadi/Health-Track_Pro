let currentQuestion = 0;
const questions = document.getElementsByClassName('question');
const submitBtn = document.getElementById('submitBtn');

function showQuestion(n) {
    questions[n].style.display = 'block';
    if (n === 0) {
        document.getElementById('prevBtn').style.display = 'none';
    } else {
        document.getElementById('prevBtn').style.display = 'inline';
    }
    if (n === (questions.length - 1)) {
        document.getElementById('nextBtn').style.display = 'none';
        submitBtn.style.display = 'inline';
    } else {
        document.getElementById('nextBtn').style.display = 'inline';
        submitBtn.style.display = 'none';
    }
}

function changeQuestion(n) {
    questions[currentQuestion].style.display = 'none';
    currentQuestion += n;
    showQuestion(currentQuestion);
}

// Initialize the first question
showQuestion(currentQuestion);
