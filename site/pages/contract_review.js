// Get the user input field and send button
const userInputField = document.getElementById('user-input');
const sendButton = document.getElementById('send-button');
const chatBox = document.querySelector('.chat-box'); // Assuming this exists in your main HTML

sendButton.addEventListener('click', function() {
    const userInput = userInputField.value.trim();

    if (userInput) {
        // Create a new div for the user message
        const userMessage = document.createElement('div');
        userMessage.textContent = `You: ${userInput}`;
        chatBox.appendChild(userMessage);

        // Simulate a bot response
        const botResponse = document.createElement('div');
        botResponse.textContent = `Bot: Reviewing your contract...`; // You can modify this logic
        chatBox.appendChild(botResponse);

        // Clear the input field
        userInputField.value = '';

        // Scroll to the bottom of the chat box
        chatBox.scrollTop = chatBox.scrollHeight; // Keeps the view at the latest messages
    }
});
