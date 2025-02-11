document.getElementById('imageInput').addEventListener('change',function(event) {
    const preview = document.getElementById('preview');
    preview.innerHTML = ''; // Clear previous images

    Array.from(event.target.files).forEach(file => {
        const reader = new FileReader();
        reader.onload = function(e){
            const img = document.createElement('img');
            img.src = e.target.result;
            img.classList.add('preview-image');
            preview.appendChild(img);
        };
        reader.readAsDataURL(file);
    });
});
document.getElementById('uploadButton').addEventListener('click', async function() {
    const files = document.getElementById('imageInput').files;
    if (files.length == 0) return ;
    const formData = new FormData();
    Array.from(files).forEach(file => {
        formData.append('files', file);
    });
    try {
        const response = await fetch("/stitch", {
            method: 'POST',
            body: formData
        })
        const responseData = await response.json();
        const responsePreview = document.getElementById('responsePreview');
        responsePreview.innerHTML = '';

        if (responseData.imageUrl) {
            const img = document.createElement('img');
            img.src = responseData.imageUrl;
            img.classList.add('response-image')
            responsePreview.appendChild(img);
        }
    } catch (error){
        console.error('Error uploading images: ',error);
    }
});