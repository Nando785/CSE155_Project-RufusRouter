// const CameraInput = document.getElementById("CameraInput");
//         const Preview = document.getElementById("Preview");

        // CameraInput.addEventListener("change", function() {
        //     const file = this.files[0]; // Corrected from this.file[0]
        //     if (file) {
        //         const reader = new FileReader();
        //         reader.onload = function(e) {
        //             Preview.src = e.target.result;
        //             Preview.style.display = "block";
        //         }
        //         reader.readAsDataURL(file);
        //     }
        // });

        document.querySelector('form').addEventListener('submit', function(event) {
            event.preventDefault();  // Prevent the default form submission
        
            // Get the location and destination from the form inputs
            const location = document.getElementById('location').value;
            const destination = document.getElementById('destination').value;
        
            const data = { location, destination };
        
            // Make the fetch request to the Flask server
            fetch('http://localhost:5500/navigate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
            .then(response => {
                console.log('Response Status:', response.status);  // Check the response status
                if (!response.ok) {
                    throw new Error('Failed to load');
                }
                return response.json();
            })
            .then(data => {
                const resultDiv = document.getElementById("result");
                resultDiv.textContent = data.path.join(" -> ");
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
        
        
        
        