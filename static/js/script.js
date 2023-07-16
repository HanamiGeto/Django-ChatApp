let objectDate = new Date();
let timeToString = objectDate.toLocaleString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true })
let time = timeToString.slice(0, -2) + " p.m.";
let day = objectDate.getDate();
let month = objectDate.getMonth();
let year = objectDate.getFullYear();
let monthText = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
let date = monthText[month] + " " + day + ", " + year + ", " + time;


async function sendMessage() {
    let fd = new FormData();
    fd.append('textmessage', messageField.value);
    fd.append('csrfmiddlewaretoken', token);
    try {
        waitSendMessageTemplate();
        let response = await fetch('/chat/', {
            method: 'POST',
            body: fd
        });
        let json = await response.json();
        document.getElementById('deleteMessage').remove();
        sentMessageTemplate();
    } catch(e) {
        console.error('An error occured', e);
    }
}

function waitSendMessageTemplate() {
    messageContainer.innerHTML += `
        <div id="deleteMessage" class="message message-right">
            <span>${messageField.value}</span>
            <span class="time">${date}</span>
        </div>`;
}

function sentMessageTemplate() {
    messageContainer.innerHTML += `
        <div class="message message-right">
            <span>${messageField.value}</span>
            <span class="time">${date}</span>
        </div>`;
    messageField.value = '';
}