let answer = generateAnswer();
let attempts = 9;
const maxAttempts = 9;

const resultDiv = document.getElementById('results');
const resultImg = document.getElementById('game-result-img');
const attemptsSpan = document.getElementById('attempts');
const submitButton = document.querySelector('.submit-button');
const inputFields = document.querySelectorAll('.input-field');

window.onload = () => {
    attemptsSpan.textContent = attempts;
};

function generateAnswer() {
    const list = [];
    while (list.length < 3) {
        const rand = Math.floor(Math.random() * 10).toString();
        if (!list.includes(rand)) {
            list.push(rand);
        }
    }
    console.log("정답:" + list);
    return list;
}

function check_numbers() {
    const inputs = Array.from(inputFields).map(input => input.value.trim());

    if (inputs.some(num => num === '')) {
        alert("모든 칸에 숫자를 입력해주세요.");
        inputFields.forEach(input => input.value = '');
        inputFields[0].focus();
        return;
    }

    const isEqual = new Set(inputs).size !== inputs.length;
    if (isEqual) {
        alert("중복되지 않은 숫자를 입력해주세요.");
        return;
    }

    let strike = 0, ball = 0;

    inputs.forEach((digit, idx) => {
        if (digit === answer[idx]) {
            strike++;
        } else if (answer.includes(digit)) {
            ball++;
        }
    });

    let resultText = '';
    if (strike === 0 && ball === 0) {
        resultText = '🔴';
    } else {
        const s = strike > 0 ? `S ${'🟢'.repeat(strike)}` : '';
        const b = ball > 0 ? `B ${'🟡'.repeat(ball)}` : '';
        resultText = [s, b].filter(Boolean).join(' ');
    }

    const resultEntry = document.createElement('div');
    resultEntry.textContent = `${inputs.join('')} → ${resultText}`;
    resultDiv.appendChild(resultEntry);

    attempts--;
    attemptsSpan.textContent = attempts;

    if (strike === 3) {
        resultImg.src = 'success.png';
        buttonChange();
        //endGame();
    } else if (attempts === 0) {
        resultImg.src = 'fail.png';
        buttonChange();
        //endGame();
    }
}

function resetGame() {
    answer = generateAnswer();
    attempts = maxAttempts;
    attemptsSpan.textContent = attempts;
    resultImg.src = '';
    resultDiv.innerHTML = '';

    inputFields.forEach(input => {
        input.value = '';
        input.disabled = false;
    });

    submitButton.textContent = '확인하기';
    submitButton.onclick = check_numbers;
    submitButton.style.backgroundColor = "lightblue";

    inputFields[0].focus();
}


// function endGame() {
//     submitButton.disabled = true;
//     inputFields.forEach(input => input.disabled = true);
// }게임 비활성화를 만든 흔적


function buttonChange() {
    submitButton.textContent = '다시 시작';
    submitButton.onclick = resetGame;
    submitButton.style.backgroundColor = "yellow";
}