document.getElementById('submit-button').addEventListener('click', async () => {
            const systemPrompt = document.getElementById('system-prompt').value;
            const selectedModel = document.getElementById('model-select').value;
            const userInput = document.getElementById('user-input').value;
            const responseContainer = document.getElementById('response-container');

            responseContainer.innerHTML = ''; // Clear previous responses

            if (!userInput.trim()) {
                responseContainer.innerHTML = '<div class="warning">Please enter a message before clicking "Submit".</div>';
                return;
            }

            try {
                const payload = {
                    messages: [userInput],
                    model_name: selectedModel,
                    system_prompt: systemPrompt
                };

                const response = await fetch('http://127.0.0.1:8000/chat', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(payload)
                });

                if (response.ok) {
                    const data = await response.json();

                    if (data.error) {
                        responseContainer.innerHTML = `<div class="error">${data.error}</div>`;
                    } else {
                        const aiResponses = data.messages.filter(msg => msg.type === 'ai').map(msg => msg.content);

                        if (aiResponses.length > 0) {
                            responseContainer.innerHTML = `<div class="response"><strong>Agent Response:</strong> ${aiResponses[aiResponses.length - 1]}</div>`;
                        } else {
                            responseContainer.innerHTML = '<div class="warning">No AI response found in the agent output.</div>';
                        }
                    }
                } else {
                    responseContainer.innerHTML = `<div class="error">Request failed with status code ${response.status}.</div>`;
                }
            } catch (error) {
                responseContainer.innerHTML = `<div class="error">An error occurred: ${error.message}</div>`;
            }
        });