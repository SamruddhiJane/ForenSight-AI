function uploadFile() {

    const fileInput = document.getElementById("fileInput");
    const status = document.getElementById("status");

    // Check if a file was selected
    if (fileInput.files.length === 0) {
        status.textContent = "Please select a file first.";
        return;
    }

    const file = fileInput.files[0];

    // Create form data
    const formData = new FormData();
    formData.append("file", file);

    status.textContent = "Uploading...";

    // Send file to Flask backend
    fetch("http://127.0.0.1:5000/upload", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {

        if (data.message) {
            status.textContent = data.message;
        } else if (data.error) {
            status.textContent = data.error;
        }

    })
    .catch(error => {
        status.textContent = "Error connecting to backend.";
        console.error(error);
    });
}