let timer;
let ms = 0;
let seconds = 0;
let minutes = 0;
let isRunning = false;

const time = document.getElementById('time');
const record = document.getElementById('records');

function format(num){
    return num < 10 ? `0${num}` : `${num}`;
}

function display(){
    time.textContent = `${format(minutes)}:${format(seconds)}:${format(ms)}`;
}

function startwatch(){
    if (isRunning) return;
    isRunning = true;

    timer = setInterval(() => {
        ms++;
        if (ms === 100) {
            ms = 0;
            seconds++;
        }
        if (seconds === 60) {
            seconds = 0;
            minutes++;
        }
        display();
    }, 10);
}

function stopwatch(){
    if (!isRunning) return;
    isRunning = false;
    clearInterval(timer);

    const li = document.createElement("li");
    li.classList.add("record_item");

    const btn = document.createElement("button");
    btn.classList.add("record_btn");

    const img = document.createElement("img");
    img.classList.add("record_img");
    img.src = "circle-line-b.png"; 
    img.alt = "선택 버튼";
    btn.onclick = (e) => {
        e.stopPropagation(); 
        li.classList.toggle("selected");
        img.src = li.classList.contains("selected")
            ? "circle-fill-b.png"  
            : "circle-line-b.png";  
        
        updateToggleImage();
    };

    btn.appendChild(img);
    const span = document.createElement("span");
    span.textContent = `${format(minutes)}:${format(seconds)}:${format(ms)}`;
    li.appendChild(btn);
    li.appendChild(span);
    record.appendChild(li);
}

function resetwatch(){
    ms = 0;
    seconds = 0;
    minutes = 0;
    clearInterval(timer);
    display();
}

function deleteList(){
    const selected = document.querySelectorAll(".record_item.selected");
    selected.forEach(item => item.remove());
}

function toggleSelectAll() {
    const items = document.querySelectorAll(".record_item");
    const allSelected = items.length > 0 && [...items].every(item => item.classList.contains("selected"));
    const img = document.getElementById("toggle_img");

    items.forEach(item => {
        const toggleBtn = item.querySelector("button");
        const toggle_img = item.querySelector("img");
        if (allSelected) {
            item.classList.remove("selected");
            if (toggle_img) toggle_img.src = "circle-line-b.png";
        } else {
            item.classList.add("selected");
            if (toggle_img) toggle_img.src = "circle-fill-b.png";
        }
    });

    img.src = allSelected ? "circle-line.png" : "circle-fill.png";
}

function updateToggleImage() {
    const allItems = document.querySelectorAll(".record_item");
    const selectedItems = document.querySelectorAll(".record_item.selected");
    const toggleImg = document.getElementById("toggle_img");

    if (allItems.length > 0 && allItems.length === selectedItems.length) {
        toggleImg.src = "circle-fill.png";
    } else {
        toggleImg.src = "circle-line.png";
    }
}

