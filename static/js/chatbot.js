// Toggle chatbot visibility
function toggleChatbot() {
    const chatbot = document.getElementById("chatbot-container");
    if (chatbot) {
        chatbot.style.display = (chatbot.style.display === "block") ? "none" : "block";
    }
}

// Handle sending user message
function sendMessage() {
    const inputField = document.getElementById("chatbot-input");
    const messagesDiv = document.getElementById("chatbot-messages");

    if (!inputField || !messagesDiv) return;

    const userMessage = inputField.value.trim();
    if (userMessage === "") return;

    appendMessage(`You: ${userMessage}`, "user-message");
    inputField.value = "";

    const diseaseElement = document.querySelector("h2 span");
    const disease = diseaseElement ? diseaseElement.innerText : null;

    if (!disease) {
        appendMessage("Chatbot: ⚠️ Please upload an image first to detect disease.", "bot-message");
        return;
    }

    // Disable input while waiting for response
    inputField.disabled = true;

    fetch("/chatbot", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ disease: disease, question: userMessage.toLowerCase() })
    })
    .then(response => response.json())
    .then(data => {
        if (data && data.response) {
            appendMessage(`Chatbot: ${data.response}`, "bot-message");
        } else {
            appendMessage("Chatbot: ❌ Unexpected response from server.", "bot-message");
        }
    })
    .catch(error => {
        console.error("Error:", error);
        appendMessage("Chatbot: ❌ Sorry, something went wrong. Please try again later.", "bot-message");
    })
    .finally(() => {
        inputField.disabled = false;
        inputField.focus();
    });
}

// Append a message to the chatbot window
function appendMessage(message, className) {
    const messagesDiv = document.getElementById("chatbot-messages");
    if (!messagesDiv) return;

    const messageElement = document.createElement("div");
    messageElement.className = className;
    messageElement.innerText = message;

    messagesDiv.appendChild(messageElement);
    messagesDiv.scrollTop = messagesDiv.scrollHeight; // Auto-scroll to latest message
}
