import config from '/@src/config';

const uploadCadFilesRoute = config.routes.baseApi.uploadCadFiles;

export async function uploadCadFiles(formData: FormData) {
    fetch(uploadCadFilesRoute, {
        method: 'POST',
        body: formData
    })
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error('File upload failed');
            }
        })
        .then(data => {
            console.log('Server response:', data);
        })
        .catch(error => {
            console.error('Error uploading file:', error);
        });
}
