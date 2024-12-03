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
    

        document.getElementById('navigation-form').addEventListener('submit', function(e) {
            e.preventDefault(); // Prevent form from submitting traditionally

            // Get values from the dropdowns
            var location = document.getElementById('location').value;
            var destination = document.getElementById('destination').value;

            // Prepare data to send (without file upload)
            var formData = {
                location: location,
                destination: destination
            };

            localStorage.setItem('userData', JSON.stringify(formData));
            const savedData = JSON.parse(localStorage.getItem('userData'));
            // this is what briefly appears on the console
            console.log(savedData); // print saved data to console

            fetch('http://localhost:5000/test', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(savedData),
            })
            .then(response => response.json())
            .then(result => console.log('Success: ', result))
            .then(error => console.log('Error: ', error));
        });
        
        
        
        


     
    /* Jordan Richard Code for how webpages would be displayed */

    
        // Event listener for the form submission
    document.querySelector('form').addEventListener('submit', function(event) {
        event.preventDefault();  // Prevent the default form submission behavior

        // Get the selected destination value from the dropdown
        const destination = document.getElementById('destination').value;

        // Redirect based on the selected destination
        switch (destination) {
            case 'acs':
                window.location.href = '/acs';  // Redirect to the ACS page
                break;
            case 'cob1':
                window.location.href = '/cob1.html';  // Redirect to the COB 1 page
                break;
            case 'cob2':
                window.location.href = '/cob2.html';  // Redirect to the COB 2 page
                break;
            case 'library1':
                window.location.href = '/library1.html';  // Redirect to the KL page
                break;
            case 'se2':
                window.location.href = '/se2.html';  // Redirect to the SE2 page
                break;
            case 'ssm':
                window.location.href = '/ssm.html';  // Redirect to the SSM page
                break;
            case 'ssb':
                window.location.href = '/ssb.html';  // Redirect to the SSB page
                break;
            default:
                alert('Invalid selection!');  // Show an alert for unexpected values
        }
    }); 
