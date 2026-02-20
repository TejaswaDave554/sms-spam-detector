// SMS Spam Detector - JavaScript functionality

document.addEventListener('DOMContentLoaded', function() {
    // Character counter for message input
    const messageTextarea = document.getElementById('message');
    if (messageTextarea) {
        const charCounter = document.createElement('div');
        charCounter.className = 'char-counter text-muted small mt-2';
        charCounter.innerHTML = '0 characters';
        messageTextarea.parentNode.appendChild(charCounter);

        messageTextarea.addEventListener('input', function() {
            const count = this.value.length;
            charCounter.innerHTML = count + (count === 1 ? ' character' : ' characters');

            // Add visual feedback
            if (count > 300) {
                charCounter.classList.add('text-warning');
                charCounter.classList.remove('text-muted', 'text-danger');
            } else if (count > 500) {
                charCounter.classList.add('text-danger');
                charCounter.classList.remove('text-muted', 'text-warning');
            } else {
                charCounter.classList.add('text-muted');
                charCounter.classList.remove('text-warning', 'text-danger');
            }
        });
    }

    // Form validation
    const spamForm = document.querySelector('form');
    if (spamForm) {
        spamForm.addEventListener('submit', function(e) {
            const messageValue = messageTextarea.value.trim();
            if (messageValue === '') {
                e.preventDefault();

                // Create alert if it doesn't exist
                if (!document.querySelector('.alert-warning')) {
                    const alert = document.createElement('div');
                    alert.className = 'alert alert-warning mt-3';
                    alert.role = 'alert';
                    alert.innerHTML = 'Please enter a message to check.';

                    // Insert after the form group
                    const formGroup = document.querySelector('.form-group');
                    formGroup.parentNode.insertBefore(alert, formGroup.nextSibling);

                    // Remove alert after 3 seconds
                    setTimeout(() => {
                        alert.remove();
                    }, 3000);
                }
            }
        });
    }

    // Example message buttons
    const exampleContainer = document.getElementById('example-messages');
    if (exampleContainer) {
        const examples = [
            { text: "Hi, how are you?", likely: "ham" },
            { text: "URGENT: You've won a prize! Call now!", likely: "spam" },
            { text: "Meeting tomorrow at 10am", likely: "ham" },
            { text: "FREE! Buy now limited offer", likely: "spam" }
        ];

        examples.forEach(example => {
            const btn = document.createElement('button');
            btn.className = `btn btn-sm btn-outline-${example.likely === 'spam' ? 'danger' : 'success'} m-1`;
            btn.innerHTML = example.text;

            btn.addEventListener('click', function() {
                messageTextarea.value = example.text;
                // Trigger input event to update character counter
                messageTextarea.dispatchEvent(new Event('input'));
                // Scroll to form
                document.querySelector('form').scrollIntoView({ behavior: 'smooth' });
            });

            exampleContainer.appendChild(btn);
        });
    }

    // Animated result on result page
    const resultBox = document.querySelector('.result-box');
    if (resultBox) {
        resultBox.style.opacity = '0';
        resultBox.style.transform = 'translateY(20px)';
        resultBox.style.transition = 'opacity 0.5s ease, transform 0.5s ease';

        setTimeout(() => {
            resultBox.style.opacity = '1';
            resultBox.style.transform = 'translateY(0)';
        }, 300);
    }
});
