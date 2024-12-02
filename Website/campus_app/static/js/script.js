const CameraInput = document.getElementById("CameraInput");
const Preview = document.getElementById("Preview");

CameraInput.addEventListener("change", function() {
    const file = this.files[0]; // Corrected from this.file[0]
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            Preview.src = e.target.result;
            Preview.style.display = "block";
        }
        reader.readAsDataURL(file);
    }
});

const dropdownMenu = document.createElement("select");
dropdownMenu.id = "dropdownMenu";
dropdownMenu.innerHTML = `
    <option value="option1">Option 1</option>
    <option value="option2">Option 2</option>
    <option value="option3">Option 3</option>
`;
document.body.appendChild(dropdownMenu);