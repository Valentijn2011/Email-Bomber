document.getElementById('emailForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const formData = new FormData(e.target);
    const target = formData.get('target');
    const server = formData.get('server');
    const fromAddr = formData.get('fromAddr');
    const fromPwd = formData.get('fromPwd');
    const subject = formData.get('subject');
    const message = formData.get('message');
    const amount = formData.get('amount');

    const statusDiv = document.getElementById('status');
    statusDiv.textContent = 'Starting bombing...';

    fetch('/start_bombing', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            target,
            server,
            fromAddr,
            fromPwd,
            subject,
            message,
            amount,
        }),
    })
    .then(response => response.json())
    .then(data => {
        statusDiv.textContent = data.message;
    })
    .catch((error) => {
        console.error('Error:', error);
        statusDiv.textContent = 'An error occurred. Check the console for details.';
    });
});
